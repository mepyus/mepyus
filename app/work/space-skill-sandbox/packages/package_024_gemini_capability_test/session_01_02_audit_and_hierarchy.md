# Session 01 & 02: Audit and Hierarchy

## P023 Self-Audit
- **과잉 확정:** "전형적인 사례로 평가", "1순위로 선정" 등 단정적 표현이 사용됨. 이는 `observed signal` 수준을 넘어선 `judgment`에 해당함.
- **자동화 편향:** 'Scriptable Unit'을 정의하면서 수동 작업의 자동화 자체에 초점을 맞춤으로써, 도구가 '판단'을 침범할 위험을 충분히 경고하지 못함.
- **범위 수렴:** SEU를 SU로 좁히려는 시도는 용어의 유연성을 저해하고 개념을 조기에 고착시킬 우려가 있음.

## Definition Hierarchy (SEU vs SU)
- **Small Execution Unit (SEU):** 프로젝트의 가장 상위 개념. "검증 비용을 낮추는 작고 한정된 모든 실행 단위"를 의미함. (체크리스트, 프롬프트 유닛, 수동 리뷰 유닛 포함)
- **Scriptable Unit (SU):** SEU의 하위 유형. 쉘 스크립트 등으로 자동화된 동작 단위.
- **결론:** SU는 SEU의 일부일 뿐이며, 모든 SEU가 SU가 될 필요는 없음. 루프의 성격에 따라 수동 SEU가 더 안전하고 효과적일 수 있음.
