# Evidence Selection Rules v0

## Execution

Select evidence when it:

- directly answers the interpreted goal;
- defines authority, boundary, or non-goal;
- explains current position or current PASS baseline;
- exposes conflict, tension, or unresolved gap;
- gives path-level support for where to search next.

Discard evidence when it:

- is only generated display output and the source is available;
- belongs to UI/surface work while Phase 1 asks for CLI space enablement;
- is historical reference without current relevance;
- repeats another stronger source without adding relation or gap value.

Record as weak candidate when:

- source relevance is plausible but not direct;
- authority level is unclear;
- it may matter in Phase 2 but is not needed to answer the current packet.

## Interpretation

Evidence selection is not a popularity vote over search hits. It is a relation assignment step. A report can be weak for authority but strong for current symptom. A baseline can be strong for principle but silent on a concrete runtime path.

## Validation

- selected assets carry reasons.
- discarded assets carry reasons.
- weak candidates are retained without overpromoting them.
- conflict sources are not erased.
