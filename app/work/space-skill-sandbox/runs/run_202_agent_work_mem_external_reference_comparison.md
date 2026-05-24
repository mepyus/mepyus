# Run 202 - agent-work-mem External Reference Comparison

## 1. Status

Status: external reference comparison note
Authority: candidate comparison memory / not baseline / not official workflow
Purpose: compare one User-provided external reference against current-position, process-memory, worker handoff, and usage-card concerns

`STATUS: AGENT_WORK_MEM_COMPARISON_NOTE_COMPLETE`

## 2. Source Identification

- source name: `daystar7777/agent-work-mem`
- source URL: `https://github.com/daystar7777/agent-work-mem`
- source type: external GitHub reference
- user-provided: yes
- intended role in our space: external reference comparison
- adoption status: not adopted

Source pages read:

- `https://github.com/daystar7777/agent-work-mem`
- `https://github.com/daystar7777/agent-work-mem/blob/main/PROTOCOL.md`

Read scope:

- repository README summary / structure
- PROTOCOL overview and selected rules relevant to shared memory, append-only logs, reading order, handoff, agent identity, and tiered context

No broad browsing beyond the provided repository was performed.

## 3. Four-Line User-Facing Card

### 지금 어디까지 왔나?

외부자료 하나가 User에 의해 제공됐다.

이 자료는 여러 AI coding agent가 같은 작업 기억을 읽고 넘겨받는 방법을 설명한다.

우리 공간에서는 아직 채택 대상이 아니라, current-position / process-memory / handoff 고민과 비교해 볼 참고자료다.

### 무엇을 움직일 수 있나?

설치하거나 적용하지 않고, 닮은 점과 다른 점만 비교할 수 있다.

특히 "에이전트들이 같이 읽는 작업 기억 폴더", "어디서부터 읽을지 알려주는 안내판", "작업이 이어지도록 남기는 실행 기록", "인계 메모" 같은 아이디어를 우리 구조와 나란히 볼 수 있다.

### 무엇을 조심해야 하나?

이 자료가 좋아 보인다고 해서 `AIMemory/`를 만들거나, `INDEX.md`를 공식 인덱스로 삼거나, `work.log`를 우리 원장으로 바꾸면 안 된다.

외부 프로토콜은 우리 baseline, workflow, router, automation, CLI/tool adoption plan이 아니다.

### 다음 판단은 무엇인가?

이번 단계에서는 Codex가 비교 메모만 남긴다.

나중에 User가 원하면, 특정 아이디어 하나를 candidate inspiration으로 더 좁혀 읽을 수 있다.

## 4. What This External Material Is About

`agent-work-mem` presents a vendor-neutral, markdown-based shared memory approach for multiple AI coding agents. Its core idea is that agents coordinate through an `AIMemory/` folder containing orientation, protocol, logs, archives, and handoff files.

The README describes a reading order where agents start from `AIMemory/INDEX.md`, then `PROJECT_OVERVIEW.md`, then the recent tail of `work.log`. It also describes append-only work logging, cross-agent handoff files, agent identity/capability records, hot/warm/cold context tiers, and natural-language handoff commands that trigger structured handoff behavior.

The PROTOCOL describes stronger rules: AI-authored markdown goes under `AIMemory/`, `work.log` is append-only shared memory, agents read log tail before work, authored files include model identity, and multi-agent work uses disciplined ownership of log writes.

## 5. Comparison With Our Space

