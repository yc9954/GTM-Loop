# GA와 광고 분석 사용 지도

2026-10-24, 현재 저장소의 스킬·진입 링크·선택 목록·버전·플러그인 메타데이터를 대조했다. 실제 계정이나 성과 데이터를 읽은 보고서가 아니다.

## 어떤 스킬로 시작하는가

| 질문 | 스킬 | 근거와 결과 |
|---|---|---|
| 어떤 나라·채널·콘텐츠가 반응했나? | [ga-performance-review](../skills/ga-performance-review/SKILL.md) | 실제 GA/내보내기, 같은 기간·분모·목표 행동 → 관찰·불확실성·다음 제작 가설 |
| Google/Meta 광고의 비용·전환은 어떤가? | [ads](../skills/ads/SKILL.md) + [ga-performance-review](../skills/ga-performance-review/SKILL.md) | 광고 계정/내보내기의 노출·클릭·비용·전환, 검색어와 입찰 키워드 → 판단과 실험 제안 |
| 유사 광고의 훅·구도·편집은 어떻게 쓰나? | [meta-library-research](../skills/meta-library-research/SKILL.md) + [ad-creative](../skills/ad-creative/SKILL.md) | 실제 관찰한 공개 광고와 시점 → 표현 원리·필요한 샷·제품 적합성. 실제 광고 성과를 추정하지 않음 |
| 이벤트·UTM이 맞게 측정되는가? | [analytics](../skills/analytics/SKILL.md) | 사이트 이벤트·콘텐츠 ID·수집 설정과 관측 자료 |
| 전환이 광고 플랫폼에 전달되는가? | [conversion-tracking](../skills/conversion-tracking/SKILL.md) | 제출·예약 등 성공 신호와 실제 전달 경로 |
| 어느 채널의 기여인가? | [attribution](../skills/attribution/SKILL.md) | 기간·기여 모델·식별 범위와 한계 |
| 표현 변경이 차이를 만들었나? | [ab-testing](../skills/ab-testing/SKILL.md) | 사전 가설·비교 조건·표본·중단 기준 |
| 다음 소스·콘티·편집은 누가 맡나? | [gtm-cycle-review](../skills/gtm-cycle-review/SKILL.md) | 근거 시점·창작물 버전·미결 검토 → 인계 기록과 다음 검토 시점 |

## 실제 도구와 자료 경계

| 자료 | 저장소에 있는 경로 | 확인할 것 |
|---|---|---|
| GA4 | [가이드](../tools/integrations/ga4.md), [CLI](../tools/clis/ga4.js) | 속성·기간·권한·현재 읽기 성공 여부 |
| Google Ads | [가이드](../tools/integrations/google-ads.md), [CLI](../tools/clis/google-ads.js) | 계정 접근·검색어/키워드·비용 통화·전환 기간 |
| Meta Ads 계정 | [가이드](../tools/integrations/meta-ads.md), [CLI](../tools/clis/meta-ads.js) | 계정 성과 조회와 현재 권한 |
| 공개 Meta 광고 라이브러리 | [조사 스킬](../skills/meta-library-research/SKILL.md) | 관찰한 광고·국가·시점·표현. 계정용 CLI를 공개 수집기로 간주하지 않음 |
| 오프라인 자료 | 사용자 제공 CSV/내보내기 | 원본 출처·시간대·기간·필터·누락·데이터 반영 시점 |

파일이 있다고 연결됐다는 뜻은 아니다. 실제 작업의 환경·도구 선택은 사용자 지시와 설치 환경을 따른다. 키·원자료·계정/고객 식별 정보는 공개 저장소에 저장하지 않는다.

## 한 번의 사용 예

“Soban Tales의 지난 비교 기간 GA와 광고 내보내기를 국가·콘텐츠 ID로 비교해줘. GA 반응과 광고 비용·전환을 구분하고, Meta 라이브러리의 참고 광고는 성과 미확인 레퍼런스로 표시해줘. 다음에 바꿀 훅 하나와 소스/영상 담당 인계안을 만들고, 자료가 없으면 미측정으로 남겨줘.”

분석·레퍼런스 수집 → 가설 → free-footage-sourcing 또는 허용된 Higgsfield 제작 → video-direction/video-shotcraft → 버전별 검토 → 요청 범위의 배포 → 같은 조건 재측정으로 연결한다. 실제 광고 집행·메시지 발송·게시가 요청되지 않았다면 이 자료를 만든 사실이 해당 실행 권한이 되지는 않는다.

## 반영 위치와 이번 보완

- [README](../README.md#ga광고-분석과-레퍼런스-조사): 성과 분석과 공개 광고 조사를 구분한 진입표. 전체 지도·폴더 트리에는 59개 스킬이 반영되어 있다.
- [핵심 루프 가이드](gtm-loop.md#연결-자료): 새 GA/Meta/사이클 스킬과 ads의 직접 링크 보완.
- [역할별 bundle](../bundles/project-table.json): GA/Meta·계측·실험·제작 연결 확인, 옛 브랜치 상태를 보관 기록으로 정정.
- [제품별 안내](soban-tales/README.md): 기존 56개 스냅샷과 최신 맥락을 작업 시 읽는 추가 3개의 구분 유지.
- 플러그인 소스 경로는 skills 전체 디렉터리이며 59개 스킬을 포함한다. [Claude 설정](../.claude-plugin/plugin.json), [마켓플레이스](../.claude-plugin/marketplace.json), [Codex 설정](../.codex-plugin/plugin.json), [앱 표시 설정](../.agents/plugins/marketplace.json)의 설명/주소/소유 정보를 현재 GTM Loop로 정리했다. 설치 식별자는 호환성을 위해 유지했다.
- ads 진입문의 “계정 직접 접근” 가정을 제거하고 실제 연결 또는 제공 자료를 확인하도록 수정했다. 원본 저작권·라이선스는 유지한다.
- [버전 기록](../VERSIONS.md): 로컬 2.16.1, ads 2.7.1. 실제 GA/광고 데이터 조회나 계정 연결 테스트는 이번 문서 점검에서 수행하지 않았다.

- [에이전트 작업 지침](../AGENTS.md): 삭제된 과거 브랜치를 현재 원격 브랜치로 가정하지 않도록 정정했다.
