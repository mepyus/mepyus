# line thickening runtime insertion v0

## 1. purpose

This spec defines the minimum runtime insertion for line thickening.

The goal is not to build a new inference system.
The goal is to make rereading itself accumulate line-centered evidence so that thin -> medium -> thick judgments can emerge from append-only observations.

## 2. scope

This insertion adds three thin surfaces:

1. `line_registry`
   - current line state summary
2. `reread_observation_log`
   - append-only observation packets
3. `promotion_rule`
   - conservative thickness evaluator

## 3. non-goals

- no graph expansion
- no ontology lift
- no full automation pipeline
- no large UI work
- no hard promotion of every observed line

## 4. data surfaces

### 4.1 line registry

Recommended surface:

- `runtime/manifests/line_registry.json`

Role:

- current-state summary for line candidates
- derived from observations
- not the truth archive

Required fields:

- `line_id`
- `line_name`
- `status` in `candidate / probing / stable / operating`
- `thickness_level` in `thin / medium / thick`
- `first_seen_at`
- `last_seen_at`
- `support_count`
- `resistance_count`
- `surface_types_seen`
- `notes`

### 4.2 reread observation log

Recommended surface:

- `runtime/logs/reread_observation_log.jsonl`

Role:

- append-only packet for one reread run
- line-centered evidence with support, weakness, resistance, and next probe
- duplicate suppression allowed only for exact repeats

Required fields:

- `run_id`
- `asset_or_surface`
- `view_type`
- `line_name`
- `evidence`
- `grounding_type` in `direct / fallback / inferred`
- `support_points`
- `weakness_points`
- `resistance_or_counterexample`
- `next_probe_surface`
- `thickness_before`
- `thickness_after`

### 4.3 promotion rule

Role:

- thin / medium / thick / operating conservative evaluation
- do not auto-promote aggressively
- require repeated surface/view evidence and direct grounding before stronger statuses

Minimum criteria:

- repeated appearance across distinct surface/view pairs
- direct grounding exists
- support and resistance are both represented
- line can be used as a temporary compare/probe line

## 5. behavior rules

### 5.1 support and resistance are symmetric in the record

Support alone is not enough.
Resistance and counterexample evidence must be retained with equal visibility.

### 5.2 do not inflate line names

Do not create many line names just to look richer.
The registry should stay sparse and grounded.

### 5.3 avoid premature promotion

The first implementation must stay conservative.
If a line is still weak, keep it thin or probing.

### 5.4 append-only first

Observation logs are append-only.
Registry is a summary projection and may be updated from the log, but it must remain derived from observations.

## 6. minimal runtime contract

The runtime helper should support:

1. append one reread observation packet
2. upsert one registry row
3. evaluate promotion conservatively
4. write a small promotion record

## 7. one-line lock

> line thickening runtime insertion is the minimum append-only observation and registry layer that lets rereading itself accumulate evidence for thin -> medium -> thick judgments without hardening lines too early.
