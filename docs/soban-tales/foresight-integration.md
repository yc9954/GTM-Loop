# FORESIGHT 참고 자료의 Soban Tales 통합

첨부 ZIP의 진입 지침·제작 이력·소스 색인·QA·검사 스크립트를 읽고 방법만 정제했다. 미디어 목록 두 JSON과 UI 메타데이터는 내용 검토하지 않았다. 실제 FORESIGHT 미디어와 Blender 장면은 열지 않았다. ZIP 안에는 라이선스 파일이 없으므로 원본 패키지·코드를 재배포하지 않고 이 프로젝트를 위한 새 가이드를 작성했다.

| 참고 자료의 교훈 | Soban Tales 적용 |
|---|---|
| 최근 파일보다 선택한 기준본 | 기존 120초 검토본과 최신 수정 본편을 해시·계열로 구분 |
| 원본 엔진에서 목표 해상도로 렌더 | 광고는 원 장면 재렌더, 투사는 고정 7:4 좌표 유지 |
| 단독 proof와 앞 장면을 거친 렌더의 차이 | Blender 캐시·동작 경계·렌더 결과 비교로 확장; 동일 결함이라고 단정하지 않음 |
| 카메라 수정만으로 기하 문제 해결 안 됨 | 그립·하중·바닥·기물·소매를 원 장면에서 고침 |
| 전역 박자와 별도 Foley | 한 공연 안의 음악 연속성; 식사/서빙 대기는 수동 큐로 분리 |
| 파일 검사와 감상 승인 분리 | 기술·정상속도·청취·현장 네 좌석을 별도 상태로 기록 |
| 편집 원본·의존성·검수 범위 전달 | .blend·외부 캐시·텍스처·음향·큐시트와 run manifest |

## 결과

- [Blender/VFX 제작 판단](../../skills/video/references/soban-blender-vfx.md)
- [편집·음향·검수](../../skills/video/references/soban-edit-delivery.md)
- [빈 run manifest](../../skills/video/assets/soban-run-manifest.json)
- [첨부 출처와 파일별 해시·검토 범위](foresight-source.json)

두 가이드는 video-direction·video-shotcraft에도 각각 동봉하여 독립 설치를 지원한다. Blender 사용안은 모델/리그·모션·접촉·의상·음식·합성·현장의 책임을 구분한 제작 지침이며 실행된 장면이나 완료한 플러그인이 아니다. 원본 ZIP의 scripts/media_check.py는 읽기만 했고 복사하거나 실행하지 않았다.

검증 범위는 세 스킬의 형식·분량·참조 링크, 버전 일관성과 manifest의 빈 상태/JSON 형식이다. Blender 실행·영상 렌더·시청·청취·현장 검수는 이번 통합의 완료 항목이 아니다. 설치된 Codex 플러그인 캐시는 갱신하지 않았다.
