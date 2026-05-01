[[DOCROLE:memo]]
[[RUNMODE:ingest_only]]
[[PRIORITY:normal]]

# Software engineering laws GeekNews note v0

## source metadata

- source_url: `https://news.hada.io/topic?id=28760`
- source_title: `소프트웨어 공학의 법칙들`
- source_author: `GeekNews summary linking to lawsofsoftwareengineering.com`
- source_type: `external article summary`
- source_capture_date: `2026-04-23`
- source_note_kind: `paraphrased ingest memo`

## why this source matters

This source matters because it gathers many software engineering laws into one operating summary.

It is useful for our space not as a direct architecture order, but as a compact source of recurring pressures around:

- team size and communication limits
- planning and schedule distortion
- architecture boundaries and complexity control
- quality, testing, and maintenance discipline
- decision bias and metric misuse

The source is broad, but several items overlap with active concerns in our space:

- bounded teams over uncontrolled scale
- structure before free-form expansion
- complexity moved into the system rather than into the operator
- working simple systems before layered complexity
- metrics and validation needing careful interpretation

## what the source is

The page is a summary collection of software engineering laws and patterns.

The visible sections include:

- teams
- planning
- architecture

Each item gives a short principle and operating implication.

Representative examples visible on the page include:

- Conway's Law
- Brooks's Law
- Dunbar's Number
- Premature Optimization
- Goodhart's Law
- Hyrum's Law
- Gall's Law
- Law of Leaky Abstractions
- Tesler's Law
- CAP Theorem
- Second-System Effect

## core signal groups

## 1. team and coordination limits

The source repeatedly says software structure is shaped by communication limits and team boundaries.

Main signals:

- communication structure affects architecture
- adding people can increase coordination cost faster than output
- larger groups reduce individual effectiveness
- knowledge concentration creates bus-factor risk

This group reinforces the pressure toward:

- bounded roles
- smaller accountable surfaces
- explicit ownership and handoff

## 2. planning and schedule distortion

The source also gathers laws that warn against naive planning.

Main signals:

- work expands to fill available time
- final polishing takes much longer than expected
- even buffered schedules still overrun
- metrics become corrupted when turned into direct targets

This group reinforces the pressure toward:

- bounded claims
- better stop conditions
- schedule and status language that resists overconfidence

## 3. architecture and complexity discipline

The strongest architectural signals on the page are about complexity boundaries.

Main signals:

- complex systems should evolve from working simple systems
- abstractions always leak
- complexity can move but not disappear
- observed behavior becomes the real contract when enough users depend on it
- second systems tend to become overbuilt

This group strongly overlaps with our current space because we repeatedly prefer:

- bounded operating surfaces
- explicit boundaries
- feature-first attachment over whole-system replacement
- conservative expansion after a working minimum

## bounded relevance to our current space

This source is broad and should not be treated as a direct design spec.

Current bounded relevance:

- useful as a reference summary of recurring engineering pressures
- especially relevant to boundary, scale, complexity, and anti-overbuild reading
- not suitable as a direct promotion source by itself
- best used as external reread material that can later be compared against internal operating choices

## current bounded judgment

- useful as broad operating reference
- stronger for repeated boundary and complexity reminders than for direct implementation guidance
- keep as thin external ingest material
- no promotion from this source alone
