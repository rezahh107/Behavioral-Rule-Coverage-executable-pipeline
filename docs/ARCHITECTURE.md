# Architecture

## Overview

The repository is organized into four layers.

```text
Documentation Layer
  Explains purpose, boundaries, workflow, and roadmap.

Data Model Layer
  Defines behavioral rules and coverage records with JSON Schemas.

Example Layer
  Provides generic example records to demonstrate the model.

Validation Layer
  Provides lightweight checks that can later evolve into executable coverage validation.
```

## Current Architecture

```text
README.md
AGENTS.md
STATUS.md
ROADMAP.md
docs/
  PROJECT_CHARTER.md
  ARCHITECTURE.md
  CLAIM_BOUNDARIES.md
  RULE_COVERAGE_MODEL.md
  EXECUTABLE_PIPELINE_MODEL.md
  LLM_WORKFLOW.md
schemas/
  rule.schema.json
  coverage-record.schema.json
examples/
  rules/
  coverage/
scripts/
  validate_bootstrap.py
.github/
  workflows/
```

## Future Architecture

The future executable pipeline may add:

```text
Rule inventory
  Finds or imports rule records.

Rule normalization
  Assigns stable IDs and lifecycle states.

Coverage mapping
  Maps rules to sources, examples, fixtures, tests, and checks.

Validator
  Verifies records and reports pass/fail/unknown status.

Report generator
  Emits JSON and Markdown reports.

CI integration
  Runs validation on pull requests and main branch changes.
```

## Design Constraints

- Keep the bootstrap dependency-free.
- Do not add a database.
- Do not add a web server.
- Do not claim enforcement before executable checks exist.
- Keep schemas small until real usage justifies expansion.

## Data Flow

Initial intended flow:

```text
source document
→ behavioral rule record
→ coverage record
→ example or fixture
→ validation script
→ report
```

## Trust Boundary

The repository distinguishes:

- documented rules;
- human-reviewed rules;
- machine-verifiable rules;
- executable checks;
- validation reports.

A documented rule is not automatically machine-verifiable.

A machine-verifiable rule is not automatically enforced in CI.

A CI workflow file is not the same as a successful CI run.

## Implementation Status

The repository currently implements only bootstrap validation. The full executable coverage pipeline is planned.
