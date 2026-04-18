# Autoresearch Structural DNA Analysis

Date: 2026-04-15
Actor: Gemini-CLI
Source: `references/git_search/autoresearch-master/`
Reason: Decomposition of autonomous research loop for application to VECTORFL maturation.

## 1. Key Structural Axes

### A. Axis of Autonomous Evolution (Loop-Forever)
- **DNA**: `Git Branch Advancement + Experiment Loop`.
- **Structural Setting**:
  - `train.py`: Autonomous experiment runner.
  - The agent iterates forever, discarding or keeping changes based on `val_bpb`.
- **Meaning**: Research is an iterative, stateful process that advances only on empirical gain.

### B. Axis of Provenance Tracking (Result Ledger)
- **DNA**: `Commit Hash + Metric + Memory + Status`.
- **Structural Setting**:
  - `results.tsv`: Tab-separated logs of every experiment's outcome.
- **Meaning**: Failure is as valuable as success, as long as it's logged and indexed.

### C. Axis of Time-Budgeted Maturation
- **DNA**: `Fixed Budget (5m) + Ground Truth Metric`.
- **Structural Setting**:
  - `TIME_BUDGET = 300`: Forces evaluation before exhaustion.

## 2. Adoption Strategy for VECTORFL

| Pattern | Structural Axis | Recommended VECTORFL Application |
| :--- | :--- | :--- |
| **Experiment Branching** | Evolution | Use temporary branches for maturing new `Interpretations`. |
| **Metric-Based Discarding** | Performance | Log the "Clarity Score" of a Fragment and discard if maturation doesn't improve it. |
| **Autonomous Loop** | Autonomy | Allow Gemini to auto-optimize `Interpretations` in `app/work/` until a stop command is issued. |

## 3. Gemini's Judgment
`Autoresearch`가 보여준 가장 핵심은 **"성공하지 못한 실험 결과도 기록으로 남겨야 한다"**는 것입니다. 이는 현재 우리가 Fragment 중심의 해석 엔진에서 가장 부족한 점(실패한 해석의 데이터화)입니다. 모든 '의미 있는 시도'를 이벤트로 저장하는 방식으로 엔진을 강화해야 합니다.

---
*Note: This analysis is stored in `gemini/external_analysis/` as per the current session protocol. No files outside `gemini/` were modified.*
