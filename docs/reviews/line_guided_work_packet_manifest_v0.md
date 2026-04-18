# Line-Guided Work Packet Manifest v0

## 목적

이 문서는 [line_guided_work_packets.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/line_guided_work_packets.json)
을 `translation only` 수준의 첫 manifest로 고정한다.

여기서 중요한 것은 실행 루프를 만드는 것이 아니라,
Paperclip식 assignment가 우리 공간의 line packet으로
어떻게 번역되는지를 먼저 보는 것이다.

## v0 범위

v0는 아래까지만 한다.

- source assignment 보존
- primary/support line translation
- context refs 연결
- execution guidance 작성

아직 하지 않는 것:

- 실제 run state 관리
- reinjection 기록
- reuse loop 자동화
- UI board 렌더

## 왜 v0가 필요한가

지금 가장 먼저 검증할 것은
`assignment를 바로 실행시키지 않고 line packet으로 번역하는 것이 실제로 유의미한가`
이다.

이걸 보기 위해서는 복잡한 integration보다
샘플 packet 2~3개가 더 낫다.

## 샘플 packet 구성

현재 v0는 세 개의 Paperclip식 assignment translation을 담는다.

1. routing/handoff 안정화

- primary line: `line_transition_over_surface`
- support line: `line_input_to_reading_organ`

2. transcript preprocess shaping

- primary line: `line_input_to_reading_organ`
- support lines: `line_pre_read_eye`, `line_raw_return_preservation`

3. validation output reread

- primary line: `line_transition_over_surface`
- support line: `line_raw_return_preservation`

## 운영 규칙

v0에서는 아래 규칙만 본다.

1. 새 line을 만들지 않는다.
기존 registry line만 쓴다.

2. support line은 최대 2~3개로 제한한다.

3. context refs는 최소 근거만 연결한다.
히스토리 전체를 packet 안에 싣지 않는다.

4. guidance는 짧고 실행 가능해야 한다.
issue 설명 복붙이 아니라 line-aware 작업 안내여야 한다.

## 성공 기준

v0는 아래가 되면 충분하다.

- 같은 assignment를 그냥 issue로 읽는 것보다 더 선명한 작업 packet이 나온다
- packet만 읽어도 왜 이 일이 이 line에 걸리는지 설명 가능하다
- 다음 단계에서 reinjection 필드를 붙일 자리가 자연스럽다

## 다음 단계

v0 다음은 두 갈래 중 하나다.

- `translation only` packet을 1~2개 더 늘려서 line coverage를 확인
- 아니면 한 packet에 한해 `reinjection stub`만 붙여 v0.1로 올리기

현재로서는 후자가 더 자연스럽다.
