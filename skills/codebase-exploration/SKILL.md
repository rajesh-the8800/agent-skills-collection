---
name: codebase-exploration
description: Helps understand and analyze an existing codebase by identifying structure, entry points, data flow, and important modules
metadata:
  version: 1.0.0
---

## Provides

- Codebase structure discovery
- Entry point and module tracing
- Data flow and dependency review
- Legacy and unfamiliar code understanding

## Use When

- Working with a new codebase
- Exploring a complex or legacy project
- Understanding how features are connected
- Preparing to debug, extend, or refactor existing code

---

## Instructions

### 1. Start with Project Structure

- Identify the main folders, frameworks, and package layout
- Look for entry points, configuration files, and build setup
- Determine whether the project is frontend, backend, full-stack, or monorepo-based

Review targets:

- `src/`, `app/`, `server/`, `packages/`
- `package.json`, `pyproject.toml`, `Cargo.toml`
- framework or build config files

---

### 2. Find the Entry Points

- Locate where the application starts and how modules are wired together
- Trace routing, bootstrapping, initialization, and dependency setup
- Identify where requests, UI rendering, background jobs, or services begin

---

### 3. Map Key Features and Modules

- Group files by feature, domain, or technical layer
- Identify important modules such as auth, API clients, database access, state management, and shared utilities
- Focus on the files most relevant to the current task before reading everything

---

### 4. Trace Data Flow

- Follow how data enters, changes, and leaves the system
- Track requests, state updates, database reads and writes, and external service calls
- Note boundaries between UI, business logic, persistence, and infrastructure

---

### 5. Identify Conventions and Patterns

- Look for naming conventions, folder patterns, testing style, and architectural rules
- Check whether the codebase uses feature folders, layered architecture, MVC, services, hooks, or domain modules
- Follow existing patterns before proposing changes

---

### 6. Understand Dependencies and Integrations

- Review core internal dependencies and important third-party libraries
- Identify external APIs, databases, queues, caches, and background workers
- Note where environment configuration or secrets affect behavior

---

### 7. Investigate Legacy or Complex Areas Carefully

- Prefer reading the smallest useful set of files first
- Confirm assumptions by tracing actual call paths instead of guessing from filenames
- Watch for duplicated logic, dead code, outdated comments, or partially migrated systems

---

### 8. Verify Before Concluding

- Do not claim behavior unless it is supported by code, configuration, tests, or runtime wiring
- Prefer concrete file references over intuition or naming-based assumptions
- If a conclusion is uncertain, state that it is a hypothesis and explain what still needs verification
- Cross-check critical behavior in more than one place when possible, such as route definition plus handler, or component usage plus state source

---

### 9. Summarize Findings Clearly

- Explain the codebase in terms of structure, responsibilities, and important flows
- Highlight the files or modules most relevant to the current task
- Call out uncertainty, risky areas, and places that need deeper validation
- Separate confirmed findings from assumptions or open questions

Standard exploration flow:

1. Scan structure and configs
2. Find entry points
3. Identify key modules
4. Trace data flow
5. Verify key conclusions in code
6. Summarize how the system fits together

---

### 10. Preferred Response Shape

- `Overview`: short summary of what the codebase or feature appears to do
- `Key Files`: the most relevant files and why they matter
- `Flow`: how control or data moves through the system
- `Confirmed`: conclusions directly supported by code
- `Unclear`: questions, gaps, or areas not yet verified

---

### 11. Safety Notes

- Do not assume architecture from folder names alone
- Legacy codebases often contain patterns that are no longer actively used
- A fast high-level map is useful, but important behavior should be verified in code
- Prefer concrete file references and call paths over vague summaries
- When the evidence is incomplete, say so clearly instead of filling gaps with guesses

## Standard Flow

```javascript
scan project structure
-> locate entry points
-> identify key modules and conventions
-> trace data flow and dependencies
-> verify conclusions with file-backed evidence
-> summarize relevant architecture and risks
```
