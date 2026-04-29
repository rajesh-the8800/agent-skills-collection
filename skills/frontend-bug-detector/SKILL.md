---
name: frontend-bug-detector
description: Detects bugs, anti-patterns, and risky frontend implementations in React, Next.js, and Angular codebases, especially during debugging, code review, and investigation of unexpected UI behavior
metadata:
  version: 1.0.0
---

# Frontend Bug Detector

## Provides

- React hook bug detection
- Import and dependency issue checks
- State and rendering issue review
- Async, side-effect, and lifecycle bug checks
- Framework-specific review points for Next.js and Angular

## Use When

- Debugging frontend issues
- Reviewing pull requests
- Investigating unexpected UI behavior
- Looking for performance or rendering problems
- Working with React, Next.js, or Angular codebases

---

## Instructions

### 1. Start with Structure and Entry Points

- Identify the main frontend folders and entry points
- Focus first on the modules involved in the reported bug or target feature
- Trace where state, props, routing, and async calls enter the flow

---

### 2. Check Hooks and Lifecycle Usage

- Flag conditional hook usage
- Look for missing or unstable dependencies in `useEffect`, `useMemo`, and `useCallback`
- Check for infinite re-render loops caused by state updates inside effects or render paths
- Review cleanup handling for subscriptions, timers, and listeners

Examples:

- Missing dependencies in `useEffect`
- Hook calls inside conditions or loops
- Effects that trigger repeated state changes

---

### 3. Validate Imports and Module Wiring

- Check for unused imports, broken import paths, duplicate imports, and circular dependencies
- Confirm that shared utilities, hooks, and services are imported from the intended source
- Look for stale or moved files that leave dead references behind

---

### 4. Review State Management

- Check for direct state mutation
- Look for stale closures, incorrect state updates, or state derived in unsafe ways
- Review whether global state is used where local state would be simpler
- Confirm that async state updates handle loading, success, and failure safely

---

### 5. Review Rendering Logic

- Flag missing `key` props in lists
- Look for expensive work performed directly during render
- Check whether repeated inline objects or functions are causing noisy rerenders
- Identify overly large components with mixed responsibilities

Note:

- Do not recommend memoization automatically in every case
- Flag rendering inefficiency only when there is a plausible rerender or cost issue

---

### 6. Check Async and Side Effects

- Look for unhandled promises and API calls without error handling
- Check for race conditions between multiple requests or rapid state changes
- Confirm async work is canceled, ignored, or cleaned up when components unmount
- Review retry, loading, and failure behavior for user-facing actions

---

### 7. Check Framework-Specific Risks

#### React / Next.js

- Review server and client boundary issues
- Check for hydration mismatches or browser-only APIs used in server-rendered paths
- Review routing and data-fetching patterns for misuse

#### Angular

- Review lifecycle hook usage
- Check template bindings, services, and module wiring
- Look for subscription cleanup issues and change-detection pitfalls

---

### 8. Report Findings by Severity

- Group issues as critical, high, medium, or minor
- Include:
  - issue
  - file
  - explanation
  - suggested fix
- Separate confirmed bugs from likely risks or anti-patterns
- Include passed checks only when they materially help the review

Standard workflow:

1. Identify the affected feature or module
2. Trace structure and entry points
3. Review hooks, imports, state, and rendering
4. Check async behavior and framework-specific risks
5. Return a structured bug report

---

### 9. Safety Notes

- Do not report a pattern as a bug unless code behavior supports it
- Prefer file-backed findings over stylistic opinions
- Distinguish correctness bugs from performance suggestions
- Call out uncertainty clearly when the surrounding runtime or framework wiring is not visible

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

- List meaningful validations that passed

## Example

```javascript
useEffect(() => {
  fetchData();
}, []); // Missing dependency if fetchData changes across renders
```
