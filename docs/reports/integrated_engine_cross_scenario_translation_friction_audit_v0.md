# Integrated Engine Cross-Scenario Translation Friction Audit v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

The current integrated-engine baseline remains usable in stop-and-use / use observation mode.

This audit finds translation friction, not structural failure. The friction appears when internally precise language such as `VectorFL review`, `return validation`, `reflux`, `anchor drift`, `current_loop_state`, and `support trace` must be understood as user-facing operating guidance.

No wording patch planning is opened. No scaffold, manifest, read-map, selected-object, trace UI, runtime binding, or extension work is authorized by this audit.

## 1. audit boundary

Observed scenario families:

- S1 normal request loop
- S3 drift / reprocess / reflux loop
- one real-use-like case: Gemini/Codex parallel design-material handoff

This audit records:

- internal phrase or panel wording
- first-pass reading
- supported reread reading
- user-facing easy translation attempt
- where translation friction appears
- friction classification

It does not produce patch wording and does not recommend UI changes.

## 2. classification key

| classification | meaning |
|---|---|
| `internal-to-user wording gap` | Internal language is structurally accurate but not immediately user-comprehensible. |
| `support-dependent meaning` | Meaning recovers only after reading packets, connection records, or protocol notes. |
| `scenario-specific compression` | A phrase compresses route context that differs by scenario. |
| `fixture-scope limitation` | Current direct read mapping is first-fixture centered; other samples need manual panel-role reading. |
| `hold-feature expectation leak` | A phrase tempts selected-object, trace UI, runtime binding, or extension expectations. |
| `not-a-problem` | The term is readable enough under current use mode. |

## 3. S1 normal request loop

Scenario route:

```text
user request
-> VectorFL review / mediation
-> engine processing
-> return
-> VectorFL validation
-> reflux / user decision remains open
```

| internal phrase or panel wording | first-pass reading | supported reread reading | user-facing easy translation attempt | where translation friction appears | friction classification |
|---|---|---|---|---|---|
| `VectorFL review -> engine processing / external support` | Sounds like a hidden step or missing connection record. | Protocol says this transition is confirmed by request route intent plus later return packet, not a separate record in the current low-intensity bundle. | "VectorFL checks the request before work proceeds." | Easy wording hides that the route is reconstructed from packet intent and return evidence. | `support-dependent meaning` |
| `return validation` | Can sound like the engine already validated its own result. | Engine return is processing output; VectorFL validates before user decision / reflux / reprocess. | "The result comes back for checking before it is treated as usable." | User-facing wording must avoid making validation sound engine-owned. | `internal-to-user wording gap` |
| `reflux` | Unfamiliar term; can sound like a failure or rollback. | Reflux preserves maturation-worthy material for reread and future line/axis growth. | "Keep the useful residue for later growth." | Easy wording loses the sense that reflux is a route/reason packet, not just storage. | `internal-to-user wording gap` |
| `current_loop_state` | May sound like full workflow history. | It is current-position state; full progression requires panel connection records. | "Where the loop is right now." | Simple translation is accurate, but users may still expect timeline history. | `support-dependent meaning` |

S1 summary:

- The route is readable.
- Friction is mostly caused by internal precision around validation, reflux, and loop-state scope.
- No S1 term currently blocks scenario reading.

## 4. S3 drift / reprocess / reflux loop

Scenario route:

```text
engine return exists
-> VectorFL detects anchor drift
-> route does not move directly to user decision
-> engine reprocess request is created
-> loop remains open in reprocess / rewind state
```

| internal phrase or panel wording | first-pass reading | supported reread reading | user-facing easy translation attempt | where translation friction appears | friction classification |
|---|---|---|---|---|---|
| `anchor drift` | Sounds technical; may read as vague mismatch. | Anchor mismatch is a real stop reason that prevents direct user decision and triggers reprocess. | "The result no longer fits the reference point." | Easy wording explains mismatch but can understate the route-braking authority of anchor criteria. | `internal-to-user wording gap` |
| `anchor_context_panel` as support panel | Because it is visually/support-wise secondary, it can seem advisory only. | Connection record shows anchor context / validation mediation can stop progression and wake reprocess. | "Reference check panel." | User-facing translation may not reveal that the support criterion can hold the route. | `support-dependent meaning` |
| `reprocess / rewind` | Can sound like confusion or undoing work. | Loop is intentionally held open for correction; current state records previous slot, held reason, and rewind reason. | "Send it back for correction." | Easy translation risks making the route look like failure rather than structured correction. | `scenario-specific compression` |
| `held_from_closure_reason` / `rewind_reason` | Internal state labels are clear to operators, not natural to users. | They explain why the loop did not close and why it moved back toward reprocess. | "Why this was not finished yet." | Friendly wording loses the separation between closure hold and rewind cause. | `internal-to-user wording gap` |
| Drift connection record outside current primary read map | Looks like evidence/history may be missing. | Interface note says drift-reprocess samples are manually checked through same panel-role grammar. | "Use the extra route record for this scenario." | This is not wording friction; it is fixture scope. | `fixture-scope limitation` |

