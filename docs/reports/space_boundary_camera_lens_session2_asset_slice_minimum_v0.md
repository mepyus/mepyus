# Space Boundary Camera-Lens Session 2 Asset Slice Minimum v0

## 1. status

```yaml
report_status: session_validation_report
package: docs/reports/space_boundary_camera_lens_operationalization_package_v0.md
session: Session 2. asset-slice minimum check
verdict: PASS_WITH_NOTE
baseline_lock: false
schema_enforcement: false
implementation: false
runtime_manifest_created: false
index_mutation: false
helper_patch: false
```

## 2. goal check

Question:

```text
Can Codex avoid loading the whole space by using a smaller source-surface asset slice?
```

This session treats the lens order as the camera selection rule and defines the minimal document slice per source surface.

## 3. common first pass

For all surfaces, the common first pass is:

```text
1. run scripts/cli/space_boundary_lookup_packet.py
2. inspect source_surface_guess
3. apply source-surface lens order
4. read only the minimum slice for that surface
5. let Codex judge final state and card
```

The lookup packet is not the decision.

It is the starting packet.

## 4. external material URL / file

Examples:

- GeekNews topic
- GitHub repo
- paper/blog
- `inputs/external_cases/*.md`

Required first slice:

```yaml
source_surface: external_material_url_or_file
required_first_slice:
  - input material or URL/source record
  - docs/indexes/space_boundary_material_flow_map_v0.md
  - docs/indexes/space_translation_language_base_v0.md
  - docs/indexes/external_material_microspace_index_v0.md
```

Optional second slice:

```yaml
optional_second_slice:
  - related prior analysis report if a microspace card points to it
  - docs/notes/executable_runner_index_v0.md only if a runner/action question appears
  - references/git_search/<repo> only if concrete repo comparison is requested
```

Avoid by default:

```yaml
avoid_by_default:
  - full runtime artifacts
  - broad docs/reports search
  - unrelated external clusters
  - implementation specs
```

Escalate when:

```yaml
escalate_when:
  - source-level verification is requested
  - concrete comparison target exists
  - material may deserve a microspace card
  - execution or bounded worker-role is being considered
```

First lens order:

```text
technical -> maker-intent -> user-intent -> line/axis -> risk -> residue
```

## 5. generated report / Codex output

Examples:

- `docs/reports/*_trial_v0.md`
- Codex comparison report
- closeout report
- package output

Required first slice:

```yaml
source_surface: generated_report_or_codex_output
required_first_slice:
  - target report
  - docs/indexes/space_boundary_material_flow_map_v0.md
  - docs/indexes/space_translation_language_base_v0.md
```

Optional second slice:

```yaml
optional_second_slice:
  - related package/report referenced by the target report
  - docs/indexes/external_material_microspace_index_v0.md only if the report is explicitly about external material
  - docs/indexes/space_asset_map_v0.md if report role is unclear
```

Avoid by default:

```yaml
avoid_by_default:
  - treating report body keyword matches as cluster proof
  - external material microspace as primary route when the source is Codex output
  - reference repos unless comparison is requested
  - runtime logs unless report claims runtime behavior
```

Escalate when:

```yaml
escalate_when:
  - report claims implementation/runtime behavior
  - report is being considered for package closeout or patch readiness
  - output needs to become validation_return or return record
```

First lens order:

```text
user-intent -> line/axis -> risk -> residue -> return-state
```

## 6. runtime artifact / event log

Examples:

- `runtime/events/*.jsonl`
- receipts
- manifests
- test logs
- operation board outputs

Required first slice:

```yaml
source_surface: runtime_artifact_or_event_log
required_first_slice:
  - target runtime artifact
  - docs/indexes/space_asset_map_v0.md
  - docs/guides/space_asset_retrieval_manual_v0.md
  - docs/indexes/space_boundary_material_flow_map_v0.md
```

Optional second slice:

```yaml
optional_second_slice:
  - docs/indexes/space_translation_language_base_v0.md for state/lens language
  - runtime/contracts/ if artifact is a contract/return instance
  - docs/notes/executable_runner_index_v0.md if a runner produced the artifact
  - related report only if artifact points to it
```

Avoid by default:

```yaml
avoid_by_default:
  - external_material_microspace_index as primary route
  - interpreting runtime terms as external architecture terms
  - full runtime directory reads
  - promotion from log existence
```

Escalate when:

```yaml
escalate_when:
  - a specific claim needs evidence
  - event type or receipt chain is unclear
  - runtime artifact must be tied to a report or package output
```

First lens order:

```text
evidence/event -> technical -> risk -> residue -> line/axis
```

## 7. worker return / structured return

Examples:

- `runtime/cli_sessions/*/structured_return.json`
- bounded comparer return
- packet preparer return
- executor return

Required first slice:

```yaml
source_surface: worker_return_or_structured_return
required_first_slice:
  - target structured return
  - relevant return contract if known
  - docs/indexes/space_boundary_material_flow_map_v0.md
  - docs/indexes/space_translation_language_base_v0.md
```

