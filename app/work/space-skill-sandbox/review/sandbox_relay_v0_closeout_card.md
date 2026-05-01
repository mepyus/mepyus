# Sandbox Relay v0 Closeout Card

## 1. 한 줄 결론
Sandbox Relay v0는 `inbox / task packet / outbox` 구조를 통해 수동 복붙 병목을 'Trigger 1회' 수준으로 줄이는 파일 기반 작업 전달 표면을 구축하고, 두 차례의 실제 외부 자료 테스트(Saltlux Goover 사례)를 통해 반복 작동성을 성공적으로 검증함.

## 2. Relay v0가 해결하려는 문제
- 사용자가 매번 긴 지시서와 맥락을 Gemini에게 수동으로 복붙해야 하는 운영상의 피로도 및 병목 해결.
- 작업 요청과 결과 보고의 형식을 표준화하여 의사소통 비용 절감 및 기록의 일관성 확보.

## 3. 생성된 Relay 구조
- **relay/inbox/**: 사용자가 `request_template_v0.md` 기반의 요청서와 외부 자료를 넣는 물리적 위치.
- **relay/prompts/**: Gemini가 요청서를 읽고 샌드박스 규약(`worker_guide_v0_3_candidate`)에 따라 실행하기 위한 `gemini_task_packet_template_v0.md` 지침서.
- **relay/outbox/**: Gemini가 `result_template_v0.md` 형식으로 분석 결과를 반환하는 출력 표면.
- **relay/README.md**: 릴레이 운영 원칙 및 사용자/Gemini의 역할 정의서.

## 4. 검증된 작동 흐름
`사용자 Inbox 요청 → Gemini 가이드/스킬 라우팅 → Run/Validation 수행 → Outbox 결과 반환`
이 흐름은 자동화 코드 없이 순수 파일 시스템과 Gemini의 판단력만으로 안정적으로 작동함이 확인됨.

## 5. request_001 결과
- **주제**: Saltlux Goover 사례 구조 판독.
- **성과**: 첫 번째 릴레이 드라이런 성공. 5개 스킬이 정확히 라우팅되었으며, 수동 복붙 단계가 대폭 감소함.

## 6. request_002 반복성 결과
- **주제**: Saltlux Goover 기술 분석 (Luxia/MCP).
- **성과**: `request_001`에서 수립된 규약을 수정 없이 재사용하여 동일한 품질의 분석 결과 도출. 릴레이 구조의 범용성 및 반복 가능성 입증.

## 7. 사용자가 얻은 실용적 의미
- 사용자는 이제 긴 채팅 지시 대신 샌드박스 내 `request` 파일 하나만 작성하고 실행을 명령하면 됨.
- Gemini는 `task packet`을 통해 샌드박스 가이드와 금지 사항을 스스로 인지하므로, 사용자의 감시 부담이 줄어듦.
- 결과가 표준화된 `outbox`로 돌아오므로, 사용자는 결과와 footer를 보고 신속하게 다음 의사결정을 내릴 수 있음.

## 8. 남아 있는 수동 단계
- `inbox/request` 파일 작성.
- Gemini에게 실행 턴을 트리거(Trigger)하는 명시적 호출.
- `outbox/result`에 대한 최종 사용자 판단 및 승인.

## 9. 유지된 경계
- **Relay v0는 자동화가 아니다**: watch mode나 cron 같은 자동 트리거링이 포함되지 않음.
- **Relay v0는 watch mode가 아니다**: 파일 변경을 감시하여 스스로 실행되지 않음.
- **Relay v0는 MCP/hook이 아니다**: 외부 도구 연결이나 시스템 이벤트 훅을 생성하지 않음.
- **Relay v0는 production workflow가 아니다**: 샌드박스 내부의 실험적 전달 표면임.
- **Relay v0는 source-space promotion이 아니다**: 본체 기준을 수정하지 않음.
- **Relay v0는 자동 skill router가 아니다**: 가이드 기반의 수동 라우팅임.
- **Relay v0는 파일 기반 작업 전달 표면이다**: 순수 파일 읽기/쓰기를 통한 중계에 집중함.

## 10. 아직 하면 안 되는 것
- watch mode 추가 및 자동 실행 스크립트 도입.
- MCP 연결 및 실시간 시스템 훅 생성.
- 자동 skill routing 및 자동 reingestion 구현.
- Relay v0를 공식 운영 워크플로우로 취급하여 감시 소홀.
- Graphify / gstack 등 외부 도구 설치.

## 11. 사용자 판단이 필요한 지점
- **지속성**: Relay v0 방식을 향후 모든 샌드박스 실험의 기본 통로로 채택할지 여부.
- **자동화 전이**: 현재의 파일 기반 중계가 충분히 안정적이라면, 다음 단계로 watch mode 등의 자동화를 고려할지 여부.
- **템플릿 최적화**: 사용자의 입력 부담을 더 낮추기 위해 `request` 형식을 더 축소할지 여부.

## 12. 다음 선택지
- **A. Relay 방식으로 외부 자료 테스트를 반복**: 다양한 도메인의 자료를 더 투입하여 견고함을 확인.
- **B. Relay v0는 유지하고, 다른 스킬/런으로 이동**: `Run Record Review` 등 분석력 강화로 이동.
- **C. Relay template 표현을 더 줄이는 micro-refine (추천)**: 템플릿의 가독성을 높이고 필수 입력 항목을 줄여 수동 부담 최소화.
- **D. 현재 상태에서 보류하고 사용자 검토**: 추가 작업 없이 현재 패키지 결과를 정독.

## 13. 4-line footer
status: 완료
summary: Sandbox Relay v0가 inbox/task packet/outbox 구조로 두 번 반복 작동했고, 자동화 없이 수동 복붙 병목을 trigger 1회 수준으로 줄이는 후보 구조로 정리됨
risk: 아직 sandbox candidate relay이며 watch/hook/MCP/자동 실행 시스템이나 production workflow가 아님
next: 사용자 검토 후 relay template을 더 줄일지, relay 방식으로 다음 외부 자료 테스트를 계속할지 판단

---
This is a sandbox Relay v0 closeout card only.
No automation, hook, MCP, watch mode, tool installation, source-space promotion, baseline, schema, controller, router, ontology, or production workflow was created.
Sandbox Relay v0 remains a file-based sandbox relay surface, not an automation system.
worker_guide_v0_3_candidate and all consulted skills remain sandbox candidates.
