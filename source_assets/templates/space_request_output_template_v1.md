# Space Request Output Template v1

## Purpose

This template fixes the output surface for a routed request.

The answer should remain user-facing first, but it must still preserve:

- what was read from the space
- what came from model reasoning
- what came from external reinforcement

## 1. User Request Restatement

- `user_request_summary`:

## 2. Request Interpretation

- `how_the_request_was_interpreted`:
- `route_mode_used`:

## 3. Core Space Assets Used

- `space_assets_used`:
- `why_these_assets_mattered`:

## 4. Structural Reading Result

- `structure_read_result`:

## 5. Space Mapping Judgment

- `how_this_maps_to_our_space`:

## 6. External Reinforcement Judgment

- `external_reinforcement_used`:
- `if_yes_what_it_changed_or_confirmed`:

## 7. Final Usable Output

- `usable_output`:

## 8. Operating Close

- `current_position`:
- `what_can_be_used_now`:
- `what_should_not_be_used_yet`:

## 9. Immediate Next Use

- `immediate_next_use`:

## 10. Later Maturation

- `what_should_mature_later`:

## 11. Uncertainty / Needs Confirmation

- `uncertainty_or_confirmation_needed`:

## Surface Rule

Order the answer like this:

1. user-language summary
2. structural judgment
3. usable output
4. uncertainty if needed

## Minimal Example

```md
### User Request Restatement
- You asked for a way to read OMX team/ralph and attach it to our space.

### Request Interpretation
- I treated this as external structure adaptation into our current space, with bounded external reinforcement.

### Core Space Assets Used
- lower-to-upper bridge notes
- current operating index

### Structural Reading Result
- OMX team and ralph appear to be moving toward clearer separation rather than hard linked lifecycle.

### Space Mapping Judgment
- In our space, the coordinated execution layer and the persistence/verification layer should remain distinct.

### Final Usable Output
- Use team-like behavior as coordinated execution.
- Keep ralph-like behavior as separate follow-up persistence/verification.

### Operating Close
- Current position: bounded adaptation note, not a runtime import.
- What can be used now: role separation and follow-up boundary.
- What should not be used yet: linked lifecycle adoption.

### Uncertainty / Needs Confirmation
- Check whether the latest external docs still treat team/ralph separation as active direction.
```
