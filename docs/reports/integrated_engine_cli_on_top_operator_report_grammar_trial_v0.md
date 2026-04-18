# Integrated Engine CLI On-Top Operator Report Grammar Trial v0

Date: 2026-04-16

## 0. verdict

PASS_WITH_NOTE

이 문서는 `integrated_engine_cli_on_top_shared_language_grammar_reread_v0`에서 잠근 보고 문법을 현재 CLI-on-top 상태에 시험 적용한다.

이 문서는 UI copy, final glossary, wording patch, scaffold 수정, manifest/read-map 변경을 만들지 않는다. 목적은 Codex가 사용자에게 어떤 식으로 "나의 언어로 번역 리포트"를 해야 하는지 시험하는 것이다.

## 1. current operating status

현재 통합엔진 UI는 `app/ui/integrated_engine`에서 실행되는 안정 폴더를 사용한다. `gemini/mock_test`는 이제 본체가 아니라 Gemini proposal / design clay로 남아 있다.

CLI는 3면 바깥의 새 surface가 아니다. VectorFL surface 안에서 다루는 on-top 실행층이다.

지금 실제로 가능한 일은 다음이다.

- VectorFL면에서 Codex CLI 작업을 실행한다.
- Codex 결과가 `runtime/cli_sessions`에 session artifact로 남는다.
- 최신 결과와 최근 결과를 VectorFL면에서 바로 읽는다.
- 결과에 `reread`, `implementation return`, `validation target`, `deposit candidate` mark를 붙인다.
- User surface와 Engine surface가 같은 CLI return을 각자 역할에 맞게 후보 재료로 읽는다.
- User / Engine surface에서 본 후보를 다시 VectorFL follow-up으로 보낼 수 있다.

## 2. surface-by-surface reading

### 2.1 User surface reading

사용자면은 Codex를 직접 실행하는 곳이 아니다.

사용자면은 VectorFL에서 나온 CLI return을 업무 후보, 결정 후보, route board ticket으로 정리한다.

현재 읽기:

- 최신 CLI return은 "이제 사용자가 볼 수 있는 업무/결정 신호"다.
- route board의 Backlog / Handoff / Review는 자동 배정이 아니라 후보 분류다.
- deposit-ready count는 "편입 완료"가 아니라 "나중에 deposit 판단할 후보가 있다"는 신호다.

사용자에게 올라와야 하는 말:

```text
지금 사용자면에는 Codex 결과가 업무 후보로 올라와 있다.
아직 자동 배정이나 공식 편입은 아니다.
사용자는 이 후보를 다시 VectorFL로 보내거나, 다음 package를 열지 판단한다.
```

### 2.2 VectorFL surface reading

VectorFL면은 현재 CLI 운영의 중심이다.

현재 읽기:

- CLI 작업을 직접 요청한다.
- 결과를 latest / recent turn으로 되읽는다.
- mark를 붙여 다음 route를 지정한다.
- User/Engine에서 올라온 후보를 다시 follow-up context로 가져온다.

사용자에게 올라와야 하는 말:

```text
VectorFL면은 Codex와 대화하며 결과를 되읽는 자리다.
여기서 붙는 mark는 완료 선언이 아니라 다음 읽기 방향이다.
```

### 2.3 Engine surface reading

엔진면은 Codex return을 처리/반환/검증/추출 재료로 읽는다.

현재 읽기:

- latest CLI return은 processing return material이다.
- validation queue는 검증 후보를 보여준다.
- extraction/deposit material queue는 보관 또는 추출 후보를 보여준다.
- 엔진면은 이 결과를 판단기관처럼 확정하지 않는다.

사용자에게 올라와야 하는 말:

```text
엔진면에는 Codex 결과가 처리 반환 재료로 들어와 있다.
검증이나 deposit 후보로 보일 수 있지만, 아직 자동 편입이나 최종 판단은 아니다.
```

## 3. route and authority reading

현재 열린 route:

- VectorFL -> Codex run -> structured return
- structured return -> mark
- mark -> User candidate / Engine material / VectorFL follow-up

현재 닫힌 route:

- Gemini adapter
- automatic deposit ingestion
- automatic assignment
- automatic promotion / canonicalization
- session history/browser expansion
- UI Korean copy replacement

권위 경계:

- Codex output은 return material이다.
- mark는 route signal이다.
- User는 package opening / promotion / 다음 작업 판단 권위를 가진다.
- VectorFL은 reread / mediation / validation route를 잡는다.
- Engine은 처리/반환 재료를 보여주지만 판단 권위를 흡수하지 않는다.

## 4. friction reading

현재 사용자가 어렵게 느끼는 지점은 구조가 전혀 안 된 문제가 아니다.

핵심 friction은 다음이다.

