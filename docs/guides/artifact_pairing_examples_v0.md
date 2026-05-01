# Artifact Pairing Examples v0

## Strong Pair

Question: compare Phase 1.8 and Phase 1.9 run 03 merge reports.

Pair:

- before: `runtime/merge_diff_reports/phase1_8_run_03_merge_diff_report.json`
- after: `runtime/merge_diff_reports/phase1_9_run_03_merge_diff_report.json`

Why: both share run stem and logical slot, while phase markers provide ordering.

Expected confidence: `strong_pair`.

## Plausible Pair

Question: compare two contract versions.

Pair:

- before: `runtime/contracts/merge_diff_report_v3.json`
- after: `runtime/contracts/merge_diff_report_v4.json`

Why: same contract family and version markers suggest lineage, but semantics still need field/path reading.

Expected confidence: `strong_pair` when both files exist; `plausible_pair` when only stem/path context is available.

## Weak Pair

Question: compare generated artifacts, but the selected paths are unrelated runtime records.

Pair:

- before: first selected JSON path
- after: second selected JSON path

Why: fallback only; no family key was confirmed.

Expected confidence: `weak_pair`, with cautious diff or hold support only.

## Rejected Candidate Note

If three or more files share a family, the selected pair should record intermediate candidates. This makes the comparison auditable and tells the next run where a narrower before/after question should probe.
