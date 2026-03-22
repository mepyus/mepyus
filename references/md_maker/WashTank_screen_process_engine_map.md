# WashTank Screen Process Engine Map

## 목적

이 문서는 `WashTank`의 주요 화면을

- 공정 단계
- 운영 역할
- 엔진 연결

기준으로 한 번에 볼 수 있도록 압축한 매핑표다.

지금까지 만든 서술형 문서들을
빠르게 다시 보는 기준표로 쓰기 위한 문서다.

## 매핑표

| 화면 | 공정 위치 | 운영 역할 | 주된 관심사 | 엔진 연결 성격 |
|---|---|---|---|---|
| `Officein.jsx` | 공정 완료 이후 | 사무실 기록 허브 | 완료 이력, 입고 기록, 날짜별 조회 | 조회 중심 |
| `Officeout.jsx` | DONE 이후 다음 단계 | 사무실 전환 허브 | 다음 공정 선택, 출고 요청, 후속 작업 생성 | 조회 + 전이 |
| `Eir.jsx` | 공정 시작점 | 현장 입고 화면 | 입고 입력, 초기 상태 확인, 시작 판정 | 생성 + 초기 전이 |
| `WashingWaiting.jsx` | 세척 대기 / 진행 | 현장 세척 보드 | READY / IN_PROGRESS, 세척 큐, 시작/완료 | 조회 + 전이 |
| `Inspection.jsx` | 세척 이후 검사 | 현장 검사 화면 | 측정 시작, 측정 기록, 검사 시작, 검사 완료 | 다단계 전이 |
| `RepairShop.jsx` | 검사 이후 예외 분기 | 현장 수리 워크벤치 | 수리 등록, 수리장 처리, 완료 | 생성 + 전이 |
| `Delivery.jsx` | 출고 준비 / 출고 | 현장 출고 큐 | 날짜 기준 READY, 우선순위, 준비 완료 | 조회 + 완료 전이 |
| `Shuttle.jsx` | 부지 간 이동 | 이동 작업 화면 | 이동 시작, 이동 완료, 승인 연결 | 위치 전이 + 이벤트 |
| `Ehandler.jsx` | 1부지 현장 역할 | 1부지 장비기사 화면 | 역할 단위 작업 소비 | 역할 기반 소비 |
| `Fhandler.jsx` | 2부지 현장 역할 | 2부지 장비기사 화면 | 역할 단위 작업 소비 | 역할 기반 소비 |
| `head.jsx` | 상위 관제 감각 | 공정 보드 / 모니터 | 공정별 READY / ACTIVE 보드 | 공통 조회 + 단순 전이 |
| `Workspace.jsx` | 상위 래퍼 | 작업 공간 컨테이너 | 공통 상태 표시, 상위 공간 제공 | 직접 엔진보단 래핑 |
| `main.jsx` | 전체 상위 계층 | orchestration 레이어 | 상태 수집, 화면별 데이터 shape, trigger wiring | 상위 조정 |
| `OfficePageContainer.jsx` | 연결 계층 | Office 컨테이너 | 초기 로드, 검색, 하위 화면 주입 | 연결 / 주입 |

## 읽는 법

이 표를 볼 때 중요한 것은 화면을 "기능 단위"로만 보지 않는 것이다.

예를 들어:

- `Officein`은 단순 조회 화면이 아니라 기록 허브다
- `Officeout`은 단순 출고 화면이 아니라 전환 허브다
- `Inspection`은 단일 검사 페이지가 아니라 다단계 이벤트 소비자다
- `Shuttle`은 위치 수정이 아니라 별도 공정 이벤트 화면이다

즉 같은 탱크를 다루더라도,
각 화면은 전혀 다른 운영 역할을 맡는다.

## 공정 축으로 다시 묶기

### 시작 / 입구

- `Eir.jsx`

### 중간 공정

- `WashingWaiting.jsx`
- `Inspection.jsx`
- `RepairShop.jsx`

### 이동 / 전환

- `Shuttle.jsx`
- `Officeout.jsx`

### 종료 / 준비

- `Delivery.jsx`
- `Officein.jsx`

### 역할 전용

- `Ehandler.jsx`
- `Fhandler.jsx`

### 상위 구조

- `head.jsx`
- `Workspace.jsx`
- `main.jsx`
- `OfficePageContainer.jsx`

## 엔진 연결 축으로 다시 묶기

### 조회 중심

- `Officein.jsx`
- `Delivery.jsx`
- 일부 `head.jsx`

### 조회 + 상태 전이

- `Officeout.jsx`
- `WashingWaiting.jsx`

### 생성 + 상태 전이

- `Eir.jsx`
- `RepairShop.jsx`

### 다단계 이벤트 소비

- `Inspection.jsx`

### 위치 / 이동 이벤트

- `Shuttle.jsx`

### 상위 조정 / 주입

- `main.jsx`
- `OfficePageContainer.jsx`
- `Workspace.jsx`

## 이 표가 필요한 이유

서술형 문서가 많아질수록,
가끔은 한 장짜리 기준표가 있어야 전체가 다시 잡힌다.

이 표의 역할은:

- 화면 위치를 한 번에 확인하고
- 공정 흐름 안에서 자리를 보고
- 엔진 연결 방식을 빠르게 떠올리는 것

이다.

즉 이 문서는 `WashTank` 문서 묶음의 빠른 참조표다.

## 한 줄 정리

`WashTank`의 화면들은 파일명 기준보다
공정 위치 / 운영 역할 / 엔진 연결 방식으로 다시 묶어 읽는 편이 훨씬 선명하다.
