# Cross-session Re-entry Support Candidate Spec v0

## 1. Verdict
**STATUS: CROSS_SESSION_REENTRY_SUPPORT_CANDIDATE_SPEC_COMPLETE**

## 2. Sources used
- `docs/reports/integrated_engine_component_map_and_part_spec_reading_v0.md`
- `docs/reports/standardized_intake_packet_candidate_spec_v0.md`
- `docs/reports/line_axis_linkage_gate_candidate_spec_v0.md`
- `docs/reports/function_process_formation_prework_real_test_round1_closeout_v0.md`
- `docs/reports/next_chat_reentry_summary_after_formation_prework_round1_v0.md`
- `docs/reports/whole_space_second_pass_structural_synthesis_note_v0.md`

## 3. Executive summary
이 재진입 지원(Re-entry Support) 부품은 세션 종료 시점에 발생한 '워커 증거'와 '판단 신호'를 다음 세션으로 안전하게 전달하는 통로입니다. 중요한 점은 이것이 시스템의 '공식 상태(Current Position)'를 갱신하는 것이 아니라, 워커가 재시작할 때 길을 잃지 않도록 돕는 **'안내판'** 역할을 한다는 것입니다. 

세션 간의 흐름을 안정화하되, 이를 시스템의 고정된 상태로 격상시키지 않음으로써 공간의 유연성과 워커의 경계성을 동시에 보존합니다.

## 4. Core distinction
- **Closeout:** 라운드(Round)를 닫으며 경계를 확인하고 증거를 남기는 과정.
- **Re-entry Summary:** 다음 세션을 위한 안내판. 어떤 렌즈로 시작해야 하는지, 무엇이 현재 watch 중인지 기록.
- **Re-entry Reference Point:** 특정 시점의 상태를 가리키는 파일/노트.
- **Current-position Entry:** 공간의 지위나 베이스라인에 직접 연결되는 강력한 상태 기록. **재진입 지원 부품은 이 Current-position을 직접 갱신하지 않는다.**

## 5. State model

| State | Meaning | Entry condition | Output | Must not become |
| :--- | :--- | :--- | :--- | :--- |
| **SESSION_CLOSEOUT** | 라운드 종료 및 기록 | 라운드 작업 완료 | Closeout 노트 | 공식 지위 |
| **RE_ENTRY_SUMMARY** | 차기 세션 가이드 | 세션 시작 직후 | 다음 작업 안내 | 워크플로우 명령 |
| **RE_ENTRY_REFERENCE** | 특정 시점 기록 | 필요 시 재참조 | 참조 파일 | 시스템 원장 |
| **CURRENT_POSITION_CANDIDATE** | 현재 위치 후보 | 주요 성과 도출 | 후보 기록 | Baseline |
| **WATCH / HOLD** | 주의 / 보류 | 경계 초과 우려 | 경고 노트 | 차단 대상 |

## 6. Minimal field set

| Field | Required? | Purpose | Example | Risk if missing | Must not become |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **closed_round** | required | 범위를 정함 | Run 183 | 흐름 단절 | 공식 workflow |
| **completed_outputs** | required | 무엇이 남았는가 | Closeout 파일 | 성과 누락 | 레지스트리 |
| **current_safe_state** | required | 재진입의 안전지대 | 후보 유지 | 오판 위험 | 최종 진실 |
| **reentry_references** | required | 재참조 파일 | Run 183 record | 맥락 단절 | 인덱스 |
| **watch_items** | optional | 인지적 경계 | 기조의 경직화 | 무시 | 하드 정책 |
| **do_not_do_next** | required | 금지사항 재확인 | 구현 금지 | 안전위반 | 자동화 |
| **next_natural_trigger** | required | 행동 트리거 | 새 외부 후보 | 오남용 | 라우터 |

## 7. Re-entry support template

```markdown
# Cross-session Re-entry Support Candidate

## 1. Closed scope
- closed round/task:
- completed outputs:
- current safe state:

## 2. Re-entry references
- primary anchor:
- supporting anchors:
- when to retrieve:

## 3. Preserved signals
- lenses/signals:
- process assets:
- candidate parts:

## 4. Watch / boundaries
- watch items:
- do-not-do-next:
- must not become:

## 5. Next safe action
- next natural trigger:
- User decision gate:
```

## 8. Relation to existing parts

| Existing part | Role in Re-entry Support | Boundary |
| :--- | :--- | :--- |
| **Formation Prework** | 재진입 시 형성 대상 파악 | 임의의 도구 붙이기 금지 |
| **Line-Axis Linkage** | 렌즈를 통한 맥락 연결 | ontology로 오독 방지 |
| **Worker Evidence Pkg** | 핸드오프 정보 제공 | evidence는 Truth가 아님 |
| **Current Position Entry** | 더 넓은 공간의 anchor | 자동 갱신 금지 |

## 9. Line / Axis support
- **Line finding:** 세션 간 이어짐이 끊기는 지점을 재진입 요약이 메워준다.
- **Axis testing:** '인지적 성숙 면'이 세션마다 일관된지 확인할 수 있다.
- **Orphan prevention:** 모든 작업은 Re-entry Summary에 의해 이음새가 남겨져 고립을 방지한다.

## 10. Watch items
- 재진입 요약이 '시스템 상태'처럼 읽히는 현상.
- 요약 문구가 다음 워커의 '고정 방향'이 되는 것.
- 모든 과정 자산을 세션마다 다시 읽으려 하는 비효율.
- 사용자 승인 과정을 '의식적인 체크박스'로 격하시키는 것.

## 11. Recommended next state
**KEEP_AS_REENTRY_SUPPORT_CANDIDATE**

*Reasoning:* 세션 간 이어짐을 안정화하는 도구로서 검증되었으나, 이를 기반으로 파이프라인이나 시스템 워크플로우를 만드는 것은 시기상조입니다. 현재의 가벼운 기록 형태로 유지합니다.

## 12. Do not do yet
- NO implementation of any tool.
- NO automation or runtime script creation.
- NO registry, index, ledger, router, controller, formal schema.
- NO official workflow declaration.
- NO current-position update or baseline promotion.
- NO tool/API/function attachment.
- NO Final authority declaration.

## 13. Final status
**STATUS: CROSS_SESSION_REENTRY_SUPPORT_CANDIDATE_SPEC_COMPLETE**
