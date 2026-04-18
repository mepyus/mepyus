# External Case First Pass — alexkarp_youtube.txt canonical input v1

- case_name: `alexkarp_youtube_raw_transcript_v1`
- source_ref: `inputs/external_cases/alexkarp_youtube.txt`
- source_type: `external_case_primary_transcript`
- source_origin: `raw_talk_or_conversation_transcript`
- source_status: `primary_transcript_with_asr_noise`
- stance: `observe_and_separate_before_adopt`
- comparison_cases:
  - `saltlux_agentic_ai_ontology_raw_transcript_v1`
  - `aifrontier_01_28_raw_transcript_v1`
  - `oh_my_opencode_raw_input_v1`
  - `enterprise_ai_adoption_and_ultrathink_raw_transcript_v1`
  - `andrewng_stanford_raw_transcript_v1`
- source_asset_group: `external_case_inputs`
- source_asset_path: `source_assets/external_case_inputs/external_case_first_pass_alexkarp_youtube_input_v1.md`

## Purpose
Use `inputs/external_cases/alexkarp_youtube.txt` as the canonical source for a first-pass external case reading.

The task is not to accept the transcript as truth or summarize it as a polished article.
The task is to:

1. record one exploration observation against the canonical raw source
2. split observed elements into `core_candidate / outer_candidate / defer / observer_only`
3. check repeated and non-repeated frames against previous external cases
4. read the current refinement trigger state without opening refinement prematurely

## Reading posture
- treat the file as a raw transcript with ASR noise, interviewer framing, and strong geopolitical rhetoric
- separate domain-control and harsh-environment operating frames from strong market and political claims
- prefer repeatable enterprise / regulated-work software-layer frames over positioning language
- do not promote the whole transcript into core
