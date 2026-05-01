# Tone-Aware Metadata Report Revision Decision (v0)

## 0. Status

- status: sandbox decision candidate
- script_modified: false
- source_space_rule: false
- baseline: false
- automation: false
- judgment_tool_shift: false

## 1. Decision

**Recommendation:** `package_metadata_scan.sh`의 출력을 보정하는 소규모 리비전(Package 019)을 준비할 가치가 충분함.

리포트 내에 최소한의 "Tone Guard 가이드라인"을 통합하는 것은 리포트를 무겁게 만들기보다, 발견된 데이터의 성격(Signal vs Rule)을 규정함으로써 리뷰어의 안전한 판단을 돕는 '인지적 안전장치' 역할을 할 것으로 추정됨.

## 2. 핵심 질문에 대한 답변

- **Reviewer에게 "Candidate/Signal"임을 더 잘 알려야 하는가?** YES. 현재 리포트에도 `reviewed_by: pending`과 `Candidate Guess` 섹션이 있지만, 이것이 왜 중요한지(확정적 판단 지양)에 대한 짧은 톤 가이드가 있다면 오해의 소지를 더 줄일 수 있음.
- **Tone Guard 통합이 리포트를 무겁게 만드는가?** NO. 수십 줄의 가이드를 넣는 것이 아니라, 헤더(Header)나 특정 섹션에 1~2줄의 고정된 경고문(Disclaimer)을 넣는 방식이라면 가독성을 해치지 않음.
- **최소한의 변경으로 충분한가?** YES. `reviewed_by: pending`, `candidate label`은 이미 훌륭한 토대임. 여기에 "이 리포트는 관찰된 신호(Observed signals)일 뿐 확정된 규칙이 아님"을 명시하는 문구 하나만 추가되어도 효과적일 것임.
- **Judgment Tool로 변질될 위험이 있는가?** NO. 스크립트가 파일의 옳고 그름을 판단하는 것이 아니라, "나는 단지 기계적으로 나열했을 뿐이니 당신(리뷰어)이 톤을 낮춰서 읽으라"고 안내하는 것이므로, 오히려 Discovery Tool로서의 겸손함을 강화함.

## 3. 제안하는 최소 변경 (Proposed Revision Shape)

Package 019에서 사용자 승인을 득한 후 다음 변경을 검토함:

### A. 헤더 섹션에 톤 안내 추가
```markdown
## 0. Status
- status: generated
- scan_mode: observed signals only
- tone_guidance: candidates require review, avoid over-finalization
...
```

### B. Candidate Guess 섹션 강화
```markdown
## 4. Candidate Guess
- ...
- **Tone Guard:** 모든 후보(Candidate)는 잠정적이며, 확정적 단정(입증됨, 완벽함 등)을 지양합니다.
```

### C. Closeout 섹션 명시성 강화
```markdown
## 11. Closeout
이 보고서는 관찰된 데이터의 메타데이터 요약입니다. 
베이이라인 승격이나 소스 공간 수정을 결정하지 않으며, 모든 결과는 검토 대상(Pending review)입니다.
```

## 4. 한계 및 주의사항

- 본 결정은 스크립트 수정을 강제하지 않으며, 다음 패키지에서 구현 여부를 최종 결정함.
- 톤 가이드를 넣는 것이 AI의 모든 보고를 약하게 만드는 "기계적 위축"으로 이어지지 않도록 주의해야 함. (사실 관계 보고는 여전히 명확해야 함)

## 5. Verdict

**Verdict: PASS_FOR_REVISION_PLAN**

메타데이터 스캔 도구에 톤 가이드를 결합하는 것은, 도구가 수집한 데이터가 '진실'로 오인되는 것을 막는 가장 효율적인 지점에서 작동하는 안전 장치임.
