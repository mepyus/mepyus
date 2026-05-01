# Reusable Operating Settings Catalog v0

Status: candidate reusable settings catalog
Authority: not baseline / not official workflow / not policy / not automation
Purpose: harvest useful operating settings from the Package 033 / Light-Full / 4-axis application loop

These are candidate reusable settings, not fixed templates.

Use them by copying the shape and changing details. Do not harden them into workflow, schema, policy, or automation.

## 1. Current Position Entry Setting

### When to Use

- session may be lost
- next session needs safe re-entry
- recent state must be recovered without overreading
- current work should not auto-continue

### Minimal Fields

- status / authority
- current position
- current anchors
- boundaries
- next safe position
- what must not be inferred

### Full Fields if Needed

- related closeout
- state by package / run
- source refs
- watch items
- mode guidance

### Recent Example

`app/work/space-skill-sandbox/outputs/current_position_entry_after_4_axis_loop_v0.md`

### What It Protects

- session-loss drift
- latest-run bias
- automatic next-task inference
- promotion from memory summary

### What It Must Not Become

- official session protocol
- baseline memory spine
- workflow controller
- mandatory ledger

### Detail Fields to Change Next Time

- package / run state
- latest closeout path
- active candidate references
- forbidden inference list
- next safe position

### Watch Items

- entry becoming too broad
- next step inferred from stale state
- candidate memory treated as authority

## 2. Light / Full Mode Setting

### When to Use

Use when deciding how heavy a handoff or observation should be.

### Minimal Fields

Light mode:

- identity
- context
- authority_status
- source_refs
- forbidden_actions
- next

Full mode:

- identity
- context
- memory_layer
- source_refs
- authority_status
- permission
- allowed_actions
- forbidden_actions
- routing
- validation
- risk
- next

### Full Fields if Needed

Add:

- watch items
- what must not be inferred
- approval gate
- invalidation condition

### Recent Example

`app/work/space-skill-sandbox/outputs/handoff_checklist_light_vs_full_mode_note_v0.md`

### What It Protects

- over-ceremony for low-risk work
- under-specified authority-sensitive work
- Light mode used where Full mode is needed

### What It Must Not Become

- default routing rule
- official workflow
- schema
- enforcement mechanism

### Detail Fields to Change Next Time

- risk level
- source refs
- authority status
- approval condition
- whether task crosses memory / package / provenance boundaries

### Watch Items

- Full mode heaviness
- Light mode under-protecting authority-sensitive work
- mode choice becoming policy

## 3. Target Selection Preflight Setting

### When to Use

- choosing one safe artifact before reread
- avoiding premature analysis
- comparing candidate targets by metadata only

### Minimal Fields

- candidate_path
- artifact type
- why low-risk
- why it fits the lens
- what it may reveal
- known risks
- confidence: low / medium
- final recommendation

### Full Fields if Needed

- avoid list
- hard boundaries
- target type criteria
- verdict

### Recent Example

Provenance-Integrity / Harness-Orientation target selection preflights that selected:

- `operating_order_source_map_v0.md`
- `current_position_handoff_package_033_candidate_evidence_v0.md`

### What It Protects

- artifact analysis before target approval
- broad corpus scanning
- unstable package movement
- implementation drift

### What It Must Not Become

- automatic router
- ranking system
- source registry
- approval bypass

### Detail Fields to Change Next Time

- axis / lens
- candidate list
- avoid list
- low-risk criteria
- final recommended target

### Watch Items

- metadata selection becoming hidden analysis
- confidence overstatement
- final recommendation treated as approval

## 4. Bounded Reread Setting

### When to Use

- applying one lens or axis to one internal artifact
- checking whether a candidate example fits without modifying it

### Minimal Fields

- target reviewed
- lens / axis used
- verdict
- what it shows well
- current authority
- what must not be inferred
- smallest safe next step

### Full Fields if Needed

- what risks it prevents
- remaining watch items
- why it fits
- what needs downgrading

### Recent Examples

- `run_160_affordance_program_trial_v0_reread_codex_review.md`
- `run_162_signal_memory_run_identity_correction_reread_codex_review.md`
- `run_164_provenance_integrity_source_map_reread_codex_review.md`
- `run_166_harness_orientation_current_position_handoff_reread_codex_review.md`

### What It Protects

- reread becoming rewrite
- example becoming baseline
- lens becoming policy
- artifact becoming implementation target

### What It Must Not Become

- content revision
- promotion review
- official validation
- implementation plan

