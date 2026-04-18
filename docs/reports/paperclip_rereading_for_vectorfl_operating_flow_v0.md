# paperclip rereading for vectorfl operating flow v0

## 1. verdict

이번 재읽기의 핵심 판정은 이렇다.

Paperclip는 `예쁜 host shell`이 아니라,  
사용자가 실제로 일을 `찾고 -> 열고 -> 수정하고 -> 재배정하고 -> 기관을 손보고 -> 감사 추적하는`
운용 page grammar를 이미 갖춘 제품이다.

따라서 VectorFL Paper에서 가져와야 하는 것은
시각 톤보다 먼저 이 `operable page grammar`다.

## 2. what was misread before

이전에는 Paperclip를 다음처럼 얕게 읽었다.

- sidebar/frame 분위기
- detail shell 감각
- list/detail 톤
- host shell reference

하지만 이번에 다시 읽어보면, 실제 핵심은 아래였다.

- `Issues`는 단순 목록이 아니라 live work triage page
- `IssueDetail`은 단순 보기 화면이 아니라 run/comment/document/workspace가 합쳐진 work detail page
- `IssueProperties`는 side note가 아니라 reassignment / retagging / rebinding control surface
- `AgentDetail`은 보기 페이지가 아니라 instructions/configuration/skills/runs/budget를 수정하는 operable node page
- `Inbox`는 보조 convenience가 아니라 operator triage page
- `Activity`는 strip이 아니라 append-only audit page

즉 Paperclip의 native line은 `graph`가 아니라
`list -> detail -> inspector -> operable node page -> audit`
연쇄다.

## 3. why this matters for VectorFL Paper

사용자가 지금 터미널에서 실제로 하는 일은 대체로 아래 흐름이다.

1. 자료를 넣는다
2. 내가 읽게 한다
3. md 여러 개가 생긴다
4. 사용자가 다시 md를 열어 맥락을 붙인다
5. 내부 자료를 다시 끌어온다
6. 다음 지시를 내린다
7. 다시 처리한다
8. 결과를 비교하고 잠근다

VectorFL Paper의 목적은 이 수작업을
한 제품 표면의 operable flow로 끌어올리는 것이다.

그러므로 Paperclip를 다시 읽을 때도
`이 page class가 이 수작업 중 무엇을 제품 안에서 가능하게 하는가`
를 기준으로 읽어야 한다.

## 4. native page grammar reread

### 4-1. work list page

근거:

- [Issues.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Issues.tsx)
- [IssuesList.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/IssuesList.tsx)

읽힘:

- 현재 들어온 work object를 찾는다
- search / filter / group / board-list 전환을 한다
- row 수준에서 assignee/state를 바꾼다
- live issue와 non-live issue를 같은 작업면에서 본다

VectorFL 쪽 의미:

- 새 source/case가 들어왔을 때 무엇을 먼저 잡아야 하는지 정하는 시작면

### 4-2. work detail page

근거:

- [IssueDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/IssueDetail.tsx)

읽힘:

- 하나의 work object를 중심에 놓고
- comment thread
- documents
- workspace
- live run
- timeline/event
- inline editing
을 한곳에서 다룬다

VectorFL 쪽 의미:

- source 하나에 대해
  `원본 -> 분절 -> line -> translation -> recall -> next action`
  을 중심면에서 다루는 page class가 필요하다는 뜻

### 4-3. right-side inspector

근거:

- [IssueProperties.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/components/IssueProperties.tsx)

읽힘:

- assignee를 바꾼다
- project를 바꾼다
- labels를 바꾼다
- linked workspace와 metadata를 읽는다

핵심:

- inspector는 요약면이 아니다
- 현재 선택 object의 다음 이동과 속성 변경을 실제로 수행하는 control surface다

VectorFL 쪽 의미:

- 선택된 line이나 case 뒤에
  `internal linkage / handoff / adoption / routing`
  을 실제로 조정할 수 있는 inspector가 필요하다

