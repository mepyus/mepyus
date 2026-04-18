# middle layer requirement before fix v1

## 1. purpose
- define the missing functions between raw intake and case-level frame extraction.
- this is a requirement note, not a patch note.

## 2. placement
- upstream:
  - [inputter.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/inputter.py)
  - [labeler.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/labeler.py)
- downstream:
  - external first-pass / compare / refinement style case reading

## 3. required functions

### A. transcript pre-normalization
- normalize speaker markers, timestamps, chapter headers, and repeated interview scaffolding
- downweight presenter-style connector language before anchor scoring
- preserve source identity while reducing discourse noise

### B. topic-bearing anchor uplift
- separate:
  - generic discourse anchors
  - topic-bearing anchors
  - known-object anchors
- rank topic-bearing anchors above filler-like high-frequency terms

### C. case block aggregation
- regroup dust units into larger topic-bearing blocks
- avoid direct compare on hundreds of flat sentence-level dust units
- produce provisional case blocks that are still traceable to source

### D. provisional frame sketch
- emit lightweight candidate structures such as:
  - background / problem setup
  - structure entry
  - mechanism explanation
  - operating constraint
- do not emit promotion or baseline judgments

### E. defer / rhetoric bucketization
- separate:
  - reusable frame candidates
  - emphasis candidates
  - rhetoric / teaching convenience / observer-only language

### F. compare-ready packaging
- output a compact packet for later compare:
  - source identity
  - normalized topic-bearing anchors
  - provisional case blocks
  - candidate frame sketch
  - defer bucket

## 4. non-goals
- baseline promotion
- core promotion
- current surface update logic
- shared reality rewrite
- universal ontology expansion

## 5. acceptance condition
- when this layer exists, raw interview transcripts should no longer collapse almost entirely into `review / compare` with generic discourse anchors at the top.
- they should still remain conservative, but topic-specific case signal should become visible before manual first-pass.

## 6. one-line lock
- the missing middle layer must make raw transcript inputs compare-ready without making them promotion-ready.
