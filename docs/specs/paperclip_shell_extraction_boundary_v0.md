# Paperclip Shell Extraction Boundary v0

이 문서는 `git_search/paperclip`를 VectorFL Paper의 shell reference로 쓸 때  
어디까지를 참조하고 어디부터는 들이지 않을지를 짧게 잠근다.  
Paperclip 전체를 가져오는 문서가 아니라, `shell-only extraction boundary`를 고정하는 문서다.

## 1. 목적

현재 필요한 것은 Paperclip 전체 구조를 차용하는 것이 아니라,
VectorFL Paper를 위한 `운용면 shell`만 보수적으로 참조하는 것이다.

즉 이 문서는 아래를 잠근다.

- Paperclip에서 가져올 수 있는 shell 감각
- 지금 단계에서 가져오면 안 되는 ontology / orchestration 층
- VectorFL Paper의 첫 구현에서 참조 가능한 최소 범위

## 2. Keep As Shell Reference

현재 단계에서 Paperclip에서 참조 가능한 것은 아래다.

### 2-1. queue composition

- case list / work list를 다루는 shell 감각
- row/card 기반 진입 구조
- status badge / freshness / preview 배치 감각

### 2-2. detail console composition

- 현재 보고 있는 항목을 중심 pane으로 다루는 감각
- body + sidecard + supporting panel 구성을 가진 운용면 감각

### 2-3. governance / history panel composition

- 진행 상태와 보류 사유를 panel/card로 드러내는 감각
- activity / history / trace를 옆면 또는 하위 strip으로 유지하는 감각

### 2-4. program / connection surface composition

- 외부 연결 상태를 별도 panel이나 view로 보이게 하는 감각

## 3. Do Not Import As Canonical Structure

현재 단계에서 Paperclip에서 canonical로 들이면 안 되는 것은 아래다.

- `company`
- `project`
- `goal`
- `issue`
- `heartbeat`
- `approval / budget` naming
- agent hierarchy를 바로 VectorFL 팀 구조로 등치하는 방식

즉 Paperclip의 ontology와 orchestration naming은 shell reference가 아니다.

## 4. Current Extraction Boundary

지금 단계에서 추출 경계는 아래처럼 잠근다.

### allowed shell range

- navigation / frame 감각
- queue/list shell
- current detail console shell
- governance / history side panels
- programs / connections panel

### not yet allowed

- company workspace model
- issue lifecycle model
- heartbeat orchestration model
- approval / budget workflow model
- agent runtime control logic

## 5. First Build Priority

VectorFL Paper 첫 shell 구현 우선순위는 아래다.

1. `Current Reading shell`
2. `Inputs / Intake shell`
3. `Cases / Queue shell`
4. `Programs / Connections shell`
5. `History / Trace shell`

즉 첫 중심면은 current-reading이고,
queue와 input은 진입면,
program/history는 보조면으로 읽는다.

## 6. Extraction Note

Paperclip에서 가져오는 것은 “기능”보다 `운용 표면의 구성 감각`이다.

즉:

- queue를 어떻게 보이게 하는가
- 현재 reading body를 어떻게 중심 pane에 두는가
- governance와 history를 어떻게 별도 panel로 드러내는가

이 감각을 참조하는 것이지,
Paperclip의 일감 ontology를 VectorFL에 이식하는 것이 아니다.

## 7. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`Paperclip는 VectorFL Paper에서 queue, console, governance/history, program connection을 보여주는 shell composition reference로만 사용하며, company/issue/heartbeat/approval 같은 ontology와 orchestration naming은 canonical structure로 들이지 않는다.`
