# Roadmap

This roadmap is phased to prevent premature complexity and false completeness.

## Phase 0 — Repository Bootstrap

Goal: Create a clean, understandable project foundation.

Deliverables:

- repository structure;
- core documents;
- initial schemas;
- examples;
- bootstrap validation script;
- lightweight CI workflow.

Status: implemented in initial bootstrap.

## Phase 1 — Rule and Coverage Schema Stabilization

Goal: Make the core data model stable enough for repeated use.

Planned work:

- review `schemas/rule.schema.json`;
- review `schemas/coverage-record.schema.json`;
- add schema documentation;
- add more valid and invalid examples;
- define stable rule ID conventions;
- decide whether to add a canonical coverage matrix schema.

Exit criteria:

- examples validate consistently;
- maintainers agree on lifecycle and coverage states;
- schema changes are documented.

## Phase 2 — Fixtures and Validation Records

Goal: Introduce real validation fixtures.

Planned work:

- add valid fixture examples;
- add invalid fixture examples;
- define fixture naming conventions;
- document expected pass/fail behavior;
- add fixture provenance fields where needed.

Exit criteria:

- at least one rule has both valid and invalid examples;
- validation records clearly distinguish unknown, not executable, and failed coverage.

## Phase 3 — Minimal Executable Validator

Goal: Add a deterministic validator for rule and coverage records.

Planned work:

- implement a small validation script;
- validate schemas and examples;
- emit JSON and Markdown reports;
- avoid heavy dependencies unless explicitly approved.

Exit criteria:

- validator returns non-zero on invalid examples;
- validator reports clear diagnostics;
- CI runs the validator.

## Phase 4 — CI Integration

Goal: Wire validation into GitHub Actions.

Planned work:

- strengthen `validate-docs.yml`;
- add generated report artifacts;
- fail CI on malformed rule and coverage records;
- keep advisory and strict modes separate.

Exit criteria:

- bootstrap validation runs on pull requests;
- strict failures are limited to clearly defined checks.

## Phase 5 — Coverage Dashboard / Reporting

Goal: Make rule coverage easy to review.

Planned work:

- generate `reports/coverage-report.json`;
- generate `reports/coverage-report.md`;
- summarize lifecycle and coverage states;
- identify unknown and not-covered rules.

Exit criteria:

- maintainers can see which rules are documented, backed by examples, test-backed, or executable.

## Phase 6 — Cross-Repository or Project-Level Adoption

Goal: Allow other repositories to adopt the pipeline.

Planned work:

- define adoption instructions;
- support target repository metadata;
- define import/export of rule records;
- document limitations for prompt-only audits.

Exit criteria:

- a second repository can use the model without relying on this chat history.
