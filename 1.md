````md
[[A]] [[OBJ:codex_tank_process_md_v2]] [[ROLE:engine]]

# CODEx 지시서 — 탱크프로그램 공정별 MD 추출 v2
# 기준 갱신: 현재 실제 사용 페이지 + services 계층만 분석 대상으로 삼는다

## 0. 이번 턴의 목적

기존 탱크프로그램 레퍼런스 폴더에서
**현재 실제 사용 중인 페이지들과 services 계층만 기준으로**
공정별 md 문서를 추출한다.

이번 작업의 목적은 코드 수정이 아니다.

목적은 아래 둘이다.

1. **현재 실제 운용 공정/페이지를 md 자산으로 고정**
2. **services 계층(특히 jms 계열)을 기준으로 데이터/상태 흐름을 읽어내기**

즉 이번 턴은:
- 리팩터링 아님
- 구조 개선 아님
- 샘플 파일 정리 아님
- 위치값 잘못된 테스트 파일 수정 아님

**현재 실제 사용하는 페이지 + services 핵심만 읽고 문서화**하는 작업이다.

---

## 1. 실제 사용 페이지 기준선

아래 import 목록을 현재 메인에서 사용하는 실제 페이지 목록으로 간주한다.

```jsx
import HeadPage from './Head';
import OfficeOutPage from './Officeout';
import OfficeInPage from './Officein';
import WashingWaitingPage from './WashingWaiting';
import EirPage from './Eir';
import EhandlerPage from './Ehandler';
import FhandlerPage from './Fhandler';
import InspectionPage from './Inspection';
import RepairShopPage from './RepairShop';
import DeliveryPage from './Delivery';
````

즉 이번 문서화 대상은 아래 10개다.

* Head
* Officeout
* Officein
* WashingWaiting
* Eir
* Ehandler
* Fhandler
* Inspection
* RepairShop
* Delivery

---

## 2. 분석 범위 축소 기준

### 2.1 이번에 적극적으로 분석할 것

* 위 10개 실제 사용 페이지
* `services/*`
* 특히 `jms.js`, `jms_core.js`, `supabase.js`
* 페이지에서 services를 어떻게 호출하는지
* 어떤 상태/리스트/전이 액션이 services를 통해 수행되는지

### 2.2 이번에 보조 참고만 할 것

* `hooks/*`
* `constants/*`
* `utils/*`
* 실제 페이지가 직접 참조하는 경우에만 문서에 적는다

### 2.3 이번에 무시/보류할 것

아래는 현재 샘플 또는 실험 파일/폴더일 가능성이 높으므로
**직접 main에서 안 쓰면 이번 턴 핵심 대상에서 제외**한다.

* `components/*`
* `pages/*` 하위의 보조 페이지
* 위치값 잘못 설정된 임시 파일
* main에서 직접 안 쓰는 샘플 화면
* `Workspace.jsx`, `TankControl.jsx`, `Shuttle.jsx`, `WashingBay.jsx`, `WashingDirty.jsx` 등

단, 현재 실제 사용 페이지가 이 파일들을 import하면
그때만 "관련 파일"로 기록한다.

---

## 3. 최종 출력 구조

```text
docs/
  processes/
    head.md
    officeout.md
    officein.md
    washingwaiting.md
    eir.md
    ehandler.md
    fhandler.md
    inspection.md
    repairshop.md
    delivery.md

  shared/
    process_index.md
    state_transition_map.md
    service_reference_map.md

  current/
    CURRENT.md
```

---

## 4. 사용자 기준 공정 해석(초기값)

아래는 사용자 설명 기준 해석이며,
문서 안에서 `USER_CONTEXT`로 명시하고
코드에서 확인되면 `CODE_CONFIRMED`로 승격한다.

### 4.1 Officein

* 공정 + done 상태 탱크를 받아온다
* 완료(done)를 ready로 바꾸는 공간

### 4.2 Officeout

* ready 상태 탱크를 다음 공정 progress로 바꾸는 공간

### 4.3 EIR

* 입고된 탱크 외부 검사 및 점검
* 데이터를 기록
* 완료 후 done으로 보내 Officein으로 연결

### 4.4 WashingWaiting

* 세척 모니터링 페이지

### 4.5 RepairShop

* 수리장 페이지

### 4.6 Ehandler / Fhandler

* 장비기사가 야드 내 탱크 위치값을 넣는 페이지

### 4.7 Inspection

* 현재 실제 사용 페이지이므로 별도 공정/검사 단계로 취급
* 실제 역할은 코드에서 확인

### 4.8 Delivery

* 출고 리스트를 보여주는 페이지

### 4.9 Head

* 메인 헤더/탭/네비게이션/페이지 전환의 관문일 가능성 높음
* 실제 역할은 코드에서 확인

---

## 5. 이번 문서화의 핵심 시선

이번에는 페이지 자체보다도
**페이지가 services 계층을 어떻게 사용하는지**가 중요하다.

즉 각 페이지 문서에서 반드시 봐야 하는 건 아래다.

1. 어떤 service 함수를 호출하는가
2. 어떤 데이터셋을 가져오는가
3. 어떤 상태 전이 액션을 보내는가
4. 어떤 필터/공정명/상태명을 기준으로 리스트를 나누는가
5. 어떤 저장/업데이트가 실제로 발생하는가

즉:

* 페이지 = UI 설명문
  이 아니라
* 페이지 = **services 호출을 통해 어떤 공정을 수행하는가**
  로 읽는다.

---

## 6. 각 공정 md 문서 템플릿

모든 공정 문서는 아래 구조를 따른다.

# 공정명

## 1. 목적

* 이 페이지가 왜 존재하는가

## 2. 화면 역할

* 사용자가 여기서 무엇을 하는가
* 시스템 입장에서 어떤 공정 단계인가

## 3. 진입 조건

* 어떤 상태/공정/리스트에서 이 페이지가 쓰이는가

## 4. 입력

* 어떤 데이터가 들어오는가
* 어떤 필터/검색/선택/UI 입력이 있는가

## 5. 출력 / 결과

* 어떤 목록/상세를 보여주는가
* 어떤 저장/전이/업데이트를 수행하는가

## 6. 상태 전이

* 어떤 상태를 어떤 상태로 바꾸는가
* 코드 기준 상태명과 사용자 해석 상태를 둘 다 적는다

## 7. services 사용

* 어떤 service 파일을 참조하는가
* 어떤 핵심 함수/쿼리/업데이트 호출이 있는가

## 8. 주요 액션

* 버튼, 저장, 완료, 전송, 상태변경, 위치입력 등

## 9. 예외 / 주의

* 누락, 충돌, 수동 확인, 불명확한 로직, TODO

## 10. 관련 파일

* 직접 연결된 jsx / service / hook / constants 파일

## 11. USER_CONTEXT

* 사용자 설명 기반 공정 의미

## 12. CODE_CONFIRMED

* 코드에서 직접 확인한 사실

## 13. TODO / 보류

* 아직 확인 안 된 부분
* 추가 확인 필요 service / 상태명 / 함수

---

## 7. shared 문서 템플릿

### 7.1 process_index.md

포함 내용:

* 공정명
* 한 줄 목적
* 진입 상태
* 종료 상태
* 주요 service
* 관련 md 링크

### 7.2 state_transition_map.md

포함 내용:

* 코드 확인된 상태 전이
* 사용자 설명 기반 상태 전이
* 둘의 차이
* `CODE_CONFIRMED / USER_CONTEXT / TODO` 태그 구분

예시:

* EIR 완료 -> done
* Officein 처리 -> ready
* Officeout 처리 -> progress

### 7.3 service_reference_map.md

포함 내용:

* 각 페이지가 어떤 service 함수/파일을 쓰는지 맵핑
* `jms.js`, `jms_core.js`, `supabase.js` 역할 구분
* 읽기/쓰기/상태전이/조회 성격 구분

### 7.4 current/CURRENT.md

포함 내용:

* 완료한 문서 목록
* services 분석에서 확인한 핵심 전이
* 아직 애매한 페이지
* 다음 확인 포인트

---

## 8. 사실 기록 규칙

아래 태그를 강제한다.

### CODE_CONFIRMED

코드에서 직접 확인된 사실

### USER_CONTEXT

사용자 설명 기준 의미

### TODO

코드상 아직 확인 안 된 항목

### 금지

* 추정 사실을 확정처럼 쓰지 말 것
* 사용자 설명을 코드 사실처럼 쓰지 말 것
* 코드 사실과 해석을 섞지 말 것

---

## 9. 이번 턴 작업 절차

## Step 1. main 기준 실제 페이지 확정

* main 또는 라우팅 기준으로 실제 import/사용 페이지를 확인
* 위 10개를 현재 운용 페이지로 잠금

## Step 2. 각 페이지의 direct import 확인

각 페이지가 아래 중 무엇을 직접 쓰는지 확인

* `services/*`
* `hooks/*`
* `constants/*`
* `utils/*`

## Step 3. services 계층 우선 해석

특히 아래를 우선 본다.

* `jms.js`
* `jms_core.js`
* `supabase.js`

확인할 것:

* 조회 함수
* 상태 변경 함수
* 저장 함수
* 공정명/상태명/필터값
* 페이지별로 어떤 service를 호출하는지

## Step 4. 공정 md 생성

우선순위에 따라 각 공정 문서를 작성한다.

## Step 5. 상태 전이 요약 작성

페이지별 문서를 바탕으로
전체 상태 전이 문서를 작성한다.

## Step 6. service reference map 작성

어떤 페이지가 어떤 service를 쓰는지 표처럼 정리한다.

---

## 10. 이번 턴 우선순위

### 우선 1 — 핵심 전이 공정

* officein.md
* officeout.md
* eir.md
* inspection.md

### 우선 2 — 운영/현장 공정

* washingwaiting.md
* repairshop.md
* ehandler.md
* fhandler.md

### 우선 3 — 주변/출력 공정

* delivery.md
* head.md

### 마지막

* process_index.md
* state_transition_map.md
* service_reference_map.md
* CURRENT.md

이유:
이번 턴의 핵심은
**done / ready / progress 및 검사/수리/위치입력 흐름이 services 기준으로 어떻게 연결되는지**
보는 것이기 때문이다.

---

## 11. 페이지별 체크포인트

### 11.1 officein.md

반드시 확인:

* done 목록을 어디서 불러오는가
* ready 전환 액션이 어떤 service 함수로 가는가
* 공정 필터가 있는가
* officeout과 어떤 상태 축으로 이어지는가

### 11.2 officeout.md

반드시 확인:

* ready 목록 조회 방식
* progress 전환 액션
* 다음 공정 지정 방식
* 상태명/필드명/서비스 호출

### 11.3 eir.md

반드시 확인:

* 검사 입력/기록 저장
* 완료 처리
* done 전환 여부
* Officein으로 이어지는 흔적

### 11.4 inspection.md

반드시 확인:

* EIR과 다른 별도 검사 단계인지
* 어떤 데이터/상태를 다루는지
* 어느 service를 사용하는지

### 11.5 washingwaiting.md

반드시 확인:

* 모니터링 전용인지
* 세척 진행/완료 갱신까지 하는지
* 어떤 상태명/공정명을 기준으로 묶는지

### 11.6 repairshop.md

반드시 확인:

* 수리 대상 불러오기
* 수리 완료/다음 단계 전이
* service 호출 구조

### 11.7 ehandler.md / fhandler.md

반드시 확인:

* 위치 입력 방식
* 위치 저장 service
* tank 식별 방식
* 둘의 차이점

### 11.8 delivery.md

반드시 확인:

* 출고 리스트 조회 방식
* 확정/표시 전용 여부
* 상태 필터

### 11.9 head.md

반드시 확인:

* 페이지 전환/탭 구성
* 공정 선택/헤더 역할
* 단순 UI인지 실제 상태 영향이 있는지

---

## 12. 품질 기준

좋은 결과물은 아래를 만족해야 한다.

1. 코드 안 보고도 각 공정 목적을 설명할 수 있다
2. 공정별 상태 전이를 말할 수 있다
3. 어떤 service가 핵심인지 알 수 있다
4. 실제 쓰는 페이지와 샘플 페이지가 분리되어 있다
5. 나중에 이 md만 보고 다시 구조를 잡을 수 있다

---

## 13. 금지사항

* 샘플/실험 파일까지 전부 분석하지 말 것
* 실제 미사용 페이지를 핵심 공정처럼 다루지 말 것
* UI 설명만 쓰고 service 흐름을 생략하지 말 것
* 상태명을 vague하게 쓰지 말 것
* 코드 확인 없이 상태 전이를 확정하지 말 것
* 문서화 중 코드 수정하지 말 것

---

## 14. 작업 완료 후 보고 형식

### 1. 완료 문서

* 생성한 md 목록

### 2. 핵심 services 결과

* `jms.js`, `jms_core.js`, `supabase.js` 역할 요약
* 페이지별 핵심 service 호출 정리

### 3. 상태 전이 확인 결과

* 코드로 확인한 전이
* 사용자 설명과 일치한 전이
* 아직 애매한 전이

### 4. 보류 항목

* page/service 연결이 헷갈리는 부분
* 추가 확인 필요 함수/상태명

### 5. 다음 추천 작업

* 다음에 더 파고들 공정 또는 service
* 이번 턴에서는 수정하지 않음

---

## 15. 한 줄 요약

이번 작업은 현재 실제 사용 중인 페이지 10개와 services 계층만 기준으로,
**각 공정의 목적 / 역할 / 상태 전이 / service 호출 / 입력 / 출력 / 예외를 md 자산으로 추출해
나중에 다시 공정 구조를 재구축할 수 있게 만드는 문서화 작업**이다.

```
```
