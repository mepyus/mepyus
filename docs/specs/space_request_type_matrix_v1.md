# Space Request Type Matrix v1

## 1. Purpose

This matrix defines the current request types used by the space request orchestration package.

## 2. Request Types

- `structure_read`
- `adaptation`
- `variation`
- `incident_triage`
- `external_enrichment`
- `reinjection_design`

## 3. Type Definitions

### structure_read

- read and explain a target within our current space

### adaptation

- map an external or internal target into our own space and produce an applied structure

### variation

- produce a changed or alternative form based on current space material

### incident_triage

- decide whether an incident is no-trigger, bounded-trigger, or needs escalation

### external_enrichment

- use bounded external reinforcement when the target or uncertainty requires it

### reinjection_design

- decide how a result should be handed back into the space as a reusable asset

## 4. Default Search Scope By Type

| type | default internal scope | external scope default |
| --- | --- | --- |
| `structure_read` | existing space assets | usually none |
| `adaptation` | existing space assets + target mapping assets | bounded external if target or freshness requires it |
| `variation` | relevant internal precedent | usually none |
| `incident_triage` | current operating rule / trigger assets | none unless the incident itself depends on outside facts |
| `external_enrichment` | internal mapping assets first | yes, but bounded |
| `reinjection_design` | result + current space placement assets | none by default |

## 5. Required Internal Questions By Type

### structure_read

- what is the target
- what internal assets already speak to it
- what is the core structure

### adaptation

- what should map into our space
- what should stay outside
- what should be separated rather than imported

### variation

- what should remain stable
- what should change
- what form is needed now

### incident_triage

- is there a real trigger
- what current placement applies
- is bounded reopen even allowed

### external_enrichment

- what uncertainty remains after the internal read
- what must be checked externally

### reinjection_design

- should the result be stored
- what class best fits it
- what remains unresolved

## 6. External Enrichment Conditions

Use external enrichment when:

- the user asks for latest/current
- the main target lives outside the space
- internal reading leaves bounded unresolved conflict

## 7. Expected Output By Type

| type | expected output |
| --- | --- |
| `structure_read` | structure-grounded explanation |
| `adaptation` | mapped structure or applied proposal |
| `variation` | changed draft or bounded alternative |
| `incident_triage` | stop / bounded reopen judgment |
| `external_enrichment` | reinforced answer with source separation |
| `reinjection_design` | reinjection class and candidate storage judgment |

## 8. Reinjection Potential By Type

- `structure_read`
  - low to medium
- `adaptation`
  - medium to high
- `variation`
  - medium
- `incident_triage`
  - low unless it becomes a bounded operational note
- `external_enrichment`
  - medium when the reinforced result is reusable
- `reinjection_design`
  - directly relevant

## 9. Mixed Request Rule

Requests may combine types.

Example:

- read an external structure
- adapt it to our space
- reinforce with external freshness
- produce a reusable output

This should be handled as:

- `adaptation + external_enrichment + reinjection_design`

## 10. Matrix Summary

The matrix exists to help the system decide:

- what to read first
- when to use external reinforcement
- what kind of output should be produced
- whether reinjection should be considered
