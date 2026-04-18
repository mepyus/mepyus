# VectorFL UI Blueprint: Flow-Centric Canvas
Date: 2026-04-15
Role: Codex Handoff Specification

## 1. Design Philosophy
- **From Panels to Flow**: Card/Panel 구조를 폐기하고, 연속적인 3단 캔버스 워크플로우로 전환.
- **Product-Ready Aesthetics**: `slate-50` 배경을 사용하여 제품 수준의 차분하고 현대적인 톤앤매너 구현.
- **State Persistence**: `Tabs`의 unmount 전략을 폐기하고 `CSS Grid` 내 레이어 기반 상태 유지를 수행.

## 2. Layout Schema (Codex Implementation Guide)

```tsx
// Grid Architecture
<div className="grid grid-cols-[300px_1fr_400px] h-screen bg-slate-50">
  {/* [User Surface] Command Rail: Input & Intent-based Goal */}
  <section className="border-r border-slate-200">...</section>

  {/* [VectorFL Surface] Maturation Canvas: Fragment Flow */}
  <main className="overflow-hidden flex flex-col">...</main>

  {/* [Engine Surface] Inspect Tray: Audit & State */}
  <aside className="border-l border-slate-200 shadow-xl">...</aside>
</div>
```

## 3. Core Implementation Directives
- **Remove Cards**: 모든 패널 내부의 `Card` 컴포넌트를 제거하고, `Surface`의 기본 여백(`padding`)과 간격으로 정보를 분리할 것.
- **Component Lifecycle**: `ui-components.tsx`의 `Tabs` 내 로직을 `FragmentRegistry` Context를 사용하도록 변경하여 `unmount`시 상태가 소실되지 않도록 수정.
- **Visual Grammar**:
  - 배경: `bg-slate-50`
  - 텍스트: `text-slate-900`
  - 보더: `border-slate-200`
  - 상태 배지: 투명도 높은 배경색(Primary 100)으로 부드럽게 표현.

## 4. Why this matters (Context for Codex)
기존 구조는 패널이 정보를 가두어 사고의 흐름을 끊고 있습니다. 본 변경은 파편화된 정보를 사용자의 작업 궤적(Workflow) 위로 안착시키기 위함입니다. 헌법 제4조(관심사의 분리)에 따라 3면이 서로 연결되면서도 독립적으로 동작해야 합니다.

---
*Note: This specification is intended for the Codex agent to implement in the next integration step.*
