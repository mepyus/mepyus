# integrated_engine_current_primary_purpose_lock_v0

## 1. Verdict

**PASS_WITH_NOTE**

현재 단계의 우선 판단은 **확장/제품화/자동화 확대보다 현재 1차 용도(current primary purpose) 재고정이 우선**이라는 것이다.

이번 워크트리에서 새로 형성된 자산들은 단순 개념 보강이 아니라, 실제로 **space 안의 재료를 package chain으로 통과시키며 판단 가능한 중간 산출물과 memory 자산으로 남기는 운영 골격**이 형성되었음을 보여준다.  
다만 자산 종류가 빠르게 늘어나면서, 본체 목적과 주변 보조층이 혼합되어 읽힐 위험이 커졌기 때문에 현재 시점에서는 목적 lock이 필요하다.

---

## 2. Locked Current Primary Purpose

현재 통합엔진/OMX/package chain의 1차 용도는 다음과 같이 잠근다.

**들어온 재료와 작업 흔적을 package chain으로 다시 읽고, 그 과정을 candidate, review, memory 수준의 판단 가능한 자산으로 번역하는 운영 구조.**

보다 넓게 말하면, 현재 구조의 1차 용도는 **철학, 기록, 작업 흔적, 외부 참고물, 실행 로그를 단순 저장하거나 즉시 실행하는 것이 아니라, space 안에서 reread/retranslation하여 다음 판단 가능한 중간물과 memory 자산으로 전환하는 것**이다.

이 lock에서 중요한 점은 다음과 같다.

- 공간은 단순 저장소가 아니라 reread/retranslation을 위한 운영 공간이다.
- 엔진은 단순 처리기가 아니라 단계적 변환과 판단 자산 형성을 담당하는 구조이다.
- worker/CLI/외부도구는 본체가 아니라, 이 reread/translation chain을 보조하는 역할 제한된 실행자이다.

---

## 3. Why This Purpose Now

현재 이 목적이 우선인 이유는 다음과 같다.

### 3.1 구현 가능성이 원래 목적을 덮기 시작한 상태

현재 워크트리에는 specs, reports, space packages, runtime logs, OMX state, CLI session, adapter/worker contract, UI/API 자산이 함께 형성되어 있다.  
이 상태에서는 화면, 자동화, worker 확장, supervisor continuation loop 등이 구조의 중심처럼 보이기 쉽다.  
그러나 실제 중심 자산은 그것들이 아니라 **package chain을 통해 재료를 reread하고 판단 자산으로 변환하는 운영 체인**이다.

### 3.2 지금은 더 만드는 단계보다, 이미 만든 것을 무엇에 먼저 쓰는지 고정해야 하는 단계

새 스펙과 리포트 수가 늘어난 것은 구조의 성장이 아니라, 오히려 **현재 구조가 실제로 어떤 용도를 먼저 감당하고 있는지 판독해야 하는 시점**임을 뜻한다.  
지금 이 시점에서 용도를 고정하지 않으면 이후의 확장 논의는 화면 개선, CLI 부착, worker 운영, automation 확대 등으로 쉽게 흘러 기준을 잃게 된다.

### 3.3 현재 자산은 이미 “운영 골격”을 보여주고 있다

이번에 생긴 자산은 철학 메모가 아니라 다음을 보여준다.

- intake bundle이 실제 입력 단위로 다뤄지고 있음
- intake -> digestion -> review -> memory chain이 실제 package로 남고 있음
- candidate/body note가 중간 판단 층을 형성하고 있음
- supervisor/worker contract가 보조 실행자의 경계를 잡고 있음
- runtime events / cli sessions / .omx state가 과정 자체를 운영 자산으로 남기고 있음

따라서 현재 1차 용도는 추상적 비전이 아니라, **이미 워크트리에서 가장 많이 구체화된 실제 운영 기능**으로 봐야 한다.

---

## 4. Asset-Grounded Reading of the Current Worktree

현재 워크트리의 자산 구성은 다음과 같은 실제 중심을 보여준다.

### 4.1 핵심 스펙 자산

`docs/specs` 아래에는 package chain, package record, surfaces, vocabulary minimum, handoff minimum, candidate/body note placement, supervisor handoff, worker adapter prompt contract, worker return normalization policy 등이 형성되어 있다.

이는 현재 구조의 중심이 UI나 개별 실행기가 아니라, **재료를 단계적으로 넘기고 남기기 위한 패키지/핸드오프 규약 체계**임을 보여준다.

### 4.2 핵심 리포트 자산

`docs/reports` 아래에는 manual trial, round comparison, chain audit, example conversion, worker validation, boundary audit, continuation loop validation, normalization hardening, freeze judgment 등이 형성되어 있다.

