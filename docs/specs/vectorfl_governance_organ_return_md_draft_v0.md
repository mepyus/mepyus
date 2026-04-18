# Governance Organ RETURN.md Draft v0

## return purpose

Governance organ의 반환은  
현재 무엇이 보류되고 무엇이 아직 열리지 않아야 하는지,  
그리고 언제 다시 확인할 수 있는지를 current-reading과 다음 기관이 같이 읽게 하는 것이다.

즉 반환의 목적은:

- hold state를 분명히 하고
- restriction을 숨기지 않고
- release condition과 next check trigger를 남기고
- trace/reentry와 current-reading을 끊지 않는 것이다

## minimum return blocks

### 1. governance caution

- 현재 왜 caution이 필요한지
- 예:
  - "Direct presentation remains held until transition closure is rechecked."

### 2. restriction set

- observer_only
- promotion_forbidden
- closure_before_presentation
- direct_action_hold

### 3. release condition

- 무엇이 충족되어야 다음 단계로 넘어갈 수 있는지

### 4. next check trigger

- 언제 다시 reread / review / refresh를 해야 하는지

### 5. current-reading-ready fragment

- current-reading body 옆에 붙일 짧은 caution fragment
- 예:
  - "Readable, but still closure-incomplete."

## preferred wording

- "hold until ..."
- "keep in observer-only ..."
- "do not promote yet ..."
- "recheck when ..."
- "current reading is usable, but ..."

## avoid wording

- "approved"
- "fully ready"
- "safe to proceed" without explicit release condition
- "resolved" when restriction remains

## return example shape

- governance_caution:
  - "Direct presentation remains held until transition closure is rechecked."
- restriction_set:
  - `observer_only`
  - `promotion_forbidden`
  - `closure_before_presentation`
- release_condition:
  - "Confirm transition closure or downgrade to residue-backed operator readout."
- next_check_trigger:
  - "Re-run transition reread after next surface refresh or linked program state change."
- current_reading_ready_fragment:
  - "Readable, but still closure-incomplete."

## handoff note

이 반환은 current-reading surface와 trace/history 면에 같이 걸려야 한다.

그래서 최소한 아래는 빠지면 안 된다.

- restriction set
- release condition
- next check trigger
- current-reading-ready fragment

## final sentence

Governance organ의 반환은 yes/no 승인표가 아니라,  
지금 무엇이 왜 hold인지, 무엇이 아직 금지 상태인지, 언제 다시 확인할 수 있는지를 current-reading과 다음 handoff에 함께 남기는 protection-aware return이어야 한다.
