# Project Table: 준의 마케팅 묶음

이 문서는 공개 저장소용 스킬 구성과 사용법이다. 비공개 제작 조사·실계정 성과·고객 자료는 포함하지 않는다.

## 기반과 역할별 선택

[marketingskills 원본](https://github.com/coreyhaines31/marketingskills)은 공식 `marketing-skills` 전체52개 묶음 하나를 제공한다. 역할별 별도 공식 번들이 있는 것은 아니다. 기존 main의 원본52개·영상2개·실사 수집/편집2개에 준의3개를 더해 **59개**로 구성한다. 원작자 라이선스와 크레딧은 보존한다.

| 묶음 | 선택 | 용도 |
|---|---|---|
| 공통 | product-marketing, content-strategy, customer-research, gtm-cycle-review | 제품·대상·가설·협업·시점 |
| 준 | ga-performance-review, meta-library-research, analytics, attribution, ads, ad-creative, ab-testing, competitor-profiling | 성과·키워드·표현 원리에서 제작 질문 도출 |
| 댄 | free-footage-sourcing, footage-repurposing | 출처 있는 실사 스톡 수집·편집. 생성/혼합 경로는 별도 범위 |
| 알렉스 | video, video-direction, video-shotcraft | 사건·구도·편집·사운드·검수 |
| 필요할 때 | conversion-tracking, social, copywriting, cro, seo-audit | 계측·배포·도착 페이지·검색 기회 |

[선택 목록](../bundles/project-table.json)은 설치기나 계정 연결기가 아니다. `popups`는 웹 모달 스킬이므로 오프라인 팝업 사업이라는 이유로 고르지 않는다. ASO/paywalls도 현재 핵심 묶음에서 제외한다. 댄의 작업이 통합된 main을 받아 연결했고 원격 codex/dan 자체는 변경하지 않았다.

## 추가한 진입점

- [GA 성과 분석](../skills/ga-performance-review/SKILL.md): 같은 조건의 기간·분모·목표 행동·검색어/키워드·비용을 대조하고 다음 한 가지 변경을 정한다.
- [Meta 레퍼런스 조사](../skills/meta-library-research/SKILL.md): 실제 관찰 구간, 훅·소재·배경·사건·편집을 기록하고 필요한 제작 샷으로 바꾼다. 미확인 성과를 좋은 광고의 증거로 쓰지 않는다.
- [시점별 협업 검토](../skills/gtm-cycle-review/SKILL.md): 분석·소스·제작·고객 반응을 연결한다. [협업 기준](../skills/gtm-cycle-review/references/operating-contract.md)은 미아님·낸ㅣ님을 기획/공개후보/학습 검토에 포함하되 최종 승인권을 추정하지 않는다.
- [기록 검사기](../skills/gtm-cycle-review/scripts/review_cycle.py): 자료 누락·신선도·미완성 기간·변경된 영상 버전의 검토 누락을 표시한다. 관찰의 진위·창작 품질·게시 권한을 판정하지 않는다.

## 한 회차의 사용법

**근거 → 가설 → 미아님·낸ㅣ님 검토 → 자체 영상+스톡/허용된 생성물 준비 → 알렉스 편집 → 버전별 검수 → 요청 범위의 공개 → 같은 조건 재측정.**

예시 요청: “gtm-cycle-review와 ga-performance-review로 이번 주 콘텐츠에서 바꿀 요소 하나를 정해줘. 접근 가능한 자료부터 읽고, 준의 분석, 댄의 소스 브리프, 알렉스의 컷 수정안, 미아님·낸ㅣ님이 볼 기획 비교안을 같은 콘텐츠 ID로 묶어줘. 자료가 없는 부분은 미측정으로 남겨줘.”

제품 사실은 기존 [제품 기준](../.agents/product-marketing.md)과 실제 공개 가능한 근거를 사용한다. 기술 검사 통과를 공연 승인·서비스 이해·고객 만족으로 바꾸지 않는다. 스톡 인물의 표정이나 생성된 후기를 실제 고객 반응으로 기록하지 않는다.

주기는 집행 중 일간 이상 점검, 데이터 반영 후 초기 점검, 주간/표본 충족 시 제작 판단, 새 자산·메뉴·일정 변경 직후 검토로 나눈다. [Google](https://support.google.com/analytics/answer/11198161?hl=en)은 처리 중 수치가 달라질 수 있음을 설명한다. 자주 조회한다고 자료가 완결되는 것은 아니다. 이 주기를 자동 예약하지 않는다.

공식 도구명은 [Higgsfield Genjutsu](https://higgsfield.ai/genjutsu). 소개된 동작 전이·요소 교체 기능은 실제 계정의 지원이나 생성 성공과 구분한다. [Pexels](https://www.pexels.com/license/)의 무료 이용 허가도 무조건적인 권리 부재가 아니다. 입력·이용 조건·생성 비용은 작업별로 확인한다.

## 검증과 실사용 준비

브랜치 작성 시의 검증 기록: 회귀 시나리오11개, 새 스킬3개의 형식,59개 버전 정합, 선택 목록의 경로를 검사했다. 소스 ZIP3개를 별도 폴더에 풀어 검사기를 실행했다. 합성 테스트 결과를 실측 성과나 사람 승인과 섞지 않는다.

```sh
python3 skills/gtm-cycle-review/scripts/review_cycle.py skills/gtm-cycle-review/assets/cycle.example.json --now 2026-10-24T09:00:00+09:00
python3 -m unittest discover -s tests -p 'test_gtm_cycle.py'
node scripts/check-versions.mjs --base gtm-loop/main
```

첫 실사용에는 사이트·GA 속성·목표 행동·광고 플랫폼·접근 경로/내보내기 자료와 고객 반응의 보관 위치가 필요하다. 계정 ID·원자료·고객 인용 원문·비공개 제작 기록은 공개 저장소 밖에 둔다. 실제 읽기와 사람 검토 전에는 운영 검증 완료라고 보고하지 않는다.

main 통합 시에는 11개 회귀 시나리오를 다시 실행했다. 실제 계정·자료·영상 검증은 추가 수행하지 않았다. 최신 통합 결과는 [통합 기록](branch-integration.md)에 남긴다.
