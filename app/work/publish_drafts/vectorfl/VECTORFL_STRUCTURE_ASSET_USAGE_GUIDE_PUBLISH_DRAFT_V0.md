# VectorFL 구조와 자산 사용 가이드 v0

상태: 공개용 초안 / 사용자 기능 설명 중심 / NOT_AUTHORITY
작성일: 2026-05-25T20:40:04.749509+09:00

이 문서는 지금까지 만든 VectorFL의 구조, 내부 자산의 형태, 그리고 사용자가 그것을 어떻게 활용할 수 있는지를 쉽게 설명하기 위한 공개용 초안이다.

이 문서의 목적은 세 가지다.

1. VectorFL이 무엇을 하는 구조인지 이해한다.
2. 우리가 만든 자산들이 어떤 역할을 하는지 구분한다.
3. 다음 작업을 하기 전에, 무엇을 사용하고 무엇을 아직 건드리면 안 되는지 확인한다.

주의: 이 문서는 제품/기능 설명용 문서이며, 공식 authority registry가 아니다. 파일 이동, 삭제, 아카이브, promotion, registry 변경을 승인하지 않는다.

---

## 1. VectorFL을 한 문장으로 설명하면

VectorFL은 흩어진 입력, 기록, 패킷, 실행 결과, 검증 흔적을 바로 정리하거나 삭제하지 않고, 먼저 읽고 분류하고 연결해서 안전하게 다음 행동을 결정하게 해주는 공간 운영 레이어다.

쉽게 말하면:

> VectorFL은 작업 공간의 물건을 바로 옮기는 정리 도구가 아니라, 먼저 물건의 종류와 위험도를 읽어 지도와 라벨을 붙이는 시스템이다.

VectorFL은 다음 질문에 답한다.

- 이 자산은 원본인가, 후보인가, 실행 기록인가, 검증 증거인가?
- 이 자산을 움직이면 링크나 맥락이 깨지는가?
- 이 자산은 나중에 Codex/Gemini/Hermes에게 넘길 수 있는 패킷인가?
- 이 자산은 authority, registry, current-position과 관련되어 있어 조심해야 하는가?
- 지금 할 수 있는 안전한 작업은 무엇이고, 어디서 멈춰야 하는가?

---

## 2. VectorFL의 기본 작동 방식

VectorFL은 보통 다음 순서로 작동한다.

1. 원본을 보존한다.
2. 자산을 넓게 검색한다.
3. 자산의 역할을 분류한다.
4. 원본을 옮기지 않고 pointer/map/view를 만든다.
5. 위험한 자산은 HOLD 또는 freeze로 표시한다.
6. 검증 가능한 것은 실제 로컬 검증으로 확인한다.
7. 다음 안전 작업을 고른다.
8. authority, registry, promotion, move/archive/delete 경계에서 멈춘다.

핵심은 “바로 실행하지 않는 것”이다.

VectorFL은 먼저 자산이 무엇인지 이해한 뒤, 실행 가능한 상태와 공식 권위 상태를 분리한다.

---

## 3. 전체 구조도

```text
VectorFL internal asset cleanup map (workspace-internal / NOT_AUTHORITY)

[T/L schema lens]
   |
   v
[P_PACKET_HANDOFF_ASSET] -- CLOSED_FOR_NOW
   |  compact -> subtype -> codex no-call dedupe -> freeze/reusable/active -> receipt compact -> active brief
   v
[U_RUN_BUNDLE_ASSET] -- CLOSED_FOR_NOW
   |  compact -> subtype review -> retention rule candidate -> generated dedupe evidence map
   v
[G_GATE_GUARD_ASSET] -- SAFE_STOP_RULE_CANDIDATE
   |  compact -> subtype review -> guard rule candidate
   v
[S_STATE_PROMOTION_ASSET] -- READ_ONLY_FREEZE_MAP_SAFE_STOP
   |  inbox/candidate/matured/authority confusion map
   |  authority/registry/current-position/promotion boundary reached
   X STOP: no promotion / no registry mutation / no current-position mutation

Deferred:
  - B_BRIDGE_ADAPTER_ASSET: live external/API/tool boundary
  - X_POINTER_GRAPH_ASSET: future safer pointer-only candidate
  - cleanup apply: requires explicit approval + manifest + rollback + post-validation
```

