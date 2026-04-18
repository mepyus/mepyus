# Integrated Engine Language Loop Harvest Setup Note v0

Date: 2026-04-16

## 0. verdict

PASS

2차 셋업으로, 내부 언어 루프가 쌓은 결과를 다시 읽어 line / connection / axis 후보로 수확하는 harvest 도구를 추가했다.

이 작업은 UI copy, final glossary, wording patch, Gemini adapter, deposit ingestion, automatic assignment, promotion/canonicalization을 열지 않는다.

## 1. why this setup is needed

1차 루프는 Codex를 반복 실행해서 내부 언어 번역 데이터를 만든다.

하지만 10회/20회 결과가 쌓이면 사용자가 raw session을 하나씩 열어야 하는 부담이 다시 생긴다.

따라서 2차 셋업의 목적은:

- loop 결과를 하나의 harvest로 다시 모은다.
- 반복되는 internal phrase / human-readable line / connection / axis를 분리한다.
- 어떤 축이 반복되는지 빠르게 본다.
- 아직 UI 문구나 final glossary로 승격하지 않는다.

## 2. implemented script

추가한 script:

```text
scripts/harvest_integrated_engine_language_loop.py
```

역할:

- `runtime/language_loops/<loop_id>/loop.json`을 읽는다.
- 각 session의 `structured_return.json`과 `operator_report.md`를 읽는다.
- `internal phrase or signal observed`, `human-readable line`, `repeated connection`, `emerging axis candidate` 등 필드를 추출한다.
- 같은 axis / connection을 묶는다.
- `harvest.json`과 `harvest.md`를 생성한다.

## 3. usage

최신 loop 수확:

```bash
python3 scripts/harvest_integrated_engine_language_loop.py
```

특정 loop 수확:

```bash
python3 scripts/harvest_integrated_engine_language_loop.py --loop-id language_loop_20260416T111421Z
```

생성 위치:

```text
runtime/language_loops/<loop_id>/harvest.json
runtime/language_loops/<loop_id>/harvest.md
```

## 4. validation performed

통과:

```bash
python3 -m py_compile scripts/harvest_integrated_engine_language_loop.py
```

1회 성공 loop에 대해 harvest 실행:

```bash
python3 scripts/harvest_integrated_engine_language_loop.py --loop-id language_loop_20260416T111421Z
```

결과:

- harvest path: `runtime/language_loops/language_loop_20260416T111421Z/harvest.md`
- extracted row count: `2`
- top axis: `readable-report-before-UI-copy axis`

## 5. current first harvest reading

첫 harvest는 1회 loop만 대상으로 했기 때문에 아직 작다.

그래도 다음 축이 잡혔다.

```text
readable-report-before-UI-copy axis
```

확인된 line:

- 화면 문구를 바로 바꾸기 전에, Codex가 상태를 설명하는 순서를 먼저 안정시켜야 한다.

do-not-flatten:

- 한국어화를 단순 UI 번역 또는 final glossary 작성으로 줄이면 안 된다.
- engine material을 최종 결과나 승인된 판단으로 줄이면 안 된다.

next reread question:

- 반복 보고에서 같은 line이 안정적으로 살아남는가?
- engine queue language가 대기 후보와 처리 완료를 충분히 분리하는가?

## 6. how to use with 10/20 loops

추천 순서:

```bash
python3 scripts/run_integrated_engine_language_loop.py --count 10 --sleep 2 --timeout 120
python3 scripts/harvest_integrated_engine_language_loop.py
```

20회:

```bash
python3 scripts/run_integrated_engine_language_loop.py --count 20 --sleep 2 --timeout 120
python3 scripts/harvest_integrated_engine_language_loop.py
```

읽을 순서:

1. `runtime/language_loops/<loop_id>/harvest.md`
2. 반복 axis가 강한 session의 `operator_report.md`
3. 필요한 경우 해당 `structured_return.json`

## 7. boundary

이 harvest가 하는 것:

- 반복 line 수집
- connection group 수집
- axis group 수집
- do-not-flatten note 수집
- next reread question 수집

이 harvest가 하지 않는 것:

- UI copy 작성
- final glossary 확정
- feature promotion
- deposit ingestion
- Gemini adapter 실행
- 자동 판단

## 8. current operating meaning

이제 구조는 두 단계가 됐다.

```text
run_integrated_engine_language_loop.py
-> Codex 반복 reread
-> cli_sessions / operator_report 생성
-> harvest_integrated_engine_language_loop.py
-> line / connection / axis 수확
```

이 덕분에 내가 2차 셋업을 진행하는 동안, 별도 루프를 돌려 내부 언어 번역 데이터를 쌓고, 끝난 뒤 harvest로 반복 축을 빠르게 볼 수 있다.

## 9. closeout

PASS.

내부 언어를 즉석 한국어로 바꾸는 대신, 반복 run과 harvest를 통해 shared operational language 후보를 점진적으로 두껍게 만드는 경로가 준비됐다.
