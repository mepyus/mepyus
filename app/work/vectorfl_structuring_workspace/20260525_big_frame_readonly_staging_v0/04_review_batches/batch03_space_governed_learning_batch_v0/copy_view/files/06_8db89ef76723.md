# human language line synthesis layer spec v0

## verdict

- this layer is not a simple translation layer
- this layer is not a “make it easier” summary layer
- this layer exists to reread internal materials, follow their connections and repeated lines, and restate what a concept becomes inside the space in human language

## why this layer is needed

The space is now relatively strong in:

- code language
- structure language
- operating language
- bounded observation and surfaced readout

But this is still insufficient when the user asks:

- what is `ontology` in this space?
- what is `harness` in this space?

The current weakness is not only that the explanation is hard.
The deeper weakness is that the space still tends to answer in its own internal reaction language:

- weak
- strong
- active
- parked
- thick
- thin

Those are useful internally, but they do not yet produce the longer human-language explanation the user needs.

## module identity

This layer should be understood as:

- a rereading layer
- a line-synthesis layer
- a human-language meaning surface

It is not:

- a dictionary layer
- a one-line simplification layer
- a pure post-processing paraphrase layer

## core sequence

This layer must follow the sequence below:

1. recover relevant internal materials
2. trace connections between those materials
3. follow repeated or reinforced lines
4. interpret what those lines mean inside the space
5. restate that meaning in longer human-language prose

The final output must therefore be:

- internally grounded
- line-aware
- connection-aware
- human-readable as flowing explanation

## minimum structural contract

When the user asks about a concept, this layer must try to answer through the following structure.

### 1. material recovery

Find the smallest internal corpus needed across:

- `docs/specs`
- `docs/notes`
- `docs/reports`
- `source_assets`
- current close-out / operating notes

Rules:

- follow the trace of the concept and its line links
- do not scan the whole repo blindly
- recover only the streams that actually participate in the concept’s meaning

### 2. connection tracing

For the recovered materials, identify:

- where the concept appears strongly
- where it is reframed
- where it is resisted
- where it is attached to other operating or philosophical concerns

This step must show:

- not just repeated keyword use
- but relation across materials

### 3. line interpretation

Interpret which repeated lines are alive around the concept.

This can include:

- segment/document lines
- space reread lines
- upper operating lines

Questions:

- what line keeps recurring around the concept?
- what line makes that concept survive in the space?
- what tension or ambiguity is carried by that line?

### 4. human-language synthesis

Produce not a bullet definition, but a connected human-language explanation.

The explanation should:

- refer back to the recovered internal materials
- reflect the traced connections
- carry the line interpretation
- become readable as one longer explanatory movement

## separation rule

This layer must keep structure language and human language connected, but not collapsed.

That means:

- it may start from structure language
- it may mention active/parked/weak/thick where needed
- but it must not stop there

The human-language result must answer:

- what the concept becomes in the space
- why it matters
- what tension or direction it carries

## human language as a surviving line layer

This layer does not treat human language as cosmetic output.

Instead:

- human language is itself a layer where line survives
- a concept should remain traceable from:
  - internal material
  - connection structure
  - repeated line
  - human-language synthesis

So the human-language paragraph is not decoration.
It is the upper readable continuation of the line.

## output form requirement

The output must include prose that reads as a connected paragraph or paragraphs.

It must not end as:

- one-line glossary
- short bullet definition only
- generic common-sense explanation

The output may include bullets for trace scaffolding,
but it must contain at least one genuine connected human-language passage.

## case requirement

This layer must be able to show the pattern through real examples.

Minimum current examples:

- `ontology`
- `harness`

Each example should reach:

- internal material trace
- connection structure
- repeated line
- current meaning in the space
- longer human-language restatement
- remaining weak or missing parts

## non-goals

- no new runtime or engine behavior in this spec
- no fake connections that are not supported by internal materials
- no dictionary-style freezing of concepts
- no reduction into “easy explanation only”
- no broad redesign of the whole reading stack

## current conclusion

- the next necessary layer is not “simpler wording”
- it is a human-language line synthesis layer
- this layer exists to let the space answer in a form the user can think with, not just in a form the engine can observe with
