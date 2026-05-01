# Layer-Aware Space Reading Seed v0

## 1. Why this note exists

The ASSETS.md thought experiment showed that a coherent design can still stand on a different layer than the user's intended space philosophy.

The assistant's asset-management design was internally coherent under enterprise knowledge management, quality control, ontology, and automation lenses. The user's correction showed that the same coherence could over-fix a living space before its meaning, lines, axes, connections, and reading layers had matured.

## 2. Core principle

The space does not merely store the user's answers.
The space stores and retrieves the layers, lines, axes, connections, flows, and contexts through which the user reads a situation.

## 3. What the user means by "there is no single correct answer"

- The question is not only whether an answer is correct.
- The question is also which layer makes that answer appear correct.
- A proposal may be valid in an enterprise-management layer but risky in a living-space maturation layer.
- A design may be coherent but still stand on the wrong layer for the current purpose.

This means the space should not collapse every answer into accept/reject. It should preserve the layer where the answer has value, identify where it becomes risky, and lower it into the right position.

## 4. Why CLI needs the space

CLI normally reads the prompt and produces an answer from the immediate context.

The space should help CLI retrieve:

- user's long-term direction
- prior line/axis formation
- relevant connections and flows
- risk memories
- worker over-promotion traces
- external lens value
- previous cases where a coherent answer stood on the wrong layer
- do_not_use_as warnings
- user-facing lowering requirements

## 5. Layer-aware reading flow candidate

```text
input
-> detect immediate interpretation layer
-> retrieve relevant space lines / axes / memory
-> compare alternative lenses
-> identify layer conflict
-> decide placement: core / conditional / comparison / quarantine / future option / archive
-> produce user-facing output
-> reflux residue into space
```

## 6. Relation to reverse ontology

The user's space should not begin by forcing fixed categories onto material.

Instead:

```text
material enters
-> the space reads it through multiple lenses
-> repeated lines appear
-> axes form
-> connections and flows are detected
-> only then should provisional structure be formed
```

This is closer to reverse ontology than fixed ontology.

## 7. Do not

- Do not convert this into ontology/schema immediately.
- Do not make this an automatic classifier.
- Do not treat the current lens list as complete.
- Do not make Gemini the final lens reader.
- Do not collapse all lenses into the user's philosophy lens.
- Do not ignore other lenses just because they do not fit the current space philosophy.
- Do not turn this into ASSETS.md or asset registry.

## 8. Status

```yaml
state: seed / candidate
not:
  - baseline
  - protocol lock
  - automation
  - schema
  - asset registry
```
