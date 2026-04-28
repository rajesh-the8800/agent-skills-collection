---
name: api-integration-frontend
description: Handles API calls, data mapping, and UI binding in frontend applications
metadata:
  version: 1.0.0
---

## Provides

- API integration using fetch or axios
- Data mapping and transformation
- Binding API data to UI components
- Loading and error state handling

## Use When

- Connecting frontend with backend APIs
- Fetching and displaying dynamic data
- Handling async operations in UI
- Building dashboards, lists, or detail pages

---

## Instructions

### 1. Define API Function

- Create a reusable function for API calls
- Handle request and response parsing

Example:

```javascript
const fetchUsers = async () => {
  const res = await fetch("/api/users");

  if (!res.ok) {
    throw new Error("API request failed");
  }

  return res.json();
};