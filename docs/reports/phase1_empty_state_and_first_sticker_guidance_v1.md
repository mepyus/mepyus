# phase1 empty-state and first-sticker guidance v1

## package status

complete for this turn

## files changed

- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [phase1_empty_state_and_first_sticker_guidance_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_empty_state_and_first_sticker_guidance_v1.md)

## 1. surface empty-state changes

Each phase1 surface now explains a different kind of emptiness instead of collapsing everything into a generic blank state.

- Operating: shows `phase1 has no stickers yet` as a thin status note and keeps the surface observational.
- Explore: shows a first-path hint, current path summary, preview readiness state, and a disabled save affordance when the path is incomplete.
- Search: distinguishes idle search from no results. Empty query is treated as normal direct-access waiting state.
- Memory: explains that there is no saved interpretation path yet and that click traces do not appear here.
- Similar: distinguishes `no saved seed yet` from `seed active but local result is still thin`.

## 2. first-sticker guidance placement

Guidance was kept thin and structural rather than tutorial-heavy.

It now appears in:

- Explore preview area:
  - `current path=object -> lens -> position`
  - `preview ready` or `preview incomplete`
  - `save disabled reason=...`
- Explore boundary note:
  - `choose object -> choose lens -> choose position -> inspect preview -> save explicit sticker -> open Memory or Similar`
- Search idle note:
  - clarifies that direct access starts when the user asks for something

No onboarding modal, wizard, or fake sample data was added.

## 3. how state-aware affordances are separated

The UI now separates these cases more explicitly:

- `save disabled reason`
  - shown in Explore when object/lens/position/preview is still incomplete
- `no sticker`
  - shown in Memory when no explicit path has been saved yet
- `no seed`
  - shown in Similar when local re-query cannot start because no sticker seed exists
- `no query`
  - shown in Search when direct access has not been asked for yet
- `result weak`
  - shown in Similar when seed exists but current results are still low-confidence and thin

This keeps `empty`, `not started`, `condition unmet`, and `weak derivation` from collapsing into one message.

## 4. still normal to be empty

Some empty states remain healthy and expected:

- Search can stay idle with no query.
- Memory can remain empty until the user explicitly saves a path.
- Similar can remain empty until a sticker becomes an active seed.
- Similar can also return only thin matches even after activation; that is shown honestly rather than inflated.

## 5. weak or intentionally limited parts

- Explore guidance is still minimal and inline. It does not attempt full walkthrough behavior.
- Similar derivation itself was not strengthened in this turn.
- Operating remains thin and does not become an onboarding panel.

## 6. next candidates

- make the Explore current-path strip slightly more prominent without turning it into a wizard
- add one lighter transition cue when the first saved sticker makes Memory and Similar become active
