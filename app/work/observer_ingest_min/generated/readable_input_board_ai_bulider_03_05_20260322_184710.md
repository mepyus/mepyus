# readable input board / ai_bulider_03_05_20260322_184710

## 1. 입력 정보
- input_id: `ai_bulider_03_05`
- label: `AI_bulider_03_05`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/AI_bulider_03_05.md`
- input_kind: `mixed`
- detected_profile: `article`

## 2. split 결과
- split_mode_used: `paragraph`
- raw_line_count: `226`
- unit_count: `46`

## 3. unit 목록 요약
- unit_001 — paragraph / para_001 ~ para_002 — "니어 개발자가 AI와 6개월간 25만 라인의 시스템을 만들며 발견한 것들
나에게 딱 맞는 바퀴를 만드는 시대
Kim, min tae
Kim, min tae Follow
26 min read
·
Mar 5, 2026
..."
- unit_002 — paragraph / para_003 ~ para_004 — "AI 와 함께 25만 줄 규모의 프로젝트를 만들었습니다. 한 사람이, 6개월 만에! AI가 폭발적인 생산성을 제공한다는 건 이미 많은 분이 체감하고 계실 겁니다. 하지만 규모가 커지면 다른 문제가 보이기 시작합니다...."
- unit_003 — paragraph / para_005 ~ para_006 — "Baden for Claude Code
0에서 25만 라인까지
Day1Company에서 Methii라는 서비스를 개발하고 있습니다. 업계에 오래 있었지만, AI 코딩 에이전트를 개발의 중심에 놓고 본격적으로 작업하기..."
- unit_004 — paragraph / para_007 ~ para_008 — "Methii는 그래프 기반 학습 캔버스 서비스입니다. 사용자가 어떤 주제에 대해 학습 트리를 만들면, AI가 콘텐츠를 생성하고, 캔버스 위에서 지식 구조를 시각화합니다. 여기에 퀴즈, 콘텐츠 스타일 변환, 다국어 지..."
- unit_005 — paragraph / para_009 ~ para_010 — "이후에는 Claude와 단독으로 작업하며 규모를 키워갔습니다. 6개월이 지난 지금, Methii의 코드베이스는 이렇게 생겼습니다. 소스 파일 1,271개. 코드 약 249,000줄. Turborepo 모노레포 안에 ..."
- unit_006 — paragraph / para_011 ~ para_012 — "Git 커밋 1,185개. 컨트리뷰터 1명. 설계와 판단은 제가 했고, 실행은 AI가 했습니다. 이 조합은 폭발적인 생산성을 만들어냈습니다. 한 사람이 이 규모의 시스템을 6개월 만에 만들 수 있었던 건 분명히 AI..."
- unit_007 — paragraph / para_013 ~ para_014 — "AI는 읽었다고 착각한다
Methii의 LLM 파이프라인에는 Prompteer라는 자체 제작 프롬프트 관리 라이브러리가 있습니다. LLM 기반 서비스를 만들다 보면 프롬프트 관리가 금방 복잡해지는데, 오픈소스에 이를..."
- unit_008 — paragraph / para_015 ~ para_016 — "더 근본적인 문제는 따로 있었습니다. AI가 Prompteer의 문법 문서를 실제로 읽지 않고도, “읽은 것 같다”는 추론 위에서 작업을 진행한다는 것이었습니다. 파일을 열어 확인하는 도구를 갖고 있으면서도, 실제로..."
- unit_009 — paragraph / para_017 ~ para_018 — "Press enter or click to view image in full size Methii Knowledge Tree GCS
AI는 엄청난 분량의 작업을 빠르게 처리합니다. 하지만 실제로 확인하지 않고 매우 ..."
- unit_010 — paragraph / para_019 ~ para_020 — "문서는 특정 시점의 스냅샷일 뿐이다
처음에는 문서로 시스템을 설명했습니다. AI에게 코드베이스를 이해시키기 위해 상세한 설계 문서를 작성했습니다. 에디터 콘텐츠 아키텍처, 이벤트 시스템, i18n 아키텍처, 빌링 시..."
- unit_011 — paragraph / para_021 ~ para_022 — "문서와 코드의 불일치가 조금씩 쌓이기 시작했습니다. 처음에는 사소했습니다. 문서에는 ApiService라고 되어 있지만 코드에서는 이미 httpClient 싱글톤으로 전환된 상태. 문서에는 컨트롤러에 비즈니스 로직이..."
- unit_012 — paragraph / para_023 ~ para_024 — "결국 하나의 결론에 도달했습니다. 시스템을 설명하는 것은 코드 그 자체여야 합니다. 문서는 특정 시점의 스냅샷일 뿐이고, 코드만이 항상 현재 상태를 정확하게 반영합니다. 그런데 코드가 시스템을 스스로 설명하려면, 코..."
- unit_013 — paragraph / para_025 ~ para_026 — "그리고 품질을 유지하는 버팀목은 규칙입니다. 규칙도 코드와 함께 유지되어야 하는 대상입니다. 이 생각의 전환이, 이후 모든 것의 출발점이 됐습니다...."
- unit_014 — paragraph / para_027 ~ para_028 — "규칙에서 파이프라인으로
코드 품질을 지키는 규칙을 만들기로 했습니다. 그런데 어떤 규칙을 만들 것인가? ESLint 같은 정적 분석 도구로 잡을 수 있는 것들 — unused imports, 세미콜론 스타일, 들여쓰..."
- unit_015 — paragraph / para_029 ~ para_030 — "“컨트롤러에서 50줄 이상의 복잡한 비즈니스 로직을 직접 작성하지 않는다.” “다른 도메인과의 상호작용을 정확히 이해한다.” “핵심 작업은 에러가 전파되어야 한다.” “레이아웃 계산을 렌더링 사이클 내에서 수행하지 ..."
- unit_016 — paragraph / para_031 ~ para_032 — "Press enter or click to view image in full size INDEX.yaml
여기서 핵심적인 설계 결정이 있었습니다. INDEX.yaml이라는 트리거 매핑 파일을 만들어, 수정 대상 파일..."
- unit_017 — paragraph / para_033 ~ para_034 — "Press enter or click to view image in full size rules/concerns/registry-pattern.md
규칙을 만들었습니다. 그런데 규칙은 만드는 것보다 지켜지게 하는 것..."
- unit_018 — paragraph / para_035 ~ para_036 — "작업 에이전트에게 “규칙을 확인하고 준수하라”고 지시할 수는 있습니다. 하지만 이건 자기 코드를 자기가 심판하는 구조입니다. 앞서 보았듯이 AI는 확인하지 않고도 “확인했다고 착각”할 수 있습니다. 규칙을 실제로 읽..."
- unit_019 — paragraph / para_037 ~ para_038 — "Press enter or click to view image in full size .claude/agents/rule-guard.md
작업 흐름은 이렇습니다. 작업 에이전트가 수정 계획을 세우면, Rule Gua..."
- unit_020 — paragraph / para_039 ~ para_040 — "그런데 여기서 한 가지 문제를 더 풀어야 했습니다. 검증 결과가 구조화되지 않으면, 어떤 규칙이 자주 위반되는지, 어떤 도메인이 취약한지, 시간이 지나면서 품질이 나아지고 있는지 파악할 수 없습니다. Rule Gua..."
- unit_021 — paragraph / para_041 ~ para_042 — "Press enter or click to view image in full size CLAUDE.md 의 Rule Gard 지침
이 프로토콜이 존재하는 이유는, 이 데이터가 최종적으로 흘러들어갈 곳이 있기 때문입니..."
- unit_022 — paragraph / para_043 ~ para_044 — "AI의 기억은 믿을 수 없다
규칙도 만들었고, 파수꾼도 세웠습니다. 그런데 더 근본적인 문제가 남아 있었습니다. Claude Code에서 작업이 길어지면 컨텍스트 압축(context compaction)이 일어납니다..."
- unit_023 — paragraph / para_045 ~ para_046 — "지침이 프롬프트 수준에만 존재하는 한, 이 문제는 구조적으로 해결할 수 없습니다. AI의 기억은 본질적으로 불안정하고, 그 위에 세운 모든 약속은 시간이 지나면 흔들립니다. 이 문제에 대해 여러 방면에서 접근했습니다..."
- unit_024 — paragraph / para_047 ~ para_048 — "첫째, CLAUDE.md를 극도로 절제했습니다. 25만 줄 코드베이스의 모노레포 전체를 다루면서도 134줄. Baden 보고 지침, Rule Guard 흐름, 아키텍처 개요, 개발 명령어 — 에이전트가 알아야 할 최..."
- unit_025 — paragraph / para_049 ~ para_050 — "Press enter or click to view image in full size AI의 기억이 희석되는 정확한 시점에, 지침을 기계적으로 재주입하는 것입니다. 이건 프롬프트 수준의 해결이 아니라 인프라 수준의 ..."
- unit_026 — paragraph / para_051 ~ para_052 — "그런데 아직 하나가 빠져 있습니다. 이 모든 장치가 실제로 작동하고 있는지 어떻게 확인할 것인가? Baden — 관측할 수 없으면 통제할 수 없다
규칙을 만들었습니다. 파수꾼을 세웠습니다. 기억 소실에 대한 보정 장..."
- unit_027 — paragraph / para_053 ~ para_054 — "Get Kim, min tae’s stories in your inbox
Join Medium for free to get updates from this writer. Enter your email
Subscrib..."
- unit_028 — paragraph / para_055 ~ para_056 — "Remember me for faster sign in 에이전트가 지금 규칙을 실제로 참조하고 있는지, Rule Guard를 호출했는지, 파일을 탐색은 했는지, 검증은 거쳤는지 — 이것들을 실시간으로 볼 수 있어야 ..."
- unit_029 — paragraph / para_057 ~ para_058 — "설계 철학: 자유 서술, 사후 분류
Baden의 가장 핵심적인 설계 결정은 에이전트에게 고정된 이벤트 타입을 강요하지 않는다는 것입니다. 에이전트가 행동을 보고할 때, read_auth_logic, modify_ha..."
- unit_030 — paragraph / para_059 ~ para_060 — "이 접근법은 AI의 특성을 정면으로 반영합니다. AI 에이전트는 미리 정해진 분류 체계를 외우고 매번 정확하게 맞추는 일에 강하지 않습니다. 앞서 본 것처럼, 명시적 지침이 있어도 학습 데이터의 관성에 끌려가거나, ..."
- unit_031 — paragraph / para_061 ~ para_062 — "Press enter or click to view image in full size CLAUDE.md
MCP 도구: 에이전트와의 접점
Baden은 MCP(Model Context Protocol)를 통해 에이전트와..."
- unit_032 — paragraph / para_063 ~ para_063 — "baden_start_task: 사용자가 새로운 지시를 내리면 가장 먼저 호출합니다. 프로젝트 이름과 사용자의 지시 내용을 받아 taskId를 반환합니다. 이후 같은 작업의 모든 보고에 이 taskId가 포함되어, ..."
- unit_033 — paragraph / para_064 ~ para_065 — "타임라인: 에이전트의 작업 패턴을 공간으로 펼치다
Baden 대시보드의 중심은 타임라인 뷰입니다. 가로축은 시간, 세로축은 행동의 성격에 따라 다섯 개 레인으로 나뉩니다. User: 사용자가 에이전트에게 내린 지시와..."
- unit_034 — paragraph / para_066 ~ para_067 — "이 구조가 드러내는 것은 단순한 이벤트의 나열이 아니라 에이전트의 작업 패턴 자체입니다. 좋은 에이전트 작업은 Exploration → Planning → Implementation → Rules의 흐름을 자연스럽게..."
- unit_035 — paragraph / para_068 ~ para_069 — "하나의 사용자 지시에서 시작된 모든 행동은 taskId로 연결됩니다. 타임라인에서는 이 연결이 L자형 연결선으로 시각화되어, 복잡한 작업에서도 인과 관계의 흐름을 놓치지 않습니다. 메인 에이전트가 Rule Guard..."
- unit_036 — paragraph / para_070 ~ para_071 — "규칙 검증의 시각화
Rules 레인에서는 Rule Guard의 검증 사이클이 실시간으로 표시됩니다. 대시보드 상단의 카운터 — Check 58, Violation 7, Pass 69 — 가 현재 세션의 규칙 준수 상..."
- unit_037 — paragraph / para_072 ~ para_073 — "예를 들어 rule_violation 이벤트를 클릭하면, 어떤 규칙(S-temporal)을 위반했는지, 어떤 파일(generate-goalmap-content.workflow.ts)의 어떤 항목("MUST NOT: ..."
- unit_038 — paragraph / para_074 ~ para_075 — "아키텍처
서버는 Express + SQLite + WebSocket. SQLite를 선택한 건 로컬 도구의 성격에 정확히 맞기 때문입니다. 별도의 데이터베이스 서버 없이 ~/.baden/baden.db 파일 하나로 ..."
- unit_039 — paragraph / para_076 ~ para_077 — "MCP 서버는 @modelcontextprotocol/sdk 기반의 stdio 트랜스포트로, 에이전트 쪽의 실패가 모니터링 시스템에 영향을 주지 않도록 에러를 조용히 무시하는 설계를 채택했습니다. 모니터링 도구가 작..."
- unit_040 — paragraph / para_078 ~ para_079 — "INDEX.yaml과의 연동
Baden은 프로젝트의 rules/INDEX.yaml을 파싱하여 규칙 메타데이터를 등록합니다. 규칙 파일의 마크다운 본문을 렌더링하여 대시보드에서 직접 열람할 수 있고, 각 규칙별 참조/..."
- unit_041 — paragraph / para_080 ~ para_081 — "나에게 딱 맞는 바퀴
결과부터 말씀드리면, 이 파이프라인은 효과가 있었습니다. 최근 2개월간 제가 직접 코드를 작성한 경우는 전무합니다. 설계하고, 판단하고, 지시하고, 결과를 검토하는 것이 저의 역할입니다. 실행은..."
- unit_042 — paragraph / para_082 ~ para_083 — "물론 이 시스템이 완벽하지는 않습니다. CLAUDE.md 기반의 보고 강제는 결국 에이전트가 지침을 따르느냐에 의존하는 부분이 있고, Hooks로 보정하더라도 100%를 보장할 수는 없습니다. Rule Guard 역..."
- unit_043 — paragraph / para_084 ~ para_085 — "하지만 이 경험 전체를 관통하는 더 큰 이야기가 있습니다. 개발자의 세계에는 오래된 격언이 있습니다. “바퀴를 재발명하지 마라.” 그래서 우리는 늘 이미 있는 바퀴를 찾아 씁니다. 대부분의 경우 그게 맞습니다. 하지..."
- unit_044 — paragraph / para_086 ~ para_087 — "AI 시대에 이것이 근본적으로 달라졌습니다. “나에게 딱 맞는 최적의 바퀴”를 만드는 데 주저함이 없어졌습니다. 101개의 프롬프트 템플릿을 관리하는 데 딱 맞는 프롬프트 매니저가 필요했습니다 — Prompteer를..."
- unit_045 — paragraph / para_088 ~ para_089 — "이것이 가능했던 건 AI가 실행력을 제공하기 때문입니다. 제가 가진 건 오래 일하며 쌓인 설계 감각과, “이건 이렇게 되어야 한다”는 판단력입니다. AI가 가진 건 그 판단을 코드로 빠르게 실현하는 실행력입니다. 이..."
- unit_046 — paragraph / para_090 ~ para_092 — "AI 에이전트의 능력은 계속 발전할 것입니다. 컨텍스트 윈도우는 더 커질 것이고, 추론 능력은 더 정확해질 것이고, 기억 소실 문제도 점차 개선될 것입니다. 하지만 발전하면 할수록, 아니 발전하면 할수록 — “에이전..."

## 4. 당장 읽히는 흐름
- 앞쪽은 소개/문제제기, 중간은 설명 확장, 뒤로 갈수록 주제 전환이 생기는 흐름으로 읽힌다.

