---
name: frontend-codebase-intelligence
description: Analyze and understand frontend codebases, especially React, Next.js, and Angular projects, by extracting structure, components, routing, dependencies, and entry points when exploring unfamiliar UI code
---

# Frontend Codebase Intelligence

This skill helps analyze modern frontend applications by identifying structure, components, routing, and dependencies.

---

## Capabilities

### 📂 Structure Understanding
- Generates a high-level folder structure
- Focuses on important frontend directories:
  - src/
  - components/
  - pages/ / app/
  - hooks/
  - services/

---

### ⚛️ Component Intelligence (React / Next.js)
- Detects:
  - Functional components
  - Arrow function components
- Identifies:
  - Component relationships (imports)
- Detects hooks:
  - useState, useEffect, custom hooks

---

### ▲ Next.js Routing Analysis
- Extracts routes from:
  - pages/
  - app/
- Identifies:
  - API routes (`/api/*`)
  - Layout structure

---

### 🅰️ Angular Basic Support
- Detects:
  - @Component
  - @NgModule
- Identifies routing modules

---

### 🔗 Dependency Mapping
- Extracts import relationships
- Builds file-level dependency graph

---

### 🚀 Entry Points
- Detects:
  - index.js / main.js
  - main.ts (Angular)
  - Next.js root files

---

## Input

- Project directory or codebase

---

## Output

- Project structure
- Component map
- Routing map
- Dependency graph
- Entry points

---

## Instructions

1. Scan the project directory recursively
2. Read [references/structure-analysis.md](references/structure-analysis.md) before summarizing project layout
3. Read [references/framework-detection.md](references/framework-detection.md) before choosing a framework-specific path
4. Read only the relevant reference guides for the detected stack:
   - [references/component-detection.md](references/component-detection.md) for React, Next.js, and Angular component patterns
   - [references/routing-analysis.md](references/routing-analysis.md) for routing extraction
   - [references/dependency-mapping.md](references/dependency-mapping.md) for import and dependency relationships
5. Ignore:
   - node_modules
   - .next
   - build/dist folders
6. Detect framework using package.json, project structure, and framework-specific config files
7. Perform:
   - Structure analysis
   - Component detection
   - Routing extraction
   - Dependency mapping
   - Entry point detection
8. Return a structured summary with:
   - Overview
   - Key files and folders
   - Detected framework and confidence
   - Component map
   - Routing map
   - Dependency relationships
   - Entry points
   - Unclear or unverified areas

---

## Notes

- Uses lightweight analysis (pattern-based)
- Framework-aware but not deeply semantic
- Extendable with AST-based parsing

---

## Limitations

- No runtime flow tracing
- Limited Angular deep analysis
- Basic Next.js server/client detection
- No state management tracking
