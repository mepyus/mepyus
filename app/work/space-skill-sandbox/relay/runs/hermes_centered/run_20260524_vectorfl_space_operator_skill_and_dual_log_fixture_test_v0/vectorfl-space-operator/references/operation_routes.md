# Operation Routes

`CODEX_SPACE_CHECK` handles "공간을 확인해".
Return a bounded snapshot of active space controls and current HOLD/proposal handles.

`CODEX_HERMES_WORK_ANALYSIS` handles "헤르메스 작업 내용을 분석해".
Return what Hermes used, merged, executed or held, and what reentry/maturation handles exist.

`CODEX_SPACE_RETRIEVAL_BY_ORIGINAL` handles Hermes pre-execution space retrieval.
Return selected refs, rejected refs, original-to-space fit, changed judgment for Hermes, risks, recommended merge inputs, and HOLD status.

`CODEX_SPACE_MATURATION_BY_REENTRY_RECORD` handles post-execution reentry.
Return HOLD-only maturation proposals and rejected maturation actions.

