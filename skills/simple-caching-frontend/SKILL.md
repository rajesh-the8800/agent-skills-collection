---
name: simple-caching-frontend
description: Reduces repeated frontend API calls using local storage, session storage, and basic client-side caching strategies
metadata:
  version: 1.0.0
---

## Provides

- Local storage caching
- Session storage caching
- Basic cache read and write patterns
- Cache expiry handling

## Use When

- Improving performance for repeated data
- Avoiding unnecessary API calls in the UI
- Reusing recently fetched data
- Caching lightweight frontend responses

---

## Instructions

### 1. Choose the Right Storage

- Use `localStorage` for data that can persist across browser sessions
- Use `sessionStorage` for data that should reset when the tab or session ends
- Keep cached data limited to safe, non-sensitive frontend values

Typical choices:

- `localStorage` for reusable reference data or user preferences
- `sessionStorage` for short-lived page data

---

### 2. Check Cache Before Calling the API

- Read cached data before making a network request
- Return cached data immediately when it is still valid
- Call the API only when cache is missing, expired, or invalid

Example:

```javascript
const getCachedUsers = () => {
  const cached = localStorage.getItem("users");

  if (cached) {
    return JSON.parse(cached);
  }

  return null;
};
```

---

### 3. Save API Results to Cache

- Store successful API responses after fetching
- Save both the data and enough metadata to decide whether it is still fresh
- Use clear cache keys for each resource

Example:

```javascript
const saveUsersToCache = (users) => {
  localStorage.setItem(
    "users",
    JSON.stringify({
      data: users,
      cachedAt: Date.now(),
    })
  );
};
```

---

### 4. Add Basic Expiry Logic

- Treat cache as valid only for a limited time
- Compare current time with the cached timestamp
- Refresh stale data automatically

Example:

```javascript
const getFreshUsers = async () => {
  const cached = JSON.parse(localStorage.getItem("users") || "null");
  const maxAge = 5 * 60 * 1000;

  if (cached && Date.now() - cached.cachedAt < maxAge) {
    return cached.data;
  }

  const res = await fetch("/api/users");

  if (!res.ok) {
    throw new Error("Failed to fetch users");
  }

  const data = await res.json();

  saveUsersToCache(data);
  return data;
};
```

---

### 5. Use Resource-Specific Cache Keys

- Build unique cache keys for different resources, filters, or users
- Avoid reusing the same key for different API responses
- Include identifiers such as page, search term, or user id when needed

Example:

```javascript
const getUserCacheKey = (userId) => `user:${userId}`;
const getSearchCacheKey = (query) => `search:${query}`;
```

---

### 6. Invalidate Cache When Data Changes

- Clear or replace cached data after create, update, or delete actions
- Avoid showing stale values after mutations
- Invalidate only the affected keys when possible

Example:

```javascript
const clearUsersCache = () => {
  localStorage.removeItem("users");
};
```

---

### 7. Handle Fallback and Error Cases

- If cache parsing fails, ignore the cache and refetch
- If the API fails, optionally continue showing recent cached data
- Keep the UI clear about whether content may be stale

---

### 8. Safety Notes

- Do not cache secrets, tokens, or highly sensitive user data in plain browser storage
- Keep cached payloads reasonably small
- Use short expiry times for frequently changing data
- Prefer in-memory caching for highly temporary values when persistence is unnecessary

## Standard Flow

```javascript
check cache
-> return cached data if still fresh
-> otherwise call API
-> store response with timestamp
-> invalidate cache when data changes
```
