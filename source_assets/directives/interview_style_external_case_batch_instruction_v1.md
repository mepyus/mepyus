[[A]] [[OBJ:codex_directive]] [[SEM:interview_style_external_case_batch_instruction_v1]]

# interview_style_external_case_batch_instruction_v1

## purpose
- `dario_amodei_youtube.txt`, `andrej_karpathy_youtube.txt`, `alexkarp_youtube.txt`를 인터뷰형 외부자료 배치로 intake하고 얇은 comparative read를 남긴다.
- 세 파일의 source identity는 유지하고, 인터뷰형 설명 구조가 반복되는지만 bounded하게 본다.
- current는 유지하고, delta는 짧게만 반영한다.

## canonical inputs
- [dario_amodei_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/dario_amodei_youtube.txt)
- [andrej_karpathy_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/andrej_karpathy_youtube.txt)
- [alexkarp_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/alexkarp_youtube.txt)

## operating rule
- 인터뷰형이라는 공통 형식은 관찰하지만, 세 파일을 하나의 대표 source로 만들지 않는다.
- dario / andrej는 이번 턴에 first-pass 자산을 새로 만든다.
- alexkarp는 기존 canonical input/first-pass 자산을 재사용하되, batch 비교에서는 동일 위상으로 읽는다.