이는 현재 구조가 단지 설계 중이 아니라, **실제 운용과 검증의 흔적을 남기고 있는 운영 체인**임을 보여준다.

### 4.3 실제 space 자산

`space/intake_bundles`, `space/packages/intake`, `space/packages/digestion`, `space/packages/review`, `space/packages/memory` 아래 실제 package 샘플들이 형성되어 있다.

이는 space가 철학적 은유가 아니라, **재료가 단계적으로 숙성되며 형태를 바꾸는 실제 작업 공간**으로 사용되고 있음을 보여준다.

### 4.4 실행/운영 자산

`runtime/cli_sessions`, `runtime/events/integrated_engine_package_run_events.jsonl`, `.omx` 상태/로그/메트릭 자산은 과정 자체를 운영 기록으로 남기고 있다.

이는 현재 구조의 핵심이 “정답 생산기”가 아니라, **과정과 경계를 추적 가능한 상태로 운영하는 장치**임을 보여준다.

### 4.5 외곽 보조 자산

`app/runtime/vectorfl_integrated_engine_api.py`, `app/ui/integrated_engine/CliHostControlPanel.tsx`, 외부 reference 자산은 현재 chain을 보조하거나 관찰하는 외곽층으로 읽는 것이 맞다.

즉, 코드/화면 자산은 중요하지만 현재 1차 용도 기준에서는 **본체가 아니라 보조 표면**이다.

---

## 5. Role Repositioning of Existing Surfaces

현재 1차 용도 아래에서 각 표면과 도구의 역할은 다음과 같이 재배치한다.

### 5.1 사용자면

사용자면의 현재 역할은 **지시를 많이 내리는 화면**이 아니라,  
**어떤 재료를 현재 reread 대상으로 삼고, 무엇을 다음 판단 단위로 변환하려는지를 세우는 면**이다.

즉, 사용자면은 현재 단계에서 “무엇을 실행할까”보다  
“무엇을 space chain에 태워 reread할까”를 정하는 입구로 읽는 것이 맞다.

### 5.2 VectorFL면

VectorFL면의 현재 역할은 **재료를 공간 언어로 읽고, package chain에 태울 수 있는 중간 형식으로 정리/판독/번역하는 면**이다.

이는 단순 해설 화면이 아니라,  
입력 재료를 intake bundle / package chain / candidate / review / memory 흐름으로 이어지게 하는 해석면이다.

### 5.3 엔진면

엔진면의 현재 역할은 **번역된 입력을 실제 chain 실행, package formation, event logging, state tracking으로 연결하는 처리면**이다.

즉, 엔진면은 단순 계산기가 아니라  
현재 1차 용도 아래에서 **reread chain을 실제 실행 가능한 운영 행위로 바꾸는 면**이다.

### 5.4 CLI / Worker / 외부도구

CLI / worker / 외부도구의 현재 역할은 **본체를 대체하는 자율 조직**이 아니라,  
현재 chain의 일부 단계에서 bounded하게 투입되는 보조 실행자이다.

이 역할 제한은 이미 다음 자산들에서 드러난다.

- integrated_engine_supervisor_handoff_protocol_v0
- integrated_engine_worker_adapter_prompt_contract_v0
- integrated_engine_worker_return_normalization_policy_v0
- worker validation / boundary audit / normalization hardening reports

즉, 현재 단계에서 CLI/worker는 **주인공이 아니라 역할 계약 아래 놓인 노동자층**이다.

---

## 6. What Is Explicitly Not Primary Right Now

다음 항목들은 현재 구조에서 중요할 수는 있으나, **현재 1차 목적은 아니다.**

### 6.1 최종 제품화

현재 자산은 제품 definition lock이 아니라 운영 chain lock에 더 가깝다.  
따라서 완성 제품 기준의 기능 정의, 상품 형태 고정, 브랜드형 구조화는 현재 1차 목적이 아니다.

### 6.2 완성 UI

UI/API 자산이 형성되었더라도, 현재 본체는 package chain과 운영 기록이다.  
화면 정리와 시각적 일관성은 유의미하지만, 현재 1차 목적을 대표하지 않는다.

### 6.3 과도한 자동화

runtime/session/worker 관련 자산이 생겼다고 해서 자동화 확대가 중심이 되는 것은 아니다.  
지금은 자동 실행 확대보다 **bounded chain의 의미와 신뢰성 유지**가 우선이다.

### 6.4 범용 멀티에이전트 플랫폼화

worker contract와 supervisor continuation loop가 존재하더라도, 현재 구조를 범용 멀티에이전트 플랫폼으로 과장해 읽지 않는다.  
지금 구조는 아직 **space reread chain을 지원하는 bounded worker 운용 골격**이다.

### 6.5 구조 과증식

