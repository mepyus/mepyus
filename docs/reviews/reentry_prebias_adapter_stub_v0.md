# Reentry Prebias Adapter Stub v0

## 목적

이 문서는
이전 residue bias와 새 artifact hint를 함께 읽어
reentry prebias를 출력하는 최소 실행 stub를 고정한다.

실행 스크립트:

- [run_reentry_prebias_stub.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_reentry_prebias_stub.py)

핵심 로직:

- [reentry_prebias.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/reentry_prebias.py)

## stub 범위

이 stub는 아래까지만 한다.

- previous artifact의 saved hint를 읽는다
- new artifact의 saved hint를 읽는다
- residue reentry rule을 읽는다
- `question_shift` 와 `source_residue_bias` 가 맞는 rule을 찾는다
- new hint와 residue rule을 합쳐 reentry prebias를 출력한다

즉 아직 classifier를 직접 부르지는 않는다.

## expected use

예:

```bash
python3 scripts/run_reentry_prebias_stub.py \
  --previous-artifact app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json \
  --new-artifact runtime/current_phase.json \
  --question-shift entry_shaping_to_transition_condition
```

## current meaning

이 stub가 생기면서
`residue-backed reentry`는 더 이상 문서 원칙만이 아니라
실제로 previous residue bias와 new artifact hint를 합쳐
next family/projection/route bias를 출력하는 단계가 된다.

## 한 줄 요약

reentry prebias adapter stub v0는
previous residue bias와 new artifact hint를 합쳐
next family entry bias를 출력하는 최소 실행 도구다.
