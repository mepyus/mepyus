# Integrated Engine Single Work Package Walkthrough Validation v0

## 1. Verdict

PASS_WITH_NOTE

The current screen can now be read as one work package moving through the fixed three-surface body:

```text
User purpose
-> VectorFL evidence / packet / mediation
-> CLI or Engine return
-> VectorFL reread
-> User decision or deposit candidate
```

This is still not a multi-work operating board. That is correct for now. The first requirement is that one work package has a readable process path before multiple packages are shown together.

## 2. Why This Check Was Needed

The user concern was not only that one panel was confusing. The deeper question was whether the current UI can hold the integrated-engine process itself:

- User Surface organizes purpose, decision, and internal-team assignment.
- VectorFL Surface performs evidence reading, packet formation, mediation, and reread.
- Engine Surface reads request, processing boundary, return material, validation, and deposit candidate.

If this one-package path is not readable, a multi-work board would only multiply the confusion.

## 3. Current Work Package Walkthrough

### User Surface

The path starts with:

1. shared operating spine
2. user local focus
3. 사용자면 운영 순서
4. `CommandHeaderPanel`
5. `UserCliAssignmentPanel`
6. `InternalTeamAssignmentPanel`

Current reading:

```text
purpose / decision signal / assignment candidate
```

This matches the User Surface role. The surface does not try to show all evidence details. It pushes detailed reread back to VectorFL.

### VectorFL Surface

The path continues through:

1. shared operating spine
2. VectorFL local focus
3. VectorFL mediation process map
4. `CliHostControlPanel`
5. `VectorFLValidationQueuePanel`
6. support line / evidence panels

Current reading:

```text
internal search / evidence bundle
-> work packet formation
-> CLI tool call
-> return / reread
```

This is the strongest part of the current path. The surface is dense, but the density is now process-ordered.

### Engine Surface

The path then reads:

1. shared operating spine
2. engine local focus
3. `EngineCliReturnPanel`
4. support engine mock body

Current reading:

```text
request candidate
-> process boundary
-> return material
-> validation / record candidate
```

This is sufficient for a thin process surface. It is not yet a full engine process model, but it is no longer only a loose return feed.

## 4. What Is Stable

- The three-surface body remains fixed.
- CLI remains an on-top tool layer.
- Shared spine stays thin and does not become a fourth surface.
- User Surface is no longer carrying full evidence density.
- VectorFL Surface owns evidence / packet / mediation density.
- Engine Surface now reads as process material rather than control authority.
- Candidate / not canonical / not ingested language is visible enough for first-pass use.

## 5. What Still Feels Thin

1. User goal and VectorFL CLI turn purpose are still separate inputs. They can be read together, but the UI does not yet form one persistent work package object from them.
2. Evidence bundle is refs-based. It shows internal-search readiness, but it is not a real internal search engine.
3. Deposit candidate is readable as a candidate, but not yet a true sedimentation pipeline.
4. Multiple concurrent work packages are not represented yet. This should wait until the single work package path is stable.

## 6. Small Patch Applied

The shell orientation band previously used older wording:

```text
Goal/Scope/Material -> Line Reading -> Engine Processing -> Return Artifact
```

That wording under-described the actual process now present in the UI.

It was changed to:

```text
User Purpose -> VectorFL Packet -> CLI / Engine Return -> VectorFL Reread -> Decision / Deposit Candidate
```

This patch does not add a feature. It aligns the shell-level direction with the current work package lifecycle.

## 7. What Must Not Be Done Next

- Do not jump directly to multi-work board.
- Do not add Gemini adapter before the Codex on-top path is stable.
- Do not add background orchestration yet.
- Do not make shared spine dense again.
- Do not make User Surface show all VectorFL evidence.
- Do not make Engine Surface a governance/control room.

## 8. Next Smallest Step

Run a browser validation on one work package:

```text
User: can the purpose and assignment candidate be read?
VectorFL: can the evidence bundle and packet be read before Send Codex Turn?
Engine: can the return be read as process / validation / deposit material?
Back to VectorFL: can the return be loaded as reread material?
```

If this passes, the next structural step can be scoped as:

```text
formal current work package object draft
```

That should come before a multi-work board.
