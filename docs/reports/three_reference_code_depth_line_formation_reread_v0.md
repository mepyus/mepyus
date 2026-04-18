[[DOCROLE:report]] [[RUNMODE:observe_only]] [[PRIORITY:high]]
[[A]] [[OBJ:three_reference_code_depth_line_formation_reread_v0]] [[SEM:deeper_code_level_reread_of_ralph_claude_code_autoresearch]]

# Three Reference Code-Depth Line Formation Reread v0

## 0. Why This Pass Exists

The earlier reread was still too surface-heavy.

This pass goes one level deeper:

- not just README
- not just plugin names
- not just workflow labels

It looks at actual implementation-bearing files and asks:

**what kind of line formation pressure is really encoded in the code?**

That matters because if we only read names, then we keep seeing only names.
If we read code-level constraints, mutable surfaces, stop conditions, and hook behavior, then we can actually compare those structures against our own space.

---

## 1. Ralph, Read Through Code

Files read:

- `references/git_search/ralph-main/ralph.sh`
- `references/git_search/ralph-main/prompt.md`
- `references/git_search/ralph-main/CLAUDE.md`
- `references/git_search/ralph-main/AGENTS.md`

### What the code is actually doing

`ralph.sh` is small, but that is exactly the point.

It does not try to interpret the project deeply.
It does four forceful things:

1. fixes the loop driver
2. forces a fresh tool invocation each iteration
3. checks only for one completion marker
4. persists continuity through a few external files

The real line formation pressure is not "AI loops forever".
It is:

- branch continuity is external
- progress continuity is external
- memory continuity is external
- completion is externally recognized

The prompt files then narrow the work even harder:

- one story
- highest priority unfinished story
- quality checks
- commit
- mark `passes: true`
- append learnings

So Ralph does not just *recommend* task slicing.
It **enforces** a narrow work unit and an append-only memory habit.

### What line is formed at code depth

At code depth, Ralph forms this line:

**narrow execution slice -> external memory append -> reusable pattern extraction -> explicit closure mark**

That is thicker than the README reading suggested.
The key is that closure is not only philosophical.
It is literally wired into:

- `passes: false/true`
- `<promise>COMPLETE</promise>`
- append-only `progress.txt`
- reusable pattern promotion to top memory

So Ralph is not only a loop.
It is a **memory-disciplined closure machine**.

---

## 2. Claude Code Main, Read Through Code

Files read:

- `references/git_search/claude-code-main/plugins/hookify/README.md`
- `references/git_search/claude-code-main/plugins/hookify/core/rule_engine.py`
- `references/git_search/claude-code-main/plugins/hookify/hooks/pretooluse.py`
- `references/git_search/claude-code-main/plugins/ralph-wiggum/README.md`
- `references/git_search/claude-code-main/plugins/ralph-wiggum/hooks/stop-hook.sh`
- `references/git_search/claude-code-main/plugins/feature-dev/commands/feature-dev.md`

### What the code is actually doing

The deep signal in Claude Code main is not "many plugins exist".
It is that **behavior can be intercepted at event boundaries**.

`hookify` makes this concrete.

`pretooluse.py`:

- reads hook input from stdin
- classifies the event into `bash` or `file`
- loads rules
- evaluates them
- emits JSON messages
- never crashes the main action path because hook failure still exits `0`

`rule_engine.py` then shows the real shape:

- rules are matched against input fields
- block rules take priority over warning rules
- the output is not just a label
- the output changes permission or injects a system message at the event boundary

So the real line is not merely "behavior shaping".
It is:

**conversation/tool event -> rule match -> warning/block intervention -> next action shape**

`ralph-wiggum` makes another layer explicit.

Its `stop-hook.sh`:

- reads transcript path
- reads latest assistant output
- checks completion promise
- updates iteration state in a local markdown state file
- feeds the same prompt back into the system when stop is blocked

This is not just looping.
It is **stateful self-reentry through hook-mediated exit interception**.

`feature-dev` then shows yet another line pressure:

- phase ordering is enforced by command structure
- architecture design is explicitly before implementation
- implementation is blocked until approval

So Claude Code main is not one line.
At code depth it contains at least three different line formation mechanisms:

- hook-level correction
- stateful session reentry
- workflow-phase gating

### What line is formed at code depth

At code depth, Claude Code main forms this line:

**event boundary -> intervention rule -> workflow shaping -> packaged operating surface**

The important difference from Ralph is this:

Ralph slices execution units.
Claude Code slices **behavioral and workflow surfaces**.

That is much richer than just saying "pluginized surface".

---

## 3. autoresearch, Read Through Code

Files read:

