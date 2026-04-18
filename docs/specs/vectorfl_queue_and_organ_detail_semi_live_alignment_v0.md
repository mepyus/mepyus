# VectorFL Queue And Organ Detail Semi-Live Alignment v0

이 문서는 `Cases / Queue`와 `Organ Detail`도  
같은 runtime bridge 위에서 더 현재 상태에 맞게 읽히도록 맞추는 기준을 잠근다.

목적은 queue, current-reading, programs/connections, organ detail이
서로 다른 fixture 현실을 가리키지 않게 하고,
하나의 semi-live current state를 서로 다른 면에서 읽는 구조로 맞추는 것이다.

## 1. Core Sentence

Queue와 Organ Detail도
Current Reading과 같은 runtime source를 참조하되,
queue는 `current asset spread + caution density + linked evidence`를,
organ detail은 `current organ role + accepted carry + active caution`을
더 현재 상태에 가깝게 보여줘야 한다.

## 2. Queue Alignment Rule

- queue row는 headline/status만이 아니라
  - saved connection count
  - attention flag
  - recent update flag
  를 같이 가질 수 있다

## 3. Organ Detail Alignment Rule

- organ detail은 fixture role 문법을 유지하되
  - current phase
  - runtime restrictions
  - current candidate count
  - recent trace carry
  같은 semi-live summary를 덧붙일 수 있다

## 4. What Must Not Drift

- queue가 generic metric board가 되는 것
- organ detail이 live manager console이 되는 것
- current-reading와 다른 현실을 가리키는 독립 surface가 되는 것

## 5. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 semi-live 단계에서는 Queue와 Organ Detail도 Current Reading과 같은 runtime bridge를 참조해 같은 현재 상태를 다른 각도에서 읽게 해야 하며, queue는 spread preview, organ detail은 responsibility preview로만 강화하는 것이 맞다.`
