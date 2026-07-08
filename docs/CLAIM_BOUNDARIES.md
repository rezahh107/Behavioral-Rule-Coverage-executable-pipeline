# Claim Boundaries

This document defines what the repository may and may not claim.

## Current Valid Claims

The repository may claim:

- it provides a structured bootstrap for Behavioral Rule Coverage;
- it defines initial concepts and lifecycle states;
- it includes minimal JSON Schemas;
- it includes generic examples;
- it includes a lightweight bootstrap validation script;
- it has a roadmap toward executable validation.

## Current Invalid Claims

The repository must not claim:

- full behavioral verification;
- complete prompt compliance enforcement;
- complete LLM safety coverage;
- production-grade policy engine behavior;
- universal compatibility with all models;
- runtime monitoring;
- complete CI enforcement of behavioral rules;
- mutation verification;
- cross-repository enforcement;
- complete policy compliance.

## Evidence Rules

A claim is valid only when backed by evidence.

Examples:

```text
Implemented file exists
  Evidence: file path in repository.

Schema exists
  Evidence: schema file in `schemas/`.

Example parses
  Evidence: validation command output.

CI passed
  Evidence: concrete workflow run or status check.

Rule is executable
  Evidence: executable check exists and is linked from coverage record.
```

## Forbidden Overclaims

Do not write:

```text
The repository enforces LLM behavior.
The pipeline guarantees compliance.
All behavioral rules are covered.
CI proves policy compliance.
This is production ready.
```

Unless future evidence explicitly supports those claims.

## Correct Bootstrap Language

Use:

```text
This repository provides a foundation.
This rule is documented.
This coverage state is unknown.
This validation path is planned.
This check is not yet implemented.
```

## Unknown Coverage

`unknown` is a valid state.

Use it when:

- the source was not inspected;
- the rule has not been reviewed;
- no coverage record exists;
- no fixture or test exists;
- validation has not been run.

Do not replace unknown coverage with assumptions.
