# gemini_cli_scope_and_permission_matrix_v0.md

## 목적
Gemini CLI의 접근 범위와 허용 행위를 명확히 제한함.

## Scope & Permission Matrix
| 영역 | 접근 권한 | 행위 제약 |
| :--- | :--- | :--- |
| `docs/reports/` | 읽기/Append | 파일 수정(대체) 금지, 단 섹션 추가 가능 |
| `runtime/` | 읽기(제한적) | 생성/수정/삭제 절대 금지 |
| `code/` | 접근 금지 | 읽기 및 수정 절대 금지 |
| `schema/` | 접근 금지 | 읽기 및 수정 절대 금지 |
| `controller/` | 접근 금지 | 읽기 및 수정 절대 금지 |

## 위반 시 조치
- 즉시 작업 중단 및 사용자 보고.

## Safety overlay note

`docs/reports/gemini_cli_safety_overlay_package_v0.md` supersedes any broad interpretation of Gemini write permission in this matrix.

Current tightened reading:

```text
Gemini default permission is no-write.
Append-only is exceptional and must target exactly one specified file and one specified section.
Execution is allowed only in read-only, dry-run, stdout-only, or sandbox-output mode.
Deletion, overwrite, move, cleanup, and direct patch application are forbidden.
```

The `docs/reports/` append permission above must not be read as general edit permission.
