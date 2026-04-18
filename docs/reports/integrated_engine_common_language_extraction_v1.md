# Integrated Engine Common Language Extraction v1

Date: 2026-04-14

## Purpose

이 문서는 통합엔진을 새로 설계하기 위한 문서가 아니다. 현재 공간 안에 축적된 언어 재료에서 통합엔진 셋업과 assistant 해석 안정성에 바로 쓸 수 있는 공통 언어층 후보를 추출한 목적형 탐색 결과다.

읽은 주요 재료:

- `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md`
- `docs/specs/integrated_engine_surface_object_contracts_v0.md`
- `docs/specs/line_contracts_consolidated_draft_v0.md`
- `docs/specs/line_contract_axes_v0.md`
- `docs/specs/integrated_engine_operating_methodology_direction_v0.md`
- `docs/baselines/concept_to_implementation_map_baseline_v0.md`
- `docs/baselines/phase_transition_and_hold_rule_implementation_baseline_v0.md`
- `docs/reviews/vectorfl_gemma4_sidecar_prototype_v0.md`
- `docs/examples/example_connection_translation_first_refinement_v1.md`
- `app/work/current_layer_baseline/engine_philosophy_declaration_v1.md`
- `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md`
- `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md`

---

## Dataset 1. Track A

Fields: `raw_expression`, `interpreted_meaning`, `bucket`, `related_surface`, `related_line_or_axis`, `human_rewrite`, `why_useful_now`, `unresolved`, `source_refs`, `repetition_signal`, `high_overlap`

### Bucket A. 3면 설명 언어

