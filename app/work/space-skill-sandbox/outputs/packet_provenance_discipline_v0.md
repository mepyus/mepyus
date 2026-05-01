# Packet Provenance Discipline v0

## 0. Status

- status: sandbox candidate
- baseline: false
- source_space_rule: false
- automation: false

## 1. Purpose

이 문서는 task packet이 누가 만들었고, 어떤 기준을 참조했고, 누가 실행할 수 있는지 기록하는 규칙 후보다.

## 2. Why Packet Provenance Matters

패킷은 단순 prompt가 아니다.
패킷은 worker에게 권한, 범위, 금지사항, 출력 형식, 검증 기준을 전달하는 운영 표면이다.

따라서 packet creator와 packet executor를 구분해야 한다.

## 3. Required Packet Metadata

모든 next task packet에는 다음 metadata를 포함해야 한다.

- packet_id:
- intended_run:
- created_by:
- created_for:
- allowed_executor:
- source_references:
- creation_context:
- execution_mode:
- forbidden_actions:
- required_outputs:
- validation_targets:
- closeout_required:
- self_execution_allowed: false

## 4. Creator Rules

Allowed packet creators:

- Codex
- ChatGPT supervisor draft, if Codex is unavailable
- User-approved manual packet

Not allowed:

- Gemini creating its own execution packet
- runner generating packet content
- script auto-generating next packet
- packet generated from raw Gemini output without review

## 5. Executor Rules

Allowed executor:

- Gemini, when executing a stored packet
- only via user-triggered manual runner or explicit user instruction

Executor must not:

- rewrite the packet scope
- add promotion
- create next packet
- validate its own authority
- expand into automation

## 6. Runner Rules

Runner must record:

- packet path
- run id
- timestamp
- dry_run status
- Gemini invoked or not
- raw output path
- outbox path
- timeout status

Runner must not:

- infer next task
- create next packet
- apply output
- validate success beyond transport-level status

## 7. Packet Review Checklist

Before execution, check:

- Does the packet exist as a file?
- Is created_by recorded?
- Is allowed_executor recorded?
- Is self_execution_allowed false?
- Are forbidden actions explicit?
- Are output paths explicit?
- Is validation separated?
- Is user-triggered execution required?

## 8. Non-Promotion Note

Packet provenance is not a baseline.
Packet provenance is not Relay v1.0.
Packet provenance is not automation.
It is a sandbox discipline candidate for safe agent handoff.