### 4-4. operable node page

근거:

- [AgentDetail.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/AgentDetail.tsx)

읽힘:

- dashboard
- instructions
- configuration
- skills
- runs
- budget

이 탭 구조로 agent 자체를 수정한다.

핵심:

- 이 페이지는 agent label viewer가 아니다
- instructionsFilePath/prompt/config/runtime policy를 손보는 운용 페이지다

VectorFL 쪽 의미:

- organ/team/lane도 detail drill-in이 아니라
  `role md / task md / caution md / output schema / enabled flag / notes`
  를 수정할 수 있는 operable page여야 한다

### 4-5. triage page

근거:

- [Inbox.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Inbox.tsx)

읽힘:

- 내가 만져야 하는 것만 모은다
- approvals
- failed runs
- alerts
- touched issues
를 한 triage model로 묶는다

VectorFL 쪽 의미:

- 모든 것을 same list로 보는 게 아니라
  `지금 operator가 먼저 개입해야 하는 것`
  을 따로 모은 triage 면이 필요하다

### 4-6. audit page

근거:

- [Activity.tsx](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/ui/src/pages/Activity.tsx)

읽힘:

- append-only stream을 별도 page로 둔다
- entity filter가 있다
- list + divider 중심이다

VectorFL 쪽 의미:

- trace는 하단 strip 보조면이 아니라
  별도 audit page class가 필요하다

## 5. where this meets VectorFL principles

이번 재읽기로 더 분명해진 접점은 아래다.

- Paperclip의 `work list`는 VectorFL의 `Cases`
- Paperclip의 `work detail`는 VectorFL의 `Case Detail`
- Paperclip의 `right-side properties inspector`는 VectorFL의 `Inspector / Routing`
- Paperclip의 `AgentDetail`는 VectorFL의 `Organ / Lane Editor`
- Paperclip의 `Activity`는 VectorFL의 `Trace Audit`

즉 가져와야 하는 것은 page class다.

반대로 그대로 가져오면 안 되는 것은 아래다.

- company / issue / agent ontology
- assignment-first canonical semantics
- board governance를 reading governance로 착각하는 것

## 6. why intake matters before surface

이번 재읽기에서 다시 확인된 중요한 점은,
좋은 shell만으로는 충분하지 않다는 것이다.

work detail page가 제대로 작동하려면
detail 안에 들어갈 대상이 이미 충분히 두꺼워야 한다.

즉:

- source가 무엇인지
- 왜 그렇게 분절했는지
- 어떤 block이 line-ready material인지
- weak/fallback가 무엇인지
- line이 source/family/directive/history와 어떻게 붙는지

가 먼저 살아 있어야 한다.

그래서 입력기를 손봐야 하는 이유는
보기 좋게 split하기 위해서가 아니라,
case detail과 inspector에서
`line recall/translation/expansion`
이 실제로 가능해지게 만들기 위해서다.

## 7. practical reading rule from now on

앞으로 Paperclip를 읽을 때는 아래 질문으로 읽어야 한다.

- 이 page는 어떤 수작업을 앱 안으로 끌어오는가
- 이 page는 무엇을 실제로 수정 가능하게 하는가
- 이 page는 다음 handoff를 어디서 조정하게 하는가
- 이 page는 append-only audit를 어떻게 분리하는가
- 이 page는 상세/속성/기관 수정이 어떻게 나뉘는가

즉 `무엇처럼 보이는가`보다
`무엇을 operable하게 만드는가`를 먼저 본다.

## 8. final sentence

이번 재읽기의 결론은 다음 문장으로 잠근다.

`Paperclip는 VectorFL에 스타일을 주는 참조가 아니라, 사용자가 지금 터미널에서 수작업으로 하는 흐름을 list/detail/inspector/editor/audit page class 안으로 끌어오는 operable host grammar다. 그리고 이 host grammar가 제대로 작동하려면 입력기와 line recall layer가 먼저 두꺼워져야 한다.`
