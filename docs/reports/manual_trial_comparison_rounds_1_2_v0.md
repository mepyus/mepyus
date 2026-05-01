# Manual Trial Comparison Rounds 1-2 v0

## Overall Verdict

PASS

The frozen phase-1 chain was usable by hand in both completed manual trials. Both topics moved through intake, digestion, review, and memory without requiring new schema, added package layers, field renaming, or tooling.

## Trial topics compared

- Round 1: OMX `.omx/state/` as mode-state storage from `references/git_search/oh-my-codex-main/AGENTS.md`.
- Round 2: OMX `.omx/project-memory.json` as cross-session memory from `references/git_search/oh-my-codex-main/AGENTS.md`.

## What feels validated now

- The frozen chain is manually usable across two narrow OMX runtime-boundary topics.
- Intake captured each source topic cleanly without interpretation overload.
- Digestion was the strongest differentiating layer in both trials because it separated source meaning from package-side preservation.
- Review was useful in both trials for preventing accidental claims about OMX runtime behavior, routing, or schema.
- Round 2 validated that OMX runtime memory and the sidecar memory package can stay distinct even when both use the word memory.
- `source_bundle_ref` did not create actual confusion in either trial; it remained broad, but readable in context.

## What feels awkward but still acceptable

- Review and memory repeated similar boundary wording in both trials.
- The repeated unresolved-schema caution felt most repetitive across the two trials.
- The memory package remained the lightest layer; it is not yet heavy, but it still justified itself as preservation intent after review.
- Round 2 carried stronger naming/meaning pressure because OMX project memory and sidecar memory package terminology overlapped.
- Round 1 had milder naming pressure around runtime state versus sidecar package records, but less direct word overlap than Round 2.

## What should remain frozen

- Keep the intake, digestion, review, and memory layer sequence unchanged.
- Keep `source_bundle_ref` unchanged.
- Keep the distinction between OMX runtime artifacts and sidecar package memory unchanged.
- Do not add schemas, package layers, renamed fields, or tooling from these trials.

## One bounded conclusion

Keep phase 1 frozen as-is.

Justification: both manual trials passed the practical usability test, the only awkwardness was manageable repetition, and the strongest possible naming-pressure case in Round 2 did not produce actual confusion.
