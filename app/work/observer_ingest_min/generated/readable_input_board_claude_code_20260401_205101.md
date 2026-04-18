# readable input board / claude_code_20260401_205101

## 1. 입력 정보
- input_id: `claude_code`
- label: `claude_code`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/claude_code.txt`
- input_kind: `mixed`
- detected_profile: `article`

## 2. split 결과
- split_mode_used: `paragraph`
- raw_line_count: `1066`
- unit_count: `100`

## 3. unit 목록 요약
- unit_001 — paragraph / para_001 ~ para_002 — "별첨 91. 클로드 코드 소스 코드 분석서 분석 대상: claude code source code (2026-03-31)
분석 일자: 2026-04-01
총 소스 파일: 약 1,884개 (TypeScript + Re..."
- unit_002 — paragraph / para_003 ~ para_004 — "Anthropic의 Claude Code 전체 소스 코드가 노출되었습니다. 본 장에서는 해당 소스 코드에 대한 심층 분석 내용을 공유합니다. 다만, 소스 코드 분석서임에도 불구하고 유출된 소스 코드는 단 한 줄도 직..."
- unit_003 — paragraph / para_005 ~ para_006 — "1. Claude Code란 무엇인가
Claude Code는 Anthropic이 만든 공식 CLI(터미널 명령줄) 도구다. 사용자가 터미널에서 Claude AI와 대화하면서 코드를 읽고, 수정하고, 실행할 수 있게 ..."
- unit_004 — paragraph / para_007 ~ para_008 — "기술적으로는 TypeScript로 작성되었고, 터미널 UI는 React 기반의 TUI(Terminal User Interface) 프레임워크인 Ink를 사용한다. 상태 관리는 Zustand 라이브러리를 채택했으며, ..."
- unit_005 — paragraph / para_009 ~ para_009 — "+---------------------+
  |   User types in     |
  |   the terminal      |
  +---------+-----------+
            |
    ..."
- unit_006 — paragraph / para_010 ~ para_011 — "둘째, 대화 루프. 사용자가 메시지를 입력하면, 그 메시지를 Claude API에 보내고, 스트리밍으로 응답을 받는다. 응답 중에 "파일을 읽어라", "명령을 실행해라" 같은 도구 사용 요청이 포함되어 있으면, 해당..."
- unit_007 — paragraph / para_012 ~ para_013 — "넷째, 결과 표시. 터미널에 대화 내용, 도구 실행 결과, 파일 변경 사항 등을 보기 좋게 렌더링한다. 이 네 단계의 핵심은 2단계와 3단계 사이의 루프다. 사용자가 "이 버그를 고쳐줘"라고 한 번 입력하면, Cla..."
- unit_008 — paragraph / para_014 ~ para_015 — "3. 실행 모드
Claude Code는 하나의 프로그램이지만, 상황에 따라 여러 모드로 동작한다. 이것은 마치 하나의 자동차가 도로에서는 일반 모드, 오프로드에서는 4WD 모드, 주차할 때는 저속 모드로 전환되는 것..."
- unit_009 — paragraph / para_016 ~ para_017 — "헤드리스 모드는 UI 없이 프로그래밍 방식으로 실행되는 모드다. Agent SDK나 파이프라인에서 Claude Code를 사용할 때 이 모드가 쓰인다. QueryEngine이라는 클래스가 이 모드의 핵심이며, 쿼리 ..."
- unit_010 — paragraph / para_018 ~ para_019 — "브리지 모드는 로컬 터미널의 Claude Code를 클라우드의 claude.ai 웹 인터페이스와 연결하는 모드다. 웹에서 입력한 명령이 로컬 환경에서 실행되고, 결과가 다시 웹으로 전송된다. 어시스턴트 모드(Kair..."
- unit_011 — paragraph / para_020 ~ para_021 — "어떤 모드를 사용하든 내부의 핵심 엔진은 동일하다. 차이점은 "사용자 입력을 어디서 받느냐"(터미널 키보드? SDK 호출? 웹 인터페이스?)와 "결과를 어디에 보여주느냐"(터미널 UI? JSON 스트림? 웹 페이지?..."
- unit_012 — paragraph / para_022 ~ para_023 — "시작 과정은 여섯 단계로 나뉜다. main.tsx startup sequence
  =========================..."
- unit_013 — paragraph / para_024 ~ para_024 — "[1] Parallel I/O prefetch            (saves ~65ms)
      |-- MDM subprocess read
      |-- macOS Keychain prefetch
     ..."
- unit_014 — paragraph / para_025 ~ para_026 — "2단계: 조건부 모듈 로딩. 코디네이터 모드, 어시스턴트 모드 같은 선택적 기능들은 해당 기능이 활성화되었을 때만 관련 코드를 불러온다. bun 빌드 시스템의 "피처 게이트"라는 메커니즘을 사용하는데, 비활성화된 기..."
- unit_015 — paragraph / para_027 ~ para_028 — "4단계: 인증. 다섯 가지 인증 방식을 우선순위에 따라 시도한다. 5단계: 모델 해석. 어떤 AI 모델을 사용할지 결정한다. 사용자가 명시적으로 지정한 모델이 있으면 그것을 쓰고, 없으면 구독 등급에 따라 기본 모델..."
- unit_016 — paragraph / para_029 ~ para_030 — "6단계: 초기 상태 구성 후 REPL 실행. 모든 준비가 끝나면 초기 상태 객체를 만들고, 선택된 모드에 따라 REPL을 실행하거나 헤드리스 모드로 진입한다. 4.2 컨텍스트 수집
모든 대화에는 두 가지 컨텍스트가 ..."
- unit_017 — paragraph / para_031 ~ para_032 — "Context injection (memoized for session lifetime)
  ================================================== System Context   ..."
- unit_018 — paragraph / para_033 ~ para_034 — "사용자 컨텍스트는 프로젝트의 CLAUDE.md 파일들과 오늘 날짜를 포함한다. CLAUDE.md는 프로젝트별 지침 파일로, Claude Code가 해당 프로젝트에서 어떻게 동작해야 하는지를 담고 있다. 컨텍스트가 중..."
- unit_019 — paragraph / para_035 ~ para_036 — "5. 쿼리 루프 — 핵심 엔진
5.1 기본 구조
query.ts(약 68KB)는 Claude Code의 심장이다. 다른 모든 시스템(도구, 권한, 훅, 상태 관리 등)은 이 파일을 중심으로 동작한다. "비동기 제너레..."
- unit_020 — paragraph / para_037 ~ para_038 — "5.2 턴(Turn)의 처리 흐름
쿼리 루프는 무한 반복문으로 구성되어 있으며, 매 반복(턴)마다 다음 과정을 거친다. Query Loop: one turn
  =====================..."
- unit_021 — paragraph / para_039 ~ para_039 — "+--[1. Message Preprocessing]-------------------------------+
  |                                                       ..."
- unit_022 — paragraph / para_040 ~ para_041 — "2단계: API 호출. 전처리된 메시지, 시스템 프롬프트, 사용자 컨텍스트, 도구 스키마를 Claude API에 보낸다. 응답은 스트리밍으로 도착하며, 텍스트 조각이 도착할 때마다 즉시 사용자에게 표시된다. 3단계:..."
- unit_023 — paragraph / para_042 ~ para_043 — "4단계: 도구 실행. 동시에 실행해도 안전한 도구들은 최대 10개까지 병렬로, 안전하지 않은 도구는 하나씩 순차적으로 실행한다. 결과가 너무 크면 디스크 파일로 저장하고 참조만 넘긴다. 5단계: 후처리. Stop H..."
- unit_024 — paragraph / para_044 ~ para_045 — "구체적인 예시로 이해하기. 사용자가 "auth.ts의 버그를 고쳐줘"라고 입력하면, 실제로 이런 일이 벌어진다. Example: "Fix the bug in auth.ts"
  =====================..."
- unit_025 — paragraph / para_046 ~ para_047 — "Turn 1:  AI: "Let me read the file first."
           --> tool_use: FileRead("auth.ts")
           --> result: [file con..."
- unit_026 — paragraph / para_048 ~ para_049 — "Turn 3:  AI: "Let me verify the fix by running tests."
           --> tool_use: Bash("npm test -- auth.test.ts")
       ..."
- unit_027 — paragraph / para_050 ~ para_051 — "6. QueryEngine — SDK용 래퍼
QueryEngine은 query.ts의 쿼리 루프를 외부 프로그램이 쉽게 사용할 수 있게 감싼 클래스다. External Program (Agent SDK, etc.)
..."
- unit_028 — paragraph / para_052 ~ para_053 — "7. 도구(Tool) 시스템
7.1 도구란 무엇인가
"도구"는 Claude가 외부 세계와 상호작용하기 위한 수단이다. 이것은 Claude Code에서 가장 중요한 개념이다. Claude AI는 그 자체로는 텍스트만 ..."
- unit_029 — paragraph / para_054 ~ para_055 — "이런 구조 덕분에 AI의 능력은 "어떤 도구가 제공되느냐"에 따라 확장된다. 45개 이상의 내장 도구가 있으며, MCP(Model Context Protocol)를 통해 GitHub, Slack, 데이터베이스 같은 ..."
- unit_030 — paragraph / para_056 ~ para_056 — "Every Tool has:
  +-----------------------------------------------------------------+
  |  name          "BashTool", "Fi..."
- unit_031 — paragraph / para_057 ~ para_058 — "Tool Assembly Pipeline
  ====================== getAllBaseTools()                     44+ tools registered
        |
   ..."
- unit_032 — paragraph / para_059 ~ para_060 — "7.4 주요 도구 설명
  Tool Categories
  =============== File Operations     Shell          Search          Web
  +-------------..."
- unit_033 — paragraph / para_061 ~ para_061 — "Agent/Team          Planning        Tasks           Skill
  +-------------+  +-----------+   +----------+   +----------+..."
- unit_034 — paragraph / para_062 ~ para_063 — "AgentTool — "다른 AI를 고용하는" 도구다. 복잡한 작업을 만나면, 메인 AI가 서브에이전트(작은 AI 일꾼)를 만들어서 부분 작업을 위임한다. 서브에이전트는 다섯 가지 방식으로 실행될 수 있다: 같은 프..."
- unit_035 — paragraph / para_064 ~ para_065 — "GrepTool — ripgrep 기반 텍스트 검색. 세 가지 출력 모드(content, files_with_matches, count)와 기본 250개 결과 제한을 지원한다. 8. 도구 실행 오케스트레이션
8.1 ..."
- unit_036 — paragraph / para_066 ~ para_067 — "Tool Execution Pipeline (for each tool_use block)
  ================================================== [1] Lookup tool b..."
- unit_037 — paragraph / para_068 ~ para_069 — "Tool Concurrency: Partitioning Algorithm
  ========================================= Input:  [Read] [Grep] [Glob] [Edit]..."
- unit_038 — paragraph / para_070 ~ para_071 — "Batch 1: [Read, Grep, Glob]  --> parallel (up to 10)
  Batch 2: [Edit]              --> serial (alone)
  Batch 3: [Read,..."
- unit_039 — paragraph / para_072 ~ para_073 — "8.3 스트리밍 도구 실행기
API 응답이 아직 스트리밍 중일 때부터 이미 도착한 도구 사용 블록의 실행을 시작하는 최적화가 있다. Streaming Tool Executor (overlaps API streamin..."
- unit_040 — paragraph / para_074 ~ para_075 — "Time ---> API stream:   [...text...][tool_use A][...text...][tool_use B][done]
                                |        ..."
- unit_041 — paragraph / para_076 ~ para_077 — "9. 명령어(Command) 시스템
명령어는 사용자가 슬래시(/)로 시작하는 입력을 통해 호출하는 기능이다. 도구(Tool)가 "AI가 사용하는 기능"이라면, 명령어(Command)는 "사용자가 직접 사용하는 기능"..."
- unit_042 — paragraph / para_078 ~ para_079 — "/commit, /review ...       /settings, /doctor ...    /help ...
  +-------------------+      +-------------------+     +-..."
- unit_043 — paragraph / para_080 ~ para_081 — "10. 태스크(Task) 시스템
태스크는 백그라운드에서 실행되는 비동기 작업을 관리하는 시스템이다. "지금 당장 결과가 필요하지 않은 작업"을 백그라운드로 보내서, 사용자가 다른 일을 하는 동안 처리되게 하는 것이 ..."
- unit_044 — paragraph / para_082 ~ para_083 — "Spawn                  Register               Run in background
  (BashTool async,  -->  AppState.tasks[id]  --> output ..."
- unit_045 — paragraph / para_084 ~ para_085 — "11. 상태 관리
11.1 AppState — 글로벌 상태
Claude Code의 모든 글로벌 상태는 AppState라는 하나의 큰 타입으로 정의된다. "상태(state)"란 프로그램이 현재 기억하고 있는 모든 정보..."
- unit_046 — paragraph / para_086 ~ para_087 — "AppState (DeepImmutable)
  ======================== +-- Settings & Config ----+  +-- UI State -----------+
  |  settings..."
- unit_047 — paragraph / para_088 ~ para_089 — "+-- Agent / Team ---------+  +-- Tasks ---------------+
  |  agentNameRegistry      |  |  tasks (mutable!)      |
  |  t..."
- unit_048 — paragraph / para_090 ~ para_091 — "+-- Bridge / Remote -----+   +-- Feature Flags -------+
  |  replBridgeConnected   |   |  kairosEnabled         |
  |  r..."
- unit_049 — paragraph / para_092 ~ para_093 — "12.1 API 클라이언트와 재시도
API 클라이언트는 Claude API와의 모든 통신을 담당하며, 약 3,000줄에 달한다. 주요 역할은 세 가지다. 베타 기능 조립은 사용하는 모델의 능력에 따라 thinking..."
- unit_050 — paragraph / para_094 ~ para_095 — "API Retry Strategy
  ================== Error        Action
  -----        ------
  429          retry-after < 500ms? wa..."
- unit_051 — paragraph / para_096 ~ para_097 — "529          3 consecutive? switch to fallback model
  (overloaded) non-foreground tasks: give up immediately 401       ..."
- unit_052 — paragraph / para_098 ~ para_099 — "ECONNRESET   disable keep-alive, recreate client
  EPIPE Persistent   retry forever with exponential backoff
  mode (ANT..."
- unit_053 — paragraph / para_100 ~ para_101 — "Auto-Compact Flow
  ================= Token usage > threshold?
        |
        v
  Circuit breaker check (3 consecutiv..."
- unit_054 — paragraph / para_102 ~ para_103 — "MCP Server Connection States
  ============================= Connected ----> Failed -----> NeedsAuth
      ^            ..."
- unit_055 — paragraph / para_104 ~ para_105 — "Transport Types:
    Stdio ------> spawn local process
    SSE/HTTP ---> connect to remote server
    WebSocket --> bidi..."
- unit_056 — paragraph / para_106 ~ para_107 — "13. 권한(Permission) 시스템
13.1 왜 권한 시스템이 필요한가
Claude Code는 사용자 컴퓨터에서 파일을 수정하고 명령을 실행할 수 있다. 이는 강력하지만 위험하다. AI가 잘못된 판단으로 중요한..."
- unit_057 — paragraph / para_108 ~ para_108 — "Tool use request arrives
        |
  [1]   v
  validateInput()            Is the input semantically valid?
        |
  [..."
- unit_058 — paragraph / para_109 ~ para_110 — "Rule sources (highest to lowest priority):
    Local settings > Project settings > User settings > Flags > Policy
Defaul..."
- unit_059 — paragraph / para_111 ~ para_112 — "Plan 모드는 코드를 실제로 변경하지 않고, 읽기 전용 도구만 허용하는 "계획 수립 전용" 모드다. AI가 코드를 분석하고 계획을 세우지만, 실행은 사용자가 승인한 후에만 이루어진다. Bypass 모드는 모든 것을..."
- unit_060 — paragraph / para_113 ~ para_114 — "14. 훅(Hook) 시스템
훅은 특정 이벤트가 발생했을 때 자동으로 실행되는 사용자 정의 동작이다. 훅을 이해하려면 "이벤트 리스너"를 떠올리면 된다. 웹 페이지에서 버튼 클릭 이벤트에 함수를 등록하듯, Claud..."
- unit_061 — paragraph / para_115 ~ para_115 — "SessionStart                                        Stop
      |                                                |
      ..."
- unit_062 — paragraph / para_116 ~ para_117 — "Hook Response Controls:
    continue: false  --> stop current operation
    decision: block  --> deny the tool execution..."
- unit_063 — paragraph / para_118 ~ para_119 — "Tools vs Skills vs Plugins vs Commands
  ======================================== Tool       Low-level, atomic action   ..."
- unit_064 — paragraph / para_120 ~ para_121 — "Skill      High-level, reusable template   "Review this code"
             Invoked by user as /command      "Create a co..."
- unit_065 — paragraph / para_122 ~ para_123 — "Command    User-facing / shortcut          /help, /settings, /model
             Can be prompt-type or UI-type
  Skill S..."
- unit_066 — paragraph / para_124 ~ para_124 — "~/.claude/skills/                     src/skills/bundled/
  .claude/skills/                       registerBundledSkill()..."
- unit_067 — paragraph / para_125 ~ para_126 — "15.2 플러그인
플러그인은 스킬보다 상위 개념으로, 스킬, 훅, MCP 서버를 하나의 패키지로 묶은 것이다. 스킬이 "개별 기능"이라면, 플러그인은 "기능 모음집"이다. 예를 들어 "GitHub 통합" 플러그인은 ..."
- unit_068 — paragraph / para_127 ~ para_128 — "BuiltinPlugin
  +--------------------------------------------+
  |  name: "github-integration"                |
  |     ..."
- unit_069 — paragraph / para_129 ~ para_130 — "16. UI 레이어 16.1 자체 제작 TUI 프레임워크 (Ink)
Claude Code의 터미널 UI는 React를 기반으로 한 자체 제작 TUI 프레임워크를 사용한다. 왜 기존 터미널 라이브러리를 쓰지 않고 자체..."
- unit_070 — paragraph / para_131 ~ para_132 — "Ink TUI Rendering Pipeline
  =========================== React component update
        |
        v
  Reconciler calcula..."
- unit_071 — paragraph / para_133 ~ para_134 — "Memory optimization:
    CharPool ------> intern strings (one copy of "hello")
    StylePool -----> intern ANSI codes + ..."
- unit_072 — paragraph / para_135 ~ para_136 — "객체 풀링은 같은 문자열이나 스타일을 여러 번 사용할 때, 메모리에 하나만 저장하고 인덱스로 참조하는 기법이다. 터미널 화면에는 같은 색상, 같은 글자가 반복되므로 메모리를 크게 절약한다. 더티 추적은 변경된 부분만..."
- unit_073 — paragraph / para_137 ~ para_138 — "프레임 조절은 업데이트 빈도를 제한하여 터미널이 느려지는 것을 방지한다. 16.2 화면 구성
  REPL Screen Layout
  ===================..."
- unit_074 — paragraph / para_139 ~ para_139 — "+---------------------------------------------------+
  |  Logo Header (memoized, rarely re-renders)         |
  +------..."
- unit_075 — paragraph / para_140 ~ para_141 — "Keybinding Contexts
  ==================== Global:       Ctrl+C = interrupt,  Ctrl+D = exit,  Ctrl+T = tasks
  Chat:    ..."
- unit_076 — paragraph / para_142 ~ para_143 — "Chord support:  Ctrl+K -> Ctrl+S  (two-key sequence)
                  First key enters "chord started" state
          ..."
- unit_077 — paragraph / para_144 ~ para_145 — "왜 브리지가 필요한가? claude.ai 웹 인터페이스에서 "이 프로젝트의 테스트를 실행해줘"라고 요청했을 때, 그 테스트는 사용자의 로컬 컴퓨터에서 실행되어야 한다(코드가 거기에 있으니까). 하지만 웹 브라우저에서..."
- unit_078 — paragraph / para_146 ~ para_146 — "claude.ai (web)               Local Machine
  +----------------+            +---------------------------+
  |  User type..."
- unit_079 — paragraph / para_147 ~ para_148 — "Multi-session: up to 32 parallel sessions
  Dedup: BoundedUUIDSet (circular buffer, fixed memory) Token Refresh:
    CCR..."
- unit_080 — paragraph / para_149 ~ para_150 — "Backoff:
    Connection errors: 2s -> 120s (cap), give up after 10 min
    General errors:    500ms -> 30s (cap)
    Shu..."
- unit_081 — paragraph / para_151 ~ para_152 — "Remote Session WebSocket
  ========================= wss://api.anthropic.com/v1/sessions/ws/{sessionId}/subscribe..."
- unit_082 — paragraph / para_153 ~ para_154 — "State Machine: closed ---(connect)---> connecting ---(onopen)---> connected
    ^                                       ..."
- unit_083 — paragraph / para_155 ~ para_156 — "Reconnection:
    - General disconnect: max 5 attempts, 2s delay
    - Session not found (4001): 3 retries (transient du..."
- unit_084 — paragraph / para_157 ~ para_158 — "19. 코디네이터(Coordinator) 모드
코디네이터 모드는 하나의 "리더" 에이전트가 여러 "워커" 에이전트를 관리하는 멀티에이전트 오케스트레이션 시스템이다. 비유하자면, 한 명의 시니어 개발자(리더)가 여러 ..."
- unit_085 — paragraph / para_159 ~ para_159 — "+-------------------+
                  |  LEADER (main)    |
                  |  - AgentTool      |  Does NOT edit cod..."
- unit_086 — paragraph / para_160 ~ para_161 — "Work Phases: [1] Research     Multiple workers in parallel
      (parallel)   Each explores different files/angles
     ..."
- unit_087 — paragraph / para_162 ~ para_163 — "종합 단계에서 중요한 규칙이 있다: 리더는 반드시 워커의 결과를 직접 이해해야 한다. "워커가 알아서 했을 테니 넘어가자"는 식의 위임은 금지된다. 이를 통해 리더가 전체 맥락을 놓치지 않고 올바른 결정을 내릴 수 ..."
- unit_088 — paragraph / para_164 ~ para_165 — "Memory System Structure
  ======================== ~/.claude/projects/{project-slug}/memory/
  |
  +-- MEMORY.md        ..."
- unit_089 — paragraph / para_166 ~ para_167 — "Memory Types: +----------+--------------------------------------------------+
  | user     | Who the user is. Role, expe..."
- unit_090 — paragraph / para_168 ~ para_169 — "NOT saved: code patterns, architecture, git history,
             debugging recipes, anything already in CLAUDE.md
각 메모리..."
- unit_091 — paragraph / para_170 ~ para_171 — "21.2 설정 소스 우선순위
  Settings Priority (highest to lowest)
  ====================================== [1] Local     .claude/s..."
- unit_092 — paragraph / para_172 ~ para_173 — "샌드박스 — 도구 실행을 격리된 환경에서 수행한다. //path는 절대 루트, /path는 설정 파일 기준 상대, ~/path는 홈 디렉토리를 의미한다. 토큰 계산 — tokenCountWithEstimation()..."
- unit_093 — paragraph / para_174 ~ para_175 — "스웜/팀 관리 — 팀 파일(TeamFile)을 통해 에이전트 간 협업을 관리한다. 인프로세스 러너는 메시지 라우팅, 도구 필터링, 권한 동기화를 처리한다. 글로벌 세션 상태 (56KB) — 세션 ID, 누적 비용, ..."
- unit_094 — paragraph / para_176 ~ para_177 — "23. 핵심 설계 패턴
마지막으로, Claude Code 전반에서 반복적으로 나타나는 설계 패턴 여덟 가지를 정리한다. 이 패턴들을 이해하면 코드의 어떤 부분을 보더라도 "아, 이건 이 패턴이구나"하고 빠르게 파악할..."
- unit_095 — paragraph / para_178 ~ para_179 — "[1] Generator Streaming     query() yields events one-by-one
                              --> real-time display of AI "..."
- unit_096 — paragraph / para_180 ~ para_181 — "[3] Memoized Context        getSystemContext(), getUserContext()
                              --> computed once, cached..."
- unit_097 — paragraph / para_182 ~ para_183 — "[5] Lazy Import             Wrap in function to avoid circular deps
                              --> loaded only when a..."
- unit_098 — paragraph / para_184 ~ para_185 — "[7] Interruption            Save transcript BEFORE query loop
      Resilience              --> crash mid-API = resume f..."
- unit_099 — paragraph / para_186 ~ para_186 — "User runs "claude" in terminal
        |
        v
  main.tsx
  +-- Auth (OAuth / API key / Bedrock / Vertex)
  +-- Mode..."
- unit_100 — paragraph / para_187 ~ para_187 — "사용자가 터미널에서 Claude Code를 실행하면, main.tsx가 인증, 모델 해석, 설정 로딩, 컨텍스트 수집을 수행한 후 REPL을 시작한다. 사용자가 메시지를 입력하면, 메시지가 정규화되어 Claude A..."

## 4. 당장 읽히는 흐름
- 입력은 중간 단위 block으로 나뉘었고, 앞/중간/뒤 흐름을 빠르게 재확인하기 좋은 분해다.

