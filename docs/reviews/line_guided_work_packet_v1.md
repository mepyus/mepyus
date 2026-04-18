# Line-Guided Work Packet v1

## 목적

이 문서는 `line-guided work packet` 을
Ralph overlay, Paperclip line-guided prototype,
그리고 이후 ingress/control-plane 실험이 함께 쓸 수 있는
공통 객체로 정의한다.

핵심 원칙은 아래다.

- 외부 프로그램의 task/issue/session을 그대로 복제하지 않는다
- 우리 공간의 line, residue, promotion, reuse 구조를 붙여서 번역한다
- packet은 실행 전 해석, 실행 중 안내, 실행 후 reinjection을 잇는 얇은 공통 형식이다

## packet의 역할

이 packet은 아래 네 층을 잇는다.

- external assignment or work unit
- vectorfl line memory
- current execution context
- post-run reinjection and next-work reuse

즉 핵심 객체는 원본 issue가 아니라,
원본 issue를 line-aware하게 번역한 packet이다.

## 상위 구조

packet은 다섯 묶음으로 본다.

- identity
- source assignment
- line translation
- execution guidance
- reinjection and reuse

## v1 schema

```json
{
  "packet_id": "lwp_20260405_0001",
  "packet_version": "v1",
  "created_at": "2026-04-05T18:00:00+09:00",
  "updated_at": "2026-04-05T18:00:00+09:00",
  "status": "translated",
  "source_program": "paperclip",
  "source_assignment": {
    "assignment_id": "issue_123",
    "company_ref": "company_alpha",
    "project_ref": "proj_workspace_ops",
    "goal_ref": "goal_line_upgrade",
    "parent_ref": "issue_118",
    "title": "stabilize structured-doc routing handoff",
    "description": "agent should harden the routing edge before next rollout",
    "assignee_ref": "agent_routing_operator",
    "priority": 2,
    "source_status": "assigned"
  },
  "line_translation": {
    "primary_line_id": "structured_doc_routing",
    "support_line_ids": [
      "observation_thickening",
      "surface_readout"
    ],
    "corridor": "routing_to_surface",
    "boundary": "runtime",
    "translation_confidence": "medium",
    "translation_reason": [
      "assignment directly modifies routing behavior",
      "existing reports show repeated handoff residue",
      "surface output depends on routing stabilization"
    ]
  },
  "context_refs": {
    "line_refs": [
      "runtime/manifests/line_registry.json#line:structured_doc_routing"
    ],
    "residue_refs": [
      "runtime/logs/reread_observation_log.jsonl#obs_204"
    ],
    "promotion_refs": [
      "runtime/logs/line_promotion_log.jsonl#prom_032"
    ],
    "board_refs": [
      "runtime/views/current_board.md"
    ],
    "evidence_refs": [
      "docs/reports/routing_handoff_review_v1.md"
    ]
  },
  "execution_guidance": {
    "objective": "reduce repeated handoff residue without widening scope",
    "acceptance_criteria": [
      "routing handoff path is explicit",
      "targeted check passes",
      "new residue is not amplified"
    ],
    "execution_hints": [
      "prefer minimal edge fix",
      "preserve current runtime ledger semantics",
      "capture any new routing caution as residue"
    ],
    "risk_notes": [
      "runtime/core boundary drift may reappear",
      "surface output may hide routing regressions"
    ],
    "promotion_gate": "review_before_complete"
  },
  "run_state": {
    "selected_for_run_at": null,
    "run_ref": null,
    "completion_claim": null,
    "checks_run": [],
    "changed_artifacts": []
  },
  "reinjection": {
    "operator_summary": null,
    "what_worked": [],
    "what_failed": [],
    "new_residue_refs": [],
    "pattern_candidate_refs": [],
    "followup_packet_refs": [],
    "decision": null,
    "decision_reason": []
  },
  "reuse": {
    "reusable_next_time": [],
    "agent_role_notes": [],
    "preferred_assignment_shapes": [],
    "avoidance_notes": []
  }
}
```

## 필드 설명

### 1. identity

필수:

- `packet_id`
- `packet_version`
- `created_at`
- `updated_at`
- `status`

`status` 는 v1에서 아래만 쓴다.

- `translated`
- `running`
- `reread_pending`
- `complete`
- `retained_residue`

### 2. source assignment

원본 프로그램의 할당 단위를 잃지 않기 위한 묶음이다.

필수:

- `source_program`
- `assignment_id`
- `title`
- `description`
- `assignee_ref`

선택:

