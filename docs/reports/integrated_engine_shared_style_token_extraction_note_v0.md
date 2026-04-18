# Integrated Engine Shared Style Token Extraction Note v0

Date: 2026-04-15

## 0. verdict

PASS

Round 3 can extract shared style-token rhythm at scaffold-file scope without promoting extensions or changing semantic structure.

This note is a bounded extraction guide, not a shared component design, CSS system, or semantic remapping.

## 1. current shared token candidates

### badge / pill

Common pattern:

- rounded pill shape
- small uppercase label
- subdued border and background
- accent color only for central or surface identity cue

Use:

- panel role labels
- read role labels
- route / field / slot labels
- support-only labels

### compact card shell

Common pattern:

- rounded card
- thin border
- dark zinc background
- compact padding
- central card receives stronger border / padding / shadow

Use:

- panel cards
- support panels
- strip items
- read cards

### support note / support boundary tone

Common pattern:

- amber-tinted low-emphasis boundary note
- small text
- placed below primary panel content

Use:

- support boundary
- support-only disclaimer
- visual-only reminder

### manifest-read card rhythm

Common pattern:

- read role pill
- path code line
- reason text
- compact inner card

Use:

- mapped manifest reads only

### center-card emphasis

Common pattern:

- larger padding
- stronger emerald border
- subtle shadow
- wider center column on large screens
- first visual order on narrow screens

Use:

- `operating_flow_panel`
- `maturation_canvas_panel`
- `execution_state_panel`

### column spacing / gap rhythm

Common pattern:

- `gap-5` outer layout
- `space-y-5` for standard columns
- `space-y-4` for overloaded right support columns

Use:

- left / center / right rhythm

### subdued right-column tone

Common pattern:

- right-side support remains present but quieter
- side inspection uses low-contrast card tone
- no right support should overtake center panel emphasis

Use:

- return decision support
- validation / reflux / evidence support
- result / history support

## 2. commonizable vs surface-specific

| token area | can be commonized | must stay surface-specific |
|---|---|---|
| badge / pill shell | shape, size, border, text density | label vocabulary and semantic meaning |
| compact card shell | border, radius, dark background, padding | central panel identity and surface class prefix |
| support note tone | amber subdued boundary tone | support wording: user decision, VectorFL typed support, engine return draft |
| manifest-read card rhythm | role pill, path code, reason stack | mapped manifest content and panel read purpose |
| center-card emphasis | stronger border, padding, shadow | which panel is central |
| column spacing | left / center / right grid rhythm | column weights per surface |
| subdued right column | quieter support tone | object class separation on VectorFL, return/history tone on engine |

## 3. why not a fully shared token system yet

- The current scaffolds are standalone read-mapping scaffolds, not a component system.
- No shared CSS module or design-system entry point has been approved.
- Surface identity still matters: user operating, VectorFL maturation, engine execution.
- VectorFL requires object-class separation that must not be collapsed into a generic card language.
- A full shared component could accidentally introduce structural coupling or imply a shared render model.

## 4. semantic drift risks

- Shared badge styling must not make anchor, maturation, and operating objects look identical.
- Shared support-note styling must not promote support layers into core panels.
- Shared center emphasis must not hide that each surface has a different center.
- Shared strip styling must not create a new route/state model.
- Shared read-card styling must not imply live manifest reads or runtime binding.

## 5. bounded extraction rule

For round 3:

- define local style-token constants inside each scaffold file only
- reuse common token names where possible
- preserve surface-specific class prefixes and semantic labels
- do not import or export a shared style module
- do not alter panel order, read mapping, manifest paths, or central panel constants

## 6. close

Round 3 shared style-token extraction is safe when it stays local, visual, and subordinate to current working baseline semantics.
