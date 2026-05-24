# Bounded Combined Bridge Usage Card Candidate v0

## Verdict

```text
BOUNDED_COMBINED_BRIDGE_USAGE_CARD_CANDIDATE_V0_PREPARED_NO_PROMOTION
```

## Use When

```text
A bounded one-shot bridge is needed where:
  Hermes hosts execution,
  Gemini produces raw/lite evidence,
  Codex performs recovery,
  Hermes writes receipt/report,
  VectorFL receives candidate evidence only.
```

## Do Not Use When

```text
The user wants recurring automation.
The task requires live web/source lookup.
The task needs external connector side effects.
The task needs authority mutation or promotion.
The approval block is incomplete.
The output directory is not exact.
```

## Minimum Fill-In Fields

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET
APPROVED_PACKET_PATH
APPROVED_OUTPUT_DIR
APPROVED_GEMINI_COMMAND
APPROVED_CODEX_COMMAND
APPROVED_NETWORK_SCOPE
APPROVED_LIVE_WEB_SOURCE_LOOKUP
APPROVED_EXTERNAL_CONNECTOR
APPROVED_PROMOTION
DECLARED_GEMINI_INPUT_FILES
DECLARED_CODEX_INPUT_FILES
EXPECTED_OUTPUTS
```

## Safe Default

```text
If any approval or path field is missing: STOP.
If Gemini lite JSON is invalid: STOP.
If negative_evidence is missing: STOP or WATCH depending on risk.
If promotion appears: STOP.
```

## Operator Sequence

```text
1. Fill packet instance from template.
2. Confirm approval block says yes and promotion=no.
3. Run Gemini command exactly.
4. Extract/validate gemini_lite_output.json.
5. Run Codex recovery command exactly.
6. Verify codex recovery return exists.
7. Write Hermes receipt/report.
8. Return candidate verdict with WATCH/HOLD.
```

## Required Final Line

```text
No promotion was performed. Recovery class remains candidate.
```
