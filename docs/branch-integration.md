# 추가 브랜치의 main 통합

2026-10-24. codex/dan의 추가 기능을 현재 main 파일과 대조해 내용만 통합했다. codex/june는 현재 main과 같은 커밋이어서 추가 내용이 없었다. 원본 marketingskills의 긴 Git 이력은 가져오지 않는다.

## 포함한 기능

- free-footage-sourcing: 실사 소스 선정·출처·이용 조건·해시 검토, 기본 no-network 수집 계획과 명시적 다운로드.
- footage-repurposing: 승인된 실사 파일 편집·크롭·자막·안전영역·기술 검수. 무음 초안 출력.
- 서울 티저/설명형 예제, 소스 목록, 참고 분석, 관찰 양식, 게시안과 과거 검증 기록.
- 전체 스킬 56개로 README·버전·제품 기준 스냅샷·폴더 지도를 정합화.

실사 전용 제약은 해당 워크플로에만 적용한다. GTM Loop의 Higgsfield 생성·재제작 경로는 유지한다. The Table이라는 이전 표현은 신규 스킬에서 Soban Tales로 정리했다. 과거 push 보류와 main 미반영 문장은 당시 기록과 이번 통합 상태를 구분했다. 테스트 직접 실행 시 레이아웃 테스트도 포함되도록 진입점을 파일 끝으로 옮겼다.

## 검증

- footage pipeline unittest: 12개 중 9개 통과, 원본 소스 MP4 부재로 3개 명시적 skip. Pillow를 임시 uv 실행 환경으로 제공했다.
- 56개 스킬의 버전 검사 통과. 새 스킬 두 개의 형식 검사 통과. 예제 JSON 파싱 확인.
- 외부 소스 다운로드·실제 영상 재렌더·전편 시청/청취·게시·광고 집행은 수행하지 않았다. 과거 seoul-verification.md는 브랜치 저자의 기록이며 이번 통합의 직접 검증이 아니다.

## 검토 파일

- [.claude-plugin/marketplace.json](../.claude-plugin/marketplace.json)
- [.claude-plugin/plugin.json](../.claude-plugin/plugin.json)
- [.codex-plugin/plugin.json](../.codex-plugin/plugin.json)
- [.gitignore](../.gitignore)
- [README.md](../README.md)
- [VERSIONS.md](../VERSIONS.md)
- [docs/experience-shot-brief.json](../docs/experience-shot-brief.json)
- [docs/footage-workflow.md](../docs/footage-workflow.md)
- [docs/repository-map.md](../docs/repository-map.md)
- [docs/seoul-campaign.md](../docs/seoul-campaign.md)
- [docs/seoul-explainer.json](../docs/seoul-explainer.json)
- [docs/seoul-food-candidates.json](../docs/seoul-food-candidates.json)
- [docs/seoul-observations.csv](../docs/seoul-observations.csv)
- [docs/seoul-publishing-kit.md](../docs/seoul-publishing-kit.md)
- [docs/seoul-reference-study.md](../docs/seoul-reference-study.md)
- [docs/seoul-short.json](../docs/seoul-short.json)
- [docs/seoul-sources.json](../docs/seoul-sources.json)
- [docs/seoul-target-loop.md](../docs/seoul-target-loop.md)
- [docs/seoul-verification.md](../docs/seoul-verification.md)
- [docs/seoul-wide.json](../docs/seoul-wide.json)
- [docs/soban-tales/README.md](../docs/soban-tales/README.md)
- [docs/soban-tales/skill-profiles.json](../docs/soban-tales/skill-profiles.json)
- [skills/footage-repurposing/SKILL.md](../skills/footage-repurposing/SKILL.md)
- [skills/footage-repurposing/references/soban-tales.md](../skills/footage-repurposing/references/soban-tales.md)
- [skills/footage-repurposing/scripts/render.py](../skills/footage-repurposing/scripts/render.py)
- [skills/free-footage-sourcing/SKILL.md](../skills/free-footage-sourcing/SKILL.md)
- [skills/free-footage-sourcing/references/soban-tales.md](../skills/free-footage-sourcing/references/soban-tales.md)
- [skills/free-footage-sourcing/scripts/collect.py](../skills/free-footage-sourcing/scripts/collect.py)
- [tests/test_footage_pipeline.py](../tests/test_footage_pipeline.py)

## codex/june 후속 통합

2026-10-24, 원본 커밋 `1f0092818578d9f9b07022d9bc901778f58ce516`의 추가 내용만 현재 main에 반영했다. 기존 가재 v4 대표 이미지·620px 표시·GTM 정체성·실사 편집 경로를 유지했다.

- GA 성과 검토·Meta 광고 레퍼런스 조사·GTM 사이클 검토 스킬과 기록 검사기 추가. 전체 59개, 로컬 버전 2.16.0.
- 역할별 bundle과 협업 기준을 연결하고, 브랜치 README의 폴더 트리에 섞인 박스 행을 실제 디렉터리 기반으로 수정했다.
- Genjutsu 공식 페이지를 확인해 현재 README/루프 가이드의 표기를 바로잡았다. 계정 연결·유료 생성은 실행하지 않았다.
- 새 사이클 테스트 11개 통과. 기존 footage 테스트 9개 통과·원본 MP4 부재로 3개 skip. 총 20개 통과·3개 skip.
- 새 스킬 3개의 형식·59개 버전·선택 목록 경로·문서 링크 검사 통과. 예제 기록이 자료 누락과 미승인 상태를 유지하는지 확인했다.
- 실제 GA 조회·광고 수집·메시지 발송·예약 실행·렌더·게시·현장 검증은 수행하지 않았다. 원격 작업 브랜치는 변경하지 않는다.

### 후속 통합 검토 파일

- [.claude-plugin/marketplace.json](../.claude-plugin/marketplace.json)
- [.claude-plugin/plugin.json](../.claude-plugin/plugin.json)
- [.codex-plugin/plugin.json](../.codex-plugin/plugin.json)
- [.gitignore](../.gitignore)
- [AGENTS.md](../AGENTS.md)
- [README.md](../README.md)
- [VERSIONS.md](../VERSIONS.md)
- [bundles/project-table.json](../bundles/project-table.json)
- [docs/gtm-loop.md](../docs/gtm-loop.md)
- [docs/project-table-june.md](../docs/project-table-june.md)
- [docs/repository-map.md](../docs/repository-map.md)
- [docs/soban-tales/README.md](../docs/soban-tales/README.md)
- [skills/ga-performance-review/SKILL.md](../skills/ga-performance-review/SKILL.md)
- [skills/gtm-cycle-review/SKILL.md](../skills/gtm-cycle-review/SKILL.md)
- [skills/gtm-cycle-review/assets/cycle.example.json](../skills/gtm-cycle-review/assets/cycle.example.json)
- [skills/gtm-cycle-review/references/operating-contract.md](../skills/gtm-cycle-review/references/operating-contract.md)
- [skills/gtm-cycle-review/scripts/review_cycle.py](../skills/gtm-cycle-review/scripts/review_cycle.py)
- [skills/meta-library-research/SKILL.md](../skills/meta-library-research/SKILL.md)
- [tests/test_gtm_cycle.py](../tests/test_gtm_cycle.py)
