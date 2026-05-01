# Space Feedback Loop Scriptability Audit v0

## 1. status

```yaml
report_status: scriptability_audit
purpose: separate scriptable space-use steps from Codex judgment steps
verdict: PASS_WITH_NOTE
implementation: false
schema_enforcement: false
runtime_manifest: false
validator_or_script_created_now: false
baseline_lock: false
```

## 2. user problem

The user wants Codex to keep using the space, reread existing assets, and return the process back into the space.

The immediate engineering question is:

```text
어디까지는 스크립트가 반복 처리할 수 있고,
어디부터는 Codex가 직접 해석해야 하는가?
```

The reason is practical:

- token cost should go down
- space lookup should become less manual
- generated outputs should naturally return to space
- implementation should not force premature schema or automation

## 3. current loop to support

Target loop:

```text
user input
→ space lookup
→ related assets / lines / lenses
→ Codex interpretation
→ user-facing output
→ return-to-space record
→ future re-emergence
```

This should not become:

```text
every input → heavy package → full report → index mutation
```

## 4. existing assets that already support the loop

| Asset | Current role |
| --- | --- |
| `docs/indexes/space_boundary_material_flow_map_v0.md` | main operating map for boundary material flow |
| `docs/indexes/external_material_microspace_index_v0.md` | findable/re-emergent external material subspace |
| `docs/indexes/space_translation_language_base_v0.md` | source language base for translation / bridge wording |
| `docs/reports/space_boundary_live_use_stabilization_closeout_v0.md` | live-use default and lens visibility rule |
| `docs/reports/external_material_microspace_feature_candidate_survey_v0.md` | strongest feature candidates: re-emergence reminder + intake cockpit |
| `scripts/record_operation_event.py` | existing event ledger writer |
| `scripts/cli/run_phase1_space_query.py` | existing broader query / exploration / reingress chain |
| `scripts/cli/explore_space.py` | draft exploration result builder from selected paths |
| `scripts/cli/write_reingress_record.py` | existing reingress record writer |
| `docs/notes/executable_runner_index_v0.md` | runner lookup index by intent |

## 5. scriptable steps

These steps are repeatable enough to script without replacing Codex judgment.

### 5.1 source surface detection

Script can classify input shape:

```yaml
url: web / external material
local_path: repo file / runtime artifact / reference repo
plain_user_text: conversation material
generated_report_path: Codex output / report artifact
runtime_json: runtime evidence
```

Script should output a guess, not a final route.

Scriptability:

```yaml
level: high
recommended_form: read-only helper
```

### 5.2 candidate asset lookup

Script can search small known indexes first:

- `docs/indexes/space_boundary_material_flow_map_v0.md`
- `docs/indexes/external_material_microspace_index_v0.md`
- `docs/indexes/space_translation_language_base_v0.md`
- `docs/indexes/space_asset_map_v0.md`
- `docs/guides/space_asset_retrieval_manual_v0.md`
- `docs/notes/executable_runner_index_v0.md`

Script output should be a compact context packet:

```yaml
candidate_assets:
  - path
  - reason
  - matched_terms
  - authority_hint
```

Scriptability:

```yaml
level: high
recommended_form: read-only lookup packet
```

### 5.3 microspace candidate match

Script can scan `external_material_microspace_index_v0.md` for cluster aliases, source URLs, and lens labels.

It can suggest:

```yaml
candidate_cluster:
candidate_material_cards:
matched_lenses:
matched_guardrails:
```

But it should not decide whether a material is direct evidence, defensive logic, or comparison frame.

Scriptability:

```yaml
level: medium_high
recommended_form: suggestion-only
```

### 5.4 user-facing card template

Script can render a blank or partially filled card:

```text
현재 판정:
이유:
선택 렌즈:
다음 이동:
금지선:
```

Script may prefill source and candidate cluster, but Codex should fill judgment.

Scriptability:

```yaml
level: high
recommended_form: template renderer
```

### 5.5 operation event recording

Existing script already supports event ledger writing:

```text
scripts/record_operation_event.py
```

This can record:

- material read
- report created
- index updated
- return-to-space completed

Scriptability:

```yaml
level: high
recommended_form: reuse existing script
```

### 5.6 return-to-space skeleton

Script can create a small skeleton record after Codex provides judgment:

```yaml
source_ref:
input_summary:
selected_assets:
selected_lenses:
codex_judgment:
return_state:
next_reemergence_trigger:
created_outputs:
```

This should remain a record helper, not an authority engine.

Scriptability:

```yaml
level: medium
recommended_form: optional writer after Codex judgment
```

## 6. Codex-required steps

These should remain Codex-led because they require interpretation, purpose reading, and maturity judgment.

### 6.1 user intent reading

Codex must decide:

```text
왜 사용자가 지금 이 재료를 가져왔는가?
```

Keyword matching can help but cannot decide the purpose.

### 6.2 lens selection

Codex must choose which lenses actually matter:

- technical
- maker-intent
- user-intent
- line/axis
- feature-direction
- risk
- residue
- narrative / mechanism / operational path

Script may suggest lenses from keywords, but Codex must confirm.

### 6.3 state judgment

Codex must decide:

```yaml
reread_priority
framing_candidate
bounded_action_candidate
guarded_execution
validation_return
archive_as_residue
```

