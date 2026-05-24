# QMD Carrier Candidate Operating Setting Compact v0

## Status

```yaml
status: candidate_operating_setting
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
current_position_update: false
```

## Setting

Use QMD as a bounded evidence access carrier only when the active material family is known and the selected active surfaces can stay within 3-7 files.

## Pattern

```text
1. Codex selects material family and active surfaces.
2. Gemini / external carrier performs broad-but-bounded internal execution.
3. QMD search --json discovers candidate pointers.
4. Exact qmd URI list feeds QMD multi-get --json.
5. Gemini / external carrier returns one packaged synthesis.
6. Codex downshifts claims and extracts Return-to-Space Value.
7. Codex writes one package-level Movement Record if reusable judgment exists.
```

## Stop

```text
full corpus indexing
embed/query/rerank as default
MCP startup
parser/schema/automation
registry/baseline/current-position update
tool output authority
micro-run proliferation
```

## Required Return

```text
PLAN_BASIS
EXECUTION_SYNTHESIS
CANDIDATE_OPERATING_SETTING
WATCH_AND_HOLD_ITEMS
RETURN_TO_SPACE_VALUE
MOVEMENT_RECORD_CANDIDATE
DO_NOT_PROMOTE
NEXT_USE
```

## Watch

```text
QMD score is metadata.
QMD body bundle is not memory.
QMD is not anchor authority.
Gemini output is raw/candidate material.
Codex is broker/recovery editor, not final user judgment.
```

`STATUS: QMD_CARRIER_CANDIDATE_OPERATING_SETTING_COMPACT_PREPARED`
