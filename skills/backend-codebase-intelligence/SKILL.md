---
name: backend-codebase-intelligence
description: Analyzes backend systems to extract architecture, modules, APIs, database usage, data flow, and entry points for faster understanding of new or legacy backend codebases
metadata:
  version: 1.0.0
---

# Backend Codebase Intelligence

## Provides

- Backend structure and architecture discovery
- Module and service mapping
- API and endpoint analysis
- Database model and query analysis
- Data flow and dependency tracing
- External integration mapping
- Entry point and runtime wiring detection

## Use When

- Understanding a new backend system
- Exploring a legacy backend codebase
- Learning how APIs, services, and data layers fit together
- Preparing to debug, extend, or refactor backend code

---

## Instructions

### 1. Start with Project Structure

- Identify the main backend folders, services, and runtime entry points
- Look for framework files, server bootstrap code, and configuration
- Determine whether the project is monolithic, modular, service-oriented, or monorepo-based

Review targets:

- `src/`, `server/`, `api/`, `services/`, `controllers/`, `routes/`
- `package.json`, `pyproject.toml`, `requirements.txt`, `Cargo.toml`, `go.mod`
- deployment, runtime, and framework config files

---

### 2. Find Entry Points and Startup Flow

- Locate where the server starts and how routes, middleware, jobs, or workers are registered
- Identify application bootstrap, dependency injection, environment loading, and database initialization
- Trace how the app begins handling requests or background work

---

### 3. Map Core Modules

- Group files by domain, feature, or technical layer
- Identify controllers, routes, services, repositories, models, middleware, jobs, and shared utilities
- Focus first on the modules relevant to the current task before reading broadly

---

### 4. Analyze API Surface

- Identify REST, GraphQL, RPC, webhook, or internal service endpoints
- Trace how requests move through routing, validation, auth, business logic, and persistence
- Note public, authenticated, admin, and internal-only paths when visible

---

### 5. Analyze Database Usage

- Identify ORM, ODM, query builder, or raw SQL usage
- Trace models, schemas, repositories, migrations, and relationships
- Look for where reads, writes, transactions, and data transformations happen
- Note whether data access is centralized or spread across handlers and services

Examples:

- Sequelize, TypeORM, Prisma, Mongoose
- SQL queries in repositories or services
- Model-to-table or schema relationships

---

### 6. Trace Data Flow

- Follow data from request input through validation, business logic, storage, and response output
- Track database reads and writes, cache usage, queue operations, and external service calls
- Note boundaries between transport, domain logic, persistence, and infrastructure

---

### 7. Identify Conventions and Architecture Patterns

- Look for naming conventions, folder structure, testing style, and layering rules
- Check whether the backend uses MVC, services and repositories, handlers, hexagonal architecture, or domain modules
- Follow existing patterns before suggesting changes

---

### 8. Understand Dependencies and Integrations

- Review key internal dependencies and major third-party libraries
- Identify databases, caches, queues, storage systems, authentication providers, and external APIs
- Note where configuration, secrets, or environment variables affect behavior

---

### 9. Investigate Legacy or Risky Areas Carefully

- Confirm behavior by tracing actual call paths instead of assuming from names
- Watch for duplicate logic, dead endpoints, outdated comments, partial migrations, and hidden side effects
- Call out areas where runtime behavior is unclear from static inspection alone
- Flag common backend anti-patterns such as business logic inside controllers, tight coupling, duplicated service logic, and unclear validation boundaries

---

### 10. Summarize Findings Clearly

- Explain the system in terms of structure, responsibilities, and important flows
- Highlight the files or modules most relevant to the task
- Separate confirmed findings from assumptions or unclear areas

Standard workflow:

1. Scan structure and config
2. Find entry points and bootstrap
3. Identify core modules and APIs
4. Inspect database models and query layers
5. Trace request and data flow
6. Summarize architecture, dependencies, and unknowns

---

### 11. Safety Notes

- Do not assume architecture from folder names alone
- Backend behavior often depends on runtime configuration, middleware, and infrastructure
- A high-level map is useful, but critical behavior should be verified in code
- Prefer concrete file references and traced paths over vague summaries

## Output Format

### Overview

- Short summary of what the backend appears to do

### Key Files and Modules

- Most relevant files or directories and why they matter

### API Surface

- Main routes, handlers, or service interfaces

### Database Insights

- Models, relationships, query layers, and storage patterns

### Data Flow

- How requests and data move through the system

### Integrations

- External services, queues, auth providers, and infrastructure dependencies

### Confirmed

- Conclusions directly supported by code

### Unclear

- Gaps, assumptions, or areas not yet verified
