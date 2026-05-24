# Codex Request Queue
# cycle_001_big_frame_candidate_map_orientation

cycle_id:
  cycle_001_big_frame_candidate_map_orientation

queue_status:
  EMPTY

Purpose:
  Collect Gemini-created structure requests if Gemini finds structural gaps.

Authority:
  request queue only

not:
  registry
  workflow
  automation
  baseline
  current-position
  output_manifest

Current requests:
  none

| request_id | source Gemini task | structural gap | requested Codex work | expected output | priority | forbidden actions | status |
|---|---|---|---|---|---|---|---|

Important:
  Gemini may propose request entries after execution.
  Codex should not act until user transfers this queue or ChatGPT / Supervisor approves.

Queue watch:
  - empty queue is not approval
  - request queue is not registry
  - Codex request is not execution permission