| agent-work-mem element | closest concept in our space | what we can learn | what we must not copy directly | risk if misunderstood |
|---|---|---|---|---|
| `AIMemory/` | sandbox-local outputs/runs plus current-position/process-memory layer | a visible shared memory surface can reduce session loss | do not create `AIMemory/` or move our memory into it | external folder structure becomes our official structure |
| `INDEX.md` | active-anchor orientation candidate / latest current-position entry | a small first-read guide helps new sessions orient | do not replace active-anchor/current-position with `INDEX.md` | index becomes registry or source of authority |
| `PROJECT_OVERVIEW.md` | whole-space orientation atlas / purpose package | onboarding primer can be useful when context is large | do not collapse atlas/purpose/model into one overview | overview becomes policy or final architecture |
| `work.log` | process-memory / run records / ops trace | append-only trace discipline is useful | do not replace run records with a single shared `work.log` | single log becomes official ledger |
| archive / cold tier | historical residue / read-later / older reports | tiered context can reduce re-entry burden | do not impose hot/warm/cold storage law on our corpus | storage tiers become filing policy |
| `handoff_*.md` | handoff checklist candidates / Codex-Gemini packet handoff | explicit transfer notes help preserve role boundaries | do not turn handoffs into an automatic router | handoff becomes command queue |
| `PROTOCOL.md` | reusable settings / operating model candidate / boundary notes | protocol-like clarity can reveal missing boundaries | do not install or treat it as our baseline | external protocol becomes source-space law |
| agent capability declaration | role boundary / worker attachment questions | capability and authority should be separated visibly | do not let capability become permission | worker capability becomes approval authority |
| natural-language handoff command | user-facing usage card / worker packet request | plain language can trigger careful preparation without exposing machinery | do not create hidden automation behind user phrases | natural language becomes implicit router trigger |

## 6. What Can Be Borrowed As Inspiration

- `INSPIRATION_ONLY` - append-only trace discipline, especially preserving corrections as new entries rather than rewriting history.
- `INSPIRATION_ONLY` - quick re-entry reading order, as a user-facing aid rather than official workflow.
- `INSPIRATION_ONLY` - handoff files as explicit transfer records between workers.
- `INSPIRATION_ONLY` - agent identity/capability declaration, if kept separate from approval authority.
- `INSPIRATION_ONLY` - tiered context management to reduce repeated broad reading.
- `INSPIRATION_ONLY` - natural-language handoff phrasing that remains visible to the User rather than hidden automation.

## 7. What Must Not Be Adopted Directly

- do not create `AIMemory/` in this project
- do not install the protocol
- do not replace current-position with `INDEX.md`
- do not replace process-memory with `work.log`
- do not turn handoff files into an automatic router
- do not treat `PROTOCOL.md` as our baseline
- do not give Codex/Gemini autonomous approval authority
- do not turn the four-line card into mandatory workflow

## 8. Space-Use Judgment

```text
USABLE_WITH_WATCH
```

Reason:

The material is useful as an external comparison reference because it touches shared memory, session recovery, agent handoff, append-only traces, capability declaration, and context tiering.

It requires watch because the repository presents a ready-to-install protocol, while our current boundary is comparison only. Direct adoption would create folder, protocol, workflow, and automation drift.

## 9. Worker Role Decision

```text
CODEX_BOUNDED_REVIEWER
CLI_NOT_NEEDED
GEMINI_NOT_NEEDED
```

Codex may compare and record.

Codex may not implement, install, or create `AIMemory/`.

Gemini is not needed for this bounded comparison.

CLI is not needed because no installation, file transformation, or automation is being tested.

## 10. Recovery Path

```text
PROCESS_MEMORY_LIGHT
```

Reason:

This material is useful as comparison memory for current-position, process-memory, worker handoff, and user-facing usage-card work. It should not update current-position unless the User explicitly decides to continue from it.

## 11. Watch Items

- external reference becoming adoption plan
- `AIMemory/` becoming our official folder structure
- `INDEX.md` becoming active-anchor / registry / official index
- `work.log` becoming our single process-memory ledger
- `PROTOCOL.md` becoming baseline
- handoff files becoming router / automation
- Codex gaining implementation authority
- Gemini becoming broad-run observer without approval
- four-line card becoming mandatory workflow

## 12. Boundaries

- no baseline promotion
- no official workflow creation
- no architecture finalization
- no automation/router/controller
- no CLI/tool adoption
- no Package 034/035/036 movement
- no Run 117 approval
- no Gemini broad run
- no Codex implementation authority
- no operating model rewrite
- no usage flow rewrite
- no four-line card protocolization
- no registry/index promotion
- no external material adoption
- no `AIMemory/` installation
- no protocol installation

`STATUS: AGENT_WORK_MEM_COMPARISON_NOTE_COMPLETE`