Optional second slice:

```yaml
optional_second_slice:
  - originating command/session record
  - related package/report referenced by return
  - runtime/events only if execution evidence is needed
```

Avoid by default:

```yaml
avoid_by_default:
  - external material clusters as primary route
  - treating successful worker output as promotion
  - broad cli_sessions sweep
```

Escalate when:

```yaml
escalate_when:
  - expected_return_form is missing
  - boundary drift is suspected
  - trust_scope changed
  - output may become guarded_execution evidence
```

First lens order:

```text
expected-vs-observed -> risk -> residue -> next-move -> line/axis
```

## 8. program artifact / generated index

Examples:

- generated JSON bundle
- label packet
- origin map
- line seed bundle
- folder inventory

Required first slice:

```yaml
source_surface: program_artifact_or_generated_index
required_first_slice:
  - target artifact
  - docs/indexes/space_asset_map_v0.md
  - docs/guides/space_asset_retrieval_manual_v0.md
  - docs/indexes/space_boundary_material_flow_map_v0.md
```

Optional second slice:

```yaml
optional_second_slice:
  - originating input file
  - generating script note from docs/notes/executable_runner_index_v0.md
  - related operator summary or readable board
  - external material microspace only if the artifact came from an external material and re-emergence is being judged
```

Avoid by default:

```yaml
avoid_by_default:
  - treating artifact existence as line proof
  - treating generated bundle as user-facing output
  - adding every artifact to microspace
```

Escalate when:

```yaml
escalate_when:
  - artifact role is unclear
  - artifact is used as evidence for a line/axis
  - artifact should become a return record or reingress record
```

First lens order:

```text
artifact-role -> evidence/event -> technical -> residue -> risk
```

## 9. conversation material

Examples:

- user clarification
- frustration statement
- concept summary
- direction-setting statement

Required first slice:

```yaml
source_surface: conversation_material
required_first_slice:
  - current conversation excerpt
  - docs/indexes/space_boundary_material_flow_map_v0.md
  - docs/indexes/space_translation_language_base_v0.md
```

Optional second slice:

```yaml
optional_second_slice:
  - related current package if explicitly referenced
  - external_material_microspace_index if user mentions external materials
  - executable_runner_index if the user asks what can run
```

Avoid by default:

```yaml
avoid_by_default:
  - converting every user thought into implementation
  - treating conversation as less important than files
  - broad docs/reports search before direction is clear
```

Escalate when:

```yaml
escalate_when:
  - user opens a package/action
  - user asks to compare with existing space lines
  - recurring frustration suggests a feature-direction candidate
```

First lens order:

```text
user-intent -> feature-direction -> line/axis -> residue -> risk
```

## 10. cross-surface minimum summary

| Surface | Required first slice count | Needs external microspace first? | Needs runtime first? |
| --- | ---: | --- | --- |
| external material | 4 | yes | no |
| generated report / Codex output | 3 | only if explicit | no |
| runtime artifact | 4 | no | yes |
| worker return | 4 | no | yes |
| program artifact | 4 | only if external-derived | yes |
| conversation material | 3 | only if mentioned | no |

## 11. token pressure judgment

This slice map reduces token pressure because Codex no longer needs to start from:

```text
all reports + all indexes + all runtime + all microspace
```

Instead:

```text
source_surface -> 3-4 first-slice assets -> Codex judgment -> optional escalation
```

The biggest savings are for:

- generated reports
- runtime artifacts
- conversation material

Those surfaces previously over-triggered external microspace and broad report reading.

## 12. validation check

| Check | Result | Note |
| --- | --- | --- |
| Each source surface has a small first slice | PASS | 3-4 first-slice assets per surface. |
| External microspace no longer overused | PASS_WITH_NOTE | Still needed for external material and explicit references. |
| Runtime artifacts get runtime-first reading | PASS | Asset map/retrieval manual become first-slice. |
| Conversation material preserved | PASS | User intent and feature-direction are first-class. |
| Avoids schema / implementation | PASS | Slice map only. |
| Ready for helper patch | HOLD | Need Session 4 readiness check after return-record fit. |

## 13. return-to-space judgment

```yaml
return_state: asset_slice_minimum_validated
next_allowed_move: Session 3. return-record fit across surfaces
helper_patch_now: false
```

## 14. verdict

```yaml
verdict: PASS_WITH_NOTE
why:
  - source surfaces can start from 3-4 asset slices
  - broad full-space reread is avoidable in normal cases
  - optional escalation paths remain available
note:
  - runtime/worker/program artifact source subtypes are still compressed under runtime_artifact in the helper
```

## 15. unresolved questions

- Should `source_surface_guess` output subtypes for `worker_return` and `program_artifact`?
- Should the helper include `required_first_slice` suggestions?
- Should generated report matching read status/return sections before body?
- Should conversation material have a lightweight memory capture path separate from reports?
