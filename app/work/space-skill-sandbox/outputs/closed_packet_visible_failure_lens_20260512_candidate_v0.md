# Closed Packet / Visible Failure Lens 2026-05-12 Candidate v0

## 1. Status

```text
Document = candidate lens
Status = CANDIDATE_PACKET_LENS
Authority = packet design aid only
Not baseline
Not official workflow
Not automation
Not schema
Not registry
Not current-position update
```

## 2. Purpose

Use external references and Obsidian 05-12 recovery to improve worker/Gemini packets.

The lens should help a packet become:

```text
closed enough to execute
open enough to fail visibly
bounded enough to return safely
```

## 3. Lens Fields

```text
source refs:
role:
read set:
do-not-read set:
assigned scope:
start coordinate:
end coordinate:
density requirement:
continuity boundary:
forbidden drift:
completion condition:
visible proof:
evaluator limits:
failure condition:
what would falsify this:
return format:
placement options:
```

## 4. Field Meanings

```text
source refs:
  what the worker can cite

role:
  what the worker is and is not

read set:
  what must be read

do-not-read set:
  what should not be used unless the package fails

assigned scope:
  what part of the problem is theirs

start coordinate:
  where the worker begins

end coordinate:
  what counts as a complete stop point

density requirement:
  how much concrete detail is required to avoid vague output

continuity boundary:
  what prior state must be preserved

forbidden drift:
  what the worker must not turn the task into

completion condition:
  what done means

visible proof:
  what evidence in the return proves done

evaluator limits:
  what the reviewer/evaluator cannot know or inspect

failure condition:
  what should make the run fail or downshift

what would falsify this:
  what would show the packet or claim is wrong

return format:
  how evidence returns

placement options:
  RETURN_ONLY / WATCH / HOLD / SANDBOX_TRIAL / WORKER_PACKET / USER_JUDGMENT_REQUIRED
```

## 5. What This Lens Blocks

```text
smooth but untested architecture
worker guessing the whole space
unbounded continuation
hidden evaluator authority
completion without visible proof
failure hidden as deferral
source import becoming local law
```

## 6. First Test Candidate

```text
Apply this lens to the next Gemini packet before execution.
Do not rewrite all existing packets.
Do not create automation.
```

`STATUS: CLOSED_PACKET_VISIBLE_FAILURE_LENS_PREPARED_WITH_WATCH`
