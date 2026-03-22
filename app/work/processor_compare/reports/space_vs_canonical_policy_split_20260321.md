# space vs canonical policy split

## 1. purpose
- 이 문서는 `정확한 승인 기준`과 `공간으로 받아들이는 기준`을 분리하기 위한 정책 초안이다
- 목적은 가능성을 너무 일찍 자르지 않으면서도, canonical 승인은 여전히 엄격하게 유지하는 것이다
- 즉 이 문서는 `정답 승인 문법`과 `space 형성 문법`을 분리해 고정한다

## 2. core split

### canonical approval grammar
- canonical은 강한 승인 상태다
- canonical은 direct corroboration 과 family-level corroboration 이 실제로 닫힌 경우에만 인정한다
- translated hit, proposal, token-supported candidate 만으로는 canonical로 올리지 않는다

### space grammar
- space는 canonical보다 넓은 층위다
- 약한 연결, review lane, pre-entry, blocked but meaningful 상태도 space 안에 포함될 수 있다
- 즉 canonical이 아니어도 space를 형성할 수 있다

## 3. space recognition criteria
- 아래 중 일부가 충족되면 space 형성 후보로 인정한다
  - weak trace 가 존재한다
  - 갈래 하나 이상이 다른 갈래를 실제로 연다
  - translation / processing / observer / family support 중 일부가 실제로 작동한다
  - blocker 가 있더라도 왜 막혔는지가 구조적으로 남아 있다
  - future accumulation 으로 다시 읽힐 수 있다

## 4. canonical approval criteria
- 아래가 실제로 닫혀야 canonical 승인 후보가 된다
  - cross-path direct overlap
  - family corroboration
  - canonicalizable quality
  - same-local support 가 cross-path direct corroboration 으로 이어짐
- 아래는 canonical 승인의 대체가 아니다
  - translated hit
  - proposal trace
  - token-supported candidate
  - internal support density

## 5. engine tier reading
- `none`
  - 아직 space 형성 전
- `possibility`
  - 약한 space 형성
- `review candidate`
  - 구조적으로 의미 있는 space 형성
- `space pre-entry`
  - space 초입
- `canonical`
  - 승인된 강한 연결

## 6. practical reading rule
- `canonical이 아니면 버린다` 는 금지한다
- `blocked 상태라도 space 자산이면 남긴다`
- `review lane` 은 실패가 아니라 구조적 보류 자산이다
- `pre-entry` 는 승인 직전이 아니라, 이미 space 형성의 일부로 본다

## 7. current repo mapping

### canonical approval side
- `canonical`
- `direct canonical overlap`
- `cross_path canonical corroboration`
- `canonical_anchor_gate`

### space side
- `possibility_candidate`
- `promotion_review`
- `proposal trace`
- `direct overlap candidate`
- `space_entry_state`
- `blocker`
- `control trace`

## 8. doc_006 reading under this policy
- `doc_006`은 아직 canonical은 아니다
- 하지만 아래를 만족하므로 space 쪽에서는 이미 인정된다
  - translation gate 통과
  - processing gate 통과
  - observer gate 통과
  - same-local_ref multi-family support 존재
  - direct overlap candidate family 존재
  - `space_entry_state = structural_led_space_pre_entry`
- 따라서 `doc_006`은
  - canonical 미승인 상태이면서
  - space 형성 상태로는 유효한 후보다

## 9. control reading
- `doc_005`, `doc_004`는 현재 `translation_missing`
- 따라서 아직 review lane 미도달
- 이들은 현재 space 형성 후보보다 더 앞단의 control로 유지한다

## 10. operating principle
1. 승인은 좁게 간다
2. space 인정은 넓게 간다
3. weak / loose / blocked 상태를 너무 빨리 삭제하지 않는다
4. 결과보다 과정과 층위를 남긴다
5. canonical은 마지막 승인층이지, 유일한 공간 인정 층이 아니다

## 11. implication for next phase
- 다음 phase에서 다뤄야 할 것은
  - space를 더 넓게 인정할 정책
  - canonical approval 을 유지한 채 review / pre-entry / deferred asset 을 정식 space 층위로 읽는 정책
- 즉 다음 phase는
  - `family canonicalization rule refinement`
  - 와 동시에
  - `space recognition grammar formalization`
  를 함께 다루는 것이 맞다

## 12. final sentence
- 앞으로는 `이게 정답 연결인가?` 와 `이게 space를 이루는가?` 를 분리해서 본다
- 전자는 좁고 엄격하게,
- 후자는 더 넓고 가능성 중심으로 읽는다
