# Maturation Queue Examples
# Tool Decision Results

## 1. Status

Status:
  MATERIALIZED_FROM_SOURCE_14_WITH_WATCH

Source:
  `14.md`

Purpose:
  Materialize the three tool-decision examples as candidate Maturation Queue Items.

Not:
  memory
  schema
  registry
  workflow
  final judgment
  approval

## 2. MQI-healthcheck-001

source_type:
  tool-use decision result

source_ref:
  OpenClaw healthcheck skill review

origin_lane:
  ChatGPT / user-provided result

raw_material_summary:
  OpenClaw healthcheck skill was reviewed as a small external tool candidate.

execution_claimed:
  no

file_changes_claimed:
  no

recovered_judgment_candidate:
  Small tool does not mean small execution boundary.

usable_candidate:
  Healthcheck can remain a bounded future test candidate, but requires Pre-use Packet before any real run.

WATCH:
  - healthcheck -> host inspection permission
  - read-only checks -> harmless assumption
  - skill workflow -> VectorFL workflow
  - cron recommendation -> automation approval
  - memory write guidance -> VectorFL memory permission

HOLD:
  - OS command execution
  - OpenClaw CLI execution
  - security audit
  - update status
  - cron scheduling
  - memory write
  - host hardening

boundary_flags:
  command_execution: yes
  file_write: possible
  credentials: unclear
  api_network: unclear
  memory_indexing: possible
  automation: possible
  baseline_promotion: no

maturation_signals:
  repeat_signal: medium
  conflict_signal: none
  promotion_risk: medium
  compression_needed: yes
  external_packet_potential: yes
  eval_seed_potential: yes
  surface_update_potential: yes

placement_candidate:
  WATCH_PATTERN_CANDIDATE

review_gate:
  required: yes
  reason: execution implied / host-security boundary / automation risk
  question: Should this remain only as a bounded-test candidate, or should a Pre-use Packet be drafted for a future exact read-only command?

output_candidate:
  eval seed candidate
  Pre-use Packet fragment
  HOLD reminder
  Small Tool Boundary Drift lens support

## 3. MQI-xurl-001

source_type:
  tool-use decision result

source_ref:
  OpenClaw xurl skill review

origin_lane:
  ChatGPT / user-provided result

raw_material_summary:
  xurl was reviewed as a small CLI wrapping authenticated X/Twitter API access.

execution_claimed:
  no

file_changes_claimed:
  no

recovered_judgment_candidate:
  Small credential-bearing CLI must not be used from read-only review.

usable_candidate:
  xurl is useful as high-risk small-tool eval seed material, not as a current tool.

WATCH:
  - small CLI -> harmless assumption
  - auth status -> safe check assumption
  - credential file existence -> consent
  - API capability -> permission
  - account read -> harmless observation
  - JSON output -> truth
  - social account access -> authority

HOLD:
  - xurl execution
  - auth status
  - reading `~/.xurl`
  - credential/token use
  - API/network call
  - account read/write
  - DM read/send
  - media upload
  - account mutation

boundary_flags:
  command_execution: yes
  file_write: possible
  credentials: yes
  api_network: yes
  account: yes
  upload_download: yes
  automation: possible
  baseline_promotion: no

maturation_signals:
  repeat_signal: strong
  conflict_signal: none
  promotion_risk: high
  compression_needed: yes
  external_packet_potential: possible
  eval_seed_potential: yes
  surface_update_potential: yes

placement_candidate:
  EVAL_SEED_CANDIDATE

review_gate:
  required: yes
  reason: credential/API/account boundary / execution implied
  question: Should this remain HOLD as eval seed material, or is there a future exact approved action requiring a Pre-use Packet?

output_candidate:
  eval seed candidate
  HOLD reminder
  external tool packet hard-stop
  one-page surface warning

## 4. MQI-docs-adrs-001

source_type:
  tool-use decision result

source_ref:
  documentation-and-adrs skill review

origin_lane:
  ChatGPT / user-provided result

raw_material_summary:
  documentation-and-adrs skill was reviewed as documentation guidance and ADR structure material.

execution_claimed:
  no

file_changes_claimed:
  no

recovered_judgment_candidate:
  Reference is not adoption.

usable_candidate:
  Useful as comparison material for documentation guidance staying reference-only.

WATCH:
  - ADR template -> VectorFL schema
  - docs/decisions path -> required structure
  - ADR lifecycle -> workflow
  - documentation guidance -> policy
  - README structure -> required product surface

HOLD:
  - creating ADR files
  - creating docs/decisions
  - modifying README
  - writing API docs
  - adopting ADR lifecycle as VectorFL workflow

boundary_flags:
  command_execution: no
  file_write: possible if followed literally
  credentials: no
  api_network: no
  account: no
  memory_indexing: no
  automation: no
  baseline_promotion: possible if adopted

maturation_signals:
  repeat_signal: medium
  conflict_signal: none
  promotion_risk: medium
  compression_needed: yes
  external_packet_potential: yes
  eval_seed_potential: yes
  surface_update_potential: no

placement_candidate:
  KEEP_AS_REFERENCE

review_gate:
  required: no unless adoption or file creation is later requested

output_candidate:
  decision anchor
  eval seed support
  do-not-repeat rule

## 5. Recovered Signal

The three examples prove that Small Tool Boundary Drift is a lens, not a universal blocker:

- healthcheck: bounded future test candidate
- xurl: HOLD under credential/API/account boundary
- documentation-and-adrs: reference-only under read-only review

`STATUS: MATURATION_QUEUE_TOOL_DECISION_EXAMPLES_MATERIALIZED_WITH_WATCH`
