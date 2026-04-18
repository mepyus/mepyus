# vectorfl operable surface set lock v0

이 문서는 `surface-only paperclip adoption` 이후  
실제로 먼저 세워야 할 VectorFL 운영화면 세트를 잠근다.

## 1. core sentence

첫 실제 운영화면 세트는 아래 여섯 class로 잠근다.

1. `Cases`
2. `Case Detail`
3. `Case Inspector`
4. `Organs`
5. `Organ Detail`
6. `Trace Audit`

이 세트는 기존 graph-like shell 보정이 아니라  
Paperclip native page class를 기준으로 한 `operable surface reset`이다.

## 2. purpose

이 세트의 목적은 아래 셋을 동시에 만족하는 것이다.

- VectorFL core semantics 유지
- Paperclip native page grammar 계승
- operator가 실제로 case/organ/trace를 다룰 수 있는 화면 class 확보

## 3. page meanings

### Cases

- work list page
- current organ / lane / restriction / next-hop가 row에서 보인다

### Case Detail

- current-reading 중심 work detail page
- progression, trace carry, linked programs가 한 detail 안에 묶인다

### Case Inspector

- right-side inspector class를 독립적으로 읽게 만든 control surface
- governance, source/context, next-hop candidate를 다룬다

### Organs

- organ management list page
- 기관을 목록과 상태, 책임 요약 기준으로 다룬다

### Organ Detail

- operable organ page
- ROLE / HANDOFF / CAUTION / RETURN bundle을 본다
- 이후 실제 save/cancel/edit flow가 이 class 위에 붙는다

### Trace Audit

- append-only audit page
- trace row와 detail drill-in을 별도 class로 유지한다

## 4. first implementation note

첫 구현에서는 live edit runtime까지 넣지 않더라도,  
적어도 page class와 operator action entry는 분명해야 한다.

즉:

- graph center panel 재활용이 기준이 아니다
- work list/detail/inspector/organ/audit class가 먼저 읽혀야 한다

## 5. final lock sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL의 첫 operable surface set은 Cases, Case Detail, Case Inspector, Organs, Organ Detail, Trace Audit 여섯 class를 먼저 세우고, 이 세트 위에서만 이후 live edit, handoff adjustment, organ assignment, trace drill-in을 확장한다.`
