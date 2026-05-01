# Formation-Movement Interface Agent Skills External Reference Validation Case v0

## 1. status

```yaml
status: validation_case
mode: dry_run_only
verdict: PASS_WITH_NOTE
case_type: external_reference_ingest
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
no_reference_promotion: true
```

## 2. source

- GeekNews summary:
  `https://news.hada.io/topic?id=28294`
- upstream repository:
  `https://github.com/addyosmani/agent-skills`
- package reference:
  `docs/reports/formation_movement_interface_package_draft_v0.md`

## 3. case setup

Situation:

- an external reference about `agent-skills` is introduced as a possible comparison source
- the material emphasizes structured workflows, role-sensitive skills, quality gates, testing as proof, and lifecycle commands
- the immediate question is whether this should be read as B evidence, broader governance support, or only as an external comparison frame

Why this is a good test case:

- it strongly touches role, boundary, and verification language
- it is intuitively tempting to over-promote into B/C-supporting doctrine
- but it is still an external source with no direct proof of internal explanatory force

Working boundary:

- no B lock
- no operating-rule adoption
- no baseline wording reuse
- no package patch

## 4. quick judgment card

```text
현재 판정: reread_priority
이유: 역할/경계/검증 언어가 강하지만, 내부 구조의 direct evidence라기보다 external comparison frame 또는 defensive logic에 가깝습니다.
다음 이동: direct evidence / defensive logic / comparison frame 구분을 전제로 compare_only 판단을 준비합니다.
금지선: B promotion, operating rule 승격, baseline 반영 금지
```

## 5. seed sidecar

Operational minimum only:

```yaml
current_purpose: agent-skills reference가 formation_movement 패키지에서 어떤 역할인지 판정
source_trace: geeknews_topic_28294 + github_addyosmani_agent_skills
initial_boundary: no evidence lock, no B promotion, no rule adoption
object_type: unclassified
```

Validation note:

- seed 단계에서 `object_type`을 확정하지 않았다
- 사용자 입력 수준은 operational minimum에 머문다
- Core 7 전체 작성을 요구하지 않는다

## 6. formed sidecar

VectorFL reread after source inspection:

```yaml
object_type: reread_priority
provisional_status: hold_for_role_clarification
boundary: external governance/skill-pack reference only; no B confirmation; no operating-rule elevation
next_allowed_move: reread_only
needed_reread_question: 이 자료는 내부 구조의 direct evidence인가, 아니면 defensive logic 또는 comparison frame인가?
source_trace: geeknews_topic_28294 + github_addyosmani_agent_skills
```

Why not `framing_candidate` yet:

- the reference clearly touches internal concerns, but still lacks demonstrated internal relocation force
- it is stronger as an external governance/comparison source than as direct candidate proof
- internal reread scenes are still needed before even bounded framing confidence rises

## 7. VectorFL reading

### relevant signals from the source

- lifecycle commands such as `/spec`, `/plan`, `/build`, `/test`, `/review`, `/ship`
- phrases like “spec before code,” “tests are proof,” and “one slice at a time”
- role-sensitive skill activation and contract/interface-oriented thinking

### likely contact points

- `A`:
  ordering / precedence / what must be set first
- `B`:
  role-boundary organization and interface distinction
- `C`:
  verification grammar, review gates, and proof requirements

### current best reading

- strongest current reading:
  `external comparison frame`
- secondary reading:
  `defensive logic`
- not justified yet:
  `direct evidence`

Instability reason:

- the source is rich in governance language but still external to the internal reread field
- it may support why A/B/C-like structures are useful without directly proving their internal body

Promotion barrier:

- no repeated internal explanatory / relocation force has been shown
- no internal scene comparison has yet demonstrated that this source actually clarifies our package better than generic engineering discipline language

## 8. direct evidence / defensive logic / comparison frame split

### direct evidence

Current verdict:

`not supported yet`

Reason:

- external source alone does not directly reinforce repeated internal scenes
- the source has not yet been tested against internal Codex / validation / external-ingest records

### defensive logic

Current verdict:

`partially supported`

Reason:

- the source strongly argues that agent work benefits from explicit stages, checks, and quality gates
- this explains why boundary/verification structures may be necessary, but does not prove our internal ontology by itself

### comparison frame

Current verdict:

`strongest current reading`

Reason:

