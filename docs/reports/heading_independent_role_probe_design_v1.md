[[A]] [[OBJ:heading_independent_role_probe_design_v1]] [[SEM:minimal_heading_independent_role_like_probe_after_pointer_stabilization]]

# heading-independent role probe design v1

## 1. purpose

- 이번 설계의 목적은 `claude_code_index.txt`처럼 heading이 약하거나 없는 입력에서도 role 계열 읽힘이 최소 수준으로 살아날 수 있는지 확인하는 것이다.
- 즉 이 문서는 generalized role system 설계가 아니라, `heading mismatch`를 줄이는 얇은 role-like probe 설계 문서다.

## 2. baseline problem after pointer probe

- paragraph role 해석은 여전히 youtube-style heading 전제에 강하게 묶여 있었다
- pointer support로 ref는 붙었지만, role 해석 기관 자체는 여전히 실행 불가능하거나 과도하게 경직될 위험이 있었다
- 따라서 이번 턴의 핵심은 `역할 확정`이 아니라 `role-like reading 가능성` 관찰이다

## 3. minimal intervention

- intervention_name: `functional_cue heading-independent role probe`
- source:
  - pointer probe 이후 `context_unit_candidates`
  - pointer probe 이후 `purpose_synthesis top_windows`
- rule:
  - explicit heading을 찾지 않는다
  - 대신 이미 살아 있는 context unit의 `page_role`, `relation_movement`, `evidence_pointers`를 이용해 약한 role-like hint를 남긴다
  - output은 role 확정이 아니라 `role_probe_status`, `role_hint_strength`, `role_like_hint`, `role_evidence_pointers` 같은 중간층으로 둔다

## 4. why this is minimal

- 새 role ontology를 만들지 않는다
- 도메인별 role 사전을 늘리지 않는다
- segmentation / pointer 로직을 다시 손대지 않는다
- 기존 pointer probe 산출물을 재활용해 heading 의존이 낮아질 때 무엇이 남는지만 본다

## 5. why this is not role fabrication

- role 이름을 evidence 없이 붙이지 않는다
- role-like hint는 context unit의 existing page role과 relation movement를 바탕으로 약하게만 표기한다
- evidence pointer가 없으면 강도를 올리지 않는다

## 6. expected read

- expected_recovery:
  - heading mismatch로 인한 hard failure 감소
  - evidence-linked role-like reading 일부 발생
  - unsupported role naming 증가 없이 약한 role hint 관찰 가능
- not_expected:
  - paragraph role generalization
  - direct grounded role support
  - object lift hold 해제

## 7. one-line summary

> heading-independent role probe는 heading이 없는 입력에서도 기능 단서와 pointer-evidence만으로 약한 role-like reading이 남는지 보는 최소 실험이며, role system 일반화가 아니라 role 생존 조건을 분리하는 단계다.
