# Executable Pipeline Model

## Purpose

This document defines the intended evolution from documentation to executable coverage.

## Pipeline Stages

### Stage 0 — Capability Declaration

Before any audit, declare what can actually be inspected or executed.

Output should include:

```text
repository read access
execution access
files inspected
commands run
unavailable evidence
```

### Stage 1 — Rule Inventory

Find candidate behavioral rules in source documents.

Bootstrap status: planned.

### Stage 2 — Rule Normalization

Convert candidate rules into stable rule records.

Bootstrap status: schema foundation exists.

### Stage 3 — Coverage Mapping

Create coverage records that link rules to examples, fixtures, checks, and reports.

Bootstrap status: schema foundation exists.

### Stage 4 — Static Validation

Validate that rule and coverage records are well-formed.

Bootstrap status: minimal validation exists through `scripts/validate_bootstrap.py`.

### Stage 5 — Fixture Validation

Check valid and invalid fixtures.

Bootstrap status: planned.

### Stage 6 — Executable Checks

Run deterministic checks for machine-verifiable rules.

Bootstrap status: planned.

### Stage 7 — CI Integration

Run validation in GitHub Actions.

Bootstrap status: lightweight workflow scaffold exists.

### Stage 8 — Reporting

Generate human-readable and machine-readable reports.

Bootstrap status: planned.

## Advisory vs Strict Mode

### Advisory Mode

Reports gaps without blocking development.

### Strict Mode

Fails when required coverage or validation is missing.

Strict mode is not implemented at bootstrap.

## Minimal Bootstrap Validation

The initial validation script checks:

- required files exist;
- JSON schemas parse;
- JSON examples parse;
- examples conform to a small supported subset of the schemas.

This is intentionally not a full policy engine.

## Future Validator Requirements

A future validator should:

- be deterministic;
- return clear exit codes;
- emit JSON reports;
- support advisory and strict modes;
- distinguish unknown from failed;
- avoid hidden network calls;
- avoid implicit model judgment.
