# Filmed-stock workflow

Adds two independent skills to the existing team repository. The original team skills and product context remain intact. Source stock, edited MP4s and local archives are not committed.

Requirements: Python 3.11+, Pillow, FFmpeg and FFprobe. Example plans specify macOS Arial font paths; set `presentation.font` and `presentation.bold_font` to installed fonts on other systems.

From the repository root:

```sh
python3 skills/free-footage-sourcing/scripts/collect.py docs/seoul-sources.json --download
python3 skills/footage-repurposing/scripts/render.py docs/seoul-short.json outputs/seoul-short.mp4
python3 skills/footage-repurposing/scripts/render.py docs/seoul-explainer.json outputs/seoul-explainer.mp4
python3 -m unittest discover -s tests -p 'test_footage_pipeline.py'
node scripts/check-versions.mjs --base gtm-loop/main
```

Source-only tests explicitly skip media-dependent checks when original clips are absent. Download the reviewed sources to run the full integration checks; changed upstream bytes fail the stored hash check instead of being silently accepted. Existing output files are never overwritten.

Examples: [campaign](seoul-campaign.md), [source ledger](seoul-sources.json), [24-second shot brief with missing assets](experience-shot-brief.json), [target understanding loop](seoul-target-loop.md), [observations template](seoul-observations.csv).

Historical local outputs: two approximately 30-second city teasers and a 70-second concept explanation. Those are silent stock edits, not footage of actual table projection or the proposed menu. Subsequent typography parameters are stored in the current example plans, so these plans are not byte-for-byte recipes for the preserved historical outputs. Local verification notes describe the specific files checked at the time.

The 24-second experience-led cut is not finished: suitable table-story and eating shots remain missing. Music listening, actual audience tests and external content publishing have not occurred. The source branch push is now authorized; older campaign notes mentioning a push hold describe the earlier state. This workflow was subsequently integrated into main without importing the inherited upstream history. Local packaged ZIPs are earlier snapshots, not the current branch source.

## Integration scope

This is the optional filmed-stock-only branch of GTM Loop. It complements the Higgsfield recreation path rather than disabling it. Historical output/QA statements below the campaign docs describe the branch author’s prior work; this merge does not independently recertify those missing local media files.
