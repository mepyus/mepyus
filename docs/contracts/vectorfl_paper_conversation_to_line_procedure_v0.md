# VectorFL Paper Conversation-to-Line Procedure v0

## Purpose
This procedure turns conversation, correction flow, notes, and scenario-bearing documents into reusable lines.

The goal is not to produce TODO lists.
The goal is to extract:
- repeated pressures
- corrected misunderstandings
- question structures
- reusable line candidates
- next internal / external action bridges

## Input Unit
Treat the following as one reasoning bundle:
- user / assistant conversation flow
- interim summaries
- close-out notes
- md contracts
- failure traces
- correction history
- scenario descriptions

Do not read only the compressed md.
Read the flow that made the md necessary.

## Pass 1: Repeated Pressures
Look only for repeated pressure, not for full summary.

Questions:
- What complaint keeps returning?
- What is repeatedly named as the real problem?
- What keeps being resisted?

Output:
- `repeated_pressures`

## Pass 2: Misunderstanding Corrections
Map how the reading changed.

Questions:
- What was first misunderstood?
- How was it corrected?
- Why was that correction necessary?

Output:
- `misunderstanding_corrections`

## Pass 3: Question Structures
Extract the questions that actually opened the structure.

Questions:
- Which question made the situation clearer?
- Which question reached the core instead of polishing the surface?

Output:
- `question_bank`

## Pass 4: Line Candidates
Generate line candidates from repeated pressure, correction flow, and question structure.

Each line candidate should include:
- `line_name`
- `core_claim`
- `repeated_evidence`
- `what_it_resists`
- `what_it_enables`

## Pass 5: Dual Translation
Translate each line in two ways.

### Internal Language
- line
- bundle
- recall chain
- evidence object
- handoff object

### Supervisor Language
- why this matters now
- what remains unstable
- whether to continue, hold, reopen, or redirect

Output:
- `dual_translation`

## Pass 6: Action Bridge
Every confirmed line must connect to action.

Bridge each line to:
- what to reread internally
- what to compare externally
- which cell should receive it
- which CLI should manage it
- what report surface should mention it

Output:
- `line_action_bridge`

## Pass 7: Validation
Validate the line before locking it.

Questions:
- Does this line recur across multiple parts of the bundle?
- Would removing it weaken the whole direction?
- Can it guide an actual next step?
- Is it more than a good-sounding phrase?

Output:
- `confirmed_lines`
- `unresolved_tensions`

## Final Output Shape
1. `repeated_pressures`
2. `misunderstanding_corrections`
3. `question_bank`
4. `line_candidates`
5. `confirmed_lines`
6. `dual_translation`
7. `line_action_bridge`
8. `unresolved_tensions`

## Prohibitions
- do not collapse the bundle into TODOs first
- do not read only the final md
- do not confirm a line without repeated evidence
- do not skip the supervisor-language translation
- do not jump to external search before internal line extraction

## One-Line Rule
Conversation-to-line reading means turning repeated pressure and correction flow into reusable judgment axes.
