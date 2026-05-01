# Pairing Reingress Learning Fields v0

## Purpose

Reingress must record not only what differed, but why the compared artifacts were paired. This makes future comparison questions less dependent on accidental selected order.

## Fields

- `useful_pairing_modes`: pairing bases that worked in the run.
- `family_key_summary`: family keys that looked reusable.
- `weak_pair_areas`: comparisons where confidence remained weak.
- `rejected_pair_summary`: plausible candidates not selected.
- `next_pairing_probe_hint`: next question or path probe that would improve pairing.
- `reusable_family_groups`: family groups worth reusing.
- `pairing_risk_summary`: risk note from merge/diff/hold.

## Interpretation

Comparison learning is incomplete if it only records the delta. The next run needs to know whether the pair itself was reliable.

Weak pair areas are not failures. They are reusable warnings that prevent future overconfident generated/runtime comparisons.

## Validation

- Pairing basis and family key must be visible in reingress.
- Weak-pair risks must survive the final record.
- No final family taxonomy lock is implied.