- `references/git_search/autoresearch-master/README.md`
- `references/git_search/autoresearch-master/program.md`
- `references/git_search/autoresearch-master/prepare.py`
- `references/git_search/autoresearch-master/train.py`

### What the code is actually doing

At README level, autoresearch looks like autonomous experimentation.
At code depth, the actual force comes from `prepare.py` and `program.md`.

`prepare.py` reveals the key part:

- `MAX_SEQ_LEN` is fixed
- `TIME_BUDGET` is fixed at 300 seconds
- `EVAL_TOKENS` is fixed
- tokenizer/data path is fixed
- evaluation utilities are fixed
- training comparability is preserved by fixing the surrounding rail

That means the mutable freedom in `train.py` is only meaningful because **the evaluation world around it is frozen**.

Then `program.md` sharpens the rest:

- only `train.py` is mutable
- `prepare.py` cannot be modified
- metric truth is `val_bpb`
- loop forever
- commit
- run
- if improved, keep
- otherwise reset

So autoresearch is not merely "agent researches by itself".
It is:

**frozen experiment rail -> single mutable code surface -> hard comparable metric -> keep/reset branch pressure**

This is much more severe than the surface reading implied.

It means line formation here is driven by optimization pressure, not by lingering reinterpretation.

### What line is formed at code depth

At code depth, autoresearch forms this line:

**fixed harness -> single mutation zone -> measurable comparison -> aggressive branch selection**

So the essence is not autonomy alone.
It is **autonomy constrained by an intentionally narrow mutation window**.

---

## 4. Combined Code-Depth Reading

Once the code is read, the three systems stop looking like general AI patterns and start looking like three different line-forcing machines.

### Ralph

forces line by:

- slicing work small
- persisting memory outside session
- extracting reusable patterns
- demanding explicit completion

### Claude Code main

forces line by:

- exposing events
- attaching intervention rules
- packaging workflows into commands/agents/hooks
- converting repeated behavioral needs into reusable operating surfaces

### autoresearch

forces line by:

- freezing the harness
- freezing most of the code
- leaving one mutation zone
- subjecting it to hard comparative pressure

So these are not just three "tools".
They are three different answers to:

**how do you make a line become operational early?**

---

## 5. What This Says About Our Space

Our space still works differently.

We do not primarily form lines by:

- fast story completion
- hook-based intervention packaging
- single mutable surface plus metric pressure

We form them by:

- preserving materials
- separating input structure and internal maturation
- rereading before freezing
- translating to user language before overclaiming
- inspecting against premature naming

That means our line formation structure is still:

**material preservation -> delayed reread -> meaning thickening -> later packaging**

Compared to the three references, this means:

- Ralph shows what later execution memory discipline could look like
- Claude Code main shows what later inspection/hook surface could look like
- autoresearch shows what later bounded mutation rails could look like

But none of these should become our foundation.

Because the code-depth reading makes the tradeoff clearer:

- Ralph narrows too early for our current meaning ecology
- Claude Code surfaces and packages too early for our current latent lines
- autoresearch optimizes too early for our current weak-possibility preservation

---

## 6. Human-Language Meaning Reread

If I say it in your language, this is what became clearer only after reading deeper.

Ralph is not simply "an iterative coding loop". It is a way of making the same kind of work stop wandering by forcing it into a very small corridor: one story, one pass, one memory rail, one completion signal. Claude Code is not simply "plugin architecture". It is a way of making repeated behavioral needs show themselves early enough that they can be intercepted, warned on, blocked, or packaged as visible commands and agent surfaces. autoresearch is not simply "AI does research". It is a way of cutting almost the whole problem away so that one narrow mutation surface can be judged inside a hard experiment rail.

Reading them this way matters because it shows that the surface names were not the important thing. The important thing was how each system decides where line formation is allowed to happen, and how quickly it turns that line into something operational. Our space still does the opposite. It lets the line stay alive inside reread for longer before it becomes a command, a loop, a mutable surface, or a metric-governed branch. That is why our space often feels slower, but it is also why it can hold more possibility before it collapses into execution.

So the deeper reading does not reduce the difference between us and them. It sharpens it. They are all useful, but useful as later parts. Each one is like a different kind of execution organ waiting for a line that has already matured enough to deserve it.

---

## 7. Current Deeper Verdict

The current deeper verdict is this:

**the three references are not mainly examples of features. They are examples of code-level line-forcing strategies.**

And the corresponding reading of our space is:

**our space is still strong at line preservation and late meaning formation, but still relatively weak at code-level organs that package matured lines into execution rails, intervention hooks, and bounded mutation surfaces.**

That does not mean our space is behind them.
It means our space is earlier in a different order:

- first line maturation
- later execution organ attachment

This is the difference that only becomes obvious when the references are read below the naming layer.