현재 위치는 `S_STATE_PROMOTION_ASSET_READ_ONLY_FREEZE_MAP_SAFE_STOP`이다.

즉, 우리는 state/promotion/authority 경계에 도달했고, 여기서 멈춘 상태다.

---

## 4. VectorFL의 8개 기능 모듈

VectorFL은 내부적으로 다음 8개 기능 영역으로 볼 수 있다.

### M1. Intake & Provenance

입력과 출처를 보존하는 영역이다.

역할:
- 사용자의 원문, 외부 자료, 기존 파일을 원본으로 유지한다.
- 어디서 온 자료인지 기록한다.
- 원본과 파생물을 섞지 않는다.

사용자가 얻는 기능:
- “이 자료가 어디서 왔는지” 추적할 수 있다.
- 나중에 잘못된 요약이나 왜곡을 되돌릴 수 있다.

### M2. Asset Graph Router

자산 간 연결과 경로를 관리하는 영역이다.

역할:
- pointer index를 만든다.
- 어떤 파일이 어떤 파일을 참조하는지 본다.
- 이동하면 깨질 링크를 미리 찾는다.

사용자가 얻는 기능:
- 파일을 옮기기 전에 무엇이 깨질지 알 수 있다.
- 정리 순서를 안전하게 잡을 수 있다.

### M3. Guard & Precheck Engine

실행 전에 멈춰야 할 조건을 확인하는 영역이다.

역할:
- gate, guard, precheck, STOP, HOLD를 관리한다.
- 실수로 authority나 registry를 건드리지 않도록 막는다.

사용자가 얻는 기능:
- 위험한 작업을 실행 전에 차단할 수 있다.
- “지금 해도 되는 일”과 “아직 하면 안 되는 일”을 구분할 수 있다.

### M4. Maturation Governance

자산의 상태 변화를 관리하는 영역이다.

역할:
- INBOX, CANDIDATE, MATURED, AUTHORITY를 구분한다.
- 후보를 공식으로 착각하지 않게 한다.
- promotion 경계를 관리한다.

사용자가 얻는 기능:
- 아직 후보인 것을 공식 기준처럼 쓰는 실수를 줄일 수 있다.

### M5. Space Inbox Review

새로 들어온 자산을 검토 대기 공간에 넣는 영역이다.

역할:
- 외부 자료, mini-space, packet, handoff 후보를 inbox에 둔다.
- 바로 반영하지 않고 review 상태로 유지한다.

사용자가 얻는 기능:
- 새 자료를 안전하게 받아들이되, 공식 구조를 오염시키지 않는다.

### M6. Adapter Factory

VectorFL을 다른 도구 앞뒤에 붙이는 영역이다.

역할:
- YouTube, Obsidian, Codex, Gemini, Hermes, CLI 도구 등에 VectorFL 패턴을 붙인다.
- 도구별 입력/출력/검증/재진입 방식을 설계한다.

사용자가 얻는 기능:
- VectorFL을 단일 앱이 아니라 여러 도구에 붙는 레이어로 사용할 수 있다.

### M7. Asset Hygiene Operator Dashboard

정리 작업을 사람이 볼 수 있게 압축하는 영역이다.

역할:
- cleanup blocker, 위험도, operator card를 만든다.
- 지금 정리 가능한 것과 아닌 것을 나눈다.

사용자가 얻는 기능:
- 많은 자산 중 무엇을 먼저 봐야 하는지 알 수 있다.

### M8. Evaluation Trace Observability

검증, receipt, rollback, trace를 관리하는 영역이다.

역할:
- 실행 전/후 검증을 남긴다.
- sha, existence, reference, negative test를 기록한다.
- rollback과 post-validation 조건을 잡는다.