| raw_expression | interpreted_meaning | bucket | related_surface | related_line_or_axis | human_rewrite | why_useful_now | unresolved | source_refs | repetition_signal | high_overlap |
|---|---|---|---|---|---|---|---|---|---|---|
| `사용자면 = 목적 선언 + 팀 운영 표면` | 사용자면은 목적 선언이 먼저이고 팀/운영은 그 뒤에 붙는 표면이다. | A | 사용자면 | goal / scope / team extension | 사용자가 무엇을 하려는지 먼저 세우고, 필요하면 사람/팀 흐름을 붙이는 면 | 기존 문서에는 팀 운영이 강하게 붙어 있어 현재 기준에서는 골격과 확장층을 분리해 읽게 해준다. | 팀 운영을 본체로 볼지 확장층으로 볼지는 현 기준에서 확장층으로 둔다. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:18`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:20`, `docs/specs/integrated_engine_operating_methodology_direction_v0.md:37` | high | yes |
| `사용자면은 task board가 아니라 운영 선언면이므로, 목적이 항상 팀보다 먼저 와야 한다.` | 사용자면의 주축은 카드/작업판이 아니라 목적 선언이다. | A | 사용자면 | goal / scope | 먼저 “무엇을 왜 어디까지 할지”를 세우고, 팀 배치는 그 뒤에 온다. | 사용자면이 Team Relay Board로 납작해지는 것을 막는 즉시 사용 가능한 문장이다. | “운영 선언면”의 운영 범위는 추가 정리 필요. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:87`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:89` | high | yes |
| `현재 목적이 어떤 공간 재료와 연결되어 있는지 보여주는 요약 영역` | 사용자면은 추상 목표만 아니라 목표가 얹힌 재료 문맥을 보여줘야 한다. | A | 사용자면 | material_context / linked_ingest | 이 목표가 맨땅에서 나온 것인지, 어떤 재료 위에서 나온 것인지 함께 본다. | Material Context를 사용자면 본체 골격으로 남기는 데 바로 쓸 수 있다. | linked_ingest_ids를 사용자면 1차 노출로 둘지는 open. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:97`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:101`, `docs/specs/integrated_engine_surface_object_contracts_v0.md:95` | medium | yes |
| `벡터플면 = 중간 흐름 / 통로 표면` | 벡터플면은 사용자 목적이 엔진 처리로 바로 떨어지기 전의 중간 판독 통로다. | A | 벡터플면 | line / relation / gap / pending | 요청을 바로 실행하지 않고, 중간 흐름으로 읽고 정리하는 면 | 3면 사이에서 벡터플면을 끼워 넣는 핵심 설명이다. | “통로”가 workflow hub로 오해될 수 있어 “중간 형성체 판독”과 함께 써야 한다. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:21`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:191`, `docs/specs/integrated_engine_operating_methodology_direction_v0.md:56` | high | yes |
| `사용자 작업과 엔진 처리 사이에서 현재 line / relation / gap / genealogy / ingress / reflux 상태를 드러내는 중간 통로` | 벡터플면은 사용자면과 엔진면 사이에서 line과 gap의 상태를 드러낸다. | A | 벡터플면 | line / relation / gap / reflux | 사용자 요청이 지금 어떤 라인, 연결, 빈칸, 되돌아옴으로 보이는지 읽는 곳 | 사용자면과 엔진면 직접 연결을 막는 설명 문장으로 유용하다. | genealogy가 현재 최소 공통 언어에 계속 들어갈지는 추가 판단 필요. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:189`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:191` | high | yes |
| `벡터플면은 예쁜 relation web이 아니라, 현재 흐름에서 어디가 얇고 어디를 보강해야 하는지를 보여주는 면이다.` | 벡터플면은 시각화보다 보강 지점 판독이 중요하다. | A | 벡터플면 | relation / gap | 멋진 관계 그림이 아니라, 어디가 약하고 무엇을 더 봐야 하는지 알려주는 면 | UI/문서 셋업에서 relation web을 목적 없이 키우지 않게 한다. | “보강”이 자동 실행으로 읽히지 않도록 read/interpret 중심으로 제한 필요. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:276`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:278` | medium | yes |
| `엔진면 = 입력 / 처리 / 환류 컨트롤 표면` | 엔진면은 입력과 처리뿐 아니라 환류까지 다루는 바닥 처리면이다. | A | 엔진면 | ingest / pipeline / validation_return | 재료를 받고, 처리 흐름을 보고, 검증 결과를 다시 재료로 돌리는 면 | 엔진면을 단순 결과 생성기나 admin dashboard로 오해하지 않게 한다. | “컨트롤”이 직접 실행 권한으로 오해될 수 있어 현재는 read/control surface로 제한. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:22`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:323`, `docs/specs/integrated_engine_operating_methodology_direction_v0.md:78` | high | yes |
| `입력이 들어온 뒤, 엔진면의 본질은 그 입력이 현재 어떤 처리 단계를 지나고 있는지 보여주는 데 있다.` | 엔진면은 파이프라인 상태를 보여주는 처리 흐름 표면이다. | A | 엔진면 | pipeline_status / current_step | 들어온 재료가 어디까지 처리됐고 어디서 멈췄는지 보는 면 | Pipeline Status 설명으로 바로 쓸 수 있다. | 처리 상태가 실행 버튼으로 확장되는 것은 현재 금지. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:382`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:384` | medium | no |
| `엔진면은 입력과 처리만이 아니라 환류를 다시 공간으로 넣는 면` | 엔진면의 반환은 결과 표시가 아니라 재료 환류까지 포함한다. | A | 엔진면 | validation_return / reingest | 처리 결과를 끝내는 곳이 아니라 다시 공간 재료로 돌려보내는 곳 | 반환/환류 언어와 3면 설명이 겹치는 high-overlap 문장이다. | auto reingest는 아직 제외. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:411`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:413` | high | yes |
| `secondary surface에서 보이는 contract는 summary consumption만 허용한다. owning surface가 바뀌는 것은 아니다.` | 한 면에 다른 면의 요약이 보여도 소유 면은 이동하지 않는다. | A | cross-surface | surface ownership | 다른 면의 요약을 볼 수는 있지만, 그 면의 주인공이 바뀌는 것은 아니다. | 3면 역할 혼합을 방지하는 운영 언어로 바로 쓸 수 있다. | summary 범위는 실제 화면 연결 때 더 좁혀야 한다. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:483`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:485`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:492` | high | yes |
| `사용자면에 엔진 inventory를 주인공으로 놓지 않는다. 벡터플면에 팀 운영을 주인공으로 놓지 않는다. 엔진면에 목적 선언을 주인공으로 놓지 않는다.` | 각 면의 주인공을 바꾸지 말라는 3면 경계 문법이다. | A | cross-surface | ownership / boundary | 사용자면은 목적, 벡터플면은 중간 판독, 엔진면은 처리/환류를 주인공으로 둔다. | assistant가 UI/문서 제안할 때 면 혼합을 빠르게 감지하게 한다. | 팀 운영이 사용자면 확장층으로 남을 때의 표현은 조정 필요. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:494`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:498` | high | yes |
| `시나리오를 루트로 삼아 현재 위치를 찍고, 다음 목표만 잘라 움직이며, 그 과정 자체를 다시 공간의 재료와 기억으로 축적` | 3면 운영은 한 번에 전체 구현이 아니라 현재 위치, 다음 목표, 과정 기억을 남기는 반복이다. | A | cross-surface | cycle / memory | 지금 어디인지 보고, 다음 한 단계만 움직이고, 그 과정도 다시 재료로 남긴다. | 3면 순환 전체 설명 후보로 유용하다. | 팀 숙성 시나리오는 현재 골격보다 미래층 비중이 있어 절제 필요. | `docs/specs/integrated_engine_operating_methodology_direction_v0.md:152`, `docs/specs/integrated_engine_operating_methodology_direction_v0.md:154` | high | yes |

### Bucket B. line / 축 설명 언어

| raw_expression | interpreted_meaning | bucket | related_surface | related_line_or_axis | human_rewrite | why_useful_now | unresolved | source_refs | repetition_signal | high_overlap |
|---|---|---|---|---|---|---|---|---|---|---|
| `원재료와 최종 개념 사이를 매개하며, 여러 단서·관계·공백·압력을 묶어 다음 해석·판단·작업·검증·환류를 유발하는 지속 가능한 중간 운용 형성체` | line의 가장 강한 공식 정의 후보다. | B | 벡터플면 | line / relation / gap / reflux | 라인은 원자료와 결론 사이에서 여러 단서와 빈칸을 묶어 다음 판단과 작업을 일으키는 중간 단위다. | line을 카드/문장조각이 아니라 중간 운용 형성체로 설명하는 핵심 문장이다. | 길어서 CLI 입력 문법에는 축약형 필요. | `docs/specs/line_contracts_consolidated_draft_v0.md:20`, `docs/specs/line_contracts_consolidated_draft_v0.md:22`, `docs/specs/line_contracts_consolidated_draft_v0.md:264` | high | yes |
| `라인은 문장도, chunk도, 문서도, 티켓도, 위키 페이지도, 처음부터 고정된 객체도 아니다.` | line의 비정의를 통해 과잉 고정을 막는다. | B | 벡터플면 | line boundary | 라인은 텍스트 조각이나 티켓 같은 완성 객체가 아니다. | assistant가 line을 DB entity나 task ticket으로 조기 변환하지 않게 한다. | “아니다” 다음의 운영 정의를 항상 함께 붙여야 한다. | `docs/specs/line_contracts_consolidated_draft_v0.md:32`, `docs/specs/line_contracts_consolidated_draft_v0.md:34` | high | yes |
| `의미를 담아두는 저장 단위가 아니라, 다음 처리와 개념 형성을 유도하는 운용 단위` | line은 storage보다 activation/operation 단위다. | B | 벡터플면 | operating_line | 라인은 저장칸이 아니라 다음 읽기와 처리를 움직이게 하는 단위다. | line을 viewer item이 아니라 작동 단위로 읽게 한다. | 실행 명령과 혼동하지 않도록 “유도”로 제한. | `docs/specs/line_contracts_consolidated_draft_v0.md:36`, `docs/specs/line_contracts_consolidated_draft_v0.md:38` | high | yes |
| `raw도 final도 아닌 사이에 있으며, 그 사이를 매개한다.` | line의 중간성을 가장 쉬운 말로 드러낸다. | B | 벡터플면 | line / middle formation | 라인은 날것도 최종 결론도 아닌 사이 단계다. | 사람 말로 바로 쓸 수 있는 line 정의다. | 너무 짧아 relation/gap 요소를 함께 붙이는 편이 안전. | `docs/specs/line_contracts_consolidated_draft_v0.md:50`, `docs/specs/line_contracts_consolidated_draft_v0.md:52` | high | yes |
| `라인은 반드시 무엇과 무엇을 잇는다.` | relation이 line의 최소 성질이다. | B | 벡터플면 | relation | 라인이라면 적어도 두 무언가를 이어야 한다. | relation/gap field의 판단 기준으로 간단히 쓸 수 있다. | 연결의 강도/종류는 line axes로 보강 필요. | `docs/specs/line_contracts_consolidated_draft_v0.md:53`, `docs/specs/line_contracts_consolidated_draft_v0.md:54` | medium | yes |
| `공백, 긴장, unresolved 상태도 품는다.` | line은 연결뿐 아니라 미결 상태도 보존한다. | B | 벡터플면 | gap / unresolved | 라인은 이어진 것뿐 아니라 아직 비어 있거나 걸리는 부분도 함께 품는다. | gap을 결함이 아니라 line의 의미 요소로 읽게 한다. | gap과 blocker의 차이는 더 분리 필요. | `docs/specs/line_contracts_consolidated_draft_v0.md:55` | high | yes |
| `anchor_refs = line의 발판 ... memory_trace_ref = line의 환류 가능성` | line 필드를 사람 말 축으로 번역한 후보군이다. | B | 벡터플면 | anchor / pressure / relation / gap / stage / maturity / memory_trace | 라인은 발판, 현재 압력, 중심 연결, 미완성, 시간, 방향, 숙성도, 다시 불릴 흔적을 가진다. | line object를 스키마가 아니라 해석 문법으로 설명할 수 있다. | 필드명은 final schema가 아님. | `docs/specs/line_contracts_consolidated_draft_v0.md:127`, `docs/specs/line_contracts_consolidated_draft_v0.md:137` | high | yes |
| `stage는 시간축이고, maturity는 숙성축이다. 둘은 같이 움직일 수 있지만 동일하지 않다.` | current_stage와 maturity_level 분리의 핵심 문장이다. | B | 벡터플면 | current_stage / maturity_level | 지금 어느 단계인지와 얼마나 익었는지는 다르다. | assistant가 stage 상승을 성공으로 과잉 판정하지 않게 한다. | stage 후보와 maturity 후보는 아직 실행 모델이 아님. | `docs/specs/line_contracts_consolidated_draft_v0.md:145`, `docs/specs/line_contracts_consolidated_draft_v0.md:150`, `docs/specs/line_contracts_consolidated_draft_v0.md:272` | high | yes |
| `stage가 오른다고 무조건 좋은 것이 아니다. promotion이 늦는 것이 실패도 아니다.` | line lifecycle을 성과 게임으로 오해하지 않게 한다. | B | 벡터플면 | stage / promotion | 다음 단계로 빨리 올라가는 것만 좋은 게 아니고, 승격이 늦어도 실패는 아니다. | hold/reflux/promoted 판단을 안정화한다. | 어떤 경우에 promotion_ready인지 추가 증거 필요. | `docs/specs/line_contracts_consolidated_draft_v0.md:171`, `docs/specs/line_contracts_consolidated_draft_v0.md:174` | high | yes |
| `hold는 rejection이 아니라 숙성 보호 상태다.` | hold를 실패가 아닌 보존 상태로 읽는 핵심 표현이다. | B | 벡터플면 / 엔진면 | hold / maturity | 보류는 버림이 아니라 더 익을 시간을 주는 상태다. | Dataset A/C와 B 모두에 걸치는 high-overlap 운영 문장이다. | hold record 조건은 별도 문법으로 보강 필요. | `docs/specs/line_contracts_consolidated_draft_v0.md:175`, `docs/baselines/concept_to_implementation_map_baseline_v0.md:480`, `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md:8` | high | yes |
| `reflux는 후퇴가 아니라 재형성 루프다.` | reflux는 실패 복귀가 아니라 다시 형성되는 순환이다. | B | 벡터플면 / 엔진면 | reflux / reingest | 되돌아온 것은 물러난 게 아니라 다시 모양을 잡는 루프에 들어간 것이다. | 반환/환류 언어와 line lifecycle을 연결한다. | reflux와 reingest의 경계는 더 정리 필요. | `docs/specs/line_contracts_consolidated_draft_v0.md:176` | high | yes |
| `라인은 더 이상 막연한 단일 표현으로 두지 않고, Origin / Meaning / Operating Role / Maturity의 최소 4축으로 함께 읽는 재사용 가능한 공간 단위` | line을 typed interpretation으로 읽는 축 문법이다. | B | 벡터플면 / assistant layer | origin / meaning / operating_role / maturity | 라인은 어디서 왔고, 무슨 뜻이고, 지금 어디에 쓰이며, 얼마나 익었는지 함께 읽는다. | assistant 입력 문법으로 바로 적립 가능하다. | 네 축이 final schema는 아님. | `docs/specs/line_contract_axes_v0.md:21`, `docs/specs/line_contract_axes_v0.md:32`, `docs/specs/line_contract_axes_v0.md:248`, `docs/specs/line_contract_axes_v0.md:259` | high | yes |
| `line을 철학어로 유지하는 것은 괜찮지만, 실행/지시/로그에서는 반드시 분절된 문법으로 내려야 한다.` | user-facing line과 internal typed line을 분리하라는 번역 문법이다. | B | 벡터플면 / 도구층 | line grammar | 겉으로는 “라인”이라고 말해도, 실행과 로그에서는 어떤 라인인지 쪼개 써야 한다. | CLI/assistant가 line을 애매하게 처리하지 않게 한다. | 분절 명사 체계는 프로토타입 후보이며 최종 아님. | `docs/reviews/vectorfl_gemma4_sidecar_prototype_v0.md:137`, `docs/reviews/vectorfl_gemma4_sidecar_prototype_v0.md:156` | high | yes |

### Bucket C. 반환 / 환류 설명 언어

| raw_expression | interpreted_meaning | bucket | related_surface | related_line_or_axis | human_rewrite | why_useful_now | unresolved | source_refs | repetition_signal | high_overlap |
|---|---|---|---|---|---|---|---|---|---|---|
| `검증 결과와 과정 잔여물이 다시 공간 재료가 되는 환류 입구` | Validation Return은 pass/fail 표시가 아니라 잔여물 재료화 입구다. | C | 엔진면 | validation_return / residue | 검증에서 나온 결과와 남은 것들을 다시 공간에 넣는 입구 | 엔진면 Validation Return 섹션 설명으로 바로 쓸 수 있다. | “과정 잔여물”의 최소 필드는 더 정리 필요. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:393`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:397` | high | yes |
| `검증이 단순 pass/fail 판정으로 끝나지 않고, 어떤 판단과 잔여물이 다시 공간에 들어갈 가치가 있는지 드러내기 위해 필요하다.` | 반환은 판단/잔여물의 재투입 가치 평가다. | C | 엔진면 | validation_return / accepted_refs / hold_refs | 검증은 통과/실패를 찍는 게 아니라 무엇을 다시 재료로 삼을지 가르는 일이다. | pass/fail UI로 축소되는 것을 막는다. | accepted/hold/reingest 상태값은 아직 final enum 아님. | `docs/specs/integrated_engine_surface_object_contracts_v0.md:373`, `docs/specs/integrated_engine_surface_object_contracts_v0.md:390` | high | yes |
| `accepted_refs`, `hold_refs`, `next_reingest_requested` | 반환 패킷의 최소 운영 어휘 후보다. | C | 엔진면 | accepted / hold / reingest | 받아들일 것, 보류할 것, 다시 넣을 요청을 나눠 본다. | CLI 결과 보고와 engine surface 표현에 바로 쓸 수 있다. | 실제 값의 생명주기와 freshness gate는 별도 필요. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:403`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:409`, `docs/specs/integrated_engine_surface_object_contracts_v0.md:392`, `docs/specs/integrated_engine_surface_object_contracts_v0.md:404` | high | yes |
| `작업 과정 자체가 공간의 기억이 된다.` | 과정 기록도 결과와 같은 환류 재료다. | C | 엔진면 / cross-surface | trace / memory | 결과만 남기는 게 아니라, 어떻게 판단했는지도 다음 재료가 된다. | assistant 보고/close-out을 공간 재료로 남기는 기준이다. | 어느 과정까지 남길지 저장 정책은 추가 필요. | `docs/specs/integrated_engine_operating_methodology_direction_v0.md:123`, `docs/specs/integrated_engine_operating_methodology_direction_v0.md:139` | high | yes |
| `결과뿐 아니라 과정 전체를 재료로 먹고 숙성된다.` | 공간은 산출물과 절차 기억을 함께 흡수한다. | C | cross-surface | memory / maturation | 공간은 결과만이 아니라 과정까지 먹고 다음 판단으로 익힌다. | 3면 순환 설명의 반환부에 바로 쓸 수 있다. | “먹고”는 사람 말에서는 “다시 재료로 삼는다”로 순화 가능. | `docs/specs/integrated_engine_operating_methodology_direction_v0.md:26`, `docs/specs/integrated_engine_operating_methodology_direction_v0.md:29` | high | yes |
| `출력값은 판독의 끝이 아니다. 출력값은 다음 기능의 씨앗이다.` | 출력은 결론이 아니라 다음 행동 원형이다. | C | 엔진면 / 사용자면 | return / next action | 출력은 끝난 답이 아니라 다음 행동을 시작하는 씨앗이다. | 반환을 “결과”가 아니라 다음 cycle material로 설명한다. | 기능으로 곧장 승격하는 것은 금지선과 함께 읽어야 한다. | `app/work/current_layer_baseline/engine_philosophy_declaration_v1.md:138`, `app/work/current_layer_baseline/engine_philosophy_declaration_v1.md:153` | high | yes |
| `mixed hold = re-entry 가능한 productive hold corridor` | hold는 폐기/실패가 아니라 재진입 가능 상태다. | C | 벡터플면 / 엔진면 | hold / re-entry | 보류된 것은 끝난 것이 아니라 다시 들어와 두꺼워질 수 있는 통로다. | hold/reflux/reingest 설명에 바로 쓸 수 있다. | re-entry가 canonical 승격을 의미하지 않는다는 금지선을 같이 붙여야 한다. | `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md:41`, `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md:56` | high | yes |
| `re-entry 있음 = canonical 은 금지` | 반환/재진입은 자동 승격이 아니다. | C | 엔진면 / 벡터플면 | re-entry / promoted | 다시 들어왔다고 바로 정답이나 승격이 되는 것은 아니다. | assistant가 return을 promotion으로 과잉 판정하지 않게 한다. | 승격 조건은 현재 금지/미해결. | `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md:50`, `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md:56` | high | yes |
| `reinjection은 그냥 저장이 아니라 다음 작동을 위한 residue 복귀다.` | reinjection은 저장이 아니라 다음 작동을 준비하는 환류다. | C | 벡터플면 / 엔진면 | reinjection / residue | 다시 넣는다는 것은 보관이 아니라 다음 작동을 위해 residue를 돌려보내는 것이다. | line pipeline과 엔진 환류를 연결하는 문장이다. | residue의 최소 구조는 아직 분절 필요. | `docs/reviews/vectorfl_gemma4_sidecar_prototype_v0.md:207`, `docs/reviews/vectorfl_gemma4_sidecar_prototype_v0.md:212` | high | yes |
| `Breadcrumb is the trace of judgment movement and reasoning` | trace는 실행 로그가 아니라 판단 이동의 흔적이다. | C | 엔진면 / assistant layer | breadcrumb / trace / memory | trace는 “무슨 명령을 실행했나”보다 “판단이 왜 움직였나”를 남기는 것이다. | Event Trace / Work Memory를 단순 debug log로 만들지 않게 한다. | breadcrumb와 event trace의 경계는 구현 시 추가 분리 필요. | `docs/baselines/concept_to_implementation_map_baseline_v0.md:139`, `docs/baselines/concept_to_implementation_map_baseline_v0.md:149`, `docs/baselines/concept_to_implementation_map_baseline_v0.md:329` | high | yes |

---

## Dataset 2. Track B

Fields: `raw_expression`, `interpreted_meaning`, `grammar_type`, `related_surface_or_layer`, `human_rewrite`, `why_useful_for_assistant`, `unresolved`, `source_refs`, `repetition_signal`, `high_overlap`

### grammar_type 1. 경계 표현

| raw_expression | interpreted_meaning | grammar_type | related_surface_or_layer | human_rewrite | why_useful_for_assistant | unresolved | source_refs | repetition_signal | high_overlap |
|---|---|---|---|---|---|---|---|---|---|
| `관측/탐색/검색/코드/보강은 모두 상부 부품으로 다루며, 결과는 공간을 덮어쓰지 않고 별도 기억층에 append한다.` | 본체와 도구층을 분리하고 결과는 append로 남긴다. | 경계 표현 | 공간 본체 / 도구층 | 관측, 검색, 코드, 보강은 본체가 아니라 붙이는 부품이고, 결과는 덮어쓰지 않고 따로 남긴다. | CLI/agent를 본체로 승격하지 않게 한다. | 통합엔진 3면에서는 “공간 본체”와 “3면 본체”의 용어 정합성 추가 필요. | `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md:40`, `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md:42` | high | yes |
| `Codex는 공간 본체를 재정의하는 존재가 아니다.` | Codex/assistant는 탐색·패치 도구이지 본체 정의자가 아니다. | 경계 표현 | CLI / assistant layer | assistant는 본체를 새로 정의하지 않고, 탐색하고 정리하고 제안한다. | 현재 미션의 역할 경계를 직접 고정한다. | “패치”가 이번 작업에서는 언어 추출 보고서 작성으로 제한됨. | `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md:91`, `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md:95` | high | yes |
| `관측기/탐색기/응결핵 테스트기는 공간 본체가 아니다.` | observation/probe/search는 detachable 부품이다. | 경계 표현 | 도구층 / 관측층 | 관측기는 공간에 질문을 던지는 부품이지 공간 자체가 아니다. | external research/automation을 tool layer로 유지하게 한다. | 응결핵 표현은 assistant용 쉬운 번역 필요. | `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md:76`, `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md:82`, `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md:597` | high | yes |
| `secondary surface에서 보이는 contract는 summary consumption만 허용한다. owning surface가 바뀌는 것은 아니다.` | 정보가 보인다고 책임 면이 바뀌지는 않는다. | 경계 표현 | 3면 경계 | 다른 면의 요약은 볼 수 있지만 그 역할을 가져오면 안 된다. | assistant가 UI/문서 재배치 때 owning surface를 혼동하지 않게 한다. | summary 범위를 실제 state 연결 때 제한해야 함. | `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:483`, `docs/specs/integrated_engine_surface_sections_and_slot_mapping_v0.md:492` | high | yes |
| `Do not turn this into a generic orchestration or workflow engine.` | 국소 규칙을 범용 오케스트레이션으로 과대 확장하지 않는다. | 경계 표현 | implementation / tool layer | 이 규칙을 전체 workflow engine으로 키우지 않는다. | 단계/hold 문법을 automation-first 설계로 오해하지 않게 한다. | 영어 원문을 한국어 운영 문장으로 통일 가능. | `docs/baselines/phase_transition_and_hold_rule_implementation_baseline_v0.md:55`, `docs/baselines/phase_transition_and_hold_rule_implementation_baseline_v0.md:59`, `docs/baselines/phase_transition_and_hold_rule_implementation_baseline_v0.md:265` | medium | yes |

### grammar_type 2. 목적 문법

| raw_expression | interpreted_meaning | grammar_type | related_surface_or_layer | human_rewrite | why_useful_for_assistant | unresolved | source_refs | repetition_signal | high_overlap |
|---|---|---|---|---|---|---|---|---|---|
| `시나리오 안에서 현재 위치와 이번 범위를 먼저 잘라야 한다.` | 작업 전 현재 장면과 범위를 좁혀야 한다. | 목적 문법 | user surface / work loop | 먼저 지금 어느 장면인지, 이번에 어디까지만 할지 자른다. | assistant가 구현 확대를 막고 목적형 탐색에 집중하게 한다. | 시나리오가 미래 팀 운영층을 포함하므로 현재 골격에 맞게 절제 필요. | `docs/specs/integrated_engine_operating_methodology_direction_v0.md:9`, `docs/specs/integrated_engine_operating_methodology_direction_v0.md:14` | high | yes |
| `이번에 하지 않을 것을 명시한다.` | non-goal을 명시해야 범위가 안정된다. | 목적 문법 | work loop | 무엇을 할지뿐 아니라 무엇을 하지 않을지도 쓴다. | assistant가 schema/automation 확정으로 새지 않게 한다. | non-goal template로 승격 가능. | `docs/specs/integrated_engine_operating_methodology_direction_v0.md:98`, `docs/specs/integrated_engine_operating_methodology_direction_v0.md:106` | high | yes |
| `지금 필요한 것은 전체 공간 뷰어가 아니다. 지금 필요한 것은 read-only operation surface다.` | 현재 목표를 전체화하지 않고 최소 추적면으로 제한한다. | 목적 문법 | operating surface | 전체를 다 보여주는 게 아니라 지금 흐름을 읽는 최소면이 필요하다. | “공간 전체 요약이 아니다”라는 이번 요청과 직접 맞는다. | read-only operation surface와 3면 표면의 관계는 추가 정리 필요. | `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md:103`, `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md:107` | high | yes |
| `구조 재설계가 아니라, 사용자 번역 표면 조율` | 작업 범위가 설계 재발명보다 번역 조율에 있다. | 목적 문법 | translation layer | 구조를 갈아엎지 않고, 사용자에게 읽히는 번역면을 조율한다. | 이번 언어 추출 작업의 목적을 안정화한다. | 현재는 사용자 번역뿐 아니라 3면/line/return까지 포함. | `docs/examples/example_connection_translation_first_refinement_v1.md:127`, `docs/examples/example_connection_translation_first_refinement_v1.md:139` | high | yes |
| `새 기능보다 바닥 셋업을 먼저 하라.` | 확장보다 운영 바닥과 경계가 우선이다. | 목적 문법 | setup / baseline | 새 기능을 붙이기 전에 경계, 기억, append 바닥을 먼저 세운다. | 구현 확대 금지를 간단히 지시할 수 있다. | 이번 산출은 문서/언어 셋업에 해당. | `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md:696`, `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md:704` | high | yes |

### grammar_type 3. 단계 문법

| raw_expression | interpreted_meaning | grammar_type | related_surface_or_layer | human_rewrite | why_useful_for_assistant | unresolved | source_refs | repetition_signal | high_overlap |
|---|---|---|---|---|---|---|---|---|---|
| `외부 가능성 -> 공간 재료 -> 목적 선언 -> 팀 숙성 -> 검증 -> 공간 환류` | 큰 시나리오 흐름이지만 한 번에 구현할 계획표는 아니다. | 단계 문법 | 3면 / future layer | 가능성을 재료로 넣고, 목적을 세우고, 읽고, 검증하고, 다시 공간으로 돌린다. | 전체 loop를 설명하되 현재 작업을 북극성으로만 쓰게 한다. | 팀 숙성은 현 3면 본체보다 확장층. | `docs/specs/integrated_engine_operating_methodology_direction_v0.md:5`, `docs/specs/integrated_engine_operating_methodology_direction_v0.md:31` | high | yes |
| `한 번에 전부 구현할 계획표로 읽지 않는다.` | 단계 흐름은 지도이지 구현 계획이 아니다. | 단계 문법 | methodology | 이 흐름은 방향 표시이지 한 번에 다 만들 목록이 아니다. | assistant가 시나리오를 feature backlog로 오해하지 않게 한다. | 없음. | `docs/specs/integrated_engine_operating_methodology_direction_v0.md:31` | high | yes |
| `지금 당장 손댈 한 단계만 자른다.` | 작업 단위를 작게 자르는 단계 문법이다. | 단계 문법 | work loop | 지금 손댈 한 조각만 정한다. | 과도한 구현과 구조 개편을 막는다. | 이번 탐색에서는 “읽고 추출할 문서군”으로 적용. | `docs/specs/integrated_engine_operating_methodology_direction_v0.md:102`, `docs/specs/integrated_engine_operating_methodology_direction_v0.md:105` | high | yes |
| `Record observations first, then judge from the accumulated observations.` | 관측을 먼저 남기고 나중에 판정한다. | 단계 문법 | assistant judgment / engine | 먼저 관찰을 기록하고, 쌓인 관찰에서 판단한다. | assistant가 한두 문장으로 과잉 일반화하지 않게 한다. | observation schema는 현재 final 아님. | `docs/baselines/phase_transition_and_hold_rule_implementation_baseline_v0.md:155`, `docs/baselines/phase_transition_and_hold_rule_implementation_baseline_v0.md:159` | medium | yes |
| `원본에서 source_line_candidate를 추출하고 ... observed_line과 residue_line을 append-only로 기록·reinject` | line 처리의 detect/translate/select/observe/reinject 단계 문법이다. | 단계 문법 | line / assistant log | 원본에서 후보를 뽑고, 번역하고, 기존 기억과 비교하고, 운영 라인을 고른 뒤, 결과와 residue를 기록해 다시 넣는다. | CLI 지시문과 작업 로그 문법으로 바로 쓸 수 있다. | source/translated/operating/observed/residue 저장 구조는 미정. | `docs/reviews/vectorfl_gemma4_sidecar_prototype_v0.md:158`, `docs/reviews/vectorfl_gemma4_sidecar_prototype_v0.md:195` | high | yes |

### grammar_type 4. 판정 문법

| raw_expression | interpreted_meaning | grammar_type | related_surface_or_layer | human_rewrite | why_useful_for_assistant | unresolved | source_refs | repetition_signal | high_overlap |
|---|---|---|---|---|---|---|---|---|---|
| `final schema 아님` / `DB 설계 문서 아님` / `canonical internal model 문서 아님` | 문서의 판단 강도를 낮춰 과잉 잠금을 막는다. | 판정 문법 | spec / contract layer | 이것은 최종 스키마가 아니라 현재 해석을 안정시키는 중간 기준이다. | assistant가 후보 문서를 final model로 오해하지 않게 한다. | 반복 문구를 통합 템플릿으로 만들 수 있음. | `docs/specs/line_contract_axes_v0.md:7`, `docs/specs/line_contract_axes_v0.md:13`, `docs/specs/integrated_engine_surface_object_contracts_v0.md:5`, `docs/specs/integrated_engine_surface_object_contracts_v0.md:14` | high | yes |
| `open questions를 남기고 억지로 수렴하지 않는다.` | 미해결을 강제로 닫지 않는 판정 문법이다. | 판정 문법 | contract layer | 애매한 질문은 지금 닫지 말고 open question으로 남긴다. | assistant가 빈칸을 임의 확정하지 않게 한다. | open question 관리 위치는 추가 필요. | `docs/specs/integrated_engine_surface_object_contracts_v0.md:32`, `docs/specs/integrated_engine_surface_object_contracts_v0.md:38` | high | yes |
| `candidate is a pattern that has been repeatedly observed and provisionally structured` | candidate는 반복 관찰된 임시 구조다. | 판정 문법 | line / implementation | 후보는 반복 관찰된 임시 패턴이지 아직 규칙이 아니다. | candidate를 구현/승격으로 바로 굳히지 않게 한다. | 반복 관찰 기준은 추가 필요. | `docs/baselines/concept_to_implementation_map_baseline_v0.md:157`, `docs/baselines/concept_to_implementation_map_baseline_v0.md:167` | high | yes |
| `Until then it remains observation + registry + trace only.` | 승격 전 후보의 상태를 제한한다. | 판정 문법 | candidate / trace | 조건을 채우기 전까지는 관찰, 등록, 흔적으로만 둔다. | future layer를 본체로 올리지 않게 한다. | condition set의 현재 적용 범위는 추가 확인 필요. | `docs/baselines/concept_to_implementation_map_baseline_v0.md:444`, `docs/baselines/concept_to_implementation_map_baseline_v0.md:453` | high | yes |
| `No reason, no decision` | 이유 없는 판정 금지 문법이다. | 판정 문법 | assistant judgment / engine | 이유, 근거, blocker, 다음 확인 조건 없이는 판정하지 않는다. | assistant가 잠금/보류/승격 판단을 설명 가능하게 한다. | 모든 문서 판단에 동일 적용할지는 범위 조정 필요. | `docs/baselines/phase_transition_and_hold_rule_implementation_baseline_v0.md:46`, `docs/baselines/phase_transition_and_hold_rule_implementation_baseline_v0.md:54` | high | yes |
| `promotion rule 논의는 아직 금지` | re-entry가 있어도 승격 규칙은 아직 닫지 않는다. | 판정 문법 | hold / promotion | 다시 들어오는 증거가 있어도 지금은 승격 규칙을 만들지 않는다. | 이번 작업에서 final lock을 막는 데 직접 유용하다. | promotion 논의 재개 조건은 더 쌓아야 함. | `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md:50`, `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md:56`, `app/work/current_layer_baseline/current_layer_baseline_contract_v1.md:90` | high | yes |

### grammar_type 5. 번역 문법

| raw_expression | interpreted_meaning | grammar_type | related_surface_or_layer | human_rewrite | why_useful_for_assistant | unresolved | source_refs | repetition_signal | high_overlap |
|---|---|---|---|---|---|---|---|---|---|
| `엔진 내부 언어와 사용자 질문의 의미 층위 사이의 번역 간극` | 시스템 분류와 사용자 의미 사이에는 번역층이 필요하다. | 번역 문법 | user surface / translation layer | 엔진 말과 사용자가 궁금해하는 말 사이에는 아직 간극이 있다. | assistant가 내부 라벨을 그대로 사용자 설명으로 내놓지 않게 한다. | “의미 층위”의 최소 표현 목록은 추가 탐색 필요. | `docs/examples/example_connection_translation_first_refinement_v1.md:63`, `docs/examples/example_connection_translation_first_refinement_v1.md:67` | high | yes |
| `층위는 사용자의 질문이 어떤 방향들로 펼쳐지는가` | layer/axis를 사용자 질문의 펼쳐짐으로 번역한다. | 번역 문법 | user surface | 층위란 내부 라벨명이 아니라 사용자의 질문이 열리는 방향이다. | 사람 말 번역의 핵심 문장이다. | line axes와 사용자 의미층의 연결은 추가 필요. | `docs/examples/example_connection_translation_first_refinement_v1.md:92`, `docs/examples/example_connection_translation_first_refinement_v1.md:100` | high | yes |
| `숫자보다 먼저 사용자 의미 층위가 열린다` | 내부 count보다 의미 설명이 먼저다. | 번역 문법 | user surface | 개수보다 먼저 사용자가 이해할 의미 방향을 열어준다. | user-facing summary 작성 기준으로 바로 쓸 수 있다. | 숫자/근거를 완전히 숨기면 안 되므로 균형 필요. | `docs/examples/example_connection_translation_first_refinement_v1.md:182`, `docs/examples/example_connection_translation_first_refinement_v1.md:204` | medium | yes |
| `라인은 표면 용어이고, 그 아래에는 typed line interpretation이 있어야 한다.` | 같은 용어를 사용자 말과 내부 해석으로 분리한다. | 번역 문법 | line / assistant layer | 겉으로는 라인이라 해도 내부에서는 origin/meaning/role/maturity를 붙여 읽는다. | 입력 문법을 만드는 데 바로 쓸 수 있다. | typed line axes는 final schema가 아님. | `docs/specs/line_contract_axes_v0.md:61`, `docs/specs/line_contract_axes_v0.md:86` | high | yes |
| `같은 line도 지금 어느 팀/어느 단계에서 쓰이느냐에 따라 성격이 달라진다.` | meaning과 operating role을 분리한다. | 번역 문법 | line / operating role | 같은 라인도 지금 어디에 쓰는지에 따라 다르게 읽힌다. | assistant가 line을 context-free string으로 처리하지 않게 한다. | 팀 기준 운영 role은 현재 확장층으로 절제 필요. | `docs/specs/line_contract_axes_v0.md:173`, `docs/specs/line_contract_axes_v0.md:191` | high | yes |
| `본체 두뇌가 아니라 통역기 + 호출기 + 설명기 + 초안 작성기` | sidecar/LLM의 역할을 사람 말로 번역한다. | 번역 문법 | CLI / sidecar | 외부 모델은 본체가 아니라 읽고 부르고 설명하고 초안을 쓰는 보조 부품이다. | CLI/agent 역할을 과대평가하지 않게 한다. | Gemma4 특정 표현은 일반 CLI/agent로 일반화할 때 주의. | `docs/reviews/vectorfl_gemma4_sidecar_prototype_v0.md:88`, `docs/reviews/vectorfl_gemma4_sidecar_prototype_v0.md:98` | high | yes |
| `기억 없는 축적은 숙성이 아니라 적재다.` | memory/trace가 없는 저장은 maturation이 아니다. | 번역 문법 | memory layer | 그냥 쌓는 것과 기억을 남기며 익히는 것은 다르다. | trace/memory가 왜 필요한지 쉬운 설명으로 쓸 수 있다. | 기억층 필드 확정은 아님. | `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md:66`, `source_assets/directives/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md:74` | high | yes |

---

## Integration Report

### A와 B에서 공통으로 반복된 핵심 표현

- `본체 / 상부 부품 / sidecar / detachable`  
  반복 의미: 공간/3면 본체와 CLI/agent/검색/관측 도구층을 섞지 않는다.

- `목적 / 범위 / 재료 / 현재 위치 / 이번에 하지 않을 것`  
  반복 의미: 작업 전에 사용자면의 목적 문법을 먼저 세워야 한다.

- `중간 흐름 / 중간 통로 / 중간 운용 형성체`  
  반복 의미: 벡터플면은 사용자 목적을 엔진 실행으로 바로 떨어뜨리지 않고 line/relation/gap/pending으로 판독하는 면이다.

- `line / relation / gap / pending / reflux / hold / promoted`  
  반복 의미: line은 단순 조각이 아니라 단계, 관계, 공백, 환류, 보류, 승격 가능성을 품는 중간 운용 단위다.

- `결과뿐 아니라 과정 / trace / memory / append-only / reingest`  
  반복 의미: 반환은 단순 결과가 아니라 다음 순환의 재료와 기억이다.

- `final schema 아님 / open questions / 보류 / 아직 금지 / future layer`  
  반복 의미: 현재는 셋업과 언어 적립 단계이지 final model 잠금 단계가 아니다.

### 지금 바로 통합엔진 셋업에 쓸 수 있는 문장 후보

- 사용자면은 목적과 범위, 그리고 그 목적이 얹힌 재료 문맥을 먼저 세우는 면이다.
- 벡터플면은 사용자 목적과 엔진 처리 사이에서 line, relation, gap, pending, reflux 상태를 드러내는 중간 형성체 판독면이다.
- 엔진면은 재료를 ingest하고 처리/검증한 뒤, 결과와 잔여 판단을 trace/memory와 함께 다시 공간 재료로 환류하는 면이다.
- line은 원재료와 최종 개념 사이에서 여러 단서, 관계, 공백, 압력을 묶어 다음 해석과 검증, 환류를 유발하는 중간 운용 형성체다.
- hold는 실패나 TODO가 아니라 이유와 재개 조건을 가진 숙성 보호 상태다.
- reflux는 후퇴가 아니라 검증/보류/비교 결과가 다시 공간 내부로 돌아와 재형성되는 루프다.

### assistant 입력 문법으로 바로 적립할 수 있는 문장 후보

- 이번 작업은 어느 장면인가?
- 이번 작업의 목적, 범위, 하지 않을 것은 무엇인가?
- 이 표현은 사용자면, 벡터플면, 엔진면, 도구층 중 어디에 속하는가?
- 이 line은 어디서 왔고, 어떤 의미 종류이며, 지금 무엇을 위해 쓰이고 있고, 어느 정도 숙성됐는가?
- 이 판단은 잠금, 기록, 보류, 미래층, 참조층, 임시 발판 중 어디에 속하는가?
- 이 return은 accepted, hold, reingest candidate, trace/memory 중 무엇으로 남는가?
- 이유, 근거, blocker, next check trigger가 없으면 판정하지 않는다.

### 아직 잠그면 안 되는 표현

- Team Relay Board를 사용자면 본체 핵심으로 고정하는 표현.
- 벡터플면을 workflow hub 또는 운영 허브로 확정하는 표현.
- `current_stage` 후보값과 `maturity_level` 후보값을 final enum으로 쓰는 것.
- `origin / meaning / operating_role / maturity` 4축을 DB schema로 고정하는 것.
- `accepted_refs / hold_refs / next_reingest_requested`를 final return schema로 고정하는 것.
- re-entry를 canonical promotion의 충분조건으로 읽는 것.
- search/reference layer를 full RAG 본체로 읽는 것.
- sidecar/CLI/agent를 본체 두뇌 또는 자동 실행 주체로 읽는 것.

### 추가 탐색이 필요한 빈칸

- 사용자면에서 팀/담당/relay가 어느 수준까지 확장층이고 어느 수준부터 본체 해석을 흐리는지.
- pending, reflux, reingest, residue의 경계.
- line의 `health`와 `maturity_level` 차이.
- `gap`과 `blocker`의 차이.
- Validation Return이 사용자면 report summary에 보일 때 허용되는 summary 범위.
- trace/event/breadcrumb/work memory의 역할 분리.
- 사용자 의미 층위와 line axes를 함께 쓰는 최소 입력 템플릿.

---

## Minimum Common Language Draft

### 3면 설명 한 줄 문장군

- 사용자면: 목적, 범위, 재료 문맥을 먼저 세우는 시작면.
- 벡터플면: 목적이 바로 실행으로 떨어지기 전 line, relation, gap, pending, reflux로 드러나는 중간 형성체 판독면.
- 엔진면: ingest, process, validate를 수행하고 trace/memory와 함께 return을 남기는 처리/환류면.
- 순환: 목적과 범위를 세우고, 중간 형성체를 판독하고, 처리/검증/기억/반환한 뒤, 그 반환을 다음 목적과 판독의 재료로 삼는다.

### line/축 설명 한 줄 문장군

- line은 raw도 final도 아닌 사이에서 관계, 공백, 압력, 방향을 묶는 중간 운용 형성체다.
- line은 문장조각이나 ticket이 아니라 다음 해석, 검증, 환류를 유발하는 운용 단위다.
- line은 최소 origin, meaning, operating_role, maturity 네 축으로 함께 읽는다.
- current_stage는 시간축이고 maturity_level은 숙성축이며, 둘은 같지 않다.
- hold는 버림이 아니라 숙성 보호이고, reflux는 후퇴가 아니라 재형성 루프다.

### 반환/환류 설명 한 줄 문장군

- return은 결과 표시가 아니라 accepted, hold, reingest 후보와 reasoning trace를 다시 공간 재료로 돌리는 환류다.
- validation은 pass/fail로 끝나는 판정기가 아니라 무엇을 다시 재료로 삼을지 가르는 숙성 기관이다.
- trace는 실행 로그만이 아니라 판단이 왜 움직였는지 남기는 기억이다.
- 결과뿐 아니라 과정도 다음 순환의 재료가 된다.

### assistant 입력용 목적/범위/단계/판정 문장틀

- 목적: “이번 작업의 목적은 ___ 이고, 통합엔진 셋업/assistant 해석 안정성에 쓰일 언어를 찾는 것이다.”
- 범위: “이번 범위는 ___ 까지이며, ___ 는 하지 않는다.”
- 단계: “현재 단계는 탐색 / 언어 적립 / 셋업 / 테스트 / 수정 / 반복 후 잠금 중 ___ 이다.”
- 면 분류: “이 표현은 사용자면 / 벡터플면 / 엔진면 / 도구층 중 ___ 에 속한다.”
- line 분류: “이 line은 origin=___, meaning=___, operating_role=___, maturity=___ 로 읽는다.”
- 판정: “이 표현은 잠금 / 기록 / 보류 / 미래층 / 참조층 / 임시 발판 중 ___ 로 둔다. 이유는 ___ 이고, next_check_trigger는 ___ 이다.”
- 반환: “이 return은 accepted / hold / reingest_candidate / trace_memory 중 ___ 로 남기며, 이유는 ___ 이다.”

