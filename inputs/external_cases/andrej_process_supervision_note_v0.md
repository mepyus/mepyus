[[DOCROLE:memo]]
[[RUNMODE:ingest_only]]
[[PRIORITY:normal]]

# Andrej process supervision note v0

## source metadata

- source_title: `Andrej Karpathy youtube discussion on LLM cognitive deficits and RL limits`
- source_author: `Andrej Karpathy discussion transcript`
- source_type: `external transcript`
- source_capture_date: `2026-04-23`
- source_note_kind: `paraphrased ingest memo from local raw capture`
- raw_source_file: `inputs/external_cases/andrej_karpathy_youtube.txt`

## why this source matters

This source matters because it questions whether end-result reward alone is an efficient supervision signal and argues for richer process-aware feedback.

It overlaps with our space around:

- structure before unconstrained trial-and-error
- supervision during the path, not only at the end
- caution toward noisy latent search when bounded process support is missing

## core claim

The source argues that current reinforcement-style approaches are inefficient when they try to learn from a long trajectory using only a final result signal.

The implied preference is for stronger process supervision:

- feedback during the path
- reflection or review on intermediate steps
- less blind stochastic searching

## structural pattern

### 1. final-result-only guidance is too weak

A single final reward leaks too little usable supervision into a long trajectory.

### 2. blind latent exploration is noisy

If the system keeps trying many paths and only rewards the ending, the learning signal is sparse and contaminated.

### 3. process-aware checking is needed

A better pattern would include intermediate review or supervision rather than only terminal scoring.

## relevance to our current space

This source does not directly map onto our runtime.

It is useful because it reinforces:

- structure before free-form agent improvisation
- bounded intermediate checks
- caution against relying on latent exploration without better supervision surfaces

## bounded judgment

Current bounded judgment:

- useful as a process-supervision reference
- relevant to recurrence around structure-before-freeform behavior
- not a direct operating rule
- keep as thin external reread material with no promotion
