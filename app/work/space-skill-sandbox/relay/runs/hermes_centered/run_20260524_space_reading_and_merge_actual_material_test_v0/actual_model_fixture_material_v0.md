# Actual Model Fixture Material V0

model_execution: NO_FIXTURE_ONLY

해석: 실제 공간 파일들을 읽어 space reading을 만들고, original + space reading + model fixture를 merge해야 한다.
검증: missing current-position, missing space refs, model-only merge, missing original ref, promotion drift, active call primitive를 negative case로 잡는다.
