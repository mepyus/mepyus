# Gemini Run Result

- packet: smoke-text
- run_id: smoke_model_observability_20260512
- timestamp: 20260512_222811
- dry_run: false
- smoke_text: true
- requested_model: gemini-2.5-flash
- output_format: text
- timeout_seconds: 60
- raw_result: app/work/space-skill-sandbox/outputs/gemini_raw_results/smoke_model_observability_20260512_gemini_raw_20260512_222811.txt
- stderr_result: app/work/space-skill-sandbox/outputs/gemini_raw_results/smoke_model_observability_20260512_gemini_stderr_20260512_222811.log

## Result


## Invocation Status

- gemini_exit_code: 0
- likely_state: model_capacity_or_quota
- requested_model: gemini-2.5-flash
- gemini_path: /usr/local/bin/gemini
- gemini_version: 0.41.2
- duration_seconds: 21
- prompt_bytes: 35
- raw_bytes: 16
- stderr_bytes: 4937
- command_summary: gemini -p "<prompt redacted>" --model gemini-2.5-flash
- stderr_nonempty: true

GEMINI_SMOKE_OK

## Stderr Tail

      '        "reason": "rateLimitExceeded"\n' +
      '      }\n' +
      '    ],\n' +
      '    "status": "RESOURCE_EXHAUSTED",\n' +
      '    "details": [\n' +
      '      {\n' +
      '        "@type": "type.googleapis.com/google.rpc.ErrorInfo",\n' +
      '        "reason": "MODEL_CAPACITY_EXHAUSTED",\n' +
      '        "domain": "cloudcode-pa.googleapis.com",\n' +
      '        "metadata": {\n' +
      '          "model": "gemini-2.5-flash"\n' +
      '        }\n' +
      '      }\n' +
      '    ]\n' +
      '  }\n' +
      '}\n' +
      ']',
    headers: {
      'alt-svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000',
      'content-length': '612',
      'content-type': 'application/json; charset=UTF-8',
      date: 'Tue, 12 May 2026 13:28:18 GMT',
      server: 'ESF',
      'server-timing': 'gfet4t7; dur=266',
      vary: 'Origin, X-Origin, Referer',
      'x-cloudaicompanion-trace-id': 'f6947986dd1e060',
      'x-content-type-options': 'nosniff',
      'x-frame-options': 'SAMEORIGIN',
      'x-xss-protection': '0'
    },
    status: 429,
    statusText: 'Too Many Requests',
    request: {
      responseURL: 'https://cloudcode-pa.googleapis.com/v1internal:streamGenerateContent?alt=sse'
    }
  },
  error: undefined,
  status: 429,
  Symbol(gaxios-gaxios-error): '6.7.1'
}
