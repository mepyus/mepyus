# Company Work Review Adapter Search Test v0
# 05-15 Adapter Experiment

## 1. Status

Status:
  COMPANY_WORK_REVIEW_SEARCH_TEST_COMPLETED_WITH_WATCH

Purpose:
  Test the Company Work Review Adapter Card v0 against public memo-writing criteria found by web search.

Boundary:
  This is a chat-only / sandbox-local dry-run.
  It does not promote the adapter, create automation, modify AGENTS.md or SKILL.md, update current-position or output_manifest, create eval files, or create workflow/schema/registry/ontology.

## 2. Sources searched

Primary source used:
  Purdue OWL, "Parts of a Memo"
  https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/memos/parts_of_a_memo.html

Supplemental page checked:
  Purdue OWL, "Sample Memo"
  https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/memos/sample_memo.html

Source reading:
  The Purdue OWL memo guide separates a memo into heading, opening, context, task, summary, discussion, closing, and attachments.
  It emphasizes that the purpose should appear early, context should include only what the reader needs, discussion should support recommendations with facts, and the closing should make the desired action clear.

Use limitation:
  The test below does not reproduce the Purdue sample memo.
  It uses a synthetic company memo draft and applies the adapter against the public criteria.

## 3. Adapter under test

Company Work Review Adapter Card v0:

```text
검수 결과:
핵심 판단:
주의할 점:
지금 하지 말 것:
건드리는 범위:
다음 한 동작:
```

Candidate source:
  `PRACTICAL_SUPPLEMENTS_V0.md`

Underlying VectorFL surfaces:
  Queue Item Mini Form
  Short Return Packet

## 4. Synthetic test input

```text
Subject: New Customer Response Process

Starting next week, all customer issues should be answered faster.
The support team should use the new response template and avoid long back-and-forth messages.
Managers should check whether the process is working and tell the team if there are problems.
This should help customers and reduce delays.
```

## 5. Adapter execution

```text
검수 결과:
  HOLD_FOR_REVISION

핵심 판단:
  메모의 방향은 이해되지만 업무 지시로 쓰기에는 실행 조건이 부족하다.
  목적은 있지만 구체적인 담당자, 시행일, 적용 범위, 확인 기준, 예외 처리, 후속 액션이 약하다.

주의할 점:
  "answered faster"가 측정 불가능하다.
  "new response template"의 위치나 적용 범위가 없다.
  "Managers should check"가 어떤 관리자와 어떤 주기로 확인하는지 모호하다.
  고객 응답 정책은 품질, 승인, 고객정보, 컴플라이언스 경계가 생길 수 있다.

지금 하지 말 것:
  이 문안을 그대로 전사 공지로 보내지 말 것.
  자동화/템플릿 배포로 연결하지 말 것.
  고객 응답 SLA나 승인 정책처럼 확정하지 말 것.

건드리는 범위:
  회사 업무 문서 검수
  고객 응대 프로세스 초안
  정책/승인/고객정보 경계 가능성 있음

다음 한 동작:
  메모를 6개 항목으로 보강한다:
  목적, 적용 대상, 시작일, 담당자, 측정 기준, 예외/승인 경계.
```

## 6. Against public memo criteria

| Memo criterion | Adapter caught it? | Finding |
| --- | --- | --- |
| Clear subject / purpose | yes | Subject exists, but purpose needs a clearer action frame. |
| Opening purpose | partial | General goal exists, but requested action is not explicit enough. |
| Context | weak | The draft does not say what problem caused the new process. |
| Task / assignment | weak | It does not name who must do what by when. |
| Supporting facts | weak | No evidence or current delay metric is included. |
| Closing / desired action | weak | No specific next action or response deadline is provided. |
| Attachments / references | missing | The response template is mentioned but not linked or attached. |

## 7. Result

Result:
  PASS_WITH_WATCH

What passed:
  The adapter quickly caught practical business risks without needing internal VectorFL language.
  It produced a clear next action instead of only a critique.
  It kept policy/automation/approval boundaries in HOLD.

What needs adjustment:
  Add one optional field for company documents:

```text
빠진 근거/첨부:
  [template, source, metric, approval reference, policy link]
```

Why:
  Public memo criteria show that supporting facts and attachments are often necessary.
  The current six-field card catches the issue, but a dedicated evidence/attachment field would make company-document review stronger.

## 8. Revised company adapter candidate

```text
검수 결과:
핵심 판단:
주의할 점:
빠진 근거/첨부:
지금 하지 말 것:
건드리는 범위:
다음 한 동작:
```

Placement:
  candidate-only

WATCH:
  Do not make the added field mandatory for very small notes.
  Do not let this become a compliance checklist.

HOLD:
  no official company approval flow
  no policy automation
  no customer-data handling
  no baseline promotion

## 9. Next test suggestion

Run the revised card against one real user-provided artifact:

```text
company email
internal announcement
report draft
customer reply
Codex/Gemini result intended for work use
```

Until then, keep this as:
  `sandbox-local adapter candidate`

## 10. Hard stop confirmation

```text
no AGENTS.md update
no SKILL.md creation
no eval creation
no automation script
no current-position update
no output_manifest update
no baseline promotion
no workflow/schema/registry/ontology creation
no external dispatch
no platform/API/browser/account/credential action
```

`STATUS: COMPANY_WORK_REVIEW_SEARCH_TEST_COMPLETED_WITH_WATCH`