사용자가 얻는 기능:
- 어떤 작업이 실제로 안전했는지 증명할 수 있다.

---

## 5. 지금 만든 내부 자산 family

이번 정리에서 VectorFL 내부 자산은 단순히 T/L 자산만 있는 것이 아니라 여러 family로 나뉜다는 것을 확인했다.

### 5.1 T/L schema lens

T는 자산의 형태를 보는 렌즈이고, L은 자산의 층위를 보는 렌즈다.

예:
- T01_SOURCE_ORIENTATION_HANDLE
- T02_POINTER_VIEW
- T03_READONLY_COPY_VIEW
- T04_CONTROL_SURFACE
- T05_AUTHORITY_SENSITIVE_SURFACE
- T06_LACL_LAYER_CARD
- T07_MATURATION_EVIDENCE
- T08_OPERATOR_DASHBOARD_ITEM
- T09_TRACE_RECEIPT_EVIDENCE
- T10_ADAPTER_SHELL

L layer 예:
- L0_SOURCE
- L1_CONTEXT
- L2_AUTHORITY
- L3_CONTROL
- L4_MATURATION
- L5_EXECUTION_TRACE
- L6_ADAPTER_BOUNDARY

이 렌즈는 공식 권위가 아니라, 자산을 읽기 위한 분류 도구다.

### 5.2 P_PACKET_HANDOFF_ASSET

패킷과 handoff 자산이다.

예:
- Codex review packet
- Gemini queue packet
- task packet
- handoff packet
- validation packet
- inbox apply packet

활용 방법:
- 나중에 Codex나 다른 도구에 넘길 후보를 구분한다.
- 이미 끝난 receipt와 미래 후보를 분리한다.
- reusable packet pattern을 찾는다.

주의:
- packet이 있다고 해서 실제 전송된 것이 아니다.
- active candidate가 있다고 해서 Codex 호출 승인도 아니다.

현재 상태:
- CLOSED_FOR_NOW

### 5.3 U_RUN_BUNDLE_ASSET

작업 실행 결과와 기록 자산이다.

예:
- run summary
- validation file
- receipt
- closeout
- rollup
- generated report

활용 방법:
- 어떤 작업이 실제로 검증됐는지 확인한다.
- validation/receipt evidence를 보존한다.
- generated run bundle을 compact해서 operator가 볼 수 있게 한다.

주의:
- generated 파일이라고 바로 삭제하면 안 된다.
- 많은 generated bundle은 검증 증거이거나 rollback 근거다.

현재 상태:
- CLOSED_FOR_NOW

### 5.4 G_GATE_GUARD_ASSET

안전장치 자산이다.

예:
- gate
- guard
- precheck
- HOLD
- STOP
- negative test
- approval boundary

활용 방법:
- 위험 작업 전 precheck에 사용한다.
- cleanup/apply/live-call 전에 멈춤 조건을 확인한다.
- negative test를 재사용 가능한 검증 패턴으로 쓴다.

주의:
- guard는 승인서가 아니다.
- precheck가 있다고 apply가 승인된 것이 아니다.

현재 상태:
- SAFE_STOP_RULE_CANDIDATE

### 5.5 S_STATE_PROMOTION_ASSET

상태와 권위 경계 자산이다.

예:
- INBOX
- CANDIDATE
- MATURED
- AUTHORITY
- promotion
- registry
- current-position
- freeze

활용 방법:
- 후보와 권위를 분리한다.
- 무엇이 아직 검토 상태인지 확인한다.
- promotion이 필요한 지점을 표시한다.

주의:
- CANDIDATE는 authority가 아니다.
- MATURED도 authority가 아니다.
- registry/current-position 변경은 명시 승인 없이는 금지다.

현재 상태:
- READ_ONLY_FREEZE_MAP_SAFE_STOP

### 5.6 B_BRIDGE_ADAPTER_ASSET

외부 도구와 VectorFL을 연결하는 자산이다.

