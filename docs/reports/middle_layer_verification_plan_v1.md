# middle layer verification plan v1

## 1. purpose
- define how to test a future middle-layer patch without changing code yet.

## 2. baseline comparison set
- structured document path
- external case intake path
- raw interview transcript path

## 3. primary test set
- [dario_amodei_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/dario_amodei_youtube.txt)
- [andrej_karpathy_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/andrej_karpathy_youtube.txt)
- [alexkarp_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/alexkarp_youtube.txt)

## 4. verification questions
- does generic discourse anchor dominance decrease?
- do topic-bearing anchors surface earlier?
- does scene/flow flattening weaken?
- does source identity remain traceable?
- do provisional case blocks become visible?
- does the output stay conservative and avoid promotion?

## 5. success indicators
- top anchors are less dominated by pronouns / filler / connectors
- case-level differences appear before manual first-pass
- output remains source-traceable
- compare-ready packets can be produced without current/shared reality expansion

## 6. failure indicators
- generic discourse still dominates
- case-level topic difference still disappears
- middle layer behaves like promotion logic
- output becomes large, unstable, or hard to trace back to source

## 7. bounded next step
- implement a read-only prototype first
- run on the 3 interview transcripts
- compare:
  - current raw probe
  - prototype middle-layer output
  - existing manual first-pass
- patch production path only after that comparison is stable

## 8. one-line lock
- test the middle layer first as a diagnostic prototype, not as a direct production rewrite.
