# Probe Support Family

이 폴더는 bounded probe 산출을 남기는 support cluster를 묶는다.

현재 포함:

- [future_segment_probe](/Users/sungsookim/universe/vectorfl_replica/app/work/archive_review/probe_support/future_segment_probe)
- [concept_segment_probe](/Users/sungsookim/universe/vectorfl_replica/app/work/archive_review/probe_support/concept_segment_probe)

정리 규칙:

- current baseline이나 staged corridor를 직접 잠그는 line source로 읽지 않는다.
- 반복 probe와 그 generated 결과를 family 단위로 보관한다.
