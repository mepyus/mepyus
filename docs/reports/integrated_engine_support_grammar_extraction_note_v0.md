# Integrated Engine Support Grammar Extraction Note v0

## 1. Verdict

PASS_WITH_NOTE

This package preserves useful support grammar from older panels without preserving every old panel as front content.

## 2. What Support Grammar Means Here

Support grammar is the reusable way the screen says:

- this is secondary
- this helps the current judgment
- this is a warning or drift signal
- this is trace/event summary
- this can be inspected, but it is not the center

It is not the literal preservation of every old dashboard panel.

## 3. Preserved Grammar

### Compact status card grammar

Source pattern:

- asset health badges
- route/status pills
- current turn/status cards

Reused as:

- slot badges
- package status cards
- state / route / authority chips

### Warning / drift / next-action grammar

Source pattern:

- `AssetInspectorPanel` warning tabs
- amber/rose support cards
- authority boundary notes

Reused as:

- blocker/open edge summaries
- hold / usable / pending state
- what-not-to-infer badges

### Event / trace summary grammar

Source pattern:

- `EventConsolePanel`
- recent CLI turn cards
- mark history rows

Reused as:

- compact session event summary
- recent turn inspector
- route/log inspector

### Inspector trigger grammar

Source pattern:

- `details` support blocks
- selected asset / line inspection
- legacy engine mock as passive support

Reused as:

- explicit `inspector slot` wrappers
- line atlas x-ray
- team/route/log x-ray
- legacy engine mock x-ray

### Support boundary grammar

Source pattern:

- passive support labels
- not-runtime-truth notes
- candidate-only boundary text

Reused as:

- support slot descriptions
- inspector descriptions
- not-front / no-automation / no-promotion boundaries

## 4. What Was Not Preserved As Front Content

- full asset inventory
- full watcher stack
- full team routing
- full packet formation body
- full recent-turn history
- full bridge reasoning

These remain available only as support or inspector material.

## 5. Validation

- Grammar was preserved rather than old panels blindly promoted.
- Support logic is now reusable across all three surfaces.
- Old support blocks were not promoted into center slots.

