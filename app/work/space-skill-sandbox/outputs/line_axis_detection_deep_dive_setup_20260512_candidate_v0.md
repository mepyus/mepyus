# Line / Axis Detection Deep Dive Setup 2026-05-12 Candidate v0

## 1. Status

```text
Document = deep dive setup
Status = CANDIDATE_NEXT_PULL_SETUP
Authority = preparation only
Not baseline
Not official workflow
Not automation
Not schema
Not current-position update
```

## 2. Why This Is The Next Pull

05-12 identifies three likely deep dives:

```text
Pipeline Growth Flow Deep Dive
Line / Axis Detection Deep Dive
Sandbox Trial Decision Deep Dive
```

This setup selects:

```text
Line / Axis Detection Deep Dive
```

Reason:

```text
Pipeline growth depends on knowing whether a real Line formed and whether an Axis actually attached.
Sandbox trial decisions should wait until that distinction is clearer.
```

## 3. Working Distinction

```text
Line = a new input touches existing space and creates a recognizable flow.
Axis = a pressure, direction, or judgment criterion attaches to that flow.
Pipeline Candidate = Line + Axis + repeatability + failure condition + return path.
```

## 4. Test Input

Use the already-read 05-12 folder as the first test input:

```text
app/work/space-skill-sandbox/outputs/obsidian_05_12_growth_frame_intake_20260512_candidate_v0.md
```

## 5. Detection Questions

### Line

```text
What new movement appeared?
Which existing asset did it touch?
Can it be named without making it a fixed process?
Does it make a next pull easier?
```

### Axis

```text
What judgment pressure attached?
What must this flow protect?
What would count as overreach?
What failure condition belongs to it?
```

### Pipeline Candidate

```text
Has this appeared more than once?
Can it be used on another input?
Is there a return path?
Can it fail visibly?
Would sandboxing it reduce cost or only create ceremony?
```

## 6. Output Shape For The Deep Dive

```text
Input:
Existing Contact:
Line Candidate:
Axis Candidate:
Not Yet Pipeline Because:
Pipeline Candidate If:
Failure Condition:
Return Path:
Placement:
Watch:
```

## 7. Boundary

```text
Do not turn this into a universal schema.
Do not classify every old document.
Do not create a flow registry.
Do not promote the detected Line/Axis to baseline.
Do not dispatch a worker until the packet boundary is explicit.
```

`STATUS: LINE_AXIS_DETECTION_DEEP_DIVE_SETUP_PREPARED`
