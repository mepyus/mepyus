# Integrated Engine Real Worker Spine Validation Closeout v0

## 1. Verdict

PASS

This round can close.

The current operating spine is validated as a bounded Codex-worker package continuity baseline. It is not validated as a general multi-worker system, polished product UI, or automatic orchestration layer.

## 2. Round Scope

This closeout covers Packages 1 through 5:

- Package 1: real worker boundary audit
- Package 2: worker adapter prompt contract
- Package 3: first real external worker run validation
- Package 4: worker return normalization hardening
- Package 5: supervisor continuation loop validation

The round asked one practical question:

Can the integrated engine spine carry one real worker through package formation, worker handoff, structured return, notebook continuity, fallback resilience, and supervisor judgment?

Bounded answer:

Yes, for one Codex actual-worker path and the tested package/notebook flow.

## 3. Package Outcome Summary

| Package | Result | What was locked |
| --- | --- | --- |
| Package 1 | PASS | Actual worker boundary is inside `CodexCliAdapter.start_run(...)`, after stdout/stderr/status are known and before `structured_return.json` is written. |
| Package 2 | PASS | Worker adapter prompt now asks actual workers for a delimited `WORKER_RETURN_JSON` block and records `worker_return_source`. |
| Package 3 | PASS | `pkg_openharness_structure_probe` completed two actual Codex worker runs with `worker_return_source = worker_emitted`; Step B reused Step A outputs. |
| Package 4 | PASS | Missing, invalid, partial, prose-only, failed, and deposit-candidate output shapes remain notebook-readable through bounded normalization. |
| Package 5 | PASS | Supervisor can make bounded `continue / hold / rerun / inspect / close` judgments from notebook evidence, with raw logs reserved for diagnosis. |

## 4. Verified Baseline

The following is now verified:

### Actual worker boundary

The actual worker path is distinct from the dry-run path.

Actual Codex output enters through:

- `completed.stdout`
- `completed.stderr`
- `completed.returncode`

The narrow insertion point for structured return handling is locked before `structured_return.json` is written.

### Structured worker return contract

The runtime supports a worker-emitted return block:

- `WORKER_RETURN_JSON`
- JSON payload
- `END_WORKER_RETURN_JSON`

The return shape includes:

- `answer`
- `findings[]`
- `files_artifacts[]`
- `next_continue_hint`
- `open_questions[]`
- `risks_or_limits[]`
- `source_refs[]`

The notebook can read the structured return as preferred material.

### Return source labeling

The spine records the source quality of a run:

- `worker_emitted`
- `runtime_normalized`
- `parser_fallback`
- `raw_fallback`

This makes supervisor judgment clearer than a raw log stack.

### Real package continuity

`pkg_openharness_structure_probe` proved real continuity:

- Step A actual worker run produced real source-reading material.
- Step B reused Step A's structured return, operator report, stdout, and source refs.
- Latest notebook output exposed answer, findings, artifacts, risks, source refs, and a concrete next hint.

This is stronger than dry-run continuity.

### Normalization resilience

Fixture validation showed notebook continuity survives:

- valid worker-emitted JSON
- missing structured block
- invalid JSON block
- partial structured block
- prose-only return
- failed / nonzero output
- deposit-candidate output

Failure and fallback states are not hidden. They become hold/inspect/rerun material.

### Supervisor continuation loop

The supervisor can make bounded decisions from notebook evidence:

- continue
- hold
- rerun
- inspect
- close

Raw logs are no longer the default read path. They remain diagnosis artifacts.

## 5. Validity Boundary

This baseline is valid only under these conditions:

- one actual Codex worker path
- current package notebook / CLI session storage
- current worker return block contract
- current normalization/read path
- bounded supervisor judgment
- package-level continuation, not global system promotion

The baseline does not claim that every worker, package, task type, or UI surface is now ready.

## 6. Held / Not Yet Generalized

The following remain held:

### Gemini/manual worker variation

Only Codex actual-worker behavior was tested. Gemini, manual workers, and other execution backends may vary in delimiter compliance, stdout shape, error behavior, and source-ref discipline.

### Multi-agent orchestration

No worker queue, dispatch policy, team dashboard, or multi-agent coordination was validated.

### Broad worker generalization

The return contract is promising, but only one actual worker type has been tested.

### Artifact quality judgment

The notebook can point to artifacts and preserve evidence. It does not independently prove artifact quality or runtime behavior.

### Product-complete UI

The operating spine can feed a surface. This round did not validate polished end-user UX, live streaming, artifact viewers, or large-work management.

### Automatic line / axis detection

No automatic line/axis inference, promotion, or internal-space governance was validated.

### Canonical ingestion / promotion

Deposit candidates and worker returns remain review material. They are not automatically ingested or promoted.

## 7. Remaining Risks

Open risks:

- Codex-only validation may overstate readiness for other workers.
- Worker-emitted JSON can still fail if the worker ignores the block contract.
- Parser fallback remains weaker and uneven.
- Failed runs are preservable but not continuation-strong until inspected or rerun.
- Source inspection does not prove behavioral runtime correctness.
- Supervisor decisions are bounded but still depend on honest risk/source labeling.
- UI may still feel operationally thin for larger multi-package work.

## 8. Promotion / Hold Judgment

Recommended judgment:

`A. actual worker 1개 기준 spine 적합성 확인 완료`

Expanded wording:

The operating spine is promoted only to a bounded baseline for one Codex actual-worker package-continuity loop.

Held:

- general multi-worker readiness
- Gemini/manual worker support
- multi-agent orchestration
- product-complete UI
- automatic bridge/promotion/ingestion

This is a package-continuity baseline, not a system-wide release claim.

## 9. Recommended Next Bounded Round

Recommended next round:

**Codex worker baseline stabilization round.**

Purpose:

- keep one-worker scope
- stabilize the current contract under real usage
- avoid UI or orchestration expansion until the baseline is less brittle

Suggested package sequence:

1. Run one more real Codex worker package with a different bounded task type.
2. Validate structured return compliance without prompt tuning.
3. Validate failed/missing/partial real outputs if they occur naturally.
4. Add minimal regression fixtures for normalization if current helper-level validation is not enough.
5. Only then decide whether Gemini/manual worker adaptation is the next round.

Alternative next round if the supervisor wants worker diversity:

**Gemini adapter boundary audit only.**

That should mirror Package 1, not jump to full Gemini integration.

## 10. Closeout Statement

This validation round successfully tightened the integrated engine into an attachable operating spine:

`package -> handoff -> worker return -> normalized RunRecord -> notebook -> supervisor decision`

The spine now has enough real evidence to support bounded Codex-worker continuation work. It should not yet be sold to itself as a general multi-agent engine.

