# Framework Detection

Detect the frontend framework using package manifests first, then confirm with file structure and framework-specific config files.

## React
- react
- react-dom

## Next.js
- next
- next.config.js
- next.config.mjs
- app/
- pages/

## Angular
- @angular/core
- angular.json
- src/main.ts
- app-routing.module.ts

## Strategy

1. Read `package.json`
2. Check `dependencies` and `devDependencies`
3. If the repo is a monorepo, also inspect package manifests inside workspace apps or packages
4. Match known framework identifiers
5. Confirm the result using file structure and framework-specific config files
6. If signals conflict, report the likely framework and call out uncertainty

## Fallback Signals

- `next` plus `app/` or `pages/` usually indicates Next.js
- `react` without `next` often indicates React or another React-based framework
- `@angular/core` plus `angular.json` strongly indicates Angular
- Multiple frameworks may coexist in a monorepo, migration, or hybrid repository

## Output Guidance

- Report the detected framework
- Include the evidence used
- State confidence as high, medium, or low if the repo shape is unusual
