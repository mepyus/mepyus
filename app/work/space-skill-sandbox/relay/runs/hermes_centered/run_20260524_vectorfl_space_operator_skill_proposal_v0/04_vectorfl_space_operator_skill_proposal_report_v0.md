# VECTORFL_SPACE_OPERATOR_SKILL_PROPOSAL_V0

verdict: GOOD_CANDIDATE_FOR_SKILL_WITH_HOLD

## 판단

네 판단이 맞음. 이 router/contract는 run 안의 일회성 산출물보다 skill 단위로 빼는 게 적합하다.

이유:
- 자연어 지시를 4개 Codex route로 안정적으로 분기함
- Codex가 무엇을 읽고 무엇을 반환해야 하는지 고정함
- Hermes 역할을 축소하지 않고, Hermes 실행/merge 중심 구조를 유지함
- Codex/Gemini default 호출 금지와 HOLD boundary를 반복 사용 가능하게 만듦

## 추천 skill

name:
- vectorfl-space-operator

recommended path if approved:
- ~/.hermes/skills/software-development/vectorfl-space-operator/

layout:
- SKILL.md
- references/hermes_centered_loop.md
- references/operation_routes.md
- references/return_schemas.md
- references/boundaries.md

## 지금 만든 것

실제 skill을 생성하지 않고, HOLD proposal만 생성했다.

- proposed SKILL.md draft:
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_vectorfl_space_operator_skill_proposal_v0/01_PROPOSED_SKILL_VECTORFL_SPACE_OPERATOR_SKILL.md

- layout proposal:
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_vectorfl_space_operator_skill_proposal_v0/02_vectorfl_space_operator_skill_layout_v0.json

- assessment:
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_vectorfl_space_operator_skill_proposal_v0/03_vectorfl_space_operator_skill_assessment_v0.json

## 실제 skill 생성 전 수정점

1. run directory 고정 경로를 줄이고 placeholder/relative handle로 바꿔야 함.
2. SKILL.md는 짧게 유지하고 긴 router/contract/schema는 references로 분리.
3. on-demand policy를 반드시 포함해야 함.
4. Gemini는 Codex-side script-chain 내부에서만 가능하다고 명시.
5. authority/current-position/registry/folder/source mutation 금지 유지.

## HOLD

현재는 skill proposal일 뿐이며 ~/.hermes/skills 또는 repo skill tree를 변경하지 않았다.
