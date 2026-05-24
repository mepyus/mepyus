# Gemini-to-Codex Structure Request
# Candidate v0

## 1. Status

request_id:
  ...

Request Type:
  GEMINI_TO_CODEX_STRUCTURE_REQUEST

Authority:
  request only

Not:
  approval
  baseline
  workflow
  registry
  schema
  automation
  current-position update

## 2. Gemini Task Context

Gemini was working on:
  ...

Source packet:
  ...

Directly inspected:
  - ...

Not inspected:
  - ...

Return state:
  RETURNED_RAW / WATCH / HOLD / NEEDS_CODEX_STRUCTURE

## 3. Structural Gap Found

Gap:
  ...

Why it matters:
  ...

Why Gemini should not solve it directly:
  ...

Why Codex is needed:
  ...

## 4. Requested Codex Work

Codex should:
  - ...

Expected output file:
  ...

Optional run record:
  ...

Expected placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH / HOLD

## 5. Boundaries

Codex must not:
  - modify current-position
  - modify output_manifest unless explicitly asked
  - promote candidate to baseline
  - create workflow / registry / schema
  - create automation
  - perform broad repo read
  - expand raw logs
  - execute Gemini analysis
  - treat Gemini return as truth

## 6. Expected Codex Return Format

Verdict:
  ...

Files created:
  - ...

Files modified:
  - ...

Files inspected:
  - ...

Recovered / structured judgment:
  - ...

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH / HOLD

Next action:
  - ...

Hard stop confirmation:
  - no current-position update
  - no output_manifest update
  - no baseline / workflow / registry / schema promotion
  - no automation
  - no broad repo read
  - no raw log expansion

