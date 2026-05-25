# VectorTube v1.1 Seed-Bounded Calibrated Search Addendum

verdict: PASS_WITH_HOLD

User correction:
- Search is not simply OFF.
- Search must be possible, but calibrated from the user-designated original seed so VectorTube does not read too much and inflate confusion.

Updated phrase:
- old: no auto search / search off
- new: seed-bounded calibrated search

Operational meaning:
1. A user seed video/transcript must exist first.
2. Hermes reads the seed through VectorFL space-thinking.
3. The model proposes bounded search intents from claims/tensions/missing layers/counterframes.
4. Search returns candidates first, not bulk transcript ingestion.
5. Candidate transcript fetch is gated by budget/user approval.
6. Selected expansions enter mini-space quarantine.
7. Only a HOLD push packet is created for VectorFL.

Default budget candidate:
- 3 queries per seed
- 5 candidate videos per query
- 0 transcript fetches before review
- 3 approved transcript fetches by default
- hard cap 7 transcripts per seed batch

HOLD remains:
- no main-space mutation
- no authority mutation
- no Obsidian write
- no bulk crawl
- no video/audio download
