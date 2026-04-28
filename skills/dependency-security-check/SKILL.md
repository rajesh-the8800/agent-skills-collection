---
name: dependency-security-check
description: Analyzes project dependencies for known vulnerabilities including outdated packages, known CVEs, and unsafe libraries
metadata:
  version: 1.0.0
---

## Provides

- Outdated package review points
- Known vulnerability and CVE checks
- Unsafe or abandoned library review guidance
- Dependency update prioritization

## Use When

- Updating project dependencies
- Maintaining an existing application
- Auditing package risk before releases
- Reviewing third-party library safety

---

## Instructions

### 1. Inventory Direct and Transitive Dependencies

- List the main dependencies used by the project
- Include transitive packages when the package manager or audit tool exposes them
- Focus first on packages related to auth, parsing, file handling, templating, networking, and build tooling

---

### 2. Check for Outdated Packages

- Identify packages that are far behind the current maintained version
- Note whether the package is still actively maintained
- Prioritize updates for security-sensitive libraries and internet-facing services

Review targets:

- Framework packages
- HTTP clients and servers
- Authentication libraries
- File upload and parsing packages

---

### 3. Check for Known Vulnerabilities

- Review dependency audit results for known CVEs and advisories
- Record severity, affected package, affected version range, and fixed version when available
- Confirm whether the vulnerable package is actually reachable in the project runtime or build path

---

### 4. Identify Unsafe or Abandoned Libraries

- Flag libraries with no recent maintenance, unresolved security issues, or poor ecosystem trust
- Review whether the package has safer maintained alternatives
- Be cautious with packages that execute code, process untrusted input, or touch the filesystem or network

Common risk areas:

- Markdown or HTML sanitizers
- XML or YAML parsers
- Template engines
- Serialization libraries

---

### 5. Review Update Risk and Compatibility

- Separate low-risk patch updates from larger version jumps
- Note where major upgrades may require code changes or migration work
- Recommend the safest update path instead of only listing outdated packages

Standard flow:

1. Audit dependencies
2. Identify vulnerable or outdated packages
3. Group findings by severity and upgrade effort
4. Prioritize high-impact security fixes
5. Suggest safer replacements when needed

---

### 6. Validate Dependency Usage

- Check whether flagged libraries are actually used in production code, dev tooling, or only local workflows
- Treat production runtime dependencies as highest priority
- Review dev dependencies too when they affect build pipelines, code generation, or developer machines

---

### 7. Report Findings Clearly

- Include package name, current version, issue type, and recommended action
- Distinguish between:
  - vulnerable and must-fix
  - outdated but low risk
  - suspicious or unmaintained
- Highlight packages that should be removed entirely rather than upgraded

---

### 8. Safety Notes

- Not every outdated package is a security issue, but stale packages deserve review
- Audit tools can produce noisy results, so validate reachability and real impact before escalating
- Security fixes should be paired with regression testing after upgrades
- Lockfiles and reproducible installs help reduce supply-chain surprises

## Standard Flow

```javascript
inventory dependencies
-> check for outdated packages
-> review known vulnerabilities and CVEs
-> identify unsafe or abandoned libraries
-> prioritize updates or replacements
```
