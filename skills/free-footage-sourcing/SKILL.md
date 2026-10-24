---
name: free-footage-sourcing
description: Find and collect free-to-use food footage for Soban Tales and other explicitly scoped marketing videos, preserving source and license evidence and evaluating fit for international visitors to Korea. Use for stock footage, B-roll, or source collection requests.
metadata:
  version: 1.0.0
---

## Soban Tales 적용 범위

[제품·제작 기준](references/soban-tales.md)을 읽는다. Soban Tales에 맞는 실제 촬영 무료 소스를 찾고 출처·이용 조건·해시·검토 범위를 기록한다. 참고 영상과 제작 허용 소스를 구분하고 실제 메뉴·장소·공연을 대체했다고 주장하지 않는다. 실사 전용 요청에 적용하며 Higgsfield 제작 경로 전체를 금지하지 않는다.

# Free footage sourcing

Collect a small, traceable set of footage that answers a target need. Read the current product brief before searching. Soban Tales introduces traditional Korean food through a visual dining experience; do not substitute generic restaurant advertising.

## Select
- State the target, their trip context, one featured place or verified dish, and one desired action. English is a test language, not proof of a nationality or language preference.
- Search exact location names or verified menu items; avoid generic food clips that contradict the product document. A tag is not proof that a dish or location is Korean: inspect frames and source descriptions.
- Prefer official Pexels pages or an authorized API. For API use, load `PEXELS_API_KEY` from the local environment; never embed keys in files or chat. Current API entrypoint: https://www.pexels.com/api/documentation/ . Verify its current route before implementing calls.
- Without an API key, use the public video page and its actual download link. Do not fabricate CDN URLs or treat a search thumbnail as the source video.
- If authentication is needed, ask the user to log in. A download failure is not proof that no footage exists. Check a known working source before claiming absence.

## Review rights and content
Read https://www.pexels.com/license/ and each original page. Free licensed footage is not necessarily public domain. Keep creator, source URL, license URL, retrieval date, local filename, SHA-256, visual inspection notes, and intended use in a manifest. Identify logos, recognizable people, music, and misleading endorsement risks. Exclude or change the shot when these conflict with its intended use. Honor API attribution separately from the media license.

Do not download competitor footage merely because it is public. Le Petit Chef is a product reference, not licensed source footage. Recreating an edit does not clear rights to its source imagery, characters, or music.

## Deliver
Provide selected assets, a source manifest, and rejected candidates with a reason. Preserve originals. Mark stock imagery as illustrative; it cannot establish Soban Tales’ actual venue, menu, price, or operating status. Send local files and source links to footage-repurposing, along with target and CTA. A missing source is a stated gap, not a fabricated scene.

For a reviewed manifest, `scripts/collect.py` defaults to a no-network plan and verifies existing file hashes. Use `--download` to retrieve selected sources. It validates the downloaded media with FFprobe and refuses to replace files; interrupted `.partial` files require inspection before retry.
```sh
python3 skills/free-footage-sourcing/scripts/collect.py docs/seoul-sources.json
python3 skills/free-footage-sourcing/scripts/collect.py docs/seoul-sources.json --download
```

## Seoul / Soban Tales correction (current workflow)
The product document takes precedence over the earlier generic bibimbap brief. Read `docs/seoul-campaign.md` and use `docs/seoul-sources.json` for the current cut. Search locations by their actual names: Namsan Seoul Tower, Gwanghwamun, Gyeongbokgung, Cheonggyecheon. Verify the landmark in sampled frames and the original page; tags alone are insufficient.

Keep official promotional films under `assets/reference/` for study only. Every production asset must have `usage: production`, `origin: filmed_stock`, and `decision: selected`; reference-only and rejected assets cannot enter the edit. Origin records the source label and visual review, not independently verified camera provenance. Inspect beginning/middle/end and the actual selected excerpt. Record portrait-crop suitability and visible people/brands.

For a filmed-stock-only task, only acquire real filmed stock. Do not generate replacement scenes via code or an AI service. If a needed royal dish is unavailable, record the gap and narrow the preview scope. Bibimbap does not match the proposed menu and is excluded from the Seoul concept teaser. Download sources through their observed official download links. Preserve the source and license evidence and SHA-256.

## Start from needed shots, not URLs
Before searching, accept brand, target, core experience, duration, CTA and aspect ratios as inputs. Create a shot brief with role and seconds for each shot. `docs/experience-shot-brief.json` is a campaign example, not a universal default. Each candidate needs source URL, review scope, role, product fit, portrait/landscape crop assessment, actual source in/out, decision, and rejection reason. An empty slot stays missing until a suitable clip is inspected. Search official stock pages for the missing action; the download helper only acquires reviewed URLs and is not an automated discovery engine. Do not infer a bite from a stirring shot, Korea from chopsticks, or an actual product demo from a caption. Prioritize the critical missing experience shot over acquiring more city vistas.
