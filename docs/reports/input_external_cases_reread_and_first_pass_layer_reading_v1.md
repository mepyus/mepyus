# input external cases reread and first-pass layer reading v1

## 0. Why this note exists

This note records a reread of `inputs/external_cases` as a raw input layer, not as a derived report layer.

The goal was to check what kind of material actually lives in the input folder, how it differs from `source_assets/external_case_inputs`, and what kinds of external materials have already been split into raw, first-pass, and report surfaces.

## 1. What was read

### Folder identity
- `inputs/external_cases/README.md`
- `inputs/external_cases/folder_status.md`

### Representative raw external cases
- `inputs/external_cases/saltlux_ai.txt`
- `inputs/external_cases/ontology_youtube.txt`
- `inputs/external_cases/choi_ai_classroom_vlm.txt`
- `inputs/external_cases/enterprise.txt`

### Structured first-pass counterpart
- `source_assets/external_case_inputs/folder_status.md`
- `source_assets/external_case_inputs/external_case_first_pass_saltlux_ai_input_v1.md`

## 2. What the input folder is actually for

The input folder is the raw source landing zone.

It is for:
- external transcripts
- external company / product case text
- raw talks and talk-like material
- uncompressed source text before structured promotion

It is not meant to hold:
- final reports
- observation summaries
- derived canonical source assets

The README also makes one important distinction:
- new raw source goes here
- structured reference docs belong elsewhere
- source input md / directive-style input belongs in `source_assets/external_case_inputs`

## 3. What the raw materials show

### 3.1 `saltlux_ai.txt`
This is a paradigm-transition transcript, not just a company talk.

The dominant spine is:
- logical AI
- semantic web
- generative AI
- agentic AI
- physical AI

It also carries:
- scaling economics
- reasoning / test-time scaling
- document AI
- public / enterprise / on-prem deployment boundaries

This makes it a conceptual bridge case between AI history and deployment constraints.

### 3.2 `ontology_youtube.txt`
This is an ontology/agent-transition talk, not a generic AI overview.

The dominant spine is:
- agents
- ontology
- active ontology
- data quality
- small-data-first ontology construction
- graph / vector / SQL / SPARQL tooling
- enterprise and public-data deployment concerns

This makes it a conceptual donor for ontology-as-operating-structure reading.

### 3.3 `choi_ai_classroom_vlm.txt`
This is a teaching transcript with a strong mechanism/definition spine.

The dominant reading unit is:
- matrix learning
- embedding distance
- positive / negative pair construction
- contrastive learning

This case became important later because it supported a more faithful closure than narrower mechanism-only cases.

### 3.4 `enterprise.txt`
This is an adoption / enterprise boundary transcript.

The dominant spine is:
- RAG vs agent
- enterprise AI adoption
- upper bound vs lower bound of enterprise AI use
- data/privacy/safety concerns
- workflow / code / function orchestration

This case is useful because it shows the operational boundary between generic AI usage and enterprise deployment concerns.

## 4. How the raw input layer differs from the first-pass layer

`inputs/external_cases` is raw input.

`source_assets/external_case_inputs` is the structured first-pass layer.

The key difference is not just formatting.

The first-pass layer adds:
- source identity
- source type
- source origin
- test intent
- bounded rules
- promotion stance

For example, `saltlux_ai.txt` is turned into a first-pass source asset that explicitly says:
- observe and separate before adopt
- do not recreate the raw source
- keep derived documents and reports separate

That means the repo already distinguishes:
- raw source
- first-pass canonical source asset
- report surface

## 5. What this reread confirmed about the repo

The repo is already behaving like a layered reading engine.

It has:
- raw input landing zones
- first-pass structuring
- derived examples
- reports
- runtime receipts / manifests / views

So the repo is not just storing text.
It is already separating:
- raw material
- first-pass promotion
- interpretive output
- runtime trace

## 6. Practical reading takeaway

The input folder should be read as the raw material source, with some legacy mixed md assets still present.

The first-pass source asset layer should be read as the controlled promotion layer.

The report layer should be read as the evidence / interpretation layer.

This separation is important because the whole space depends on preserving:
- what the source was
- what got promoted
- what was inferred
- what trace remains

## 7. Breadcrumb note

This reread was appended to the breadcrumb trail so the path can be reconstructed later from the source layer through the first-pass layer and into report surfaces.

## 8. Final reading note

The main point of this reread is not that `inputs/external_cases` is large.

The main point is that it already contains multiple external material types that can support a real understanding-based inference space:
- paradigm-transition transcript
- ontology/agent transition transcript
- teaching/mechanism transcript
- enterprise adoption transcript

Those cases are already enough to show why the repo needs:
- control plane
- reading paths
- interpretation packets
- decision lineage
- multi-lens views

