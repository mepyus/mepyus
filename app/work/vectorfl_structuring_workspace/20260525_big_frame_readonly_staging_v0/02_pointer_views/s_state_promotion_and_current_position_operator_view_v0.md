# S_STATE_PROMOTION + CURRENT POSITION

status: READ_ONLY_FREEZE_MAP / NOT_AUTHORITY / SAFE_STOP

scan_count: 9000

## state disposition
- GENERAL_STATE_POINTER_REVIEW: 793
- NOT_AUTHORITY_HOLD_STATE_EVIDENCE: 524
- AUTHORITY_REGISTRY_CURRENT_POSITION_FREEZE: 3464
- PROMOTION_STATE_FREEZE: 702
- INBOX_CANDIDATE_CONFUSION_MAP: 3517

## confusion distribution
- STATE_LANGUAGE_PRESENT: 2371
- CANDIDATE_AUTHORITY_CONFUSION_RISK: 2070
- INBOX_CANDIDATE_BOUNDARY_RISK: 3533
- REGISTRY_CURRENT_POSITION_RISK: 1007
- MATURED_AUTHORITY_CONFUSION_RISK: 19

## boundary rules
- SS_R01_INBOX_IS_NOT_CANDIDATE: INBOX는 들어온/보류된 입력 상태이며 CANDIDATE 승격이 아님
- SS_R02_CANDIDATE_IS_NOT_AUTHORITY: CANDIDATE는 검토 후보일 뿐 source-of-truth/authority가 아님
- SS_R03_MATURED_IS_NOT_AUTHORITY: MATURED는 성숙 evidence이며 authority registry mutation 전 상태
- SS_R04_AUTHORITY_REGISTRY_CURRENT_POSITION_REQUIRE_EXPLICIT_SCOPE: authority/registry/current-position 변경은 별도 명시 승인 전 금지
- SS_R05_FREEZE_MAP_IS_EVIDENCE_ONLY: freeze map은 차단/분류 evidence이며 promotion/apply 권한이 아님

## map
```
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
