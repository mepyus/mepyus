# Codex Request Queue Template
# Candidate v0

cycle_id:
  ...

queue status:
  EMPTY / CODEX_REQUESTS_READY / CODEX_STRUCTURING_MANUAL / CODEX_RETURNED / HOLD

authority:
  structure request queue only

not:
  registry
  workflow
  automation
  baseline
  current-position

## 1. Request Table

| request_id | source Gemini task | structural gap | requested Codex work | expected output | priority | forbidden actions | status |
|---|---|---|---|---|---|---|---|

## 2. Request Detail

### request_id:

Source Gemini task:
  ...

Structural gap:
  ...

Requested Codex work:
  ...

Expected output:
  ...

Priority:
  low / medium / high

Forbidden actions:
  - no automation
  - no scripts
  - no current-position update
  - no output_manifest update
  - no workflow / registry / schema / baseline promotion
  - no broad repo read
  - no raw log expansion

Status:
  DRAFT / READY_FOR_CODEX / DONE_WITH_WATCH / WATCH / HOLD

## 3. Queue Watch

- request queue must not become registry
- request priority must not become execution authority
- Codex should stay structure-focused
- Gemini observations are not truth

