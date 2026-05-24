# Supervisor Checkpoint Template
# Candidate v0

cycle_id:
  ...

checkpoint status:
  NOT_STARTED / SUPERVISOR_REVIEW_NEEDED / CYCLE_PLACED_WITH_WATCH / CYCLE_HOLD / CYCLE_CLOSED

target:
  ChatGPT / Supervisor

authority:
  placement and gate review only

not:
  baseline
  current-position
  workflow
  registry
  automation
  execution trigger

## 1. Gemini Return Status

Gemini return:
  not started / returned / missing / hold

Summary:
  ...

## 2. Codex Request Status

Codex request queue:
  empty / ready / processed / hold

Summary:
  ...

## 3. Codex Return Status

Codex return:
  not started / returned / missing / hold

Summary:
  ...

## 4. Usable Judgment

Usable judgment:
  - ...

## 5. WATCH

- ...

## 6. HOLD

- ...

## 7. Placement

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

Reason:
  ...

## 8. User Decision Needed

User decision needed:
  YES / NO

Decision:
  ...

## 9. Approval Scope

user_instruction_raw:
  ...

interpreted_approval_scope:
  ...

not_approved_items:
  ...

stop_condition:
  ...

approval_recorded_by:
  ChatGPT / Supervisor / Codex / Gemini / User

approval_scope_watch:
  compressed approval must not become blanket approval

## 10. Next Cycle Recommendation

Next cycle:
  ...

Manual gate:
  ...

Do not promote:
  - cycle checkpoint != current-position
  - placement != baseline
  - next cycle != automatic task
