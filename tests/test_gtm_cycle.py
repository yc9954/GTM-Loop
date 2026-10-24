"""Synthetic contract tests. No customer, analytics or approval facts are fabricated."""
import copy
import importlib.util
import json
import unittest
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/gtm-cycle-review"
SPEC = importlib.util.spec_from_file_location("cycle", SKILL / "scripts/review_cycle.py")
cycle = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cycle)
NOW = datetime.fromisoformat("2026-10-24T09:00:00+09:00")


def complete_record():
    record = json.loads((SKILL / "assets/cycle.example.json").read_text())
    for source in record["sources"].values():
        source.update(status="ready", checked_at="2026-10-24T08:00:00+09:00",
                      data_through="2026-10-22T23:59:59+09:00", period_complete=True,
                      evidence_uri="fixture://synthetic-only")
    evidence = {"revision": "draft-0", "decision": "accepted",
                "recorded_at": "2026-10-24T08:00:00+09:00", "evidence_uri": "fixture://synthetic-only"}
    record["reviews"] = {name: copy.deepcopy(evidence) for name in record["reviewers_required"]}
    record["checks"] = {name: copy.deepcopy(evidence) for name in cycle.CHECKS}
    return record


class CycleTests(unittest.TestCase):
    def test_missing_is_not_zero_or_complete(self):
        r = json.loads((SKILL / "assets/cycle.example.json").read_text())
        result = cycle.review(r, NOW)
        self.assertEqual(len(result["actions"]), 5)
        self.assertFalse(result["evidence_complete"])

    def test_complete_packet_never_authorizes_publication(self):
        result = cycle.review(complete_record(), NOW)
        self.assertTrue(result["review_packet_complete"])
        self.assertFalse(result["publication_authorized"])

    def test_recent_query_of_old_data_is_stale(self):
        r = complete_record()
        r["sources"]["ga"]["data_through"] = "2026-10-15T23:59:59+09:00"
        self.assertEqual(cycle.review(r, NOW)["source_states"]["ga"], "stale")

    def test_provisional_data_keeps_other_work_available(self):
        r = complete_record()
        r["sources"]["ga"]["period_complete"] = False
        result = cycle.review(r, NOW)
        self.assertEqual(result["source_states"]["ga"], "provisional")
        self.assertEqual(result["source_states"]["meta_library"], "ready")

    def test_old_version_reviews_do_not_transfer(self):
        r = complete_record()
        r["creative_revision"] = "draft-1"
        self.assertEqual(len(cycle.review(r, NOW)["review_gaps"]), 6)

    def test_customer_silence_is_not_acceptance(self):
        r = complete_record()
        del r["reviews"]["미아"]
        self.assertFalse(cycle.review(r, NOW)["review_packet_complete"])

    def test_no_search_campaign_can_be_not_applicable(self):
        r = complete_record()
        r["sources"]["search_ads"].update(status="not_applicable", reason="Synthetic prelaunch: no campaign")
        self.assertTrue(cycle.review(r, NOW)["evidence_complete"])
        del r["sources"]["search_ads"]["reason"]
        with self.assertRaises(ValueError):
            cycle.review(r, NOW)

    def test_reject_future_evidence_and_missing_timezone(self):
        for when in ("2026-10-25T09:00:00+09:00", "2026-10-24T08:00:00"):
            r = complete_record()
            r["sources"]["meta_library"]["checked_at"] = when
            with self.assertRaises(ValueError):
                cycle.review(r, NOW)

    def test_reject_invalid_thresholds(self):
        for value in (True, 0, -1, float("nan"), float("inf"), "24"):
            r = complete_record()
            r["sources"]["ga"]["max_age_hours"] = value
            with self.assertRaises(ValueError):
                cycle.review(r, NOW)

    def test_required_sources_cannot_be_silently_dropped(self):
        r = complete_record()
        del r["sources"]["customer_feedback"]
        with self.assertRaises(ValueError):
            cycle.review(r, NOW)

    def test_due_time_compares_across_timezones(self):
        r = complete_record()
        r["next_review_at"] = "2026-10-24T00:00:00Z"
        self.assertTrue(cycle.review(r, NOW)["review_due"])


if __name__ == "__main__":
    unittest.main()
