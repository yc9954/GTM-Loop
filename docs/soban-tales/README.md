# Soban Tales 특화 안내

현재 전체는 59개 스킬이다. 사용자 설명서에 근거한 기존 56개와, 작업 시 최신 제품 맥락을 읽는 GA·Meta·협업 검토 3개로 구성한다. 기존 일반 지식과 외부 라이선스는 유지했다.

- 공통 제품 기준: [product-marketing.md](../../.agents/product-marketing.md)
- 스킬별 역할 56개: [skill-profiles.json](skill-profiles.json)
- 원본 설명서: [source.docx](source.docx)
- 전문 추출: [source-extract.md](source-extract.md)
- 출처·SHA-256: [source.json](source.json)

각 skills/<name>/SKILL.md에 제품별 적용 절을 추가하고 references/soban-tales.md에 문서 기준 스냅샷을 포함했다. 독립 설치해도 제품 맥락이 따라간다. 외부 제작 자산의 최신 상태는 이번 작업에서 검사하지 않았다.

## 제작 사용

video는 투사/광고/검토본을 구분한다. video-direction은 구도·동선·연기 원인·생성 프롬프트를 설계한다. video-shotcraft는 적합한 광고/합성에 Remotion 레시피를 적용한다. 투사 마스터는 7:4 고정 좌표, 개인4/공유2/전체1 무대와 수동 서비스 큐를 따른다. 별도 VFX Skills·Blender·SURA Studio가 맡는 실제 3D 작업을 이 통합으로 구현했다고 간주하지 않는다.

마케팅·영업 스킬은 개발 단계의 파일럿·관객 조사·협업 후보에 맞췄다. ASO/paywalls처럼 현재 제품과 맞지 않는 스킬은 실제 해당 제품이 생겼을 때만 적용한다. 가짜 앱·예약·계약·매출을 만들지 않는다.

## 갱신

공통 사실은 .agents/product-marketing.md, 역할별 기준은 skill-profiles.json을 수정한 뒤 `python3 scripts/sync-soban-context.py`로 스냅샷을 갱신한다. SKILL.md의 적용 절도 역할 변경 시 함께 수정한다. 배포 전 변경된 스킬·VERSIONS.md·플러그인 버전을 갱신하고 `node scripts/check-versions.mjs --base origin/main`을 실행한다.

현재 작업은 로컬 소스 특화다. 설치된 Codex 플러그인 캐시·외부 제작 프로젝트·공연 자산은 변경하지 않았다. 실제 렌더·현장 투사·전체 공연 검증은 별도다. 원본 설명서에는 비공개 제작 정보가 있으므로 공개 저장소 배포 전 공개 범위를 검토한다.

## Blender와 VFX 제작 지침 보강

[FORESIGHT 자료 정제 결과](foresight-integration.md)에서 선택 근거·결과 파일·검증 범위를 확인한다. 실제 제작에서는 video의 Blender/VFX·편집 가이드와 빈 run manifest를 사용한다.

## GA·Meta·협업 검토 확장

기존 제품 기준 스냅샷을 가진 56개에 최신 제품 맥락을 작업 시 읽는 3개 스킬을 추가해 총 59개다. [역할별 사용법](../project-table-june.md)과 [통합 기록](../branch-integration.md)을 참고한다.

[GA·광고 분석 사용 지도](../analytics-and-ads.md)에서 계정 성과·공개 레퍼런스·계측 스킬의 차이를 확인한다.
