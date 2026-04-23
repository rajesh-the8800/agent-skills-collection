---
name: state-management-basics
description: Manages UI state effectively including local and global state handling
metadata:
  version: 1.0.0
---

## Provides

- Local vs global state handling
- Simple and reusable state patterns
- Clear data flow structure
- Predictable UI updates

## Use When

- Handling dynamic UI updates
- Managing user interactions (clicks, inputs, toggles)
- Sharing data between components
- Avoiding inconsistent UI state

---

## Instructions

### 1. Identify State Type

- Use **local state** for component-specific data  
  (e.g., input fields, toggles, modals)

- Use **global state** for shared data  
  (e.g., user info, theme, auth state)

---

### 2. Initialize State

- Define state using hooks or state containers  
- Keep initial state minimal and predictable  

Example:

```javascript
const [count, setCount] = useState(0);