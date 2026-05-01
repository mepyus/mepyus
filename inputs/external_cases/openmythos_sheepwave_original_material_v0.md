# OpenMythos Sheepwave Original Material v0

## 1. status

```yaml
material_status: external_original_material_record
source_surface: web / GeekNews / Flamehaven
space_state: unclassified_seed_to_framing_candidate
baseline_lock: false
schema_enforcement: false
implementation: false
promotion: false
```

## 2. source trace

```yaml
geeknews_topic:
  title: "OpenMythos: 공개 연구로 복원한 Claude Mythos 아키텍처 가설인가, 또 다른 AI 하이프인가"
  url: "https://news.hada.io/topic?id=28853"
  author: "flamehaven01"
  published_context: "GeekNews topic, 2026-04-25"
original_article:
  title: "The Sheepwave Has a New Shape: OpenMythos and the Rise of Architecture Hype"
  url: "https://flamehaven.space/writing/the-sheepwave-has-a-new-shape-openmythos-and-the-rise-of-architecture-hype/"
  publisher: "Flamehaven"
  date: "2026-04-24"
related_audit:
  title: "OpenMythos v0.5.0 Code Review - Audit Report"
  url: "https://flamehaven.space/writing/openmythos-v050-code-review---audit-report/"
retrieved_by: "Codex live boundary material intake"
retrieved_at: "2026-04-25"
```

## 3. bounded original summary

OpenMythos is presented as a public-research-based theoretical architecture experiment around Claude Mythos-like ideas, not as a leak, verified reproduction, or production-ready model.

The article uses OpenMythos as a case of "sheepwave": a technically plausible and emotionally attractive architecture story hardening into public confidence before source-level verification catches up.

The main public narrative was driven by claims around recurrent depth, parameter efficiency, MoE, MLA, LTI stabilization, ACT halting, Claude Mythos mystery, and the appeal of smaller models behaving like larger systems.

The article's core distinction is that an AI assistant or online community can be impressed by a README, file structure, and vocabulary before there is operational proof. That reaction is useful as surface reading, but it is not validation.

The related audit separates:

- narrative claims
- implemented mechanisms
- operational training / execution / evaluation paths

The audit finds meaningful technical components, including Prelude + Recurrent Block + Coda structure, LTI recurrent stabilization, MLA cache compression, ACT halt logic, and recurrent depth structure.

The same audit also flags unresolved operational gaps:

- efficiency claims are cited rather than reproduced in the repository
- MoE dispatch has likely throughput risk from nested Python branching
- router bias appears exposed but not clearly updated in the shipped training path
- ACT halt logic lacks an explicit ponder-loss or compute regularization path
- MoDA appears separate rather than integrated into the main model
- large context / large variant settings appear aspirational due to memory and RoPE buffer concerns

The practical conclusion is that OpenMythos is useful as a research artifact and source of architectural ideas, but not proof that architecture alone has overcome scale or production-readiness constraints.

## 4. preserved original distinctions

```yaml
not_this:
  - "Claude Mythos leaked or rebuilt"
  - "small model already thinks like a large model"
  - "README-level architecture claim equals validated system"
  - "AI assistant excitement equals verification"
  - "research artifact equals production-ready path"
more_like_this:
  - "theoretical architecture experiment"
  - "architecture-hype case study"
  - "README / mechanism / operational path separation material"
  - "AI-assisted amplification risk material"
  - "verification-path comparison frame"
```

## 5. initial safe handling

```yaml
current_purpose: "OpenMythos/sheepwave material을 공간의 외부자료로 보존하고 검증 렌즈로 읽기"
source_trace: "GeekNews 28853 + Flamehaven original article + Flamehaven audit report"
initial_boundary: "OpenMythos 채택, architecture claim promotion, baseline 반영 금지"
object_type: "unclassified"
```

## 6. no-promotion warning

This material should not be used as direct evidence for a new architecture doctrine.

It should first be used as a comparison frame for how external technical claims move through:

```text
narrative
→ mechanism
→ operational path
→ verification return
```