예:
- Codex bridge
- Gemini chain
- YouTube/VectorTube adapter
- Obsidian integration
- CLI/script runner

활용 방법:
- VectorFL을 다른 도구 앞뒤에 붙인다.
- 외부 도구의 결과를 space inbox나 reentry로 연결한다.

주의:
- live API/tool call boundary가 가깝다.
- 명시 scope 없이 실행하면 안 된다.

현재 상태:
- DEFER

### 5.7 X_POINTER_GRAPH_ASSET

자산 간 연결을 표현하는 pointer/graph 계열이다.

예:
- pointer index
- route map
- dedupe map
- conflict map
- reference map

활용 방법:
- 다음 정리 작업의 안전한 후보가 될 수 있다.
- 실제 파일 이동 없이 관계를 먼저 정리할 수 있다.

현재 상태:
- future safer pointer-only candidate

---

## 6. 사용자는 VectorFL을 어떻게 활용할 수 있는가

### 6.1 정리 전에 자산 지도를 만든다

VectorFL은 먼저 전체 자산을 보고 family를 나눈다.

사용자는 다음을 알 수 있다.

- 무엇이 원본인지
- 무엇이 실행기록인지
- 무엇이 검증증거인지
- 무엇이 후보인지
- 무엇이 authority-sensitive인지

### 6.2 파일을 옮기기 전에 link risk를 본다

VectorFL은 파일을 바로 옮기지 않는다.

먼저:
- 원본 경로 참조
- basename 참조
- copy path 참조
- control surface 참조
- move break risk

를 확인한다.

이렇게 하면 정리 후 링크나 맥락이 깨지는 것을 줄일 수 있다.

### 6.3 후보와 공식 권위를 분리한다

VectorFL은 다음 상태를 분리한다.

- INBOX: 들어온 자료
- CANDIDATE: 검토 후보
- MATURED: 성숙한 증거/구조
- AUTHORITY: 공식 기준

이 구분 덕분에 사용자는 “괜찮아 보이는 후보”를 실수로 공식 기준처럼 쓰지 않게 된다.

### 6.4 실행 흔적을 증거로 남긴다

VectorFL은 실행 결과를 receipt와 validation으로 남긴다.

예:
- 파일 존재 확인
- sha 검증
- source unchanged 확인
- negative test
- mutation statement
- rollback/post-validation 조건

이것은 나중에 정리하거나 배포하거나 승인할 때 근거가 된다.

### 6.5 외부 도구와 연결하되, 경계를 지킨다

VectorFL은 Codex, Gemini, Hermes, Obsidian, YouTube 같은 도구와 연결될 수 있다.

하지만 기본 원칙은:
- packet 먼저
- no-call 검증 먼저
- 명시 scope 전 live call 금지
- 외부 결과는 바로 authority가 아님

이다.

---

## 7. 사용 시나리오

### 시나리오 A. 흩어진 프로젝트 자산 정리

1. 전체 파일을 broad scan한다.
2. asset family를 분류한다.
3. pointer map을 만든다.
4. move risk를 본다.
5. cleanup blocker를 찾는다.
6. 명시 승인 전에는 파일을 옮기지 않는다.

결과:
- 정리할 준비는 되지만, 위험한 이동은 막힌다.

### 시나리오 B. Codex에 넘길 리뷰 패킷 준비

1. packet/handoff 자산을 찾는다.
2. active candidate와 stale receipt를 분리한다.
3. reusable pattern을 찾는다.
4. no-call brief를 만든다.
5. 사용자가 명시적으로 승인하기 전에는 Codex로 보내지 않는다.

결과:
- Codex 사용 비용과 위험을 줄이고, 필요한 packet만 선별할 수 있다.

### 시나리오 C. 실행 기록을 정리하고 싶을 때

1. run bundle을 compact한다.
2. validation/receipt/closeout/rollup을 분리한다.
3. generated summary 중복을 evidence map으로 본다.
4. 삭제하지 않고 retention rule 후보를 만든다.

