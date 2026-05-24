# Maturation Queue Item Generator Examples
# Codex / Gemini / User Correction

## 1. Status

Status:
  MATERIALIZED_FROM_SOURCE_16_WITH_WATCH

Source:
  `16.md`

Purpose:
  Materialize Queue Item Generator dry-run examples for three input lanes.

Not:
  final placement
  baseline
  memory write
  eval file
  automation

## 2. Generator Minimal Fields

source:
  source_type
  origin_lane
  source_ref

what_came_in:
  raw_material_summary
  execution_or_change_claimed
  boundary_flags

what_can_be_recovered:
  recovered_judgment_candidate
  usable_candidate
  WATCH
  HOLD
  do_not_repeat

maturation_signal:
  repeat_signal
  conflict_signal
  promotion_risk
  compression_needed
  packet_potential

placement:
  placement_candidate
  review_required
  next_action_candidate

## 3. Example A - Codex Result

source_type:
  Codex result

origin_lane:
  Codex

raw_material_summary:
  Repo-side inspection, patch, or run result returned from Codex.

execution_or_change_claimed:
  yes / unclear depending on commands or files changed

boundary_flags:
  command_execution: possible / yes
  file_write: possible / yes
  credentials: unclear / no
  api_network: unclear / no
  account: no
  memory_indexing: no
  automation: no
  baseline_promotion: possible

recovered_judgment_candidate:
  Codex can perform bounded repo-side execution, but its result must be recovered as judgment before becoming space value.

usable_candidate:
  patch summary, files inspected, files modified, run evidence, direct answer, do-not-repeat lesson

WATCH:
  - Codex result -> final truth
  - patch success -> placement approval
  - file modification -> structural promotion
  - run record -> baseline
  - repo affordance -> task authority

HOLD:
  - baseline promotion
  - current-position update
  - output_manifest update
  - AGENTS.md / SKILL.md / eval creation
  - broad repo refactor

do_not_repeat:
  Do not treat "it worked" as "this is the right direction."

maturation_signal:
  repeat_signal: medium
  conflict_signal: possible
  promotion_risk: medium / high if files changed
  compression_needed: yes
  packet_potential: yes

placement_candidate:
  PACKET_FRAGMENT_CANDIDATE or COMPRESS_ONLY or REOPEN_CANDIDATE

next_action_candidate:
  recover the mechanical result separately from the judgment before any promotion

## 4. Example B - Gemini Analysis

source_type:
  Gemini result

origin_lane:
  Gemini

raw_material_summary:
  Broad reading, synthesis, comparison, or interpretation result returned from Gemini.

execution_or_change_claimed:
  no / unclear

boundary_flags:
  command_execution: no
  file_write: no
  credentials: no
  api_network: no / already occurred outside space
  account: no
  memory_indexing: no
  automation: no
  baseline_promotion: possible

recovered_judgment_candidate:
  Gemini can provide broad semantic reading, but synthesis must remain observation until recovered by VectorFL judgment.

usable_candidate:
  summary, comparison, meaning clusters, weak signals, lens candidates, external reference interpretation

WATCH:
  - synthesis -> final judgment
  - broad reading -> authority
  - comparison -> adoption pressure
  - fluent summary -> truth
  - recommendation -> execution direction
  - external material -> VectorFL rule

HOLD:
  - direct adoption of Gemini recommendation
  - turning summary into policy
  - creating new structure from one reading
  - promoting weak signal to operating rule

do_not_repeat:
  Do not convert fluent synthesis into recovered judgment without comparison.

maturation_signal:
  repeat_signal: weak / medium
  conflict_signal: possible
  promotion_risk: medium
  compression_needed: yes
  packet_potential: yes

placement_candidate:
  KEEP_AS_REFERENCE or WATCH_PATTERN_CANDIDATE or SURFACE_UPDATE_CANDIDATE

next_action_candidate:
  use as reference insight unless repetition or conflict justifies a lens candidate

## 5. Example C - User Correction

source_type:
  user correction

origin_lane:
  user

raw_material_summary:
  User corrected the interpretation of the task direction.

execution_or_change_claimed:
  no

boundary_flags:
  command_execution: no
  file_write: no
  credentials: no
  api_network: no
  account: no
  memory_indexing: no
  automation: conceptually yes
  baseline_promotion: possible

recovered_judgment_candidate:
  User correction should redirect the active reading lens and task frame, but should not automatically become a permanent rule without repeated confirmation.

usable_candidate:
  corrected focus, task boundary, priority clarification, lens shift, do-not-repeat lesson

WATCH:
  - assistant narrowing task incorrectly
  - execution automation mistaken for maturation automation
  - tool gate focus overriding space-use focus
  - user correction becoming overgeneralized rule
  - one correction becoming permanent baseline

HOLD:
  - continuing with wrong frame
  - turning correction into broad policy
  - rewriting all prior surfaces from one correction
  - automatic memory/baseline update without need

do_not_repeat:
  Do not downgrade user correction into a summary note; apply it to the active frame.

maturation_signal:
  repeat_signal: medium / strong if correction matches repeated user direction
  conflict_signal: strong if previous frame was wrong
  promotion_risk: medium
  compression_needed: yes
  packet_potential: possible

placement_candidate:
  REOPEN_CANDIDATE or SURFACE_UPDATE_CANDIDATE or COMPRESS_ONLY

next_action_candidate:
  correct the active operating surface immediately; long-term promotion remains WATCH

## 6. Recovered Judgment

The generator can handle Codex, Gemini, and user correction through a shared structure, but lane-specific risks differ:

- Codex: execution success can masquerade as direction approval.
- Gemini: synthesis can masquerade as truth or adoption.
- User correction: active frame correction can masquerade as permanent baseline.

`STATUS: MATURATION_QUEUE_GENERATOR_EXAMPLES_MATERIALIZED_WITH_WATCH`
