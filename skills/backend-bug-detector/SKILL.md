---
name: backend-bug-detector
description: Identifies common backend issues such as null handling mistakes, improper error handling, logic flaws, and risky service behavior when debugging backend services
metadata:
  version: 1.0.0
---

# Backend Bug Detector

## Provides

- Null and undefined handling checks
- Error handling and control-flow review
- Logic flaw detection in services and handlers
- Data access, async, and backend lifecycle bug checks

## Use When

- Debugging backend services
- Investigating failing API behavior
- Reviewing backend code for correctness issues
- Looking for logic, validation, or runtime bugs in server-side systems

---

## Instructions

### 1. Start with the Affected Flow

- Identify the endpoint, worker, service, or job involved in the bug
- Trace the entry point, request path, or execution path before reviewing unrelated files
- Focus first on the smallest code path that can explain the observed behavior

---

### 2. Check Null, Undefined, and Missing Data Handling

- Look for unsafe access to nullable values
- Review optional fields, missing request data, empty query results, and absent configuration
- Check whether code handles not-found, empty, or partial-data cases correctly

Examples:

- accessing properties on possibly null database results
- assuming config values always exist
- using request fields without validation

---

### 3. Review Error Handling

- Check whether errors are caught, translated, logged, and returned appropriately
- Flag swallowed exceptions, overly generic catches, and missing error propagation
- Review whether failures leak internal details or hide the real cause

Review targets:

- controller and route handlers
- service-layer exceptions
- background jobs and queue consumers
- database and external API error paths

---

### 4. Check Business Logic and Control Flow

- Look for incorrect branching, inverted conditions, unreachable paths, and missing guard clauses
- Review authorization, validation, and state-transition logic carefully
- Check whether edge cases produce unintended results

Examples:

- incorrect status transitions
- duplicate processing paths
- incorrect fallback logic

---

### 5. Review Async and Concurrency Behavior

- Check for missing `await`, unhandled promises, and race conditions
- Review retries, timeouts, transaction boundaries, and parallel operations
- Confirm async work handles cancellation, duplicate execution, or partial failure safely when relevant

---

### 6. Review Data Access and Persistence

- Check database queries, repository calls, and cache usage for incorrect assumptions
- Look for missing transaction handling, inconsistent writes, stale reads, or improper error recovery
- Confirm not-found and uniqueness cases are handled correctly

---

### 7. Review Validation and Input Handling

- Check whether request params, body fields, headers, and job payloads are validated before use
- Look for missing type checks, range checks, and required-field enforcement
- Confirm invalid input does not silently continue into business logic

---

### 8. Check Framework and Runtime-Specific Risks

- Review middleware order, dependency injection wiring, and lifecycle hooks when relevant
- Check whether background workers, scheduled jobs, or event consumers handle retries and idempotency safely
- Look for misconfigured environment-dependent logic that only fails in certain deployments

---

### 9. Report Findings by Severity

- Group issues as critical, high, medium, or minor
- Include:
  - issue
  - file
  - explanation
  - suggested fix
- Separate confirmed bugs from likely risks or suspicious patterns

Standard workflow:

1. Identify the affected backend flow
2. Trace entry points and dependent services
3. Review null handling, errors, logic, and async behavior
4. Check persistence and validation paths
5. Return a structured bug report

---

### 10. Safety Notes

- Do not report a pattern as a bug unless code behavior supports it
- Prefer file-backed findings over style opinions
- Distinguish correctness issues from maintainability concerns
- Call out uncertainty when runtime wiring, environment config, or infrastructure behavior is not fully visible

## Output Format

### Critical Bugs

- Issue
- File
- Explanation
- Suggested Fix

### High Priority Issues

- Issue
- File
- Explanation
- Suggested Fix

### Medium Issues

- Issue
- File
- Explanation
- Suggested Fix

### Minor Issues or Improvements

- Issue
- Suggestion

### Passed Checks

- Meaningful validations that passed
