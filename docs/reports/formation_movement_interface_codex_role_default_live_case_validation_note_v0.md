# Formation-Movement Interface Codex Role Default Live Case Validation Note v0

## 1. status

```yaml
status: validation_note
mode: live_case_codex_role_default_check
verdict: PASS_WITH_NOTE
purpose: test whether the route-specific Codex role default mapping reduces manual steering in one real short-prompt case
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
```

## 2. test case

### live prompt

```text
이 두 링크 넣어봐.
```

### assumed material

- `agent-skills`
- `Flutist`

### relevant backend context

- `docs/reports/formation_movement_interface_codex_role_default_mapping_note_v0.md`
- `docs/reports/formation_movement_interface_external_governance_architecture_cluster_note_v0.md`
- `docs/reports/formation_movement_interface_workflow_controller_spec_v0.md`
- `docs/reports/formation_movement_interface_live_prompt_controller_behavior_validation_note_v0.md`

## 3. what this test is checking

This test does not ask whether the cluster is useful.

That was already established.

It asks:

> when the user gives only a short external-material prompt, does the controller now more safely assume the Codex default role without extra steering?

## 4. expected healthy behavior

For `external material`, the new default mapping says:

```text
default Codex role = no Codex yet
```

Only later, if the material stabilizes for bounded comparison:

```text
Codex = comparer
```

So the healthy path should be:

```text
short prompt
→ external material route
→ unclassified seed
→ process-first line check
→ formed judgment
→ merge into reusable cluster
→ no Codex by default at entry
→ Codex comparer only if bounded comparison is actually needed
→ compact user card
```

## 5. staged validation

## 5.1 route detection

### observed judgment

```text
external material route
```

### verdict

`PASS`

### note

The prompt is extremely short, but still safely routes without asking the user:

- whether this is ingest
- whether this is compare
- whether this is B/C/A

This is a real usability gain.

## 5.2 safe entry state

### observed judgment

```text
unclassified seed
```

### verdict

`PASS`

### note

The controller does not pressure the user into:

- evidence classification
- line ranking
- Codex invocation

too early.

## 5.3 Codex default role at entry

### observed judgment

```text
no Codex yet
```

### verdict

`PASS`

### note

This is the most important difference from the earlier operator-heavy pattern.

Before the mapping note, the ambiguity often sat here:

```text
should Codex analyze now or not?
```

With the route-default note, the safer answer becomes immediate:

```text
not yet
```

That removes one invisible operator decision.

## 5.4 process-first reading and merge

### observed judgment

- `agent-skills`:
  workflow / validation / bounded preparation grammar
- `Flutist`:
  architecture boundary / rules-as-code / check-without-mutate grammar

Merged object:

```text
external governance-architecture comparison cluster
```

Type:

```text
framing_candidate
```

Move:

```text
compare_only
```

### verdict

`PASS`

### note

The route-specific default mapping does not disturb the already healthy process-first merge behavior.

That is important.

The new usability improvement does not damage the previous analytical discipline.

## 5.5 Codex role after stabilization

### observed judgment

Once the merged cluster exists, Codex becomes appropriate only as:

```text
comparer
```

not as:

- executor
- doctrine importer
- direct-evidence confirmer

### verdict

`PASS_WITH_NOTE`

### note

The role itself is now clearer.

What still remains slightly manual is timing:

- exactly when to stop with the cluster only
- exactly when bounded comparison is worth invoking

So the role default improved.

The role-upgrade timing is still not fully automatic.

## 5.6 output shape

### observed judgment

Default public output remains:

```text
현재 판정:
이유:
다음 이동:
금지선:
```

Healthy compact card for this case:

```text
현재 판정: external governance-architecture comparison cluster
이유: 두 재료 모두 구조/경계/검증을 강하게 비추며, 바로 증거로 잠그기보다 비교 재료로 두는 것이 안전함
다음 이동: compare_only로 공간에 배치하고 필요할 때만 bounded comparison 실행
금지선: direct evidence lock / workflow import / baseline 반영 금지
```

### verdict

`PASS`

### note

The controller can now stay compact without forcing a Codex substep at entry.

## 6. operator burden check

### before this mapping note

The hidden operator had to decide:

- call Codex now or later
- if later, why later
- if now, in what role

### after this mapping note

For this route, the hidden decision compresses into:

```text
default = no Codex yet
upgrade = comparer only if bounded comparison is needed
```

### verdict

`PASS_WITH_NOTE`

### note

The burden is lower, but not gone.

The remaining ambiguity is now narrower and more honest:

```text
whether to upgrade into comparer now
```

not:

```text
what Codex even is here
```

## 7. what improved

This live case shows three concrete gains:

### A. faster safe default

The system can now say:

```text
external material -> no Codex yet
```

immediately.

### B. clearer bounded upgrade

If the material matures, the next Codex role is no longer vague.

It is:

```text
comparer
```

### C. lower front-door friction

The user can remain at:

```text
이 두 링크 넣어봐
```

without having to imply:

- compare this
- analyze this
- don't execute this
- use Codex carefully

## 8. what is still weak

The mapping note improves role defaulting.

It does not yet fully solve:

```text
the maturity threshold for upgrading from no-Codex to comparer
```

That still depends on:

- whether the cluster is already reusable enough
- whether an internal scene actually needs bounded comparison now

## 9. final judgment

Compressed judgment:

```text
이 live case에서는 route별 Codex role default mapping이 실제로 수동 조향을 줄였다.
특히 external material route에서 no-Codex-first가 명시되면서 front-door가 훨씬 자연스러워졌다.
다만 comparer로 올리는 타이밍은 아직 더 많은 실사례가 필요하다.
```

Overall verdict:

`PASS_WITH_NOTE`

## 10. next recommended check

The next most useful narrow test is:

```text
Codex task request route
```

Specifically:

can the controller now naturally default to:

```text
no Codex yet
→ packet preparer later
```

without forcing manual route explanation?
