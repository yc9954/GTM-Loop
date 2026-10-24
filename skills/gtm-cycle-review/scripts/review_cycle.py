#!/usr/bin/env python3
"""Inspect a human-authored review record; no network, scheduling or publishing."""
import argparse
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

SOURCES = ("ga", "search_ads", "meta_library", "customer_feedback", "production")
CHECKS = ("playback", "product_claims", "rights", "destination")


def text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field}: nonempty text required")
    return value


def timestamp(value, field):
    try:
        parsed = datetime.fromisoformat(text(value, field).replace("Z", "+00:00"))
    except (ValueError, TypeError):
        raise ValueError(f"{field}: timezone-aware ISO timestamp required") from None
    if parsed.utcoffset() is None:
        raise ValueError(f"{field}: timezone required")
    return parsed


def number(value, field):
    if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value) or value <= 0:
        raise ValueError(f"{field}: positive finite number required")
    return value


def review(record, now):
    if not isinstance(record, dict) or record.get("schema_version") != 1:
        raise ValueError("schema_version must be 1")
    if now.utcoffset() is None:
        raise ValueError("now: timezone required")
    for field in ("cycle_id", "creative_id", "creative_revision", "objective"):
        text(record.get(field), field)
    sources = record.get("sources")
    if not isinstance(sources, dict) or set(sources) != set(SOURCES):
        raise ValueError("sources must contain exactly: " + ", ".join(SOURCES))
    results, actions = {}, []
    for name in SOURCES:
        source = sources[name]
        if not isinstance(source, dict):
            raise ValueError(f"{name}: object required")
        owner = text(source.get("owner"), f"{name}.owner")
        state = source.get("status")
        if state not in ("ready", "missing", "not_applicable"):
            raise ValueError(f"{name}: invalid status")
        age_limit = number(source.get("max_age_hours"), f"{name}.max_age_hours")
        if state == "not_applicable":
            text(source.get("reason"), f"{name}.reason")
            results[name] = state
            continue
        if state == "missing":
            results[name] = state
            actions.append({"source": name, "owner": owner, "action": "obtain_evidence"})
            continue
        checked = timestamp(source.get("checked_at"), f"{name}.checked_at")
        if checked > now:
            raise ValueError(f"{name}: checked_at is in the future")
        text(source.get("evidence_uri"), f"{name}.evidence_uri")
        freshness = checked
        if name in ("ga", "search_ads"):
            freshness = timestamp(source.get("data_through"), f"{name}.data_through")
            if freshness > checked:
                raise ValueError(f"{name}: data_through is after checked_at")
            if type(source.get("period_complete")) is not bool:
                raise ValueError(f"{name}.period_complete: boolean required")
            if not source["period_complete"]:
                results[name] = "provisional"
                actions.append({"source": name, "owner": owner, "action": "wait_for_complete_period"})
                continue
        if (now - freshness).total_seconds() / 3600 > age_limit:
            results[name] = "stale"
            actions.append({"source": name, "owner": owner, "action": "refresh_evidence"})
        else:
            results[name] = "ready"

    required = record.get("reviewers_required")
    if not isinstance(required, list) or not required or any(not isinstance(x, str) or not x.strip() for x in required) or len(set(required)) != len(required):
        raise ValueError("reviewers_required: distinct nonempty reviewer IDs required")
    reviews = record.get("reviews")
    checks = record.get("checks")
    if not isinstance(reviews, dict) or not isinstance(checks, dict) or set(checks) != set(CHECKS):
        raise ValueError("reviews and all four checks are required")
    gaps = []
    revision = record["creative_revision"]
    for kind, ids, entries in (("review", required, reviews), ("check", CHECKS, checks)):
        for item_id in ids:
            entry = entries.get(item_id)
            if entry is None:
                gaps.append(f"{kind}:{item_id}:missing")
                continue
            if not isinstance(entry, dict):
                raise ValueError(f"{kind}:{item_id}: object or null required")
            if entry.get("revision") != revision:
                gaps.append(f"{kind}:{item_id}:different_revision")
                continue
            if entry.get("decision") != "accepted":
                gaps.append(f"{kind}:{item_id}:not_accepted")
                continue
            text(entry.get("evidence_uri"), f"{kind}:{item_id}.evidence_uri")
            when = timestamp(entry.get("recorded_at"), f"{kind}:{item_id}.recorded_at")
            if when > now:
                raise ValueError(f"{kind}:{item_id}: recorded_at is in the future")
    next_review = timestamp(record.get("next_review_at"), "next_review_at")
    evidence_complete = all(s in ("ready", "not_applicable") for s in results.values())
    return {
        "cycle_id": record["cycle_id"], "as_of": now.isoformat(),
        "source_states": results, "actions": actions, "review_gaps": gaps,
        "review_due": next_review <= now,
        "evidence_complete": evidence_complete,
        "review_packet_complete": evidence_complete and not gaps,
        "publication_authorized": False,
        "scope": "Record completeness only; truth, creative quality and authority require human review.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    parser.add_argument("--now", help="Explicit simulated time; defaults to current UTC")
    args = parser.parse_args()
    try:
        now = timestamp(args.now, "now") if args.now else datetime.now(timezone.utc)
        result = review(json.loads(args.record.read_text()), now)
    except (OSError, ValueError, TypeError, OverflowError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
