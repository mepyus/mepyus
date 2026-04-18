# observer_ingest_min terminal usage

## 1. 목적
이 문서는 `observer_ingest_min` 실행기를 터미널에서 바로 사용하는 방법만 정리한다.

핵심:
- 파일 하나를 쉽게 넣는다
- 자동으로 split mode를 고른다
- generated 파일 5종을 확인한다

---

## 2. 실행 위치
레포 루트에서 실행한다.

예:
```bash
cd /Users/sungsookim/universe/vectorfl_replica
```

---

## 3. 가장 쉬운 사용법: direct mode

### 3-1. 기본 명령
bash
python3 app/work/observer_ingest_min/run_observer_ingest_min.py \
  --input ./AI_bulider_03_05.md \
  --label AI_bulider_03_05 \
  --profile auto


설명:
- `--input`: 넣을 파일 경로
- `--label`: 실행 결과에 붙일 이름
- `--profile auto`: 입력 성격 자동 판별

실행이 끝나면 터미널에 `run_id` 가 1줄 출력된다.

예:
```bash
youtube_03_22_20260322_150717
```

이 값이 이번 실행의 결과 묶음 이름이다.

---

## 4. direct mode 인자 설명

### `--input`
단일 입력 파일 경로.

예:
```bash
--input ./youtube_03_22.md
--input ./youtube_03_18.md
--input ./basic3.md
```

### `--label`
결과 파일 이름에 들어갈 짧은 식별자.

예:
```bash
--label youtube_03_22
--label basic3_probe
```

지정하지 않으면 파일명이 사용된다.

### `--profile`
현재는 보통 `auto` 로 두면 된다.

예:
```bash
--profile auto
```

---

## 5. registry mode
여러 입력을 한 번에 넣고 싶으면 registry json을 사용한다.

### 5-1. 샘플 registry 확인
파일:
- [sample_input_registry.json](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/examples/sample_input_registry.json)

### 5-2. 실행 명령
```bash
python3 app/work/observer_ingest_min/run_observer_ingest_min.py \
  --registry app/work/observer_ingest_min/examples/sample_input_registry.json \
  --profile auto
```

registry 안의 각 입력마다 run_id가 한 줄씩 출력된다.

---

## 6. split mode가 어떻게 결정되는가
`split_mode = auto` 이면 아래 순서로 고른다.

1. timestamp가 보이면 `timestamp`
2. markdown heading이 보이면 `heading`
3. 아니면 `paragraph`

예:
- 유튜브 transcript + `## 제목`이 많으면 `heading`
- `[00:00]`, `06:40`, `00:00:00` 이 강하게 잡히면 `timestamp`
- 메모/산문이면 `paragraph`

---

## 7. 실행 후 생성되는 파일
출력 폴더:
- [generated](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/generated)

run_id가 `youtube_03_22_20260322_150717` 이라면 아래 5개가 생긴다.

1. `source_manifest_youtube_03_22_20260322_150717.json`
2. `split_units_youtube_03_22_20260322_150717.json`
3. `processing_trace_youtube_03_22_20260322_150717.json`
4. `readable_input_board_youtube_03_22_20260322_150717.md`
5. `operator_summary_youtube_03_22_20260322_150717.md`

---

## 8. 가장 먼저 읽을 파일 순서

### 1순위
`operator_summary_<run_id>.md`

이 파일에서 바로 보는 것:
- 어떤 입력으로 읽혔는지
- split mode가 무엇인지
- 몇 개 unit으로 나뉘었는지
- 앞/중간/뒤 흐름이 어떤지

### 2순위
`readable_input_board_<run_id>.md`

이 파일에서 바로 보는 것:
- unit 목록
- 각 unit의 짧은 발췌
- 전체 흐름 한 줄 메모

### 3순위
`split_units_<run_id>.json`

이 파일에서 바로 보는 것:
- 실제 unit 구조
- start/end ref
- excerpt
- char_count

---

## 9. 예시: 방금 만든 샘플 결과 열기
예시 run_id:
`youtube_03_22_20260322_150717`

```bash
cat app/work/observer_ingest_min/generated/operator_summary_youtube_03_22_20260322_150717.md
```

```bash
cat app/work/observer_ingest_min/generated/readable_input_board_youtube_03_22_20260322_150717.md
```

```bash
cat app/work/observer_ingest_min/generated/source_manifest_youtube_03_22_20260322_150717.json
```

```bash
cat app/work/observer_ingest_min/generated/split_units_youtube_03_22_20260322_150717.json
```

---

## 10. 새 파일을 넣을 때 가장 추천하는 루틴

### transcript류
```bash
python3 app/work/observer_ingest_min/run_observer_ingest_min.py \
  --input ./youtube_03_18.md \
  --label youtube_03_18 \
  --profile auto
```

### 짧은 note/memo류
```bash
python3 app/work/observer_ingest_min/run_observer_ingest_min.py \
  --input ./basic3.md \
  --label basic3 \
  --profile auto
```

실행 후:
1. 터미널에 나온 `run_id` 확인
2. `operator_summary_<run_id>.md` 확인
3. `readable_input_board_<run_id>.md` 확인
4. 필요하면 `split_units_<run_id>.json` 확인

---

## 11. 자주 보는 판독 포인트

### 입력이 제대로 들어갔는지 볼 때
`source_manifest_<run_id>.json`
- `source_path`
- `detected_profile`
- `split_mode_used`
- `unit_count`

### 너무 잘게 쪼개졌는지 볼 때
`split_units_<run_id>.json`
- `char_count`
- `text_excerpt`

### 흐름이 대충 읽히는지 볼 때
`operator_summary_<run_id>.md`
- 앞 / 중간 / 뒤 요약

---

## 12. direct mode와 registry mode를 언제 쓰는가

### direct mode
추천 상황:
- 파일 하나 바로 시험할 때
- 터미널에서 빠르게 넣고 확인할 때
- 지금은 이게 기본 사용법

### registry mode
추천 상황:
- 입력 여러 개를 한 번에 돌릴 때
- input_kind / split_mode / note를 미리 고정하고 싶을 때

---

## 13. 현재 한계
이 실행기는 아직 아래를 하지 않는다.

- canonical / mixed 판독
- corridor 분석
- re-entry 판독
- bridge admission
- source_local_ref 생성

즉 현재 목적은:
- 입력 주입
- 분해 확인
- 처리 흔적 기록
- readable summary
까지다.

---

## 14. 추천 one-shot command
가장 자주 쓸 명령:

```bash
cd /Users/sungsookim/universe/vectorfl_replica && \
python3 app/work/observer_ingest_min/run_observer_ingest_min.py \
  --input ./youtube_03_22.md \
  --label youtube_03_22 \
  --profile auto
```

---

## 15. 한 줄 요약
이 실행기는 `파일 하나를 쉽게 넣고 -> 자동으로 나누고 -> operator_summary / readable_input_board로 바로 확인하는 minimal observer ingest 면` 이다.
