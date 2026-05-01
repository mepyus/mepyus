# Space Request Orchestration Package Spec v1

## Package Overview

This package defines how a short user request becomes:

1. an internal request packet
2. a routed reading/external/model process
3. a usable output
4. a reinjection candidate when appropriate

It is not only a search package.
It is an orchestration package.

## Package Goal

The goal is to support this full chain:

- short user request
- internal expansion
- bounded source arbitration
- usable output
- optional reinjection

## Package Components

### Core contracts

- [question_route_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/question_route_contract_v0.md)
- [answer_reinjection_handoff_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/answer_reinjection_handoff_contract_v0.md)
- [user_question_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/user_question_contract_v1.md)

### Arbitration note

- [space_model_external_arbitration_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/space_model_external_arbitration_note_v0.md)

### Operational templates

- [space_request_packet_template_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/templates/space_request_packet_template_v1.md)
- [space_request_output_template_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/templates/space_request_output_template_v1.md)
- [space_reinjection_note_template_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/templates/space_reinjection_note_template_v1.md)

## Baseline Relationship

The package should be read with these assumptions:

- the user should be able to ask briefly
- the system should expand internally
- space/model/external should not be mixed blindly
- outputs should become usable artifacts when needed

## End-to-End Execution Flow

1. receive short user request
2. interpret user intent
3. select route mode
4. identify primary space scope
5. identify whether external reinforcement is needed
6. build internal request packet
7. perform reading / mapping / reinforcement
8. produce usable output
9. evaluate reinjection potential

## Input Contract

Minimum input:

- target
- purpose

Optional input:

- desired output shape
- explicit request for external reinforcement

The package must not require:

- internal route names
- schema knowledge
- storage instructions

## Output Contract

The output must include:

1. user-facing request interpretation
2. structure-grounded reasoning
3. usable result
4. uncertainty when relevant
5. reinjection judgment when relevant

## Reinjection Contract

Reinjection is optional.
It should be considered only when the output is reusable beyond the current turn.

Possible reinjection classes:

- `reference`
- `candidate`
- `operating_asset`

## Non-Goals

This package does not:

- automate storage by itself
- define canonical file placement for every future result
- replace lower input organ rules
- replace lower-to-upper bridge rules
- define UI behavior
- define lens/axis/promotion layers

## Constraints

The package must preserve:

- short user entry
- internal routing responsibility
- bounded external use
- user-purpose output
- optional reinjection rather than forced reinjection

## Extension Boundary

Future extensions may add:

- request type matrix
- runtime directive
- output surface contract
- more explicit storage handoff conventions

But v1 should stay narrow:

- request routing
- source arbitration
- packetization
- output shaping
- reinjection handoff

## Package Lock Statement

At v1, this package is the request-packetization and answer-handoff layer between:

- user question
- current space assets
- model reasoning
- bounded external reinforcement
- reusable output