S3 summary:

- The correction loop is readable.
- Friction concentrates around making `anchor drift` feel like an operational brake rather than a descriptive note.
- The support panel remains subordinate; no need to promote anchor panel to center.

## 5. real-use-like case: Gemini/Codex parallel design-material handoff

Case:

- User wants Gemini CLI to generate design/user-surface material.
- Codex should preserve baseline and translate Gemini output.
- Gemini may write under `gemini/` only.
- Codex decides whether material is usable, needs translation, carry-forward, reject/conflict, or needs user decision.

| internal phrase or panel wording | first-pass reading | supported reread reading | user-facing easy translation attempt | where translation friction appears | friction classification |
|---|---|---|---|---|---|
| `proposal-only / needs Codex translation` | May sound like bureaucratic delay or weak output. | It protects the baseline by keeping Gemini material as design clay until translated. | "Gemini drafts ideas; Codex checks what can enter the system." | Easy wording works, but loses the formal promotion barrier. | `internal-to-user wording gap` |
| `Gemini expands possibility space; Codex filters against baseline` | Understandable as collaboration metaphor. | Maps to Gemini as design/user-surface proposal worker and Codex as VectorFL-side baseline translator. | "Gemini explores options; Codex keeps them aligned." | Low friction; this is close to user-facing already. | `not-a-problem` |
| `workspace ownership` | Can sound like file-system bureaucracy. | It prevents simultaneous writes: Gemini writes only under `gemini/`; Codex writes canonical docs/patches only under scoped packages. | "Each agent has its own work area." | Easy wording hides that ownership is also an authority boundary. | `internal-to-user wording gap` |
| `collision stop condition` | Sounds like technical process management. | It defines when Gemini/Codex joint work must stop: core edit attempts, read-map changes, runtime binding, authority drift, etc. | "Stop if the idea would change the engine body." | Easy translation is good, but details matter for avoiding accidental build-mode reopen. | `scenario-specific compression` |
| `design clay` | Friendly and understandable. | Means Gemini output is raw design material, not accepted UI or core structure. | "Raw design material." | Low friction if paired with baseline translation rule. | `not-a-problem` |

Real-use-like summary:

- The parallel-agent model is easier to explain than the packet/loop terms.
- The main friction is not comprehension; it is authority status. Users may understand the design idea but not whether it is allowed to enter core.

## 6. cross-scenario findings

Repeated friction patterns:

1. Internal terms are precise because they protect boundaries.
   - `reflux`, `return validation`, `anchor drift`, `current_loop_state`, and `proposal-only` each carry a boundary that simple wording can flatten.

2. Supported reread is doing real work.
   - S1 needs packet intent + return packet.
   - S3 needs connection records + loop-state reasons.
   - Gemini/Codex parallel use needs handoff status + workspace ownership.

3. Easy translations are possible but risky if treated as replacement language.
   - "check", "send back", "save for later", and "draft ideas" help comprehension, but can erase packet roles or authority boundaries.

4. Translation friction is not yet wording-patch evidence.
   - These observations are cross-scenario friction candidates, not patch candidates.
   - No scenario reading was blocked.

## 7. carry-forward candidates

Carry forward for later translation-rule harvest:

| candidate | why carry forward | current action |
|---|---|---|
| `reflux` user-facing bridge | Reflux is structurally useful but user-unfamiliar. | carry forward; no patch |
| `anchor drift` as operational brake | Users need to feel it stops flow, not just labels mismatch. | carry forward; no patch |
| `current_loop_state` current-position boundary | Prevents expectation of full timeline. | carry forward; no patch |
| `proposal-only / needs Codex translation` | Useful for Gemini/Codex joint use. | carry forward; no patch |
| `return validation` ownership boundary | Prevents engine-final-completion drift. | carry forward; no patch |

## 8. not translation problems

Clearly not translation problems in this round:

- first-fixture scaffold read mapping
- absence of selected-object behavior
- absence of trace UI
- absence of runtime binding
- compact evidence/history trace
- support panel subordination
- Gemini writing only under `gemini/`

These remain boundary or hold issues, not language failures.

## 9. recommendation

Recommendation:

- prepare a later external translation rule harvest only after one more real-use round or Gemini/Codex handoff trial.
- keep this audit as internal friction evidence.
- do not open wording patch planning from this audit alone.

External translation rule harvest should aim to collect user-facing bridge patterns, not replace internal baseline terms.

## 10. closeout sentence

The baseline remains usable; translation friction exists mainly where internal boundary language must become user-facing guidance without losing route, role, or promotion-control meaning.
