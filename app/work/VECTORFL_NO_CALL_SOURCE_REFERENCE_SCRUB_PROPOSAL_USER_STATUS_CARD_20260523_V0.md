# VECTORFL_NO_CALL_SOURCE_REFERENCE_SCRUB_PROPOSAL_USER_STATUS_CARD_20260523_V0

status: USER_STATUS_CARD_WITH_HOLD
created_at: 2026-05-23T23:44:00+0900

쉬운 판정:

```text
API처럼 보이거나 실제 local endpoint replay로 이어질 수 있는 legacy source refs를 future operator surface에서 scrub하는 proposal을 만들었다.
```

핵심:

```text
외부 API만 금지하는 게 아니라 localhost endpoint replay/server-start도 no-call lane에서는 금지한다.
```

아직 안 한 것:

```text
기존 script 수정 안 함
기존 receipt 수정 안 함
registry 생성 안 함
authority mutation 안 함
```

다음:

```text
기존 static card를 원본 수정 없이 scrubbed copy로 한 번 생성한다.
```
