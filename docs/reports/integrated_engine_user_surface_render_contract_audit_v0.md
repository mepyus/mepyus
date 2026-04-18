# Integrated Engine User Surface Render Contract Audit v0

Date: 2026-04-15

## 0. verdict

PASS

The user surface scaffold satisfies the current v1 candidate minimum render contract at scaffold level.

## 1. central panel question

Central panel:

- `operating_flow_panel`

What it asks / answers:

- Where is the request / return / reflux operating loop now?
- What route state or open decision should the user surface see next?

Evidence in scaffold:

- `USER_SURFACE_CENTRAL_PANEL = "operating_flow_panel"`
- `operating_flow_panel` has `isCentralPanel: true`
- visual copy says "Request / return / reflux movement"
- badges include `current slot`, `active packet`, `route state`, `open decision`
- flow strip shows `request -> vectorfl_review -> return -> decision_or_reflux`

## 2. v1 candidate alignment

Aligned points:

- User surface reads as operating / distribution / decision surface.
- `request_organization_panel`, `operating_flow_panel`, `anchor_support_panel`, and `return_decision_panel` match the v1 candidate representative panels.
- Read mapping matches the v1 candidate:
  - request organization -> request packet
  - operating flow -> current loop state
  - anchor support -> active anchor
  - return decision -> return packet
- Each panel shows read role, manifest path, and reason.
- Return decision copy keeps recheck, reprocess, and reflux open rather than treating return as final completion.

## 3. weak points

1. Render fields are still descriptive rather than enumerated as a formal `render_fields` list.
2. `operating_flow_panel` relies on visual copy and route strip rather than showing actual current-loop fields.
3. Support inspection is safe, but selected route/open-question detail is not yet contractually defined.

## 4. support-layer risk

Risk level:

- low

Reason:

- Support inspection is right-side, quiet, and explicitly says decision support stays secondary.
- Optional distribution support is mentioned as subordinate.
- It does not read as team/role ownership or approval authority.

## 5. visual token vs semantic role

Verdict:

- visual tokens do not hide semantic role.

Reason:

- `user-surface-*` semantic class prefix remains.
- User-specific operating language remains visible.
- Badge and card rhythm clarifies request / return / reflux rather than replacing it.

## 6. read-map change need

Read-map change needed?

- no

The weak points can be addressed later through wording-only or render-contract note refinement, not mapping changes.

## 7. audit sentence

The user scaffold is contract-stable enough for current baseline use, with thinness limited to formal render-field specificity.
