# Anchor Route Input Evidence Matrix v0

## Status

```yaml
status: route_evidence_matrix_candidate
date: 2026-05-06
baseline_lock: false
automation: false
registry: false
schema: false
scope: may6_input_to_anchor_route_grounding
```

## Purpose

Ground the anchor map route seed in the May 6 input materials and current space records.

This matrix is evidence support for route selection. It is not a completed map and not a line registry.

## Source Read Trace

Primary input set sampled:

- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/1.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/2.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/3.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/4.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/5.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/6.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/7.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/8.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/9.md`

Method:

- keyword and section sampling, not full semantic proof
- line-number evidence pointers retained
- current route rows checked against repeated input-material patterns

## Evidence Matrix

| route_id | evidence_pointers | evidence_signal | route_effect | maturity | watch |
| --- | --- | --- | --- | --- | --- |
| `ROUTE_EXTERNAL_TOOL_PLANNING` | `05-06/1.md:12`, `05-06/1.md:499`, `05-06/2.md:71`, `05-06/2.md:687`, `05-06/7.md:47`, `05-06/9.md:733` | planning must start from space records and Plan Basis before plan | keep route; keep `PV_PLAN_BASIS_GATE`, `PV_BROAD_BOUNDED_PACKAGE`, `PV_NON_INSPECTED_DISCLOSURE`, `PV_RETURN_TO_SPACE_CLOSEOUT` | evidence_backed_candidate | avoid turning it into universal planning law |
| `ROUTE_BOUNDED_GEMINI_REREAD` | `05-06/1.md:56`, `05-06/1.md:120`, `05-06/2.md:303`, `05-06/2.md:349`, `05-06/4.md:385`, `05-06/5.md:505` | space exploration is not broad search; it is purpose-bound activation route | keep route; bounded reread remains the Gemini deep-reading default | evidence_backed_candidate | Gemini must still state non-inspected scope |
| `ROUTE_MANUAL_WORKER_RETURN_INTAKE` | `05-06/1.md:219`, `05-06/1.md:255`, `05-06/2.md:235`, `05-06/7.md:225`, `05-06/9.md:687`, `05-06/9.md:831` | user relay and external logs/memory are risks unless packaged | keep route; manual relay is bridge-only and worker output is raw trace first | evidence_backed_candidate | manual relay must not become steady-state workflow |
| `ROUTE_AUTHORITY_DOWNSHIFT` | `05-06/1.md:6`, `05-06/1.md:327`, `05-06/2.md:497`, `05-06/9.md:939`, `05-06/9.md:985`, `05-06/9.md:1003` | candidate setup must not become baseline/authority; external runtime memory is not space memory | keep route; use when tool files overclaim authority, registry, baseline, or permanence | evidence_backed_candidate | downshift is correction, not deletion |
| `ROUTE_SESSION_REENTRY` | `05-06/4.md:15`, `05-06/4.md:78`, `05-06/4.md:201`, `05-06/5.md:396`, `05-06/7.md:115`, `05-06/9.md:673` | small anchors must be re-read during work, especially before splitting/closeout | keep route; compact anchor should be used during the work, not only at start | evidence_backed_candidate | avoid context replay becoming the re-entry method |
| `ROUTE_INPUT_CLASSIFICATION` | `05-06/7.md:39`, `05-06/7.md:51`, `05-06/7.md:76`, `05-06/9.md:771`, `05-06/9.md:793`, `05-06/9.md:787` | user input must be classified into line/axis/camera/lens before plan | add candidate route; this is distinct from external tool planning because it activates before the tool route is selected | new_candidate | may overlap with `ROUTE_SESSION_REENTRY`; Gemini should validate |

## Gate Evidence

| gate | input evidence | route/PV implication |
| --- | --- | --- |
| Pre-Plan Gate | `05-06/6.md:1`, `05-06/6.md:21`, `05-06/9.md:613`, `05-06/9.md:627` | `PV_PLAN_BASIS_GATE`; classify line before plan |
| Plan Sizing Gate | `05-06/6.md:37`, `05-06/6.md:55`, `05-06/7.md:251`, `05-06/9.md:643` | `PV_BROAD_BOUNDED_PACKAGE`; split only with blocking reason |
| Runtime Re-Entry Gate | `05-06/6.md:77`, `05-06/6.md:91`, `05-06/7.md:115`, `05-06/9.md:673` | `PV_CURRENT_POSITION_ENTRY`; reread anchor before split/final/relay |
| Closeout / Return-to-Space Gate | `05-06/6.md:107`, `05-06/7.md:130`, `05-06/9.md:703`, `05-06/9.md:715` | `PV_RETURN_TO_SPACE_CLOSEOUT`; closeout must become Movement Record |

## Route Decision

- Keep current five routes as candidate routes.
- Keep `ROUTE_INPUT_CLASSIFICATION` as `merge_watch`; Gemini flagged it as likely merge candidate with external planning or session re-entry.
- Add `ROUTE_SPACE_RESIDUE_SAMPLING` as a candidate route from Gemini validation; it needs bounded older-report sampling before stabilization.
- Use Set A external-tool planning trial as the next practical validation.

## Do Not Infer

- Do not infer full nine-doc semantic coverage from keyword sampling.
- Do not promote the evidence matrix into a baseline route map.
- Do not add more routes unless they change task behavior.
- Do not treat repeated words as maturity without decision-effect evidence.

## Return-to-Space Value

- Reusable finding: the nine input documents repeatedly support a 4-gate flow: Pre-Plan, Plan Sizing, Runtime Re-Entry, Closeout/Return-to-Space.
- Reusable finding: small anchors need an input classification route before external planning when the current line is not yet fixed.
- Reusable finding: Gemini crosscheck agrees that route/PV sets are coherent enough for Set A external-tool planning trial.
- Future reuse note: the next Gemini read should validate route overlap and identify active vs residue evidence.
