# Run 006: Structured Footer Skill Check

## Declaration

```yaml
run_id: run_006_structured_footer_skill_check
skill_used: structured-footer.v0_1.skill.md
lens_used: structured-footer-lens.md
mode: read-only sandbox dry-run
baseline: false
implementation: false
automation: false
```

## Purpose

Validate whether the structured footer skill can reduce worker output into a four-line decision surface without turning the footer into approval, truth, or baseline.

## Case 1: low-risk read-only report

### input

```text
Worker created a read-only summary report and did not modify files.
```

### footer

```text
status: 완료
summary: read-only report was created without source-space modification.
risk: low; summary should not be treated as baseline.
next: stop unless the user wants validation or intake.
```

## Case 2: implementation result

### input

```text
Worker changed one UI label and claims no behavior changed.
```

### footer

```text
status: 검증 필요
summary: one label was changed, but the no-behavior-change claim still needs validation.
risk: logic or reference impact may be hidden.
next: run validation before recovery.
```

## Case 3: baseline proposal

### input

```text
Worker says this packet structure should become the new baseline.
```

### footer

```text
status: 사용자 판단 필요
summary: baseline promotion was proposed.
risk: AI cannot lock or promote candidate structure.
next: hold as candidate and ask user for explicit review.
```

## Case 4: unclear broad request

### input

```text
User asks: 전체를 알아서 정리하고 자동화해줘.
```

### footer

```text
status: 보류
summary: scope is too broad and includes possible automation.
risk: proceeding may create controller/automation or change source-space behavior.
next: clarify scope and route first to research, validation, or preflight guard.
```

## Self-check

```yaml
status_count: 4
approval_language_used: false
summary_as_truth: false
baseline_created: false
notes_preserved: true
```

## Run result

```yaml
verdict: PASS_WITH_NOTE
why_not_ok: needs validation that the footer stays short under real worker output
cases_tested: 4
low_risk_completed: 1
validation_required: 1
human_review_required: 1
hold_cases: 1
next_packet_candidate: validation_round_6
```
