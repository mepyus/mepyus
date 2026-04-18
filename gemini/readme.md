# Gemini Backend Support Layer

## Purpose
Gemini CLI is used as a read-only backend assistant.
It does not modify the engine. It only reads, summarizes, compares, and checks outputs.

## Role Separation
- User: decision and approval
- Codex: code changes and execution
- Gemini: read-only analysis (summary, diff, validation)

## Allowed
- summarize operation results
- review diffs
- check pointer structure
- generate readable explanations
- highlight suspicious points

## Not Allowed
- modify any file
- write to registry / provenance / event
- perform deletion or compaction decisions
- redefine contracts or policies
- act as execution agent

## Usage
Use prompt templates in `gemini/prompts/`.

Example:
- review_diff.md
- summarize_board.md
- check_pointer.md

## Principle
Gemini is not a hand that changes the engine.
It is an eye that reads and inspects it.