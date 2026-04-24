---
name: environment-configuration
description: Manages environment-based application settings including API URLs, dev and prod config separation, and secure variable usage
metadata:
  version: 1.0.0
---

## Provides

- Environment-based configuration structure
- API URL management per environment
- Separation of development and production settings
- Safe handling of exposed variables

## Use When

- Working across multiple environments
- Switching between local, staging, and production setups
- Managing different API endpoints per environment
- Organizing configuration for frontend apps

---

## Instructions

### 1. Centralize Configuration

- Keep environment-dependent values in one config layer
- Avoid scattering URLs and keys across components
- Group values such as:
  - API base URL
  - app mode
  - feature flags
  - analytics or service identifiers

Example:

```javascript
export const config = {
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL,
  appEnv: import.meta.env.VITE_APP_ENV,
};
```

---

### 2. Separate Environment Values

- Define different values for development, staging, and production
- Keep runtime behavior consistent while swapping config values
- Use environment files or build-time variables supported by the framework

Typical setup:

```javascript
.env.development
.env.staging
.env.production
```

---

### 3. Configure API URLs

- Store API base URLs in environment variables
- Build request paths from one shared base URL
- Avoid hardcoding full URLs inside UI components

Example:

```javascript
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

const fetchUsers = async () => {
  const res = await fetch(`${API_BASE_URL}/users`);

  if (!res.ok) {
    throw new Error("Failed to fetch users");
  }

  return res.json();
};
```

---

### 4. Expose Only Safe Variables

- Treat frontend environment variables as visible to the client
- Only expose values that are safe for browser delivery
- Never place secrets such as private API keys, database credentials, or signing secrets in frontend env files

Safe examples:

- Public API base URL
- Public app environment name
- Public feature toggles

Unsafe examples:

- Database passwords
- Private service tokens
- Server-side secret keys

---

### 5. Create a Reusable Config Module

- Export a single config object or helper functions
- Read environment variables once and reuse them everywhere
- Validate required values early if the app depends on them

Example:

```javascript
const required = (value, name) => {
  if (!value) {
    throw new Error(`Missing environment variable: ${name}`);
  }

  return value;
};

export const config = {
  apiBaseUrl: required(import.meta.env.VITE_API_BASE_URL, "VITE_API_BASE_URL"),
  appEnv: import.meta.env.VITE_APP_ENV || "development",
};
```

---

### 6. Keep Behavior Environment-Aware

- Enable debugging tools only in development when needed
- Use production-safe defaults for logging and integrations
- Keep environment checks centralized instead of repeating inline conditions

Example:

```javascript
export const isProd = config.appEnv === "production";
export const isDev = config.appEnv === "development";
```

---

### 7. Handle Missing or Invalid Config

- Fail early when required config is missing
- Show clear errors during development
- Avoid silent fallback behavior for critical settings like API endpoints

Standard flow:

1. Read environment values on app startup
2. Validate required settings
3. Build shared config object
4. Use config throughout the app
5. Swap values per environment without changing component code

---

### 8. Safety Notes

- Never commit real secrets to the repository
- Keep secret values on the backend or deployment platform
- Document required variables in project setup if needed
- Match naming conventions to the frontend framework being used, such as `VITE_` or `NEXT_PUBLIC_`

## Standard Flow

```javascript
read environment variables
-> validate required values
-> create shared config object
-> use config in API and app setup
-> switch values by environment
```
