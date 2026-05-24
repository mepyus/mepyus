# VECTORFL_NO_CALL_CURRENT_POSITION_REENTRY_SMOKE_CHECK_USER_STATUS_CARD_20260524_V0

status: USER_STATUS_CARD_WITH_HOLD
created_at: 2026-05-24T00:37:00+0900

쉬운 판정:

```text
새 current-position entry로 재진입하면 old endpoint replay가 아니라 scrubbed card/rollup으로 들어간다.
```

verdict:

```text
PASS_NO_CALL_CURRENT_POSITION_REENTRY_SMOKE_CHECK_WITH_HOLD
```

HOLD:

```text
api_call: NO
api_direct: NO
local_http_endpoint_replay: NO
local_server_start: NO
model_execution: NO
authority_mutation: NO
promotion: HOLD
```