- `company_ref`
- `project_ref`
- `goal_ref`
- `parent_ref`
- `priority`
- `source_status`

원칙:

- 원본 프로그램 의미를 보존한다
- 그러나 packet의 핵심 의미는 여기서 끝나지 않는다

### 3. line translation

이 packet의 핵심 묶음이다.

필수:

- `primary_line_id`
- `support_line_ids`
- `corridor`
- `boundary`
- `translation_confidence`

강하게 권장:

- `translation_reason`

원칙:

- `primary_line_id` 는 하나만 둔다
- `support_line_ids` 는 최대 3개 정도로 제한한다
- 새 line 생성보다 기존 line 재사용을 우선한다

### 4. context refs

translation에 사용된 기억 근거를 가리킨다.

필수는 아니지만,
prototype 가치의 대부분이 여기서 나온다.

권장 항목:

- `line_refs`
- `residue_refs`
- `promotion_refs`
- `board_refs`
- `evidence_refs`

원칙:

- 전체 히스토리를 넣지 않는다
- 다음 실행에 필요한 최소 근거만 넣는다

### 5. execution guidance

agent가 실제로 사용할 안내면이다.

필수:

- `objective`
- `acceptance_criteria`

권장:

- `execution_hints`
- `risk_notes`
- `promotion_gate`

원칙:

- issue 원문을 반복하지 않는다
- line-aware execution에 필요한 해석 정보를 담는다

### 6. run state

실행 중과 직후 상태를 위한 묶음이다.

권장 항목:

- `selected_for_run_at`
- `run_ref`
- `completion_claim`
- `checks_run`
- `changed_artifacts`

여기는 원장 전체를 대신하지 않는다.
실행 중 현재 packet과 관련된 최소 표지만 둔다.

### 7. reinjection

실행 후 공간으로 다시 밀어넣는 내용을 담는다.

핵심 항목:

- `operator_summary`
- `what_worked`
- `what_failed`
- `new_residue_refs`
- `pattern_candidate_refs`
- `followup_packet_refs`
- `decision`
- `decision_reason`

`decision` 은 v1에서 아래만 쓴다.

- `continue`
- `retain_residue`
- `promote_pattern`
- `complete`

### 8. reuse

다음 assignment translation에서 바로 재사용될 수 있는 메모층이다.

항목:

- `reusable_next_time`
- `agent_role_notes`
- `preferred_assignment_shapes`
- `avoidance_notes`

원칙:

- 이번 일의 상세 로그가 아니라
  다음 일의 입력을 더 잘 만드는 요약만 남긴다

## 번역 규칙

### rule 1. issue를 line으로 바로 동일시하지 않는다

원본 assignment 하나가 하나의 line과 정확히 일치할 필요는 없다.

따라서 아래 순서를 지킨다.

- 원본 assignment 읽기
- primary line 선택
- support line 제한
- corridor/boundary 부착

### rule 2. 새 line 남발 금지

packet을 만들 때마다 새 line을 만들면 구조가 망가진다.

우선순위:

- 기존 line 재사용
- 기존 line 조합
- 정말 필요할 때만 new candidate note

### rule 3. residue는 숨기지 않고 refs로 남긴다

애매하거나 실패한 흔적도 context에서 빼지 않는다.

대신 `residue_refs` 로 노출한다.

### rule 4. guidance는 짧고 구체적이어야 한다

agent 입력이 너무 길어지면 line translation의 장점이 사라진다.

따라서 guidance는 아래만 준다.

- 목표
- 합격 기준
- 실행 힌트
- 리스크

## v1 저장 위치

prototype 초기에는 아래 중 하나면 충분하다.

- `runtime/manifests/line_guided_work_packets.json`
- `runtime/manifests/ralph_overlay_work_registry.json`

첫 단계에서는 packet 개별 파일보다
manifest 배열로 두는 쪽이 더 단순하다.

## v1이 바로 지원하는 것

- Paperclip assignment translation
- Ralph work unit translation
- post-run reinjection summary
- next-assignment reuse seed

## v1이 아직 안 하는 것

- multi-agent shared packet editing
- automatic line creation
- budget/approval enforcement
- full UI board rendering

## 결론

`line-guided work packet` 은
외부 프로그램의 issue를 그대로 실행하지 않고,
우리 공간의 line memory를 통과시켜
실행 가능한 work unit로 다시 만드는 최소 공통 객체다.

이 packet이 있어야

- assignment translation
- line-guided execution
- process reinjection
- next-work reuse

가 한 바닥에서 연결된다.
