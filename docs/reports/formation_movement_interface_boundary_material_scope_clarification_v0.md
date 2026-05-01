# Formation-Movement Interface Boundary Material Scope Clarification v0

## 1. status

```yaml
status: scope_clarification_note
verdict: PASS_WITH_NOTE
purpose: clarify that external material means all boundary-crossing material, not only internet-sourced references
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
```

## 2. correction

The term `external material` has been too narrow.

It has mostly been used for:

```text
인터넷에서 찾은 외부 자료
GitHub repo
GeekNews link
external reference
```

But the user's intended scope is broader.

Corrected scope:

```text
external material = any material that enters the space from a boundary surface and needs reread, placement, merge, buffer, or action alignment.
```

In Korean:

```text
외부자료 = 인터넷 자료만이 아니라,
공간의 경계에서 들어와 해석/배치/머지/숙성/작업화가 필요한 모든 재료.
```

## 3. included material types

### 3.1 internet / outside-world references

Examples:

- GeekNews topics
- GitHub repositories
- blog posts
- papers
- external docs
- libraries and tools

Main question:

```text
이 외부 기술/자료의 의도와 구조가 우리 공간의 어떤 line/lens/axis와 닿는가?
```

### 3.2 user-Codex conversation outputs

Examples:

- discussion summaries
- conceptual convergence notes
- user clarifications
- Codex analysis outputs
- generated reports
- unresolved questions from conversation

Main question:

```text
이 대화 산출물이 공간 안에서 어떤 형성 객체가 되는가?
```

### 3.3 Codex-produced intermediate outputs

Examples:

- comparison output
- draft package
- bounded report
- implementation plan
- explanation draft
- validation return
- worker return summary

Main question:

```text
이 Codex 출력은 final이 아니라 어떤 validation_return / residue / refinement input인가?
```

### 3.4 runtime logs and events

Examples:

- runtime events
- receipts
- manifests
- CLI session outputs
- test logs
- failure traces
- view snapshots

Main question:

```text
이 실행 흔적은 실제 동작 증거인가, residue인가, validation_return인가, 아니면 재현/디버그 재료인가?
```

### 3.5 program-generated artifacts

Examples:

- generated files
- reports
- indexes
- manifests
- analysis fragments
- structured outputs

Main question:

```text
이 산출물은 공간에 재투입될 때 어떤 역할을 갖는가?
```

## 4. better umbrella term

`external material` is still useful for internet materials, but it is not broad enough.

Candidate umbrella term:

```text
boundary material
```

Korean:

```text
경계 재료
```

Definition:

```text
Boundary material is any material crossing into the formation space from an outer or adjacent surface: web, user conversation, Codex output, runtime, logs, events, generated artifacts, or returned worker results.
```

This term better fits the actual process:

```text
source surface
→ boundary material
→ connection camera
→ lens pass
→ space placement
→ merge / buffer / movement
→ return / residue
```

## 5. impact on the microspace

The current `external_material_microspace` should be read as an early form of a broader structure:

```text
boundary material microspace
```

The current index is still valid, but incomplete.

It currently covers mostly:

- internet references
- external GitHub tools
- external technology comparison material

It should eventually support:

- conversation-generated materials
- Codex outputs
- runtime logs
- events and receipts
- generated reports
- returned worker artifacts

This is a scope correction, not a structure patch.

## 6. impact on the connection camera

The `Space-External Connection Camera` should be renamed or interpreted more broadly as:

```text
Space-Boundary Connection Camera
```

Korean:

```text
공간-경계 연결 카메라
```

Reason:

The camera should not only read outside internet sources.

It should read any material that enters from a boundary:

```text
internet
user conversation
Codex output
runtime
logs
events
generated artifacts
worker returns
```

## 7. corrected operating question

Previous question:

```text
이 외부자료는 우리 공간의 어떤 line/lens와 닿는가?
```

Corrected question:

```text
이 경계 재료는 어떤 표면에서 들어왔고,
공간의 어떤 line/lens/axis와 닿으며,
머지/버퍼/작업화/환류 중 어디로 가야 하는가?
```

## 8. source surface map

| Source surface | Example material | First reading |
| --- | --- | --- |
| Internet / external web | GeekNews, GitHub repo, blog | technical meaning + maker intent |
| User conversation | clarification, conceptual summary, question | user intent + formation object |
| Codex output | report, comparison, draft, plan | validation_return / refinement input |
| Runtime | manifest, event, receipt, log | actual behavior evidence / residue |
| Program output | generated file, index, report | returned artifact / space insertion candidate |
| Worker return | result block, test output, failure | validation_return / branch decision |

## 9. relation to current goal

The broader scope strengthens the current goal.

The goal is not:

```text
how to handle internet references
```

It is:

```text
how to handle any material that can change the direction of the space, the feature, or the user's understanding.
```

That includes:

- what the user says while thinking
- what Codex generates
- what the program logs
- what a worker returns
- what an external repo suggests

All of these can become:

- reread_priority
- framing_candidate
- bounded_action_candidate
- guarded_execution object
- validation_return
- residue

## 10. do-not-change

- do not rename files immediately
- do not patch existing microspace index yet
- do not create new object families
- do not expand Core 7
- do not schema-enforce boundary material
- do not treat every log or Codex output as equally important
- do not automatically promote generated outputs into space doctrine

## 11. recommended next move

Recommended bounded next move:

```text
Create a short Space-Boundary Connection Camera usage note that uses boundary material as the umbrella input.
```

It should cover:

- internet material
- user conversation material
- Codex output material
- runtime/log/event material
- generated artifact material

But it should remain an operating note, not a schema.

## 12. verdict

```yaml
verdict: PASS_WITH_NOTE
correction: external_material_scope_was_too_narrow
new_umbrella_term: boundary_material
camera_name_candidate: Space-Boundary Connection Camera
microspace_implication: external_material_microspace_is_early_subcase_of_boundary_material_microspace
next_recommended_move: write_short_usage_note_before_any_rename_or_automation
```

