# Integrated Engine Current Front Support Inspector Field Map v0

## 1. Verdict

PASS_WITH_NOTE

This map captures current field placement across front / support / inspector. It diagnoses placement only; it does not redesign the UI.

## 2. Field Placement Map

| field / field group | current appearance | placement | placement diagnosis |
| --- | --- | --- | --- |
| package id | package panel small text, JSON artifact | support/front-light | appropriate as reference, not main content |
| handler label | package panel | front | appropriate; human-readable |
| handler id | package panel small text, JSON artifact | support | appropriate; should not become worker dashboard |
| purpose | User package projection | front / User center | appropriate |
| scope | User package projection, JSON artifact | front/support | included/excluded detail may be too much if fully surfaced |
| current target | all surface projections | front | useful but still technical/material-oriented |
| current stage | VectorFL/Engine package projection | front/support | appropriate |
| current status | package panel | front | appropriate |
| evidence summary | VectorFL package projection | front | appropriate, compact enough |
| validation status | Engine package projection | front/support | appropriate but technical |
| output summary | Engine package projection / return record | front/support | useful, but not yet translated into user meaning |
| return/redeposit summary | Engine package projection / return record | front/support | appropriate for authority boundary |
| next valid action | User package projection | front | appropriate but needs stronger reason chain |
| lifecycle | package panel cards | front/support | useful, may be visually heavy |
| selected lens | handler package detail / CliHost support | support | appropriate |
| lower-derived vs upper-added detail | support docs / bridge notes / package detail | support/hidden | likely too buried for diagnosing translation origin |
| bridge diagnostic | package support detail / docs | support | appropriate, but phrasing can remain technical |
| full bridge rules | not front, docs only | inspector/hold | appropriate |
| packet formation detail | CliHost support details | support | too dense; leaks verification-mode detail when opened |
| evidence bundle detail | CliHost support details / line inspector | support/inspector | appropriate but heavy |
| recent turns | CliHost support details | inspector/support | appropriate but can flood when expanded |
| latest return detail | CliHost support details / Engine panel | support/inspector | appropriate but lacks translation summary layer |
| mark history / route controls | CliHost support details | support/inspector | useful but technical |
| team/role configuration | User inspector | inspector | appropriate, but still full configuration panel |
| route/log history | User inspector | inspector | appropriate |
| legacy engine mock | Engine inspector | inspector | appropriate, but still heavy |
| asset/watch/trace support | Engine legacy mock | inspector | appropriate as x-ray, not front |

## 3. Too Exposed

Not badly exposed at front after slot restructuring, but still potentially too loud when expanded:

- packet formation detail
- mark controls
- lifecycle cards if the center becomes crowded
- technical route/authority labels

## 4. Too Buried

Potentially too buried for next design round:

- lower-derived vs upper-added field origin
- route reason
- why current status is `usable_with_hold`
- why the User next action follows from VectorFL/Engine result
- engine-produced meaning vs UI output summary

## 5. Verification-Mode Leakage

Leak points:

- packet formation detail
- latest return/mark controls
- line atlas
- legacy engine mock

These are mostly support/inspector now, but they still read like verification machinery when opened.

## 6. Missing From Front Where It Would Help

Possible missing front-level translated fields:

- plain meaning summary
- blocker in user-action language
- next-route reason
- “why this matters now”
- confidence/readiness phrase

This is diagnosis only, not an implementation proposal.

## 7. Validation

- Front/support/inspector placement captured: yes.
- Field-density problems visible: yes.
- Premature solutioning avoided: yes.

