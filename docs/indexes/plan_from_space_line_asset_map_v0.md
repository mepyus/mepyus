# Plan from Space Line Asset Map v0

## Status

```yaml
status: line_asset_map_candidate
line: Plan from Space / Session Convergence Prevention
baseline_lock: false
automation: false
```

## Line Definition

This line prevents external tools from creating plans from model-default decomposition before VectorFL space records are activated.

It asks external tools to size work, stop/continue, and return results from existing space judgment rather than generic planning habits.

## Core Problem

Model-default planning tends to split work into small analysis / design / execution / verification / review sessions.

That can look safe, but in this space it often creates:

- session convergence
- user relay burden
- closeout inflation
- weak program continuity
- hard-boundary / watch-item confusion
- output without Return-to-Space Value

## Related Assets

| Asset | Why It Matters |
| --- | --- |
| `app/work/PROGRAM_FRAME_EXTERNAL_PATTERN_MAP_V0.md` | Defines external tools as attached roles and VectorFL space as source of truth. |
| `app/work/CONTEXT_BUNDLE_TEMPLATE_V0.md` | Already contains line / axis / camera / lens, boundaries, stop conditions, and recovery route fields. |
| `app/work/PACKAGE_END_FIX_REVIEW_V0.md` | Records tool drift and evidence gaps as fix/watch classification instead of undifferentiated failure. |
| `app/work/REVIEW_RECOVERY_GATE_V0.md` | Provides Recover / Candidate / Watch / Hold / Reject / Needs User classification. |
| `app/work/SESSION_43_RESULTS_V0.md` | Package 5 closeout shows real-input loop completion with issue classification. |
| `app/work/SESSION_44_RESULTS_V0.md` | Translates philosophy into behavior, including not making the user a copy-paste relay and requiring evidence / not-inspected disclosure. |
| `app/work/SESSION_45_RESULTS_V0.md` | Shows real external material intake with evidence used, not-inspected scope, user-facing card, and Issue Log. |
| `app/work/SESSION_46_RESULTS_V0.md` | Captures candidate closeout with watch status, user burden note, backlog handling, and closed implementation/automation boundary. |
| `app/work/SESSION_47_RESULTS_V0.md` | Re-attaches external tools to memory-judgment-execution-recovery and defines Return-to-Space Value. |
| `docs/specs/space_exploration_contract_v0.md` | Defines bounded exploration as selected assets, evidence, discarded assets, gaps, and confidence. |
| `docs/reports/space_cli_token_budget_and_memory_weight_policy_v0.md` | Supports anchor stack by preferring small relevant memory over full rereads. |
| `docs/reports/space_feedback_loop_return_to_space_record_minimum_v0.md` | Provides lightweight return record minimum fields and writer HOLD judgment. |
| `docs/specs/line_maturity_and_operating_anchor_direction_lock_v0.md` | Warns not to promote weak lines into operating anchors too early. |
| `docs/reports/plan_from_space_anchor_stack_gemini_compact_crosscheck_return_v0.md` | Crosscheck that the compact Anchor Stack is legible to Gemini and that boundary integrity/non-inspected evidence disclosure is the main watch item. |
| `docs/reports/plan_from_space_bounded_exploration_gemini_manual_return_v0.md` | Manually relayed Gemini bounded exploration result confirming lineage, judgment map seeds, and Anchor Stack setup advice. |
| `docs/specs/manual_external_tool_relay_bridge_note_v0.md` | Keeps user manual relay as temporary bridge rather than normalized operating design. |

## Main Axes

- model-default planning vs space-grounded planning
- small session split vs broad-but-bounded package
- hard stop vs continue with Issue Log
- output completion vs Return-to-Space recovery
- external runtime state vs VectorFL source of truth
- line as reading lens vs line as operating anchor

## Main Cameras

- user relay burden
- program continuity
- external tool plan mode
- space recovery
- drift / overclaim
- token budget and bounded exploration

## Main Lenses

- package sizing
- Plan Basis present / absent
- hard boundary / watch / continue
- Return-to-Space Value
- evidence pointer strength
- user decision required
- external log as raw trace

## Use When

Use this line before accepting a plan from Codex, Gemini, Hermes, OmX, or any external workflow when:

- the task asks for a package or session plan
- the tool proposes analysis / design / execution / verification / review splits by default
- the user would become a relay between tools
- the work can be broad-but-bounded if boundaries are clear
- closeout needs to become Movement Record rather than completion prose

## Plan Basis Minimum

A space-grounded plan must state:

- work type
- current line
- axis
- camera
- lens
- space assets consulted
- package sizing judgment
- stop / continue rule
- Return-to-Space requirement

If these fields are missing, treat the plan as model-default until proven otherwise.

## Return-to-Space Capture

Each use of this line should record:

- whether package sizing changed because of space records
- whether a small split was justified or rejected
- which boundary/watch distinction mattered
- whether user relay burden was reduced
- what future planning rule should be reused