새 layer, 새 naming system, 새 team 체계, 새 runtime/state 분리 확대 등은 현재 1차 목적에 직접 속하지 않는다.  
지금 우선은 확장이 아니라 **현재 자산이 무엇을 위해 존재하는지 고정하는 것**이다.

---

## 7. Practical Decision Filter

앞으로 어떤 작업이 현재 1차 용도에 맞는지 판단할 때는 아래 3축 필터를 사용한다.

### Filter A. reread 기여

이 작업은 내 기록, 작업 흔적, 외부 참고물, 실행 로그를 **더 잘 다시 읽게 해주는가?**

- intake bundle 형성 개선
- package chain 연결성 보강
- candidate/review/memory 해석 일관성 강화
- auditability / traceability 보강

위와 같은 방향이면 현재 1차 용도에 부합할 가능성이 높다.

### Filter B. next-step translation 기여

이 작업은 reread된 결과를 **다음 판단 가능한 자산**으로 번역하게 해주는가?

- intake를 digestion으로 넘기는 명확성
- digestion에서 review candidate를 안정적으로 남기는 방식
- review에서 memory 자산으로 전환하는 기준
- supervisor/worker return을 판단 가능한 형태로 정규화하는 방식

위와 같은 방향이면 현재 1차 용도에 부합한다.

### Filter C. 현재 검증 가능성

이 작업은 **지금 당장 샘플, trial, audit, runtime trace로 검증 가능한가?**

- 실제 package 예시로 확인 가능한가
- manual trial 또는 run event로 확인 가능한가
- boundary / normalization / audit report로 검증 가능한가

현재 단계에서는 “좋아 보이는 큰 방향”보다 **즉시 검증 가능한 bounded 진전**을 우선한다.

---

## 8. Immediate Implication

현재 기준에서 다음에 우선해야 할 작업 성격은 다음과 같다.

### 8.1 확장보다 reread/translation/next-step conversion 강화

우선해야 할 것은 새로운 기능군 추가가 아니라,  
현재 chain이 실제로 **재료를 reread하여 candidate/review/memory 자산으로 전환하는 힘**을 더 선명하게 만드는 일이다.

### 8.2 구조 추가보다 현재 구조의 용도 명확화

현재 스펙과 리포트와 샘플은 이미 충분히 많다.  
지금 필요한 것은 새 구조 제안보다,  
각 자산이 현재 1차 용도 아래에서 왜 존재하는지 더 명확하게 읽는 일이다.

### 8.3 제품화보다 실제 작업 단위 번역 실험

다음 우선 실험은 완성 UI나 자동화 시나리오가 아니라,  
실제 입력 재료가 intake -> digestion -> review -> memory로 넘어가며 **판단 가능한 중간물**을 안정적으로 남기는지 반복 검증하는 것이다.

### 8.4 보조 실행자 확장보다 boundary 유지

worker/supervisor/CLI 관련 자산은 계속 유효하지만,  
우선순위는 확장이 아니라 **역할 경계 유지와 return normalization의 신뢰성**이다.

---

## 9. What Was Intentionally Not Changed

이번 lock에서는 다음을 의도적으로 바꾸지 않는다.

- 새 아키텍처 제안
- 새 팀 체계 제안
- 새 runtime/state layer 제안
- naming overhaul
- package chain의 대체 구조 제안
- 현재 구조를 “OS”, “platform”, “fully autonomous” 등으로 과장하는 해석
- UI/API를 본체로 재정의하는 해석

즉, 이번 lock은 구조 개편 문서가 아니라  
**현재 자산의 우선 용도를 읽고 고정하는 문서**이다.

---

## 10. Why This Lock Matters Now

이 lock이 중요한 이유는 다음과 같다.

현재 워크트리에서는 package chain 스펙, trial/audit 리포트, space package 샘플, worker/supervisor contract, runtime trace, OMX 상태가 동시에 생겨났다.  
이 상태를 목적 없이 두면, 화면 개선, CLI 강화, automation 확대, 에이전트 조직화, naming 정비 등 다양한 방향이 모두 “다음 할 일”처럼 보이게 된다.

그러나 현재 자산의 실제 중심은 그것들이 아니라,  
**space 안의 재료를 단계적 package chain으로 reread하고, candidate/review/memory 수준의 판단 가능한 자산으로 전환하는 운영 골격**이다.

따라서 지금 필요한 것은 더 많은 구조가 아니라,  
이미 생긴 구조가 **무엇을 먼저 하기 위해 존재하는가**를 고정하는 일이다.  
이 lock은 이후 확장/제품화/자동화 판단이 현재 본체를 덮지 않도록 하는 기준점이 된다.

---

## 11. Closing Note

- 이 잠금은 최종 제품 정의 lock이 아니다.
- 현재 단계에서의 1차 용도 lock이다.
- 이후 확장/제품화/자동화 판단은 이 문서를 기준으로 다시 평가한다.
