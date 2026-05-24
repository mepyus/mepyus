# Anchor Stack Recognition Probe v0

## Status

```yaml
status: probe_candidate
date: 2026-05-06
baseline_lock: false
automation: false
schema: false
registry: false
package_id: PKG_20260506_ANCHOR_STACK_OPERATIONAL_VALIDATION_V0
```

## Purpose

Define the minimum test for whether a returned Anchor Stack package becomes discoverable again by later space exploration or re-entry.

This is a local recognition probe, not automation.

## Probe Query Markers

Use `rg` or equivalent local search for:

```text
PKG_20260506_ANCHOR_STACK_OPERATIONAL_VALIDATION_V0
anchor_stack_operational_validation
session_execution_list_trial
PV_BROAD_BOUNDED_PACKAGE
PV_RETURN_TO_SPACE_CLOSEOUT
recognition_probe
```

## Pass Criteria

Pass if search returns:

- package basis
- package spec
- execution-list trial report
- Movement Record reference
- manifest/current-position pointer if promoted as current work

## Fail / Watch Criteria

Watch if:

- only the manifest can find the package
- package result is discoverable but has no route/PV fields
- package result is discoverable but not connected to Movement Record

Fail if:

- the package cannot be found by its package id or route/PV markers
- the returned result exists only as raw worker trace
- future re-entry requires the user to remember and relay the package manually

## Manual Probe Command

```bash
rg -n "PKG_20260506_ANCHOR_STACK_OPERATIONAL_VALIDATION_V0|anchor_stack_operational_validation|session_execution_list_trial|PV_BROAD_BOUNDED_PACKAGE|PV_RETURN_TO_SPACE_CLOSEOUT|recognition_probe" app/work docs
```

