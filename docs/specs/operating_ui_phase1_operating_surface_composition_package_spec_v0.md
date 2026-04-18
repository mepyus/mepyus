# operating_ui_phase1_operating_surface_composition_package_spec v0

## verdict

- the next bounded UI package for `operating-ui-phase1` is a composition package, not an engine package
- the package should make the operating-surface reading path explicit at panel level
- the package must stay thin and use existing runtime/artifact fields first

## package scope

This package adds thin panels for:

- `Input Readiness`
- `Line Status`
- `Boundary / Guard`
- `Close-out / Next Branch`

This package does not redesign the whole UI.

## package goal

The goal is to make the intended scenario-chain readable from the `Operating` surface itself:

`readiness -> line status -> observation -> boundary -> close-out`

This package exists to reduce panel overload and make the supervisor/operator reading path visible without reopening `multi_lens` internals.

## relation to current panels

Current retained panel:

- `Multi-Lens Observation`

Rule for the existing observation panel:

- keep it explanation-first
- keep `surfaced_readout` primary
- keep `raw_output_reference` secondary
- do not turn it into a decision, maturity, or promotion panel

Adjustment intent:

- line-state meaning should no longer live only inside the observation panel
- boundary/guard meaning should no longer live only inside panel subheads and meta text
- the observation panel remains the observation panel, not the whole operating-surface logic

## panel definitions

### 1. Input Readiness panel

Purpose:

- show whether the current material is ready to be read as an observation pass

Minimum fields:

- `source`
- `selected_asset_id`
- `live_availability`
- `selection_query_state`
- split/linked availability if already available from current runtime payload
- `provenance_summary`
- observation-ready summary

Question:

- is the current material ready for observation?

If some fields are unavailable:

- show explicit placeholder or empty-state wording
- do not add new engine behavior just to fill the panel

### 2. Line Status panel

Purpose:

- show the operating state of lines before the readout is interpreted

Minimum fields:

- active lines
- parked lines
- candidate lines if already available
- current non-goal summary if already available
- reopen gate summary if already available

At current v0 minimum:

- use `line_states`
- use `parked_axes`
- if candidate/current non-goal/reopen gate are unavailable, show explicit thin placeholder wording

Question:

- what kind of line produced this readout?

### 3. Boundary / Guard panel

Purpose:

- make the interpretation stop-line explicit near the observation panel

Minimum fields:

- observation only
- not a decision surface
- not a maturity surface
- no promotion signal
- no reopen trigger from display alone
- `handoff_boundary`

Question:

- where must reading stop?

If boundary detail is sparse:

- keep the guard wording and show current handoff metadata only

### 4. Close-out / Next Branch panel

Purpose:

- show whether the current scope is complete and what bounded next move exists

Minimum fields:

- current scope complete status if available
- what changed summary if available
- what did not change summary if available
- prohibition summary
- next branch options if available

If these fields are not currently available in runtime payload:

- use explicit placeholder wording such as:
  - close-out summary not attached in current payload
  - next branch remains document/supervisor-side

Question:

- should this branch close here, or is a bounded next package already defined?

## data source rule

### primary rule

- use existing runtime/artifact fields first

### secondary rule

- if a required panel field is missing from current runtime payload, use placeholder or empty-state wording

### forbidden shortcut

- do not invent new engine behavior, hidden runtime logic, or speculative payload generation just to populate the panel

## layout and reading-order intent

The intended `Operating` surface reading order is:

1. `Input Readiness`
2. `Line Status`
3. `Multi-Lens Observation`
4. `Boundary / Guard`
5. `Close-out / Next Branch`

Interpretation rule:

- the operator/supervisor should not need to infer this sequence from implementation history
- the panel order itself should teach the sequence

## implementation guardrails

- keep `Multi-Lens Observation` explanation-first
- keep raw/reference secondary
- keep parked-axis visibility explicit
- keep handoff boundary visible
- runtime still stops before operating decision

## non-goals

- no heuristic/runtime change
- no decision behavior
- no maturity behavior
- no promotion behavior
- no broad UI redesign
- no speculative new engine features
- no reopening of `multi_lens` internals

## current conclusion

- the next UI package should be a thin composition package for the `Operating` surface
- the package is successful when the reading path becomes explicit at panel level without changing runtime behavior
- missing data should remain visibly thin rather than being filled by new engine logic
