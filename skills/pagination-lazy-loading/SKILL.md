---
name: pagination-lazy-loading
description: Loads large UI datasets efficiently using pagination logic, infinite scroll patterns, and lazy loading data strategies
metadata:
  version: 1.0.0
---

## Provides

- Pagination state and navigation logic
- Infinite scroll loading patterns
- Lazy loading data in batches
- Loading and end-of-list state handling

## Use When

- Handling large datasets in UI
- Rendering long lists, tables, or feeds
- Loading content in smaller chunks
- Improving perceived performance for data-heavy pages

---

## Instructions

### 1. Track List State

- Store the current dataset in state
- Track pagination metadata separately
- Keep at least:
  - `items`
  - `page`
  - `pageSize`
  - `hasMore`
  - `isLoading`
  - `error`

Example:

```javascript
const [items, setItems] = useState([]);
const [page, setPage] = useState(1);
const [pageSize] = useState(20);
const [hasMore, setHasMore] = useState(true);
const [isLoading, setIsLoading] = useState(false);
const [error, setError] = useState(null);
```

---

### 2. Fetch Data in Pages

- Request only a limited number of records at a time
- Pass page number, cursor, or limit values to the API
- Append results for progressive loading flows
- Replace results only when filters or sort order change

Example:

```javascript
const fetchPage = async (nextPage) => {
  setIsLoading(true);
  setError(null);

  try {
    const res = await fetch(`/api/items?page=${nextPage}&limit=${pageSize}`);

    if (!res.ok) {
      throw new Error("Failed to load items");
    }

    const data = await res.json();

    setItems((prev) => [...prev, ...data.items]);
    setPage(nextPage);
    setHasMore(data.items.length === pageSize);
  } catch (err) {
    setError(err.message);
  } finally {
    setIsLoading(false);
  }
};
```

---

### 3. Implement Standard Pagination

- Show controls for next, previous, or specific pages
- Disable navigation while loading
- Reset to page 1 when search, filters, or sorting change

Standard flow:

1. Load first page on screen mount
2. Render current page data
3. User clicks next or previous
4. Fetch the requested page
5. Update controls and visible items

Example:

```javascript
const goToNextPage = () => {
  if (!hasMore || isLoading) return;
  fetchPage(page + 1);
};
```

---

### 4. Implement Infinite Scroll

- Load additional data when the user nears the bottom of the list
- Avoid repeated requests while one is already in progress
- Stop loading when `hasMore` becomes false

Example:

```javascript
useEffect(() => {
  const onScroll = () => {
    const nearBottom =
      window.innerHeight + window.scrollY >= document.body.offsetHeight - 200;

    if (nearBottom && hasMore && !isLoading) {
      fetchPage(page + 1);
    }
  };

  window.addEventListener("scroll", onScroll);
  return () => window.removeEventListener("scroll", onScroll);
}, [page, hasMore, isLoading]);
```

---

### 5. Apply Lazy Loading

- Delay loading data until the UI section becomes visible or needed
- Use this for tabs, expandable panels, secondary lists, or heavy content blocks
- Load the smallest useful batch first

Example:

```javascript
useEffect(() => {
  if (!isSectionOpen || items.length > 0) return;
  fetchPage(1);
}, [isSectionOpen]);
```

---

### 6. Handle Reset Conditions

- Clear existing items when query parameters change
- Reset page and `hasMore` state before fetching again
- Prevent mixing old results with new search results

Example:

```javascript
const resetAndReload = async () => {
  setItems([]);
  setPage(1);
  setHasMore(true);
  await fetchPage(1);
};
```

---

### 7. Handle UX States

- Show loaders during initial and follow-up fetches
- Show empty state when no data is returned
- Show error state with retry option
- Show end-of-list feedback when all data has loaded

---

### 8. Safety Notes

- Prefer cursor-based pagination if the backend supports it for frequently changing datasets
- Debounce filter or search changes before reloading data
- Avoid triggering duplicate page loads from repeated scroll events
- Preserve scroll position when appropriate for a better user experience

## Standard Flow

```javascript
load first batch
-> render visible items
-> fetch more on next page or scroll trigger
-> append new items
-> stop when no more data remains
```
