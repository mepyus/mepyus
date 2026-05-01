# Space Boundary Source Surface Lens Order Note v0

## 1. status

```yaml
report_status: operating_note
based_on:
  - docs/reports/space_feedback_loop_multi_surface_case_collection_v0.md
  - docs/indexes/space_boundary_material_flow_map_v0.md
  - docs/indexes/space_translation_language_base_v0.md
purpose: define source-surface-first lens ordering so Codex can read the space with less full-context reread
verdict: PASS_WITH_NOTE
baseline_lock: false
schema_enforcement: false
implementation: false
helper_patch: false
```

## 2. why this note exists

The multi-surface case collection showed:

```text
The same keywords mean different things depending on the source surface.
```

Example:

- `runtime` in an event log means actual happened trace.
- `runtime` in an external repo note may mean product architecture.
- `Codex output` in a generated report is validation_return material, not final truth.
- `외부자료` in conversation may point to feature direction, not only an external material card.

Therefore the first gate should be:

```text
source surface -> lens order -> asset slice -> Codex judgment
```

not:

```text
all text -> all lenses -> all clusters
```

## 3. source-surface-first rule

Default rule:

```text
Detect source surface first. Then activate only the lens order needed for that surface.
```

The lookup helper can suggest candidate assets and lenses, but Codex should override noisy lens suggestions using the source surface.

## 4. lens order by source surface

## 4.1 external material URL / file

Examples:

- GeekNews topic
- GitHub repo
- paper/blog
- `inputs/external_cases/*.md`

First lens order:

```text
technical -> maker-intent -> user-intent -> line/axis -> risk -> residue
```

If architecture/repo hype is visible:

```text
narrative-mechanism-operational path -> risk -> residue
```

Default safe states:

```text
unclassified -> reread_priority -> framing_candidate
```

Do not:

- treat external material as direct evidence on first read
- import workflow/schema/runtime directly
- use README/AI summary as validation

## 4.2 generated report / Codex output

Examples:

- `docs/reports/*_trial_v0.md`
- Codex comparison report
- closeout report
- output from a prior package run

First lens order:

```text
user-intent -> line/axis -> risk -> residue -> return-state
```

Default safe states:

```text
validation_return
process_residue
framing_support
```

Do not:

- treat report completion as final result
- treat Codex output as proof
- match full-body keywords before checking report status and return-state sections

Codex judgment:

```text
Generated reports should usually answer:
"What does this output return to the space as?"
```

## 4.3 runtime artifact / event log

Examples:

- `runtime/events/*.jsonl`
- receipts
- manifests
- test logs
- operation board outputs

First lens order:

```text
evidence/event -> technical -> risk -> residue -> line/axis
```

Default safe states:

```text
reread_priority
evidence_residue
validation_return
```

Do not:

- treat runtime traces as external material
- infer direct proof without knowing what claim is being tested
- promote logs into operating doctrine

Codex judgment:

```text
Runtime artifacts should first answer:
"What happened, what does it prove, and what does it fail to prove?"
```

## 4.4 conversation material

Examples:

- user clarification
- conceptual summary
- frustration / bottleneck statement
- direction-setting statement

First lens order:

```text
user-intent -> feature-direction -> line/axis -> residue -> risk
```

Default safe states:

```text
unclassified seed
framing_candidate
feature_direction_candidate
reread_priority
```

Do not:

- reduce conversation material to task instruction only
- ignore it as non-documentary
- immediately convert it into implementation

Codex judgment:

```text
Conversation material often reveals the direction of the space more strongly than external references.
```

## 4.5 worker return

Examples:

- bounded comparer result
- packet preparer result
- executor result
- structured return block

First lens order:

```text
expected-vs-observed -> risk -> residue -> next-move -> line/axis
```

Default safe states:

```text
validation_return -> refine / hold / downgrade / archive_as_residue
```

Do not:

- treat worker success as promotion
- treat worker output as final
- skip reread_return_hook

Codex judgment:

```text
Worker return should answer:
"What branch should this return take now?"
```

## 4.6 program artifact / generated index

Examples:

- generated JSON bundle
- generated index
- label packet
- origin map
- folder inventory

First lens order:

```text
artifact-role -> evidence/event -> technical -> residue -> risk
```

Default safe states:

```text
artifact_residue
validation_return
reread_priority
```

Do not:

- treat generated artifact existence as usefulness
- make it user-facing by default
- add it to microspace without re-emergence value

Codex judgment:

```text
Program artifacts should answer:
"What role does this artifact play in the space, and when should it reappear?"
```

## 5. minimal operating card

For all source surfaces, output to the user stays:

```text
현재 판정:
이유:
다음 이동:
금지선:
```

Internal additions can include:

```yaml
source_surface:
first_lens_order:
selected_lenses:
return_state:
reemergence_trigger:
```

These are not user form fields.

## 6. implications for the lookup helper

The current helper is useful but surface-neutral after detection.

Possible later patch:

```text
Once source_surface_guess is known, weight candidate lenses by source surface.
```

Do not patch yet.

Reason:

```text
We need a few more cross-surface cases before changing ranking behavior.
```

## 7. token-cost implication

This note supports a lighter Codex read:

```text
source surface
-> lens order slice
-> relevant index slice
-> Codex judgment
-> 4-line card
-> return record minimum
```

The aim is to avoid:

```text
every material -> reread whole space -> produce heavy report
```

## 8. validation check

| Check | Result | Note |
| --- | --- | --- |
| Covers external material | PASS | Existing OpenMythos / GoScrapy / Gemini examples fit. |
| Covers Codex output / generated reports | PASS | Prior session reports fit validation_return / residue handling. |
| Covers runtime artifacts | PASS_WITH_NOTE | Needs explicit evidence/event lens in translation base later. |
| Covers conversation material | PASS | User direction statements fit feature-direction / line-axis route. |
| Reduces token pressure | PASS_WITH_NOTE | Conceptual reduction is clear; helper weighting not implemented. |
| Avoids schema lock | PASS | This is an operating note, not enforced routing. |

## 9. next recommended move

```yaml
next_mode: collect_more_cross_surface_cases
helper_patch_now: false
recommended_future_patch:
  - source-surface-weighted lens ranking in lookup helper
  - only after more cases confirm the lens order
```

Use this note during the next material intake before reading large document sets.

## 10. unresolved questions

- Should `evidence/event lens` and `artifact-role lens` be added to the translation language base later?
- Should helper output include `first_lens_order` as a suggestion?
- Should generated report matching prioritize status/return-state sections over full text?
- How many cases are enough before source-surface-weighted lens ranking is worth implementing?
