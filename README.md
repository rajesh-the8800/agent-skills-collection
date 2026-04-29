# Agent Skills Collection

A curated collection of reusable agent skills for frontend, backend, security, API review, and codebase analysis.

## Purpose

This repository contains skill definitions that help an AI agent perform focused tasks more reliably. Each skill is written as a `SKILL.md` file and is designed to improve consistency, speed, and accuracy for a specific kind of work.

## How to Install

You can install a skill from a GitHub repository or from a direct hosted URL.

### Install All Skills from This Repository

```bash
npx skills add <owner>/<repo>
```

This installs the full collection from the repository.

### Install from GitHub

```bash
npx skills add <owner>/<repo>
```

Example:

```bash
npx skills add your-github-username/agent-skills-collection
```

### Install a Specific Skill from This Repository

```bash
npx skills add <owner>/<repo> --skill <skillname>
```

This installs only the selected skill from the repository.

Examples:

```bash
npx skills add <owner>/<repo> --skill frontend-bug-detector
npx skills add <owner>/<repo> --skill backend-codebase-intelligence
npx skills add <owner>/<repo> --skill database-query-analyzer
```

### Install from a Direct URL

```bash
npx skills add https://example.com/SKILL.md
```

### Create a New Skill Locally

```bash
npx skills init
```

This creates a starter `SKILL.md` file in the current folder.

## How to Use

After installing a skill, use it by asking the agent to perform a task that matches the skill.

Examples:

- Use `frontend-bug-detector` to review this React component for bugs.
- Use `backend-codebase-intelligence` to understand this backend project.
- Use `database-query-analyzer` to inspect slow query paths.

Notes:

- Replace `<skillname>` with the exact skill folder name.
- Skill names use kebab-case, such as `frontend-bug-detector` or `api-design-validator`.

## Repository Structure

```text
skills/
  skill-name/
    SKILL.md
    references/   # optional
    scripts/      # optional
    assets/       # optional
```

## Skill Categories

### Frontend Skills

- `api-integration-frontend`
- `basic-authentication-handling-frontend`
- `environment-configuration`
- `frontend-bug-detector`
- `frontend-codebase-intelligence`
- `frontend-security-audit`
- `form-handling-validation`
- `loading-error-state`
- `pagination-lazy-loading`
- `responsive-design`
- `seo-optimization`
- `simple-caching-frontend`
- `state-management-basics`

### Backend Skills

- `api-design-validator`
- `api-security-review`
- `backend-bug-detector`
- `backend-codebase-intelligence`
- `database-query-analyzer`

### Security and Review Skills

- `dependency-security-check`
- `frontend-security-audit`
- `network-data-flow-security-audit`
- `api-security-review`

### Exploration Skills

- `codebase-exploration`
- `frontend-codebase-intelligence`
- `backend-codebase-intelligence`

## How Skills Work

Each skill typically contains:

- a `name`
- a `description`
- step-by-step instructions
- optional reference files for deeper guidance

## Naming Convention

Skills use standard kebab-case names, for example:

- `frontend-bug-detector`
- `backend-codebase-intelligence`
- `database-query-analyzer`

## Authoring Guidelines

When adding new skills:

- keep the description trigger-friendly
- use concise instructions
- include `Provides` and `Use When` sections
- prefer practical workflows over theory
- separate confirmed findings from assumptions for analysis-oriented skills

## Notes

These skills help an AI agent work more effectively, but they do not guarantee correctness. Best results come from combining skill guidance with direct code verification.

## License

Add your preferred license here.
