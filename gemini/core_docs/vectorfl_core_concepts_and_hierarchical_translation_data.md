# VectorFL 핵심 개념 및 계층적 번역 자료 (v0.1)

이 문서는 VectorFL 프로젝트의 내부 언어와 핵심 개념을 정의하고, 그 계층적 중요성을 설명하여 통합 엔진이 번역/해석 작업에 활용할 수 있는 기초 데이터를 제공한다.

## 1. VectorFL 프로젝트의 핵심 철학

*   **해석 공간 (Interpretation Space):** 단순한 코드 저장소가 아닌, 복잡한 정보를 깊이 이해하고 통찰을 추출하기 위한 시스템적 공간.
*   **읽기 우선 (Reading-First):** 작업을 할당하고 수행하기 전에 정보 자체를 철저히 해석하고 의미를 이해하는 것을 최우선으로 하는 접근 방식.
*   **거버넌스 = 읽기 보호 (Governance as Reading Protection):** 성급한 결정, 잘못된 해석, 무분별한 변경으로부터 정보의 무결성을 보호하는 데 중점을 둔 의사결정 및 제어 체계.
*   **라인 (Line):** 정보의 핵심적인 의미, 통찰, 또는 핵심 주장으로, 해석 과정을 통해 발굴되고 숙성되는 지식의 단위.

## 2. 계층적 구조와 역할

VectorFL 시스템은 세 가지 주요 계층으로 구성되며, 각 계층은 명확한 역할과 소유권을 가진다.

### 2.1. 입력 준비 계층 (`qmd-ref intake layer`)

*   **역할:** 외부의 원시 정보를 VectorFL 코어 계층이 처리하기 쉬운 '라인 인식' 형태로 준비한다.
*   **주요 소유 객체:** `Source Registry Entry`, `Intake Block`, `Intake Packet`, `Intake Status Record`.
*   **제약:** `Weakness`, `fallback`, `provenance`를 포함한 원시 정보를 손실 없이 코어 계층으로 전달한다.

### 2.2. 핵심 해석 및 판단 계층 (`VectorFL core layer`)

*   **역할:** 입력된 정보를 해석하여 '의미'를 창출하고, '판단'을 내리며, 시스템의 '운영'을 관리하는 VectorFL의 핵심 두뇌. 캐노니컬 의미 체계와 운영 질서를 소유한다.
*   **주요 소유 객체:** `Case Record`, `Lane State Record`, `Line/State Formation Record`, `Translation Record`, `Flow Interpretation Record`, `Governance Record`, `Surface Packet`, `Trace/Memory Record`.
*   **제약:** `non-mixing rules`를 통해 외부 온톨로지(예: Paperclip의 `issue`, `company` 명칭)가 VectorFL 코어의 캐노니컬 의미 체계를 오염시키지 않도록 보호한다. 거버넌스 판단권을 소유한다.

### 2.3. 운영 화면 계층 (`paperclip-ref host shell layer`)

*   **역할:** 코어 계층의 정보를 사용자에게 시각적으로 명확하고 '조작 가능한' 형태로 표시한다. 이는 감독자가 시스템을 제어하고 흐름을 지시하는 '제어판' 역할을 한다.
*   **주요 비-캐노니컬 객체 (View Model):** `Case Queue Item`, `Current Reading View Model`, `Input Detail View Model`, `Program Connection View Model`.
*   **제약:** 캐노니컬 객체나 의미 체계를 소유하지 않으며, 단지 코어의 결과를 '표시'하고 '적응'시키는 역할만 한다. 판단권은 코어 계층에 남긴다.

## 3. 핵심 용어 및 계층적 의미

### 3.1. '공간' 관련 계층 (추상적 → 구체적)

*   **VectorFL 운영 워크스페이스 (Operating Workspace):** VectorFL의 가장 넓은 개념적 '회사 경계' 또는 '운영 영역'.
*   **공간 경계 선언 (Space Boundary Declaration):** 저장소 내에서 관찰된 공간의 실제 경계를 정의하는 문서. `baseline`, `operating`, `ledger`, `active surface`, `replayable residue`, `reference` 계층을 포함한다.
*   **운영 계층 (Operating Layer):** 입력, 구조화, 비교, 재읽기, 라우트 선택, 표면 구성이 실제로 일어나는 동적인 영역. (`app/core`, `app/runtime`, `scripts` 등)
*   **원장 계층 (Ledger Layer):** 과거 사실, 출처, 이벤트, 라인 기록, 로그를 `append-only` 방식으로 보존하는 불변의 기록 영역.
*   **활성 표면 (Active Surface):** 현재 상태와 읽기 결과를 바로 읽게 하는 '현재 읽기면 (current-reading surface)'. (`runtime/views` 등)

