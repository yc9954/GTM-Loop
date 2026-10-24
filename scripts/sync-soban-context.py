"""Refresh installed-skill snapshots from canonical Soban Tales context. Review version bumps separately."""
from pathlib import Path
import json
root = Path(__file__).resolve().parents[1]
context = (root / '.agents/product-marketing.md').read_text()
profiles = json.loads((root / 'docs/soban-tales/skill-profiles.json').read_text())
for name, profile in profiles.items():
    target = root / 'skills' / name / 'references/soban-tales.md'
    target.write_text(context + '\n## 이 스킬의 적용 범위\n\n' + profile + '\n')
print(f'Refreshed {len(profiles)} Soban Tales context snapshots')
