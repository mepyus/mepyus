# Ralph Overlay Prototype v1

## 목적

이 문서는 `references/git_search/ralph-main` 를 기능 기준으로 읽고,
그 제품 위에 우리 공간을 덧씌우는 것이 아니라
우리 공간을 바닥 커널로 두고 Ralph의 loop shell만 빌려오는
prototype 구성을 정의한다.

핵심 질문은 하나다.

- `fresh-context task loop` 를 유지하면서
  `prd.json + progress.txt` 대신
  우리 line-aware memory spine을 바닥으로 둘 수 있는가

판단은 `가능` 이다.

## Ralph가 이미 주는 것

Ralph의 핵심은 매우 얇다.

- bounded iteration loop
- 한 번에 하나의 task만 집는 규율
- fresh context 실행
- 완료 신호가 있을 때만 종료
- branch 단위 archive reset

즉 Ralph는 `작업 루프 shell` 에 가깝고,
기억이나 판정 구조는 거의 없다.

실제 기억층은 아래 셋뿐이다.

- `prd.json`
- `progress.txt`
- git history

이 얇음이 prototype에 유리하다.

## 우리 공간이 대체하는 층

Ralph의 기본 기억층을 아래처럼 치환한다.

### 1. `prd.json` -> line-bound work registry

Ralph의 `userStories[]` 는 그대로 쓸 수 있지만
저장 위치와 의미를 바꾼다.

- 기존 의미:
  단순 task backlog
- overlay 의미:
  특정 line에 귀속된 bounded work unit registry

최소 필드는 아래가 맞다.

- `id`
- `title`
- `line_id`
- `corridor`
- `priority`
- `status`
- `acceptance_criteria`
- `evidence_refs`
- `promotion_gate`
- `notes`

즉 `passes: true/false` 만으로 끝내지 않고,
무슨 line을 두껍게 하는 일인지까지 붙인다.

### 2. `progress.txt` -> append-only operation ledger + summary surface

Ralph의 `progress.txt` 는 사람이 읽는 로그 한 장이다.
우리 공간에서는 둘로 나눈다.

- append-only ledger
- current readable surface

대응 관계는 아래와 같다.

- progress append
  -> [breadcrumbs.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/breadcrumbs.jsonl)
- reusable pattern section
  -> line source / reread residue / promotion note
- current run summary
  -> observer-readable board or summary markdown

즉 원장은 append-only로 남기고,
현재 읽기면은 재합성한다.

### 3. completion 판단 -> promotion/archive/continue gate

Ralph는 story 하나가 끝나면 `passes: true` 로 올리고,
전체가 끝나면 `<promise>COMPLETE</promise>` 를 출력한다.

우리 쪽에서는 중간 판정을 더 둔다.

- `continue`
- `retain as residue`
- `promote as reusable pattern`
- `complete`

즉 실행 결과를 바로 완료로 보지 않고,
observer reread를 한 번 더 통과시킨다.

## Overlay 구조

### base kernel

우리 공간이 바닥으로 제공하는 것은 아래다.

- line memory
- append-only operation ledger
- observer reread surface
- promotion governance
- runtime/generated separation

이때 이미 있는 자산을 그대로 쓴다.

- [runtime/current_phase.json](/Users/sungsookim/universe/vectorfl_replica/runtime/current_phase.json)
- [runtime/preflight_last_decision.json](/Users/sungsookim/universe/vectorfl_replica/runtime/preflight_last_decision.json)
- [runtime/breadcrumbs.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/breadcrumbs.jsonl)
- [runtime/logs/reread_observation_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/logs/reread_observation_log.jsonl)
- [runtime/logs/line_promotion_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/logs/line_promotion_log.jsonl)

### borrowed shell

Ralph에서 빌릴 것은 아래뿐이다.

- fresh-context 반복 실행
- highest-priority incomplete unit 선택
- bounded max iteration
- explicit completion token

### new connective layer

이 prototype에서 새로 필요한 것은 아래다.

- work registry reader
- run capture adapter
- post-run reread adapter
- decision gate writer

즉 Ralph loop와 우리 runtime ledger 사이를 잇는 얇은 bridge다.

## 최소 프로토타입 파일 구조

실제 prototype은 아래 정도면 충분하다.

- `runtime/manifests/ralph_overlay_work_registry.json`
- `runtime/logs/ralph_overlay_run_log.jsonl`
- `runtime/logs/ralph_overlay_decision_log.jsonl`
- `runtime/views/ralph_overlay_current_board.md`
- `docs/reviews/ralph_overlay_prototype_v1.md`

여기서 중요한 건 새 제품용 폴더를 크게 만드는 게 아니라,
현재 runtime 계약 안에서 얇게 붙이는 것이다.

## 실행 사이클

### step 1. pick next work unit

registry에서 아래 조건의 항목 하나를 집는다.

- `status != complete`
- highest priority
- line_id가 지정됨

### step 2. fresh-context run

Ralph shell처럼 새 컨텍스트에서 한 번 실행한다.

이때 프롬프트는 아래만 본다.

- 현재 work unit
- 관련 acceptance criteria
- 필요한 최소 line summary
- 직전 residue/pattern summary

즉 전체 히스토리를 다시 싣지 않는다.

### step 3. capture operation record

실행 후 아래를 남긴다.

- changed files
- checks run
- raw completion claim
- operator summary
- linked evidence refs

### step 4. reread

observer 또는 post-run reader가 실행 결과를 다시 읽는다.

질문은 아래다.

- 이 실행이 실제로 해당 line을 두껍게 했는가
- reusable pattern이 나왔는가
- residue로 남겨야 할 실패/보류가 있는가
- acceptance criteria가 정말 충족됐는가

### step 5. gate decision

판정은 아래 넷 중 하나다.

- `continue`
- `retain_residue`
- `promote_pattern`
- `complete`

### step 6. update current surface

원장은 append-only로 두고,
현재 board만 재렌더한다.

## 왜 Ralph가 1차 prototype로 맞는가

세 가지 이유가 있다.

- 제품이 얇아서 우리 공간이 바닥을 차지하기 쉽다
- task loop가 단순해서 line-bound work unit 실험에 적합하다
- `progress.txt` 의 한계를 우리 append-only ledger 구조가 바로 대체할 수 있다

즉 Paperclip이나 OpenClaw보다 훨씬 작은 비용으로
`외부 제품 기능 + 우리 memory kernel` 결합을 검증할 수 있다.

## prototype 성공 기준

이 prototype은 아래가 되면 성공이다.

- work unit가 line 귀속으로 선택된다
- 한 번의 fresh run 뒤에 observer reread가 붙는다
- 진행 기록이 plain text 하나가 아니라 ledger + board로 나뉜다
- 완료 판단이 단순 done이 아니라 promotion gate를 통과한다

## 범위 밖

이번 v1에서 하지 않는 것은 아래다.

- multi-agent 조직 모델
- multi-channel ingress
- budget enforcement
- browser control plane

이건 각각 OpenClaw, Paperclip 단계에서 붙이는 것이 맞다.

## 결론

Ralph는 제품 전체를 가져올 대상이 아니라
`fresh-context autonomous loop shell` 로 가져올 대상이다.

우리 공간은 그 아래에서
`memory spine`, `observer reread`, `promotion gate`, `active surface`
를 맡는다.

따라서 첫 prototype은 아래 문장으로 요약된다.

- `Ralph loop over vectorfl memory spine`
