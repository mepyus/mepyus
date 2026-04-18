# Integrated Engine Current Conversation Surface Snapshot v0

## verdict
PASS_WITH_NOTE

## snapshot target

- UI source:
  - `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
  - `app/ui/integrated_engine/CliHostControlPanel.tsx`
- Current screen role:
  - conversation-first integrated-engine work surface
  - one-handler operating mode
  - Codex CLI attached through the existing integrated-engine CLI session API

This snapshot records the current state after the surface was cleaned up from mixed panel mode into a darker conversation workbench with an engine-position sidebar.

## current screen shape

The current screen is organized as:

```text
left rail
  current package context
  current purpose / status / next action

center
  Integrated Engine chat
  conversation transcript
  message input
  latest return and packet digest
  engine position log
  support packet controls
  recent turns / route marks inspector

right rail
  Engine position
  process rail
  engine / integrated engine / package meaning
  Structure Reading
  latest return
  raw state boundary inspector
```

The main intent is no longer to expose all User / VectorFL / Engine panels at once. The main intent is to let the user issue a direct instruction and see it move through the integrated-engine process.

## what is now reflected well

### 1. Direct instruction as front door

The central input is now labeled as `message to integrated engine`.

The default instruction is:

```text
내부 공간의 구조를 분석해서 가져와.
엔진/통합엔진/패키지 구조 기준으로 무엇을 읽었는지,
현재 어디를 흐르는지,
결과물을 어떻게 보면 되는지 한국어로 짧게 반환해줘.
파일은 수정하지 않는다.
```

This correctly frames the surface as an instruction-driven workbench, not a static dashboard.

### 2. Conversation transcript exists

`CliHostControlPanel.tsx` now records local UI turns:

- `you`
- `engine preflight`
- `cli handoff`
- `codex`
- `VectorFL reread`

This makes the result more conversational than the previous latest-return-only display.

### 3. Engine process location is visible

The right sidebar now names the active process as:

```text
지시 수신
-> 내부 공간 읽기
-> 패키지 형성 / CLI 실행
-> 반환 재독해
```

This is the clearest current expression of the desired engine/internal-space/package flow.

### 4. Engine / integrated engine / package distinction is present

The right sidebar includes three small meaning cards:

- `engine`: 내부 구조 읽기
- `integrated engine`: 공정/경계/route 판정
- `package`: 결과물로 담기

This is a compact, usable version of the deeper architecture.

### 5. Structure Reading slot exists

The right sidebar includes:

- `line hint`
- `axis hint`
- `precedent`
- `boundary`
- `package state`

This gives the screen a lightweight path to reflect the structures that were previously only documented.

## what is intentionally weak / bounded

### 1. Line and axis are hints only

The current `line hint` and `axis hint` are not real line/axis validation.

They are computed from current packet evidence presence and task lens. They should be read as weak surface cues, not promoted structure.

### 2. Precedent mining is not executed here

The `precedent` row intentionally says `not checked here` when evidence exists.

This prevents the screen from pretending that internal precedent mining has already happened.

### 3. Conversation transcript is not persistent

The transcript is local React state. It is not yet a durable runtime conversation record.

Refreshing the browser can lose the local turn sequence, even though backend CLI sessions remain recorded under `runtime/cli_sessions`.

### 4. CLI execution is request/return, not streaming

The current Codex path uses the existing API:

- `/api/vectorfl-engine/actions/cli-session/run`
- `/api/vectorfl-engine/actions/cli-session/mark`

The UI does not yet stream raw PTY output.

### 5. Gemini CLI is not attached

The screen names a Gemini-ready slot only conceptually. The active backend path remains Codex.

## current structure evaluation

### Does the screen carry our engine / integrated-engine / package structure?

Yes, in a bounded way.

The screen now gives a user-visible route from instruction to internal reading to package/CLI/return, and the right sidebar names the key structure layers. This is enough for a first working surface.

### Is it complete?

No.

The current structure is an operating surface, not a full engine ontology UI. It does not yet run real line/axis validation, precedent mining, persistent transcript storage, or Gemini cross-check.

### Is the current simplification acceptable?

Yes.

The previous screen was overexposed and panel-heavy. The current screen is easier to use because it keeps deep structure in compact side slots instead of making every process layer a front panel.

## most important current risk

The biggest risk is false confidence from compact labels.

Rows like `line hint`, `axis hint`, and `package state` can look more authoritative than they are. The current wording mitigates that by using weak labels:

- `pending`
- `inferred`
- `weak`
- `not checked here`
- `draft packet`

Do not strengthen those labels until real underlying checks are added.

## next safe improvement

The next safe improvement is not more layout change.

The next safe improvement is to make one small browser run and verify whether this instruction:

```text
내부 공간의 구조를 분석해서 가져와
```

produces a readable flow across:

```text
transcript
-> process rail
-> Structure Reading
-> latest return
```

If that feels coherent, the following iteration can add persistence for the transcript or a real internal-space-read packet.
