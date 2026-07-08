# Tests

This directory is reserved for future tests.

Bootstrap status:

- no full test suite exists yet;
- no behavioral rule validator tests exist yet;
- no mutation tests exist yet.

Current validation is provided by:

```bash
python scripts/validate_bootstrap.py
```

Future tests should cover:

- valid rule records;
- invalid rule records;
- valid coverage records;
- invalid coverage records;
- coverage state transitions;
- report generation;
- strict-mode failure behavior.
