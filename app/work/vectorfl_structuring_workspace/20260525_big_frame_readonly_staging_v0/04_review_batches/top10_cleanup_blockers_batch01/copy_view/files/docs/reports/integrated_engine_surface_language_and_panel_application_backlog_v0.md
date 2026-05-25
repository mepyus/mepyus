# Integrated Engine Surface Language And Panel Application Backlog v0

## Verdict

READY_BUT_NOT_APPLIED

## Purpose

This backlog translates the 2026-04-17 source notes into implementation candidates.

No UI patch is applied in this document. It exists so the next patch can be bounded and does not accidentally become final glossary work.

## Surface Language Rule

Every active core panel should use a 3-layer language structure:

1. large title: human-readable language
2. one-line explanation: why this panel matters now
3. small badge / helper text: internal label

Locked rule:

```text
human-readable phrase first; internal term as badge
```

## Active Core Mapping

| current component | current role | locked interpretation | surface human language candidate | internal label |
| --- | --- | --- | --- | --- |
| `VectorFLIntegrationShell.tsx` | 3-surface shell | work-packet operating shell | 통합 작업 화면 | `integrated_engine_shell` |
| `CommandHeaderPanel` | header | work identity header | 현재 작업 | `task_identity` |
| `FlowSummaryPanel` | summary | work lifecycle summary | 작업 흐름 요약 | `flow_summary` |
| `ExecutionRoutePanel` | route/support | current position and next route judgment | 다음 이동 방향 | `route_candidate` |
| `CliHostControlPanel` | Codex control | operator slot | 작업 도구 | `operator_slot` |
| `UserCliAssignmentPanel` | user-side CLI return | assignment candidate slot | 사용자 확인/배정 | `user_assignment_candidate` |
| `InternalTeamAssignmentPanel` | team/role manager | assignee selection slot | 담당/팀 지정 | `assignment` |
| `VectorFLValidationQueuePanel` | validation/reread queue | reread slot | 다시 볼 항목 | `vectorfl_reread` |
| `EngineCliReturnPanel` | engine CLI return | process candidate / return material slot | 엔진 검토/반환 | `engine_request_candidate` |
| `OperationLogPanel` | log | work memory layer | 작업 기록 | `transition_log` |

## Support Mapping

| current component | support interpretation | surface human language candidate |
| --- | --- | --- |
| `AssetInventoryPanel` | internal asset evidence | 관련 자료 |
| `AssetInspectorPanel` | internal asset detail evidence | 관련 자료 상세 |
| `WatchpointRegistryPanel` | warning / failure evidence | 주의/실패 흔적 |
| `BridgePanel` | movement / connection trace | 연결 기록 |
| `OperationConsolePanel` | internal process support | 내부 공정 정보 |

## Hold Mapping

These should not become front-facing core before a separate promotion gate:

| current component | hold reason | surface language if shown |
| --- | --- | --- |
| `TeamRoutingPanel` | overlaps with current team/role desk | 보류: 팀 흐름 설정 |
| `RoleConfigurationPanel` | overlaps with current role setup | 보류: 역할 설정 |
| `SupervisorQueuePanel` | risks governance/control-room drift | 보류: 감독 항목 |
| other mock-derived panels | unclear current packet role | 보류 / 참조 |

## Candidate Button Language

| current/internal phrase | human-facing candidate | note |
| --- | --- | --- |
| `Run Codex` | 작업 보내기 | internal "Codex" may remain as tool badge |
| `Send Codex Turn` | 작업 보내기 | do not hide backend, but do not make backend the title |
| `user_assignment_candidate` | 사용자 확인/배정 후보로 두기 | candidate, not assignment completion |
| `engine_request_candidate` | 엔진 처리 검토 후보로 두기 | candidate, not execution |
| `validation_target` | 다시 검토 대상으로 두기 | target, not validated |
| `deposit_candidate` | 보관 후보로 두기 | candidate, not ingested |
| `not_ingested` | 아직 보관 안 됨 | state boundary |
| `hold` | 보류하기 | not deletion |

## Patch Order

Recommended bounded order:

1. Active core titles and one-line descriptions only.
2. Route / candidate / queue button language.
3. Internal labels moved into badges.
4. Support panel human-language names if/when they are shown.
5. Hold panels hidden or labeled as hold/support, not deleted.

## Do Not Do In This Patch Family

- do not erase internal labels
- do not finalize a glossary
- do not translate all internal engine language
- do not delete old panels
- do not add a new surface
- do not open Gemini adapter
- do not add persistence as part of language cleanup

## Implementation Gate

Before applying these language changes, run one quick screen audit:

- Does the panel still show the correct surface role?
- Does the human title reduce confusion?
- Does the internal badge preserve route/state meaning?
- Does the change avoid final glossary lock?