### Detail Fields to Change Next Time

- target path
- lens / axis
- verdict options
- watch items
- next safe action

### Watch Items

- verdict overread as acceptance
- historical examples treated as current models
- risk labels treated as confirmed facts

## 5. Line-Axis Reference Note Setting

### When to Use

- a reread result should support line-axis synthesis
- the main synthesis report should not be edited
- an axis needs a small candidate support note

### Minimal Fields

- status
- source refs
- what was observed
- what this adds to line-axis synthesis
- what must not be inferred
- watch items
- next safe action

### Full Fields if Needed

- axis state
- completion note
- related run record

### Recent Examples

- `affordance_program_reread_to_line_axis_reference_v0.md`
- `signal_memory_reread_to_line_axis_reference_v0.md`
- `provenance_integrity_reread_to_line_axis_reference_v0.md`
- `harness_orientation_reread_to_line_axis_reference_v0.md`

### What It Protects

- synthesis report churn
- axis support being lost in chat
- reread result becoming hidden context

### What It Must Not Become

- line-axis revision
- final axis definition
- ontology link
- architecture map

### Detail Fields to Change Next Time

- axis name
- source refs
- observed pattern
- support value
- watch items

### Watch Items

- reference note becoming authority
- too many notes replacing synthesis
- axis support overread as proof

## 6. Candidate Closeout Setting

### When to Use

- a bounded loop can be closed but not promoted
- a sequence has enough candidate material for future review
- watch items remain active

### Minimal Fields

- loop status
- files / records reviewed
- what this supports
- what must not be inferred
- remaining watch items
- closeout status
- next safe position

### Full Fields if Needed

- axis-by-axis summary
- evidence bundle summary
- authority boundary
- no-auto-next statement

### Recent Example

`app/work/space-skill-sandbox/runs/run_168_four_axis_application_reference_loop_closeout_review.md`

### What It Protects

- repeated micro-work after loop is sufficient
- candidate close becoming promotion
- next task inferred automatically

### What It Must Not Become

- acceptance gate
- baseline closeout
- architecture declaration
- workflow launch

### Detail Fields to Change Next Time

- loop name
- reviewed records
- support claim
- watch items
- next safe position

### Watch Items

- closeout language becoming finality
- watch items being forgotten
- future worker treating closeout as approval

## 7. Non-Inference Boundary Setting

### When to Use

Use in nearly every candidate artifact.

### Minimal Fields

- no baseline
- no official workflow
- no source-space policy
- no automation
- no schema
- no graph / ontology
- no controller / router
- no package movement
- no Run 117 inference
- no Gemini execution unless routed / approved

### Full Fields if Needed

- no source registry / citation baseline
- no tool adoption / CLI approval
- no package promotion
- no engine simulation
- no universal rule
- no architecture

### Recent Examples

Used across:

- current-position entries
- reread records
- line-axis reference notes
- Run 168 closeout

### What It Protects

- over-promotion
- automatic continuation
- authority drift
- implementation drift

### What It Must Not Become

- permanent ban list
- policy
- schema
- enforcement system

### Detail Fields to Change Next Time

- package numbers
- run ids
- forbidden inferred next step
- specific promotion risks

### Watch Items

- boundary lists becoming boilerplate noise
- missing a task-specific forbidden inference
- treating forbidden actions as permanent law

## 8. Immediately Reusable Settings

The most immediately reusable settings are:

- Current Position Entry Setting
- Target Selection Preflight Setting
- Bounded Reread Setting
- Line-Axis Reference Note Setting
- Non-Inference Boundary Setting

Light / Full Mode is reusable as a decision aid.

Candidate Closeout is reusable only when a loop is actually ready to close.

## 9. Settings That Need Watch

- Light / Full Mode: avoid turning mode choice into default rule.
- Bounded Reread: avoid verdicts sounding like baseline acceptance.
- Line-Axis Reference Note: avoid multiplying notes without synthesis.
- Candidate Closeout: avoid closeout becoming promotion.
- Non-Inference Boundary: avoid boilerplate that stops being read.

## 10. What Must Not Be Inferred

- no baseline
- no official workflow
- no source-space policy
- no schema / graph / ontology
- no automation / router / controller
- no package movement
- no Run 117 inference
- no Gemini execution unless routed / approved
- no fixed template
- no architecture

## 11. Next Safe Action

Use this catalog as candidate memory for future Codex/User planning.

When a similar task appears, copy the relevant setting shape and change details.

Do not treat this catalog as official workflow or automation pattern.