1. 화면 언어가 영어와 내부 공간 언어 위주라 사용자가 즉시 판단하기 어렵다.
2. latest return과 mark는 보이지만, 그것이 사용자 업무/결정 언어로 충분히 정리되어 있지는 않다.
3. User/Engine surface에 CLI return이 반영되지만, 왜 그것이 "후보"이고 "확정"이 아닌지 화면만 보고는 약할 수 있다.
4. Codex가 한국어로 설명하지 않으면 사용자는 구조가 실제로 어디까지 동작했는지 매번 판단 부담을 가진다.

이 friction은 당장 UI 번역을 붙여 해결할 문제가 아니다.

먼저 Codex가 보고 문법을 안정적으로 써야 한다. 그 다음 반복되는 보고 라인이 실제 interface 축으로 자라는지 봐야 한다.

## 5. Korean operator report trial

아래는 현재 상태를 사용자에게 보고할 때 쓸 수 있는 시험 리포트다. 최종 UI 문구가 아니다.

```text
현재 상태는 PASS_WITH_NOTE입니다.

VectorFL면에서 Codex를 직접 실행하고, 그 결과를 최신 반환/최근 반환/mark로 다시 읽는 경로는 동작합니다. 이 CLI는 4번째 면이 아니라, 기존 통합엔진 3면 위에 얹힌 보조 실행층입니다.

사용자면에서는 Codex 결과가 업무 후보와 결정 후보로 올라옵니다. 이것은 자동 배정이 아니라 "이 결과를 다음 작업으로 열 수 있다"는 신호입니다.

VectorFL면에서는 Codex 결과를 되읽고 mark를 붙입니다. 여기서 mark는 완료 선언이 아니라 다음 route를 가리키는 신호입니다. 예를 들어 validation target은 "검증 대상으로 읽자"는 뜻이지, 검증이 끝났다는 뜻이 아닙니다.

엔진면에서는 Codex 결과가 처리 반환 재료, 검증 후보, 추출/deposit 후보로 보입니다. 하지만 아직 자동 편입이나 공식 기록 승격은 열지 않았습니다.

따라서 지금의 핵심은 "CLI 연결이 되느냐"가 아니라 "CLI 결과가 3면에서 각각 맞는 역할로 읽히느냐"입니다. 이 부분은 1차로 동작합니다.

남은 가장 큰 얇음은 화면의 언어입니다. 다만 지금 바로 한국어 UI copy를 붙이면 우리가 만든 내부 문법을 잃을 수 있습니다. 먼저 이런 방식의 보고 문법으로 상태를 설명하고, 반복되는 라인이 무엇인지 봐야 합니다.
```

## 6. what this trial preserves

이 시험 리포트가 보존한 것:

- CLI는 새 surface가 아니라 on-top layer다.
- VectorFL이 CLI 운영 중심이다.
- User surface는 업무/결정 후보를 읽는다.
- Engine surface는 처리/반환 재료를 읽는다.
- mark는 완료가 아니라 route signal이다.
- deposit candidate는 편입 완료가 아니다.
- UI copy patch는 아직 닫혀 있다.

## 7. what still feels thin

아직 얇은 것:

1. 사용자면에서 "업무 후보"와 "자동 배정 아님"의 차이를 화면만으로 판단하기 어렵다.
2. 엔진면에서 "return material"과 "검증 완료"의 차이가 사용자에게 바로 느껴지지 않을 수 있다.
3. VectorFL면의 latest/recent turn은 구조적으로는 좋지만, 사용자가 보기엔 아직 Codex와 대화하는 실제 흐름보다 내부 기록 카드처럼 보일 수 있다.

## 8. line / connection / axis feedback

이번 trial에서 새로 강해진 line:

- "mark는 완료가 아니라 route signal이다."
- "CLI 결과는 세 면에 반영되지만, 각 면에서 권위가 다르다."
- "한국어 UI copy 전에 Codex 보고 문법이 먼저 안정되어야 한다."

강해진 connection:

```text
CLI return
-> VectorFL mark
-> User work candidate / Engine return material
-> user decision or VectorFL follow-up
```

강해진 axis:

```text
readable report grammar before visible UI translation
```

## 9. next safe step

다음으로 가장 작은 유효 단계는 UI 번역이 아니다.

다음 단계는 실제 Codex run 1건 또는 현재 화면 관찰 1건을 이 보고 문법으로 다시 사용자에게 설명하고, 사용자가 그 설명으로 판단 가능한지 보는 것이다.

그 결과 같은 line이 반복되면 그때 surface별 summary layer 또는 UI readable strip을 열 수 있다.

## 10. closeout

PASS_WITH_NOTE.

현재 CLI-on-top 경로는 실제로 동작하고, 3면 반영도 시작됐다. 하지만 사용자 판단 언어는 아직 UI에 붙일 단계가 아니다. 먼저 이 문서의 operator report grammar를 사용해 Codex가 매번 "현재 상태 -> 3면별 읽기 -> 열린/닫힌 route -> friction -> 다음 작은 단계" 순서로 보고해야 한다.
