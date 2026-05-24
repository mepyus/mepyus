# VectorFL External Tool Decision Surface
# 2026-05-15 Candidate v0

## 1. Status

Verdict:
  USE_AS_PRIMARY_PRE_TOOL_JUDGMENT_SURFACE_WITH_WATCH

Position:
  external-tool candidate placement surface

Not:
  execution approval
  policy
  schema
  workflow
  ontology
  eval
  baseline

Source sequence:
  `1.md` through `10.md`

## 2. Core Definition

VectorFL does not compete with external tools. It sits before and after them as a judgment reservoir interface.

Before tool use, it asks:

- What is the actual enablement boundary?
- What is the current approval scope?
- Is this only reference material?
- Is a bounded test possible?
- Must it stay on HOLD?
- Is `USE_NOW` actually justified?

After tool use, it asks:

- What judgment was recovered?
- What remains WATCH?
- What remains HOLD?
- What should be compressed for re-entry?

## 3. Decision Branches

### REFERENCE_ONLY

Use when the material helps orientation but should not be executed, adopted, or wired into the space.

Allowed:
  reading, comparison, vocabulary check, context framing

Forbidden:
  command execution, credential use, automation, promotion

### BOUNDED_TEST_CANDIDATE

Use when a small, reversible test could clarify value or risk.

Allowed:
  explicit bounded test design, smallest non-destructive check, return packet requirement

Forbidden:
  treating the label as approval, expanding beyond the explicit boundary

### HOLD

Use when actual boundary, credential exposure, account mutation, write surface, or adoption pressure is too unclear.

Allowed:
  preserve as candidate material, extract watch item, ask for more boundary detail

Forbidden:
  silent execution, broad crawling, API calls, uploads, account actions

### USE_NOW

Use only when all of these are true:

- actual enablement boundary is known
- current approval scope explicitly covers the action
- smallest action is clear
- return format is defined
- rollback or stop condition is known
- no credential/API/account/write risk is hidden

If any condition is missing, downgrade to `BOUNDED_TEST_CANDIDATE` or `HOLD`.

## 4. Small Tool Boundary Drift Lens

Small-looking tools must be classified by actual enablement boundary, not by name, package size, or friendly wording.

Watch especially for:

- shell command
- host inspection
- file write
- credential access
- API call
- account mutation
- upload/download
- memory write
- scheduling
- audit/log surface
- broad repo or vault access

This is a lens, not a rule that all small tools are blocked.

## 5. One-page Operator Surface

Use this when a new external tool candidate appears:

```text
Candidate:
  [name / source / claim]

Intended use:
  [what the user wants from it]

Actual enablement boundary:
  [read / write / command / API / credential / account / network / memory / browser]

Current approval scope:
  [what is explicitly allowed now]

Decision:
  REFERENCE_ONLY | BOUNDED_TEST_CANDIDATE | HOLD | USE_NOW

Reason:
  [one short boundary-based reason]

Allowed now:
  [smallest allowed action]

Forbidden now:
  [specific actions not allowed]

Return requirement:
  [what must come back if used]

WATCH:
  [drift / promotion / hidden boundary]
```

## 6. HOLD

- Do not turn branch names into permanent categories.
- Do not turn examples into fixed rules.
- Do not create an eval file from seeds without a later explicit decision.
- Do not use this surface as an approval slip.

`STATUS: EXTERNAL_TOOL_DECISION_SURFACE_CANDIDATE_PREPARED_WITH_WATCH`
