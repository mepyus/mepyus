# Space Request Orchestration Baseline v1

## 1. Document Purpose

This baseline exists to lock why the space request orchestration package is needed.

The package is not a general search helper.
It is the layer that turns a short user request into a usable, space-aware, bounded operating result.

## 2. Problem This Package Solves

Without this package:

- the user must over-specify the request
- the system answers too early
- space assets, model reasoning, and external reinforcement get mixed without order
- the answer stays explanatory instead of usable
- reusable outputs are lost instead of being considered for reinjection

## 3. User Question / Internal Work Asymmetry Principle

The user should ask briefly.
The system should expand internally.

This package exists because the question surface and the work surface should not have the same complexity.

## 4. User Surface Principle

The user does not need to know:

- route modes
- packet fields
- template names
- reinjection classes
- storage candidates

The user should only need to indicate:

- target
- purpose

## 5. Internal Orchestration Principle

The system must:

1. interpret the request
2. choose a route
3. identify relevant space assets
4. decide whether external reinforcement is needed
5. produce a usable output
6. decide whether reinjection should be considered

## 6. Space-Derived / Model-Derived Separation Principle

The package must keep distinct:

- what comes from existing space assets
- what comes from model reasoning
- what comes from external reinforcement

These may work together, but they must not be treated as one undifferentiated source.

## 7. Usable Output Priority Principle

The answer must not stop at explanation.

The answer should reach:

- structure judgment
- applied form
- draft
- mapping
- recommendation

depending on the request type.

## 8. Reinjection Principle

The result should be evaluated for reinjection when it is reusable beyond the current turn.

Reinjection is:

- optional
- bounded
- secondary to the primary useful answer

## 9. Non-Goals

This baseline does not authorize:

- full automation
- canonical storage for all future outputs
- lower/upper bridge replacement
- lens/axis/promotion work
- UI definition

## 10. Lock Statements

- the user should not have to know the internal structure
- the user question should remain short
- the system must expand the request into an internal working packet
- the output should include a usable result, not only explanation
- the result may be reinjected into the space when reuse justifies it
