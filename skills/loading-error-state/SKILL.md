---
name: loading-error-state
description: Handles API loading, error, and empty states in UI
metadata:
  version: 1.0.0
---

## Provides

- Loading indicators (spinner, skeleton)
- Error messages with retry functionality
- Empty state handling for no data scenarios

## Use When

- API calls take noticeable time
- API requests fail or return errors
- API returns empty or null data
- Building user-facing frontend interfaces

---

## Instructions

When implementing API-driven UI:

### 1. Initialize State

- `loading = true`
- `error = null`
- `data = null`

---

### 2. Execute API Call

- On success:
  - Store response in `data`
  - Set `loading = false`

- On failure:
  - Store error message in `error`
  - Set `loading = false`

---

### 3. Render UI Based on Priority

Always follow this order:

1. If `loading === true`  
   → Show loading indicator (spinner or skeleton)

2. Else if `error !== null`  
   → Show error message  
   → Provide retry option  

3. Else if `data is null OR empty`  
   → Show empty state message  

4. Else  
   → Render actual data UI  

---

## Standard Flow

```javascript
if (loading) return <Loader />;
if (error) return <ErrorState message={error} onRetry={refetch} />;
if (!data || data.length === 0) return <EmptyState />;

return <DataView data={data} />;