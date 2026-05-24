# Gap And Fix Backlog

classification: CANDIDATE_FIX_BACKLOG
promotion: HOLD
authority_mutation: NO

## P0 fixes before any Phase 1 discussion
1. Strict G1 direct-transition test
   - Current suite demonstrates route-before-execution in sample flow and blocks missing LIGHT fields, DEEP scope, BLOCKED_SPECIAL.
   - Add explicit negative test: create request and call create-execution before apply-route; expected G1 PASS_BLOCKED.

2. Explicit G6/G8 close-block tests
   - Current model avoids close-request command entirely, which is safe but less demonstrative.
   - Add boundary probes proving RECEIPT_REQUIRED cannot close without receipt and REVIEW_REQUIRED cannot close without review if a close-like future command appears.

3. Guardrail table should distinguish PASS, PASS_BLOCKED, WATCH
   - Current event table records pass/block-pass but not severity dimension.
   - Add severity column or normalized result vocabulary before growing suite.

4. Remove py_compile side-effect from allowed file layout or mark as WATCH
   - Python generated __pycache__ during validation.
   - User denied deletion, so preserve as WATCH and avoid claiming exact file layout purity.

5. Add validator script inside review pack
   - This review pack includes validate_post_review.py to verify boundaries and counts.

## P1 improvements before Web MVP planning
1. More realistic state enum and transition table.
2. Dedicated guardrail registry table with guardrail ids G1-G16.
3. Export should include linked assets table details, not placeholder text.
4. CLI help examples should be expanded.
5. Add deterministic test runner command separate from sample suite.

## Keep as-is for now
1. Single-file CLI.
2. SQLite only.
3. Markdown export only.
4. Default promotion HOLD and authority NO.
5. No external execution.
