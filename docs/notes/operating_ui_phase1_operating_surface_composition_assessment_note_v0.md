# operating_ui_phase1 operating surface composition assessment note v0

## verdict

- `operating-ui-phase1` is partially aligned with `operating_surface_composition_rule_v0`
- the current UI already contains an observation readout panel for `multi_lens_document_reading_v0`
- the full reading path is not yet staged as
  `input readiness -> line status -> observation readout -> boundary/guard -> close-out/next branch`
- the next UI package should stay narrow and focus on operating-surface composition, not multi-lens internals

## scope of audit

- target UI:
  - `app/runtime/operating_ui_phase1.py`
- rule reference:
  - `docs/specs/operating_surface_composition_rule_v0.md`
- audited question:
  - how far the current `Operating` surface already matches the recommended panel order and reading path

## current panel map

Current `Operating` surface panels:

1. `Current Run`
2. `Selected Asset + State`
3. `Multi-Lens Observation`
4. `Recent Activity`
5. `Compare Hint`
6. `Path / Saved Path Hint`
7. `Search Hint`

Rule-side recommended order:

1. input readiness
2. line status
3. observation readout
4. boundary / interpretation guard
5. close-out / next branch

## current alignment

### already aligned

- `Multi-Lens Observation` is correctly placed as an observation-readout panel
- `surfaced_readout` is effectively the primary visible content
- `raw_output_reference` is kept secondary inside expandable details
- `line_states`, `parked_axes`, and `handoff_boundary` are visible together with the readout
- parked-axis visibility is preserved
- wording already contains guard language such as:
  - observation only
  - not a decision panel
  - not a maturity panel

### partially aligned

- `Current Run` and `Selected Asset + State` together act as a thin readiness/context block
- `Multi-Lens Observation` includes some line-status and boundary information, but they are embedded inside the same panel rather than staged as separate reading steps
- `Path / Saved Path Hint` contains readiness-like residue and path-state information, but it sits later in the flow and is mixed with other thin operating hints

## current gaps

### missing panels

- no explicit `input readiness` panel with a clear observation-ready question
- no explicit `line status` panel that stages active / parked / candidate before readout
- no explicit `boundary / interpretation guard` panel separated from the readout
- no explicit `close-out / next branch` panel at the end of the Operating surface

### overloaded panels

- `Multi-Lens Observation` currently carries:
  - surfaced observation
  - line status context
  - parked-axis visibility
  - handoff boundary
- this is acceptable for the current thin integration, but it overloads one panel with multiple rule layers

### misplaced information

- readiness-like information is split across:
  - `Current Run`
  - `Selected Asset + State`
  - `Path / Saved Path Hint`
- line-state information appears inside the observation panel instead of appearing before it
- boundary/guard wording is present inside subheads and meta rows, but not as its own interpretation-stop area
- no close-out / next branch information appears at the end of the Operating surface

## overclaim and drift risks

- if `Multi-Lens Observation` remains the only explicit structured panel, supervisors may read it too early without first framing readiness and line state
- because line-state and boundary are embedded inside the observation panel, the panel can gradually drift toward an all-in-one operating summary
- `Current Run`, `Recent Activity`, `Compare Hint`, and `Search Hint` can visually compete with the intended reading path
- the current UI still depends on the operator remembering the rule, rather than the panel order making the rule obvious

## reading path assessment

- the current reading path is understandable for a supervisor who already knows the implementation history
- it is not yet self-evident for a new supervisor/operator from the screen alone
- the strongest current path is:
  - current run
  - selected asset/state
  - multi-lens observation
- the weaker parts are:
  - readiness is not formally staged
  - line state is not separated before observation
  - close-out / next branch is absent from the Operating surface

## recommended next bounded UI package

- add a narrow `Input Readiness` panel near the top of `Operating`
- extract or stage a thin `Line Status` panel before `Multi-Lens Observation`
- add a thin `Boundary / Interpretation Guard` panel adjacent to or immediately after the observation panel
- add a final `Close-out / Next Branch` panel at the bottom of the Operating surface
- keep `Multi-Lens Observation` itself observational and explanation-first

## what should not be changed yet

- do not reopen `multi_lens` heuristics
- do not change active / parked semantics
- do not turn the observation panel into a decision or maturity panel
- do not do a broad Operating UI redesign
- do not pull close-out logic into runtime decision behavior

## current conclusion

- `operating-ui-phase1` already contains the right observation-panel nucleus
- it does not yet express the full operating-surface composition rule as a visible scenario chain
- the next bounded package should be a panel-order and panel-role package for the `Operating` surface
- `multi_lens` internals do not need to be reopened for that package
