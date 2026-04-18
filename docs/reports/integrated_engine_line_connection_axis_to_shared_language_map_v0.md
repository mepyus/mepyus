# Integrated Engine Line / Connection / Axis to Shared Language Map v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

이 문서는 현재까지 나온 번역/증폭 데이터를 line / connection / axis / shared grammar candidate로 재분류한다.

이 문서는 final glossary, UI copy, wording patch, scaffold 수정, manifest/read-map 변경, external style guide, 새 기능을 만들지 않는다.

## 1. map reading rule

각 행은 다음 흐름으로 읽는다.

```text
internal source expression
-> human-readable line form
-> repeated connection
-> emerging axis
-> shared operational meaning
-> usable actors
```

여기서 human-readable line form은 최종 사용자 문구가 아니다. 내부 의미를 인간이 따라갈 수 있게 만든 line이다.

## 2. shared language map

| internal source expression | human-readable line form | repeated connection | emerging axis | shared operational meaning | usable by which actors |
|---|---|---|---|---|---|
| `request / return / reflux` | 요청은 raw intent가 아니라 shaped route이고, return은 final completion이 아니라 validation 대상이며, reflux는 성숙 재료를 space로 되돌리는 route다. | S1 normal loop, protocol, lexicon, friction audit에서 반복 | route grammar axis | 작업은 요청-처리-완료가 아니라 request -> return -> validation/reflux로 순환한다. | User, VectorFL, Engine-side operators, Codex |
| `follow-up / reprocess / rewind` | follow-up은 새 요청처럼 보일 수 있지만 원인 신호가 있고, reprocess/rewind는 실패가 아니라 구조적 되감김이다. | S2 follow-up, S3 drift, protocol reprocess note | correction route axis | route는 정상 진행만 하지 않고 maturation signal이나 drift reason으로 다시 열린다. | User, VectorFL, Engine-side operators, Codex |
| `anchor drift` | anchor와 맞지 않으면 다음 단계로 넘기지 않고 멈추거나 되감는 신호다. | S3 drift observation, bridge lexicon, grammar candidate | operational brake axis | anchor는 설명문이 아니라 route를 제동하는 기준이다. | VectorFL, User, Codex, Engine-side operators |
| `current_loop_state` | 지금 loop가 어디에 있는지 알려주지만 전체 history는 아니다. | protocol note, render contract, bridge lexicon | minimal state axis | 현재 위치와 전체 이력을 분리해서 읽는다. | User, VectorFL, Engine-side operators, Codex |
| `return validation` | engine output은 바로 완료가 아니라 VectorFL validation을 거쳐 다음 route가 정해진다. | S1/S3 friction, grammar candidate, bridge seed | validation ownership axis | execution과 validation 권위를 분리한다. | VectorFL, Engine-side operators, User, Codex |
| `proposal-only / needs Codex translation` | Gemini material은 가치가 있어도 core로 바로 들어가지 않고 Codex baseline translation을 거친다. | handoff artifact, bridge lexicon, guide trial round 2 | proposal-to-core boundary axis | proposal value와 canonical authority를 분리한다. | Gemini, Codex, User, VectorFL |
| `workspace ownership` | 파일 위치는 단순 폴더가 아니라 artifact authority와 write boundary를 표시한다. | real handoff retention, guide trial, high-risk note | workspace authority axis | 어디에 있느냐는 무엇을 할 수 있느냐와 연결된다. | Codex, Gemini, User, 내부팀 |
| `hold / watch keep / not promoted` | 보이지만 아직 행동으로 열지 않는다. 버림도 아니고 patch queue도 아니다. | use-state refresh, wording watch, lexicon v1 | active non-action state axis | 현재 닫힌 상태와 미래 관찰 가능성을 동시에 보존한다. | User, VectorFL, Codex, 내부팀 |
| `collision stop / reject-conflict` | 계속하면 보호 경계를 넘기 때문에 멈추거나 현재 core와 충돌로 분류한다. | handoff artifact, translation bridge, retention check | boundary protection axis | stop/reject는 실패가 아니라 현재 route의 안전 경계다. | Codex, Gemini, User, VectorFL |
| `support reread recovery` | 첫 읽기가 얇아도 support material을 순서대로 읽으면 route/authority가 회복될 수 있다. | S2 observation, use observation protocol, grammar candidate | reread recovery axis | 모든 얇음이 patch나 feature gap은 아니다. | User, VectorFL, Codex |
| `central panel gravity` | 각 surface는 다른 중심 질문을 가진다. | visual rounds, render contract, use observation | surface gravity axis | user는 운영, VectorFL은 숙성/중재, engine은 실행/반환 중심을 유지한다. | User, VectorFL, Engine-side operators, Codex |
| `design clay` | Gemini design output은 바로 구조가 아니라 번역 가능한 raw material이다. | Gemini mock analysis, handoff artifact, explanation trial | proposal material axis | 시각적 강도와 구조 권위를 분리한다. | Gemini, Codex, VectorFL, User |

## 3. strongest repeated connections

가장 강하게 반복된 연결:

1. `request / return / reflux`와 route grammar
2. `return validation / anchor drift / reprocess`와 validation brake
3. `proposal-only / needs Codex translation / workspace ownership`과 authority boundary
4. `hold / watch keep / not promoted`과 active non-action state
5. `support reread recovery / fixture-scope / trace boundary`와 use-mode reading

## 4. emerging shared grammar candidates

현재 shared grammar 후보:

### 4.1 reasoned route grammar

Route는 source, target, purpose, reason, validation status를 가진다.

### 4.2 scoped authority grammar

Authority는 surface, workspace, user package-opening decision에 의해 결정된다.

### 4.3 active non-action grammar

Hold/watch/not promoted는 아무것도 하지 않는 상태가 아니라, 행동을 열지 않으면서 읽을 수 있게 보존하는 상태다.

### 4.4 operational brake grammar

Anchor drift, collision stop, reject/conflict는 failure가 아니라 protected boundary를 지키는 제동 신호다.

### 4.5 support reread grammar

첫 읽기가 얇은 것은 patch 근거가 아니다. route/authority/state/boundary가 support reread로 회복되는지 먼저 본다.

## 5. actor usability summary

| actor | most usable shared grammar |
|---|---|
| User | reasoned route, active non-action, package-opening authority |
| VectorFL | validation brake, support reread, line/connection/axis mediation |
| Engine-side operators | shaped input, execution state, return material, reprocess route |
| Codex | baseline translation, workspace authority, conflict/carry-forward classification |
| Gemini | proposal-only, design clay, no direct-to-core path |
| 내부팀 | surface exposure density, shared grammar boundary, interface axis |

## 6. map closeout

이 map은 final glossary가 아니다.

이 map은 내부 source expression이 인간 가독 line으로 올라오고, 반복 연결을 거쳐 axis가 되며, 여러 주체가 같이 쓸 수 있는 shared operational language가 되는 경로를 보여준다.
