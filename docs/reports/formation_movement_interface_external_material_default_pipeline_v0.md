# Formation-Movement Interface External Material Default Pipeline v0

## 1. status

```yaml
status: default_pipeline_candidate
focus: external_material_front_door
verdict: PASS_WITH_NOTE
purpose: compress the formation_movement assets into one practical default flow for external material input
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
```

## 2. one-line purpose

When external material enters, the user should not have to choose the route.

The default pipeline should do this:

```text
input
→ space reads first
→ existing lines/lenses are checked
→ Codex stays in interpreter/output mode unless worker-role elevation is needed
→ output returns to space
→ user sees a 4-line card
```

## 3. user-facing contract

The user can say only:

```text
이거 넣어봐.
```

or:

```text
이 링크 공간 기준으로 읽어봐.
```

The user does not need to say:

- use `unclassified seed`
- check `direct evidence / defensive logic / comparison frame`
- elevate Codex to bounded comparer
- do validation return
- create a cluster note

Those are internal operations.

## 4. default external-material pipeline

## 4.1 step 1. receive input

### internal action

Capture the material as:

```text
unclassified seed
```

### user-facing meaning

```text
아직 무엇인지 확정하지 않고 받는다.
```

### guardrail

Do not treat entry as:

- evidence
- task
- doctrine
- execution trigger

## 4.2 step 2. space reads first

### internal action

Before classification, check:

- which existing line it touches
- whether it is formation-side first or movement-side first
- which lens is most useful at entry
- whether it needs more ripening

### user-facing meaning

```text
먼저 우리 공간에서 어디에 닿는지 본다.
```

### guardrail

Do not ask the user to choose the line or lens.

## 4.3 step 3. assign safe temporary state

### internal action

Choose one:

```text
reread_priority
framing_candidate
hold / archive_as_residue
```

### user-facing meaning

```text
더 읽을지, 비교재료로 둘지, 보류할지 정한다.
```

### guardrail

Do not jump to:

- direct evidence
- baseline
- operating rule
- execution

## 4.4 step 4. decide whether Codex worker-role elevation is needed

### internal action

Default:

```text
Codex interpreter/output mode only
```

Elevate Codex only if:

- bounded comparison is needed
- contrastive reread is useful
- scene-by-scene contact map is needed
- output shape can be constrained

Then:

```text
elevate Codex to bounded comparer
```

### user-facing meaning

```text
기본 해석/출력 모드에 머물고, 필요할 때만 비교기 역할로 승격한다.
```

### guardrail

Do not elevate Codex into:

- executor
- doctrine importer
- evidence confirmer

## 4.5 step 5. if Codex is elevated, return output to space

### internal action

Codex output must return as:

```text
validation_return / reread material
```

Then space rereads:

- line contact
- axis contact
- lens fit
- next state

### user-facing meaning

```text
Codex 출력도 답이 아니라 다시 읽을 재료다.
```

### guardrail

Do not treat Codex output as final.

## 4.6 step 6. place in space

### internal action

Place the result as one of:

- reusable comparison object
- reread support material
- hold object
- archive_as_residue
- bounded action seed

### user-facing meaning

```text
공간 안에서 나중에 다시 쓸 위치를 정한다.
```

### guardrail

Do not store every material as a new doctrine-like note.

## 4.7 step 7. return 4-line card

### default output

```text
현재 판정:
이유:
다음 이동:
금지선:
```

### user-facing meaning

```text
지금 이 자료를 어떻게 다룰지만 짧게 알려준다.
```

## 5. minimal checklist

Use this internally for every external material input:

- [ ] Did space read before classification?
- [ ] Did we check existing lines/lenses?
- [ ] Did we avoid evidence lock?
- [ ] Did we avoid execution?
- [ ] Did we decide whether Codex worker-role elevation is actually needed?
- [ ] If Codex was elevated, did output return to space?
- [ ] Did the final user output stay as a 4-line card?

## 6. default outputs by state

### if `reread_priority`

```text
현재 판정: 더 읽을 자료
이유: 유용해 보이지만 아직 어떤 역할인지 불명확함
다음 이동: 기존 line/lens와 더 대조
금지선: 증거화 / 실행 / baseline 반영 금지
```

### if `framing_candidate`

```text
현재 판정: 비교재료 후보
이유: 기존 라인과 닿는 역할은 보이지만 직접 증거는 아님
다음 이동: 필요한 장면에서 compare_only로 사용
금지선: direct evidence lock / doctrine 채택 금지
```

### if Codex is elevated to bounded comparer

```text
현재 판정: bounded comparison 진행
이유: 자료가 특정 내부 장면과 대조될 만큼 안정됨
다음 이동: Codex 비교 결과를 validation_return으로 회수
금지선: 비교 결과를 final이나 evidence로 취급 금지
```

### if placed in space

```text
현재 판정: 공간 내 재사용 비교 객체
이유: 반복 재분류를 줄이고 특정 line/lens에서 다시 쓸 가치가 있음
다음 이동: 관련 장면에서 reread support로 사용
금지선: baseline / operating rule 승격 금지
```

## 7. applied example: agent-skills + Flutist

### user input

```text
이 두 링크 넣어봐.
```

### default pipeline result

```text
입력
→ unclassified seed
→ process-first line check
→ agent-skills = workflow / validation / bounded preparation grammar
→ Flutist = architecture boundary / rules-as-code / check-without-mutate grammar
→ merged framing_candidate
→ external governance-architecture comparison cluster
→ interpreter/output mode at entry
→ bounded comparer elevation only if bounded compare is needed
→ 4-line card
```

### final card

```text
현재 판정: external governance-architecture comparison cluster
이유: 두 자료 모두 구조/경계/검증을 강하게 비추지만, 직접 증거라기보다 재사용 가능한 비교재료임
다음 이동: prepare / ingest / validation 장면에서 compare_only로 사용
금지선: direct evidence lock / 외부 workflow 수입 / baseline 반영 금지
```

## 8. why this is the front-door version

The older assets remain useful, but they should mostly stay behind the pipeline.

The user should not have to see:

- all sidecar fields
- all validation history
- all weak-signal thresholds
- all route mapping details

unless escalation is needed.

The front-door behavior should be:

```text
short input
→ internal pipeline
→ compact card
```

## 9. remaining limits

This default pipeline is clearer, but still provisional.

Open limits:

- when exactly to elevate from `interpreter/output mode` to `bounded comparer`
- when a material should stay `reread_priority` instead of `framing_candidate`
- how much lens detail should be shown to the user
- when a placed space object should later become an action seed

## 10. final judgment

Compressed judgment:

```text
외부자료 처리의 앞단은 이제 이 pipeline 하나로 줄일 수 있다.
지금까지 만든 package/validation/controller 문서는 이 pipeline 뒤에서 작동하는 내부 기준으로 두는 것이 맞다.
```

Overall verdict:

`PASS_WITH_NOTE`
