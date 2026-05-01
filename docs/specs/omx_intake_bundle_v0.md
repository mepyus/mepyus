# OMX Intake Bundle v0

## Purpose

This spec defines the minimum meaning of an intake bundle from OMX into our space.

## Definition

An intake bundle is a bounded handoff from OMX or another external tool into the space layer.

It carries enough context for recording and digestion, without making our space responsible for execution.

## OMX Side

OMX may produce command outputs, session summaries, traces, files, or other runtime artifacts.

OMX remains responsible for how those artifacts were executed or produced.

## Space Side

Our space receives the bundle as intake material and may turn it into packages.

The space is responsible for recording, digestion, connection, review, and memory maturation after intake.

## Boundary

This version does not define hook behavior, transport, schema shape, event format, or automatic ingestion.