- the source can be used to reread internal scenes such as Codex prepare, validation-return usage, and external-ingest handling
- it is useful as a lens for bounded comparison without needing immediate promotion

## 9. surface-specific visibility

### A. User Surface judgment card

```text
현재 판정: reread_priority
이유: 구조화된 workflow와 quality gate reference로는 유용하지만 아직 내부 direct evidence는 아닙니다.
다음 이동: comparison frame으로 제한해 내부 장면과 bounded compare를 준비합니다.
금지선: B 증거 확정, 운영 규칙 채택, baseline 반영 금지
```

### B. VectorFL Surface view

```yaml
object_type: reread_priority
provisional_status: hold_for_role_clarification
boundary: external comparison source only
needed_reread_question: direct evidence인가, defensive logic인가, comparison frame인가?
candidate_role: external governance/comparison frame candidate
promotion_barrier: internal repeated explanatory force 미검증
source_trace: geeknews_topic_28294 + github_addyosmani_agent_skills
next_allowed_move: reread_only
```

### C. Engine Surface view

This case is not executable yet.

```yaml
action_shape: possible bounded compare report
execution_constraint: not_attached_yet
guardrail: no evidence lock, no rule adoption, no package mutation
expected_return_form: local comparison note only
fallback_policy: PASS_WITH_NOTE if internal scene match stays weak
trust_scope: local comparison only, not promotable
reread_return_hook: return as validation note to reassess role classification
```

## 10. transition check

| transition | verdict | reason |
| --- | --- | --- |
| unclassified seed -> formed sidecar | PASS | safe seed capture moved into `reread_priority` without premature type lock |
| formed sidecar -> reread_priority / framing_candidate | PASS | `reread_priority` is safer than permissive framing here |
| allowed_to_prepare | HOLD | bounded compare is imaginable, but not yet necessary as immediate packet |
| allowed_to_execute | FAIL-safe / disallowed | no execution packet is justified |
| short validation return sufficient? | PASS | this is still a low-risk ingest classification |
| full validation return needed now? | HOLD | only if later bounded comparison changes B/C trust scope |
| final branch | PASS | `hold` / `reread_only` are healthy; promotion remains blocked |

## 11. operator cost check

- user-filled fields: 3 수준
- user chose `object_type`: no
- Core 7 fully required: no
- User Surface exposed only as 4-line judgment card: yes
- judgment burden moved to VectorFL: yes

## 12. promotion risk check

- external reference became evidence: no
- B-adjacent reading became B promotion: no
- operating rule adoption occurred: no
- non-promotion branches remained natural: yes

## 13. short / full validation return judgment

Short validation return is enough now:

```yaml
observed_result: source is useful as external comparison frame but not yet direct evidence
reread_trigger: internal scene comparison is still missing
next_recommended_state: keep as reread_priority or bounded compare candidate later
```

Full validation return becomes necessary if:

- this source starts changing B/C trust scope
- someone tries to treat it as direct evidence
- internal compare results materially change boundary claims
- the source begins influencing package wording or operating rules

## 14. verdict

`PASS_WITH_NOTE`

Reason:

- the package reads this source conservatively
- it preserves usefulness without forcing evidence promotion
- the note is that the source is strong enough to tempt over-reading, so bounded comparison would still need guardrails if attempted later

## 15. what worked

- safe `unclassified` seed capture
- delayed `object_type` assignment
- conservative `reread_priority` choice
- user-facing output stayed lightweight
- promotion remained blocked

## 16. what remains ambiguous

- whether this source will later function better as defensive logic or comparison frame
- how much internal scene match would be enough before `framing_candidate` becomes justified
- whether B/C/A are equally contacted or whether one becomes central after bounded compare

## 17. what not to do

- do not call this B evidence now
- do not adopt its workflow as package doctrine
- do not turn “structured skill workflow” language into immediate baseline wording
- do not skip internal reread scenes

## 18. intentionally not changed

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- any existing validation case
- Core 7
- object family 5종
- no baseline lock
- no schema enforcement
- no implementation
- no runtime manifest
- no validator/script

## 19. unresolved questions

- if compared against internal Codex prepare and validation-return scenes, does this source stay comparison-frame-only or become stronger defensive logic?
- does any part of the source materially clarify B more than A/C?
- would a later bounded comparison still stay low enough risk for short validation return?
