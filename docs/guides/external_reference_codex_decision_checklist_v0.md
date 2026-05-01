# External Reference Codex Decision Checklist v0

## Purpose

This checklist reduces repeated Codex-side judgment for external reference intake and merge work.

## 1. Intake Classification

Before writing the memo, classify the source:

- is it `broad_reference`?
- is it `operating_reference`?
- is it `api_surface_reference`?
- is it still only `raw_capture`?

## 2. Raw vs Memo Decision

Check:

- can raw input honestly be ingested?
- does script-first gate/probe say the raw shape is unstable?
- does the source need paraphrased memo translation first?

Default:

- if probe is mixed or unclear, write a structured memo

## 3. Current Use Decision

State what the source is useful for now:

- boundary reminder
- operating reference
- tool surface comparison
- worker-mode comparison
- attachability reread support

## 4. Merge Candidate Decision

Ask:

- does this source complement an existing broad reference?
- does it add a concrete runtime surface?
- does it add a concrete operator lever?
- would merging reduce reread cost later?

If yes, mark as merge candidate.

## 5. Output Close Decision

For every observation or merge note, state:

- current position
- can use now
- should not use yet

## 6. Promotion Guard

Before finalizing, check:

- am I treating a single source like a rule?
- am I turning bounded support into doctrine?
- am I flattening uncertainty too early?

If yes, step back to `no promotion`.

## One-Line Summary

Classify first, memo second, merge only for complementarity, and always end with bounded operating use.
