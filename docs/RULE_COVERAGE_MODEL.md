# Rule Coverage Model

## Purpose

The rule coverage model describes how this repository represents behavioral rules and tracks their movement toward executable validation.

## Core Concepts

### Behavioral Rule

A behavioral rule is a normative expectation that constrains behavior.

Examples:

- an assistant must not invent repository state;
- a workflow must stop when required evidence is missing;
- a report must distinguish implemented facts from assumptions.

### Rule Source

A rule source is the document, prompt, policy, contract, workflow, or specification from which the rule is derived.

### Rule ID

A rule ID is a stable identifier for a behavioral rule.

Recommended pattern:

```text
BRC-RULE-0001
```

Rule IDs must not be reused for different meanings.

### Coverage Record

A coverage record describes how a rule is covered.

It links a rule to:

- source reference;
- lifecycle state;
- coverage state;
- fixture references;
- executable check references;
- validation status.

### Executable Check

An executable check is a deterministic script, test, CI step, or validation command that can pass or fail.

### Fixture

A fixture is a small artifact used to demonstrate expected valid or invalid behavior.

### Validation Report

A validation report is a structured output that records whether checks passed, failed, were unknown, or were not executable.

### Unknown Coverage

Unknown coverage means the repository does not yet have enough evidence to classify coverage.

### Human-Reviewed Rule

A human-reviewed rule has been reviewed and accepted by a maintainer, but it may not be machine-verifiable.

### Machine-Verifiable Rule

A machine-verifiable rule has a structure that can be checked by deterministic tooling.

### Non-Executable Rule

A non-executable rule is important but cannot currently be checked by deterministic tooling. It may still be documented and human-reviewed.

## Rule Lifecycle

Allowed lifecycle states:

```text
proposed
documented
normalized
fixture_backed
test_backed
executable
deprecated
```

### proposed

The rule is suggested but not yet accepted as part of the repository model.

### documented

The rule is written in a source document.

### normalized

The rule has a stable ID and structured record.

### fixture_backed

The rule has at least one example or fixture.

### test_backed

The rule has a test or validation check, but it may not yet be part of CI.

### executable

The rule has an executable check that can produce deterministic pass/fail output.

### deprecated

The rule is retired and should not be used for new coverage decisions.

## Coverage States

Allowed coverage states:

```text
covered
partially_covered
not_covered
not_executable
unknown
```

### covered

The rule is covered by the expected mechanism for its current lifecycle state.

### partially_covered

Some evidence exists, but coverage is incomplete.

### not_covered

The rule has no meaningful coverage yet.

### not_executable

The rule is not currently suitable for deterministic execution.

### unknown

Evidence is missing or not reviewed.

## Bootstrap Rule

At bootstrap, most real project rules should be `unknown`, `not_covered`, or `documented`. Do not mark rules as executable until executable checks exist.
