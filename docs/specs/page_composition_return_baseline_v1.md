# page composition return baseline v1

## verdict

return the upper baseline to page composition and lock current pages as core, companion, and parked

## purpose

This document restores the top-level reading frame to page composition.

The main question is no longer:

- what phase comes next

The main question is:

- what pages exist now
- which are core pages
- which are companion/support pages
- which are still candidate pages only

## 1. current page set

### core pages

#### operating

- role
  - thin current-state observation page
- route
  - inside `/operating-ui-phase1`
- meaning
  - reads current state only

#### explore

- role
  - path-centered page for placing an object into an interpretation position
- route
  - inside `/operating-ui-phase1`
- meaning
  - object -> lens -> position -> preview -> explicit save

#### search

- role
  - direct access page
- route
  - inside `/operating-ui-phase1`
- meaning
  - finds object / lens / position / saved path / seed-related item without forcing exploration flow

#### memory / saved path

- role
  - explicit saved-path page
- route
  - inside `/operating-ui-phase1`
- meaning
  - handles explicit saved paths only

#### similar / local re-query

- role
  - seed-based local re-query page
- route
  - inside `/operating-ui-phase1`
- meaning
  - rereads nearby structure from one activated seed

### companion / support pages

#### history / reread / trace

- role
  - time-axis reading companion page
- route
  - `/operating-ui-history`
- meaning
  - rereads prior checkpoints, grouped activity slices, translated trace units, and prior-state references

This is a companion page, not a new upper operating center.

### parked candidate pages

#### saved-path curation

- role
  - possible later page for lightly rereading and curating explicit saved paths
- current status
  - parked
  - no active route
  - not part of the current operating set

## 2. core vs companion vs parked

### core

Core pages are the pages needed for the current operating set:

- observe now
- author one interpretation path
- directly access a target
- hold explicit saved paths
- reread local similar structure

### companion

Companion pages help reread or support the operating set without replacing it:

- history / reread / trace

### parked

Parked candidate pages are not active pages yet:

- saved-path curation

## 3. page movement meaning

### inside core pages

- movement means switching among current operating jobs
- example:
  - observe now
  - author a path
  - search directly
  - inspect a saved path
  - activate a seed for local re-query

### core -> companion

- movement means leaving current-state work temporarily to read time-axis context
- this is explicit only

### companion -> core

- movement means returning to the main operating set with contextual historical reference only
- this is explicit only
- this is not restore, load, rerun, or overwrite

### any movement to parked candidate

- not allowed now
- parked candidate remains candidate only

## 4. mandatory boundary reminders

- `Operating`
  - thin current-state observation page
- `Explore`
  - path-centered page for placing an object into an interpretation position
- `Search`
  - direct access page
- `Memory`
  - explicit saved path page only
- `Similar`
  - seed-based local re-query page
- `History`
  - companion page for time-axis reading only

History may remain part of the current operating set as a companion page, but it must not turn the upper interpretation frame into phase progression.

## 5. explicit-only and forbidden moves

### explicit-only

- `Search -> Explore`
- `Search -> Memory`
- `Search -> Similar`
- `Memory -> Similar`
- `core -> companion`
- `companion -> core`

### forbidden

- hidden mutation across page boundaries
- history companion behaving as restore/load/rerun
- history companion behaving as command center
- parked saved-path curation behaving as if it were active

## 6. candidate reminder

The only current parked candidate page in this composition map is:

- `Saved-Path Curation`

It stays candidate-only until separately reopened.

## 7. immediate next action

main operating set entry/navigation labeling 정리

This is the most direct next task after returning to page composition because it makes the page map visible at entry level without reopening phase or roadmap framing.