### 3.2. '품질/상태' 관련 계층 (실험적 → 캐노니컬)

*   **Weekend Pilot:** 가장 실험적이고 비공식적인 단계. 가설 테스트나 아이디어 검증을 위한 임시 구현. 캐노니컬 자산이 아니다.
*   **Page Shell:** 기본적인 UI 컨테이너 또는 레이아웃. 기능적이지만 'proper' 표준을 완전히 준수하지 않거나 핵심 로직을 포함하지 않을 수 있다. VectorFL은 이 단계를 넘어서려 한다.
*   **Operable Surface:** 구조화되고 상호작용적인 UI로, 사용자가 시스템을 적극적으로 '조작'하고 관리할 수 있도록 한다. Paperclip의 검증된 페이지 클래스 패턴을 차용한다.
    *   **조작 가능한 페이지 클래스 (Operable Page Classes):** `work list page`, `work detail page`, `right-side inspector`, `operable organ detail`, `activity audit` 등 Paperclip에서 차용한 기능적 UI 패턴.
*   **Proper (VectorFL Paper Proper):** 캐노니컬하고 이상적이며 완전히 검증된 시스템 구조 및 운영 흐름. VectorFL 시스템이 궁극적으로 구현해야 할 목표이자 표준.

### 3.3. '작업/흐름' 관련 계층 (입력 → 결과)

*   **작업 패킷 (Work Packet):** 사용자 지시, 메모 등으로부터 생성되는 작업의 초기 입력 단위.
*   **케이스 (Case):** `Intake material`과 후속 해석/운용을 묶는 중심 사례 단위.
*   **라인 (Line):** 해석 과정을 통해 발굴되고 숙성되는 정보의 핵심적인 의미/통찰.
*   **레인 (Lane):** 케이스 내부 진행 상태와 현재 라인 결과/보류를 유지하는 상태.
*   **게이트 (Gate):** 작업 흐름 내에서 감독자의 명시적인 승인/보류/재검토 판단이 필요한 지점. (예: `actual_export_only gate`)
*   **드라이 런 (Dry Run):** 실제 변경 없이 잠재적 후보를 검증하는 시뮬레이션 프로세스.
*   **비교 (Comparison):** 여러 후보를 기준과 비교하여 상대적 강점과 약점을 평가하는 과정.
*   **핸드오프 (Handoff):** 한 계층 또는 구성 요소에서 다른 계층으로 정보를 전달하는 행위. (`lossless handoff` 강조)
*   **브릿지 (Bridge):** AI (Codex, Gemini)와 같은 외부 워커(worker)를 VectorFL 시스템에 연결하여, 입력과 출력을 VectorFL의 내부 형식으로 번역하는 역할.

## 4. 통합 엔진의 번역 데이터 수집 방향

통합 엔진이 번역에 활용할 데이터는 위에서 정의된 각 계층의 `책임`, `소유 객체`, `제약` 및 `핵심 용어`들이다. 특히 `Paperclip native vs VectorFL principles comparison`에서 강조된 바와 같이, 외부 시스템에서 `operable page class`와 `assignment/detail/inspector 구조`를 가져오되, `VectorFL의 current-reading/governance/trace의 canonical 질서`를 유지해야 한다.

따라서 번역 데이터는 다음을 포함한다:

*   **용어 정의 및 계층적 관계:** 각 핵심 용어의 VectorFL 내 의미, 상위/하위 계층과의 관계.
*   **객체 소유권:** 어떤 정보가 어떤 계층에 속하고, 어디에서 생성/판단되고 어디에서 표시만 되는지.
*   **흐름 및 판단 지점:** 작업 패킷의 흐름, 핸드오프 경계, 각 게이트에서의 감독자 판단 유형.
*   **AI 워커의 역할 및 제약:** Codex, Gemini와 같은 AI가 어떤 입력을 받아 어떤 출력을 내며, 어떤 `forbidden_scope`와 `constraint`를 가지는지.

이러한 데이터는 통합 엔진이 VectorFL의 '의미'와 '판단'을 외부 '작업'과 '표시'로 정확히 번역할 수 있는 기반이 될 것이다.
