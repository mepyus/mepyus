# Codex Space Execution Split Check v0

## Verdict

`PASS_WITH_NOTE`

## Why This Check Was Needed

As the space grows, asking Codex to manually do all probing, sweeping, validation, and interpretation would create unnecessary token pressure.

The repo already has:

- executable capability registry
- runner index
- many bounded probe and validation scripts

What was missing was a front rule for:

- Codex-only
- space-script-first
- hybrid

## What Was Added

- [codex_space_execution_split_manual_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/codex_space_execution_split_manual_v0.md)
- [run_execution_split_advisor.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_execution_split_advisor.py)

## Dry Checks

### 1. Intent: `전처리 필요 여부 판정`

Expected:

- `space-script-first`

Reason:

- there is already a direct capability and runner for external input gate probing

### 2. Intent: `git_search 외부도구를 분석하고 우리 공간에 붙일 구조를 리포트해줘`

Expected:

- `hybrid`

Reason:

- there are scriptable evidence-gathering surfaces
- but final structure, mapping, and judgment must remain Codex-side

## What This Locks

- scripts should own bounded evidence collection where a capability already exists
- Codex should own interpretation, mapping, and final usable packaging
- hybrid should be the default for external adaptation and repo-attachment analysis

## What This Does Not Lock

- automatic execution routing
- authority to run mutating scripts without judgment
- replacement of request orchestration with scripts

## Final Note

This split is intentionally narrow.

It exists to reduce unnecessary manual/token-heavy work while keeping boundary-sensitive reasoning on the Codex side.
