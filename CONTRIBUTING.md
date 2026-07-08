# Contributing

This repository is in bootstrap phase. Contributions should preserve clarity, minimalism, and evidence boundaries.

## Before Contributing

Read:

- `README.md`
- `AGENTS.md`
- `docs/PROJECT_CHARTER.md`
- `docs/CLAIM_BOUNDARIES.md`
- `STATUS.md`
- `ROADMAP.md`

## Contribution Principles

- Prefer small, reviewable changes.
- Do not add heavy dependencies without discussion.
- Do not overclaim implemented behavior.
- Keep examples generic and free of private data.
- Update documentation when changing schemas or concepts.
- Add validation only when it is deterministic and useful.

## Pull Request Checklist

A pull request should state:

- what changed;
- why it changed;
- validation performed;
- known limitations;
- whether the change affects schemas, examples, or CI.

## Validation

Run:

```bash
python scripts/validate_bootstrap.py
```

Do not claim validation passed unless this command was actually run.
