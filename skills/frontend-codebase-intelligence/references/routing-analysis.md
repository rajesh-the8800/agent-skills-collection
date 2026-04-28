# Routing Analysis

## Next.js

### Pages Router
pages/index.js → /
pages/about.js → /about
pages/blog/[slug].js → /blog/:slug
pages/docs/[...parts].js → /docs/*

### App Router
app/page.js → /
app/blog/page.js → /blog
app/blog/[slug]/page.js → /blog/:slug

### Important App Router Cases

- Route groups: `app/(marketing)/about/page.js`
- Dynamic segments: `app/users/[id]/page.js`
- Catch-all: `app/docs/[...slug]/page.js`
- Optional catch-all: `app/docs/[[...slug]]/page.js`
- Nested layouts: `layout.js`
- Parallel routes and special files should be called out if seen, even if not fully mapped

### API Routes
pages/api/*
app/api/*

---

## React

- Look for:
  - react-router
  - <Route> components
  - `createBrowserRouter`
  - `createRoutesFromElements`
  - route config arrays
  - nested routes and layout routes

---

## Angular

- app-routing.module.ts
- Extract:
  - path
  - component mapping
  - lazy-loaded modules where visible

## Output Guidance

- Distinguish confirmed routes from inferred routes
- Call out dynamic, catch-all, grouped, or lazy-loaded routes separately
- If the router is built programmatically and cannot be mapped fully, say so clearly
