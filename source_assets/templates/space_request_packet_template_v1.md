# Space Request Packet Template v1

## Purpose

This template turns a short user request into an internal working packet.

The user does not need to fill this.
The system or operator fills it before the main reading/execution pass.

## 1. Packet Metadata

- `request_id`:
- `created_at`:
- `operator`:

## 2. Raw Request

- `raw_user_request`:
- `user_goal`:

## 3. Interpreted Request

- `interpreted_intent`:
- `request_type`:
- `target_object`:
- `desired_output`:

## 4. Route Decision

- `route_mode`:
  - `model-only`
  - `space-first`
  - `external-first`
  - `space-plus-external`
  - `answer-plus-reinjection`
- `why_this_route`:

## 5. Primary Space Scope

- `primary_folders`:
- `primary_docs`:
- `related_assets`:

## 6. External Scope

- `external_target_material`:
- `external_enrichment_needed`:
- `if_yes_what_to_check`:

## 7. Internal Working Questions

- `find_questions`:
- `structure_questions`:
- `connection_questions`:
- `enrichment_questions`:
- `output_questions`:
- `reinjection_questions`:

## 8. Required Extraction

- `relevant_lines`:
- `relevant_axes`:
- `relevant_boundaries`:
- `relevant_rules`:

## 9. Output Plan

- `intended_output_shape`:
- `delivery_surface`:
- `space_vs_model_vs_external_separation_needed`:

## 10. Reinjection Plan

- `reinjection_needed`:
- `asset_status`:
  - `none`
  - `reference`
  - `candidate`
  - `operating_asset`
- `storage_candidate`:

## 11. Stop Conditions / Risks

- `stop_conditions`:
- `risk_notes`:

## Minimal Example

```md
- request_id: req_omx_team_ralph_001
- created_at: 2026-04-23
- operator: codex
- raw_user_request: Read OMX team/ralph, map it to our space, enrich if needed, and propose an attachment structure.
- user_goal: usable structure proposal for our own space
- interpreted_intent: external structure adaptation into our own operating space
- request_type: adaptation + external_enrichment + reinjection_candidate
- target_object: OMX team/ralph workflow semantics
- desired_output: mapped attachment proposal
- route_mode: space-plus-external
- why_this_route: target lives in imported external material but must be adapted to our current space
```