This is not a pure classification problem because the same material can move differently depending on user purpose and current context.

### 6.4 promotion barrier / guardrail

Codex must write the actual guardrail:

```text
무엇을 너무 빨리 승격/실행/수입하면 위험한가?
```

This is a judgment boundary, not just a label.

### 6.5 merge / buffer / action decision

Codex must decide whether the material should:

- stay as residue
- update a microspace index
- become a comparison frame
- become a bounded action candidate
- ask user for judgment
- stop

### 6.6 translation preservation

Codex must preserve route, authority, state, boundary, and maturation meaning before simplifying language.

The translation base can reduce token use, but cannot replace this judgment.

## 7. hybrid steps

These are best handled by script + Codex together.

| Step | Script role | Codex role |
| --- | --- | --- |
| Source reading | fetch or locate source, capture metadata | interpret technical/maker/user meaning |
| Asset lookup | propose top candidate docs | choose which are actually relevant |
| Lens suggestion | keyword-based lens candidates | select active lenses and explain why |
| Card generation | render template | fill judgment |
| Return record | create skeleton / append event | decide return state and re-emergence trigger |
| Index update | locate insertion point / draft entry | decide whether update is warranted |

## 8. token-saving design

The most useful script is not a full pipeline.

The most useful script is a compact context packet generator.

Candidate output:

```yaml
input_ref:
source_surface_guess:
matched_microspace_clusters:
candidate_assets:
  - path
  - reason
  - matched_terms
candidate_lenses:
  - lens
  - reason
existing_guardrails:
  - guardrail
card_template:
  current_judgment:
  reason:
  selected_lenses:
  next_move:
  do_not:
```

This would let Codex read 1 compact packet instead of rereading 5-10 large docs every time.

## 9. likely script candidates

### Candidate 1. `space_boundary_lookup_packet.py`

Purpose:

```text
Given input text/url/path, produce compact lookup packet from existing indexes.
```

Inputs:

- raw input text
- optional local path
- optional source URL

Outputs:

- source_surface_guess
- candidate assets
- matched external material cluster
- candidate lenses
- known guardrails
- blank user-facing card

Risk:

- If it pretends to decide state, it will over-automate.

Recommended status:

```yaml
priority: 1
safe_to_build_later: yes
mode: read_only
```

### Candidate 2. `space_return_record_writer.py`

Purpose:

```text
After Codex judgment, write a small return-to-space record or append event.
```

Inputs:

- source_ref
- judgment card
- output refs
- return_state

Outputs:

- JSONL event via existing event ledger, or small markdown record

Risk:

- Can create document noise if used for every trivial answer.

Recommended status:

```yaml
priority: 2
safe_to_build_later: yes
mode: write_after_judgment
```

### Candidate 3. `external_material_cockpit_card.py`

Purpose:

```text
Render external material cockpit card from lookup packet + Codex-filled fields.
```

Risk:

- Could become a form instead of a surface output.

Recommended status:

```yaml
priority: 3
safe_to_build_later: maybe
mode: template_only
```

### Candidate 4. `translation_base_slice.py`

Purpose:

```text
Select a small translation-language subset by source type.
```

Examples:

- external material subset
- Codex handoff subset
- user-facing explanation subset
- runtime return subset

Risk:

- If slice is too broad, token savings disappear.

Recommended status:

```yaml
priority: 4
safe_to_build_later: yes
mode: read_only
```

## 10. what should not be scripted yet

- final state judgment
- lens selection as final decision
- promotion / baseline / implementation decision
- direct evidence vs comparison frame as final label
- guarded execution elevation
- microspace index mutation without Codex judgment
- automatic report generation for every input
- automatic external web fetching and ingestion as default

## 11. implementation boundary

If implemented later, start with:

```text
read-only lookup packet generator
```

Do not start with:

```text
full pipeline automation
automatic index mutation
runtime manifest creation
validator
agent router
```

Reason:

```text
The current bottleneck is retrieval/context cost and habit consistency, not lack of execution power.
```

## 12. recommended minimal architecture

```text
User input
→ script: lookup packet
→ Codex: judgment + user-facing card
→ optional script: event / return record
→ space: re-emergence material
```

This keeps Codex doing interpretation while scripts reduce repetitive search and record work.

## 13. verdict

```yaml
verdict: PASS_WITH_NOTE
scriptable_now:
  - source surface guess
  - candidate asset lookup
  - microspace cluster suggestion
  - card template rendering
  - event recording
  - return record skeleton
codex_must_keep:
  - user intent reading
  - lens selection
  - state judgment
  - guardrail writing
  - promotion/action decision
  - translation preservation
best_next_build_candidate:
  - scripts/cli/space_boundary_lookup_packet.py
main_token_saving:
  - compact context packet instead of rereading large docs
main_guardrail:
  - helper scripts suggest; Codex decides
```

## 14. unresolved questions

- Should the lookup packet search only known indexes, or also bounded reports?
- Should event recording be automatic after every created report, or only after non-trivial boundary material?
- Should return-to-space records be markdown, JSONL, or both?
- Should the lookup helper include web source metadata, or only local space lookup?
- How small can the translation-language slice be while still preserving space meaning?

