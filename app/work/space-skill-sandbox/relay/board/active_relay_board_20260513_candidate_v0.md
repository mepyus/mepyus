# Active Relay Board
# 2026-05-13 Candidate v0

## 1. Status

candidate relay board
not current-position
not workflow
not registry
not automation

Purpose:
  reduce manual relay fatigue by making packet state visible.

Authority:
  orientation surface only

## 2. Active Packets

| packet_id | from | to | state | source path | expected return | current owner | watch |
|---|---|---|---|---|---|---|---|
| gemini_big_frame_candidate_map_draft_packet_precheck_20260513_v0 | ChatGPT / Supervisor via Codex packet authoring | Gemini | RETURNED_RAW | app/work/space-skill-sandbox/relay/packets/to_gemini/gemini_big_frame_candidate_map_draft_packet_precheck_20260513_v0.md | Gemini observation return received in chat | ChatGPT / Supervisor review | preflight return must not be treated as map creation approval |
| big_frame_candidate_map_draft_packet_20260513_v0 | Gemini preflight via Codex packet authoring | Codex | DRAFT | app/work/space-skill-sandbox/relay/packets/to_codex/big_frame_candidate_map_draft_packet_20260513_v0.md | Big Frame Candidate Map draft only after explicit user approval | User judgment | packet exists but execution remains manual and unapproved |
| chatgpt_supervisor_handoff_big_frame_map_draft_decision_20260513_v0 | Codex packet authoring | ChatGPT / Supervisor | READY_TO_SEND | app/work/space-skill-sandbox/relay/packets/to_chatgpt/chatgpt_supervisor_handoff_big_frame_map_draft_decision_20260513_v0.md | Supervisor placement and packet state recommendation | User manual transfer | handoff must not be treated as execution approval |

## 3. Manual Transfers Needed

| transfer_id | target CLI | path to provide | user action | status |
|---|---|---|---|---|
| transfer_001_manual_relay_trial_001 | Gemini | app/work/space-skill-sandbox/relay/packets/to_gemini/gemini_big_frame_candidate_map_draft_packet_precheck_20260513_v0.md | Give packet path to Gemini | RETURNED_RAW |
| transfer_002_chatgpt_supervisor_handoff | ChatGPT / Supervisor | app/work/space-skill-sandbox/relay/packets/to_chatgpt/chatgpt_supervisor_handoff_big_frame_map_draft_decision_20260513_v0.md | Give handoff packet content/path to ChatGPT for placement decision | READY_TO_SEND |

## 4. Waiting Returns

| packet_id | waiting from | landing zone | expected return | watch |
|---|---|---|---|---|

## 5. Ready for Supervisor Review

| return_id | source CLI | raw return path | review needed | watch |
|---|---|---|---|---|
| gemini_big_frame_map_draft_preflight_return_20260513 | Gemini | user-provided chat return | decide whether draft packet remains DRAFT / READY_TO_SEND / HOLD | return must not approve map creation by itself |

## 6. Ready for Codex Recovery

| reviewed_return | placement | codex packet needed | status |
|---|---|---|---|

## 7. HOLD

| item | reason | unblock condition |
|---|---|---|
| Big Frame Candidate Map draft execution | draft packet exists, but map creation is not yet approved | explicit user approval to execute app/work/space-skill-sandbox/relay/packets/to_codex/big_frame_candidate_map_draft_packet_20260513_v0.md |

## 8. Board Watch

- board must stay thin
- board must not become current-position
- board state must not become approval
- packet state must not become automatic execution
