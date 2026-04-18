# External Case First Pass — enterprise.txt canonical input v1

- case_name: `enterprise_ai_adoption_and_ultrathink_raw_transcript_v1`
- source_ref: `enterprise.txt`
- source_type: `external_case_primary_transcript`
- source_origin: `raw_podcast_or_talk_transcript`
- source_status: `primary_transcript_with_asr_noise`
- stance: `observe_and_separate_before_adopt`
- comparison_cases:
  - `saltlux_agentic_ai_ontology_raw_transcript_v1`
  - `aifrontier_01_28_raw_transcript_v1`
  - `oh_my_opencode_raw_input_v1`

## Purpose
Use `enterprise.txt` as the canonical source for a first-pass external case reading.

The task is not to accept the transcript as truth or summarize it as a polished article.
The task is to:

1. record one exploration observation against the canonical raw source
2. split observed elements into `core_candidate / outer_candidate / defer / observer_only`
3. check repeated and non-repeated frames against previous external cases
4. read the current refinement trigger state without opening refinement prematurely

## Reading posture
- treat the file as a raw transcript with ASR noise and interview rhetoric
- separate structure frames from strong claims and speaker positioning
- prefer repeatable operating frames over polished phrasing
- do not promote the whole transcript into core
