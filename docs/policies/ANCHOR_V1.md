# Anchor V1

## Purpose

Anchor is not a simple tag.

Anchor is the intermediate structure that connects:

- source recovery
- processing values
- space interaction

In replica terms:

`source <-> anchor <-> processing values <-> space`

## Why Anchor Matters

The replica ingests repeated materials from a narrow topic domain:

- AI papers
- reviews
- youtube transcripts
- summaries
- topic-focused notes

The useful question is not just "what document is stored?"

The useful questions are:

- what topic axis repeats across sources?
- what fragments overlap across different sources?
- what fragment behaves as method, failure, evidence, or background?
- what should connect in space and what should remain apart?

Anchor is the working connection protocol for those questions.

## Difference From Tags

Tag:

- often document-level
- human-applied
- broad and loose
- mostly for grouping or search

Anchor:

- fragment-level
- derived or normalized from source evidence
- keeps provenance and recovery coordinates
- affects space interaction
- must support explanation of why a connection exists

## Core Roles

Anchor has five roles:

1. recovery
2. grouping
3. distinction
4. space projection
5. explanation

## Recommended Layers

Use these four layers first:

1. `source_anchor`
2. `object_anchor`
3. `semantic_anchor`
4. `structural_anchor`

Do not open relational anchors as a core requirement yet.

## Layer Definitions

### 1. Source Anchor

Purpose:

- source recovery
- provenance trace

Current replica fields already partially cover this:

- `source_path`
- `source_range`
- `page_ref`
- `paragraph_index`

### 2. Object Anchor

Purpose:

- identify what the fragment is about
- group fragments around the same object or component

Examples:

- `model.transformer`
- `pipeline.rag`
- `component.retriever`
- `benchmark.mmlu`
- `artifact.prompt_cache`

### 3. Semantic Anchor

Purpose:

- identify what meaning or issue is being discussed
- group fragments even when wording differs

Examples:

- `retrieval.failure`
- `context.window.limit`
- `tool.use.coordination`
- `evaluation.bias`
- `hallucination.risk`
- `cost.efficiency.tradeoff`

### 4. Structural Anchor

Purpose:

- identify what role the fragment plays in discourse
- distinguish claim/evidence/background/bridge/limit even under the same topic

Examples:

- `role.claim`
- `role.evidence`
- `role.counterexample`
- `role.method`
- `role.definition`
- `role.background`
- `role.failure_mode`
- `role.limit`
- `role.bridge`
- `role.open_question`

## Current Replica Position

Current implementation status:

- `source_anchor`: partially alive
- `object_anchor`: weak, shallow
- `semantic_anchor`: weak, shallow
- `structural_anchor`: missing

Current bottleneck:

- anchors exist, but still behave too much like extracted tokens
- connections need anchors that act as reasons, not just searchable terms

## Anchor V1 Adoption Rule

For the next implementation steps:

- preserve current source recovery fields as `source_anchor` baseline
- improve anchor extraction toward `object_anchor` and `semantic_anchor`
- introduce lightweight `structural_anchor` hints when possible
- do not redesign the whole engine around relational anchors yet

## Immediate Use

Anchor V1 should guide:

- fragment enrichment
- dust view explanation
- connection reason reporting
- future space-side grouping logic

## Anchor Fields

The working anchor structure should preserve at least:

- `anchor_type`: what anchor layer it belongs to
- `key`: canonical machine-comparable handle
- `label`: readable display name
- `evidence_text`: why this anchor was attached
- `confidence`: confidence score
- `origin`: where it came from, such as `rule`, `ai`, or `manual`
- `normalization`: alias and canonical normalization hints

## Handle Rule

Anchor should be treated more like a handle than a loose tag.

Prefer dot-path canonical handles such as:

- `pipeline.rag`
- `component.retriever`
- `retrieval.failure`
- `role.failure_mode`

Reasons:

- reduce tag explosion
- make comparison rules easier
- separate object / meaning / role
- simplify UI filtering
- keep minimum order without hard ontology lock-in

## Anchor Generation Flow

Recommended anchor generation flow:

`raw source -> source segmentation -> context-bearing fragment -> object extraction -> semantic labeling -> structural reading -> anchor normalization -> processed_fragment storage -> dust projection`

Anchorizer is not an isolated worker.
It sits after segmentation and labeling, then normalizes and structures anchor output.

## Guiding Questions

### Object Anchor

- what does this fragment directly talk about?
- what is the central system, model, dataset, component, or concept?

### Semantic Anchor

- what is the core meaning or issue?
- what is being presented as a problem, strength, limitation, or insight?

### Structural Anchor

- what function does this fragment play?
- is it a definition, claim, evidence, counterexample, limit, or bridge?

## Match Levels

Connection should not use anchor equality only.

Recommended levels:

1. `exact_match`
   - canonical keys are the same
2. `family_match`
   - upper handle family is shared
3. `cross_type_resonance`
   - object is shared but structural role differs
4. `complement_match`
   - semantic handles differ but meaningfully compensate or bridge

## Initial Domain Examples

Examples for AI paper / review / transcript input:

- `object.model.long_context`
- `object.pipeline.rag`
- `object.component.retriever`
- `semantic.retrieval.failure`
- `semantic.context.window.limit`
- `semantic.retrieval.compensation`
- `semantic.evaluation.bias`
- `structural.role.claim`
- `structural.role.evidence`
- `structural.role.background`
- `structural.role.failure_mode`
- `structural.role.limit`
- `structural.role.bridge`

## UI Display Rule

Anchor should not appear as a noisy tag cloud.

Recommended source-reader presentation:

- top area: 1-3 main object anchors
- side panel: semantic anchor list
- small badges: structural anchors

Click behavior should open:

- fragments with the same object anchor
- fragments with the same semantic anchor
- contrast / related fragments
- nearby dust / point / local space in the space layer

## Space Usage

In space:

- object anchors help local thematic cohesion
- semantic anchors help meaning proximity and repetition
- structural anchors change placement and interaction behavior

Examples:

- `claim` without evidence may form a thin unstable cluster
- `claim + evidence + limit` may support a thicker local space
- same object with `claim` and `critique` may form tension

## Mistakes To Avoid

- using only free-text anchors without canonical keys
- omitting structural anchors
- weakening source recovery anchors
- locking ontology too early
- attaching anchors only at full-document level

## Operating Strategy

Use two anchor classes early:

### Fixed Anchors

Frequently reused canonical anchors such as:

- `pipeline.rag`
- `component.retriever`
- `role.claim`
- `role.evidence`
- `role.limit`
- `evaluation.bias`

### Provisional Anchors

Temporary anchors not yet promoted into the fixed set, such as:

- `prov.memory_pressure_pattern`
- `prov.agent_handoff_friction`

## Initial Volume Rule

Do not attach too many anchors to one fragment early on.

Recommended limits:

- object: 1-3
- semantic: 1-3
- structural: 1-2

The goal is not anchor abundance.
The goal is stable, comparable, explainable handles per fragment.