결과:
- 중요한 검증 증거를 잃지 않고 실행 기록을 정리할 수 있다.

### 시나리오 D. 공식 상태를 정하기 전

1. INBOX/CANDIDATE/MATURED/AUTHORITY 언어를 검색한다.
2. 혼동 위험을 찾는다.
3. freeze map을 만든다.
4. promotion이나 registry 변경은 명시 승인 전 HOLD한다.

결과:
- 후보와 공식 기준이 섞이는 것을 막을 수 있다.

---

## 8. 현재 우리가 만든 것의 의미

우리는 아직 최종 제품을 만든 것이 아니다.

하지만 다음을 만들었다.

- VectorFL 구조 지도
- 자산 family taxonomy
- T/L schema lens
- packet/handoff 정리 흐름
- run bundle retention rule 후보
- guard rule 후보
- state/promotion freeze map
- current position map
- STOP_AND_REVIEW closeout

이것은 제품화 전에 필요한 “공간 이해와 안전 경계”다.

---

## 9. 현재 위치와 다음 작업

현재 위치:

```text
S_STATE_PROMOTION_ASSET_READ_ONLY_FREEZE_MAP_SAFE_STOP
```

즉:
- state/promotion/authority 경계에 도달했다.
- 더 진행하면 공식 policy, promotion, registry mutation으로 오해될 수 있다.
- 그래서 STOP_AND_REVIEW로 마무리했다.

다음 추천 작업:

```text
X_POINTER_GRAPH_ASSET_POINTER_ONLY_MAP
```

이유:
- 지금 만든 자산 family들을 연결할 수 있다.
- live API/tool boundary가 아니다.
- authority mutation도 아니다.
- 다음 구조화 작업으로 비교적 안전하다.

보류할 작업:

```text
B_BRIDGE_ADAPTER_ASSET
```

이유:
- 외부 도구/API/live call 경계가 가깝다.
- 다음 세션에서 명시 scope를 잡고 하는 것이 안전하다.

아직 금지된 작업:

- cleanup apply
- file move
- archive
- delete
- source edit
- promotion
- registry mutation
- current-position mutation
- live external call

---

## 10. 문서 요약

VectorFL은 “정리 전에 이해하는 시스템”이다.

그것은 파일을 바로 옮기지 않고, 먼저 다음을 만든다.

- map
- pointer
- evidence
- guard
- freeze
- receipt
- operator view

사용자는 이것을 통해:

- 어떤 자산이 중요한지
- 어떤 자산이 위험한지
- 무엇을 다음에 볼지
- 어디서 멈춰야 하는지
- 어떤 작업이 실제 승인 전까지 HOLD인지

알 수 있다.

현재 우리가 만든 VectorFL은 아직 authority가 아니다.
하지만 내부 자산을 안전하게 읽고, 구조화하고, 다음 작업으로 넘길 수 있는 작업대는 만들어졌다.

---

## 부록 A. 현재 하드 HOLD

현재 모든 산출물은 다음 HOLD를 따른다.

- NO_MOVE
- NO_ARCHIVE
- NO_DELETE
- NO_SOURCE_EDIT
- NO_PROMOTION
- NO_AUTHORITY_MUTATION
- NO_REGISTRY_MUTATION
- NO_CURRENT_POSITION_MUTATION
- NO_CLEANUP_APPLY
- NO_LIVE_EXTERNAL_CALL

---

## 부록 B. 근거 파일

이 문서는 다음 workspace evidence를 바탕으로 작성되었다.

- internal asset family map:
  `/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/internal_asset_family_map_and_position_rollup_v0.json`

- ASCII map:
  `/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/internal_asset_family_map_ascii_v0.txt`

- STOP_AND_REVIEW closeout:
  `/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/internal_asset_cleanup_stop_and_review_closeout_v0.json`

- final validation:
  `/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260525_internal_asset_cleanup_stop_and_review_closeout_v0/validation/02_validation_internal_asset_cleanup_stop_and_review_closeout_v0.json`
