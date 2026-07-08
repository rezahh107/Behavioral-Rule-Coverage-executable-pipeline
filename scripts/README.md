# Scripts

This directory contains repository maintenance and validation scripts.

## Implemented

- `validate_bootstrap.py`

## Current Bootstrap Validation

Run:

```bash
python scripts/validate_bootstrap.py
```

The script checks:

- required files exist;
- JSON schemas parse;
- JSON examples parse;
- examples conform to the initial schemas using a minimal built-in schema checker.

## Not Yet Implemented

- full JSON Schema validation engine;
- rule extraction;
- coverage matrix generation;
- fixture validation;
- mutation verification;
- report generation.

Future scripts should remain deterministic and dependency-light unless maintainers explicitly approve additional dependencies.
