---
name: basic-authentication-handling-frontend
description: Manages frontend login sessions and authentication flow including token storage, protected routes, session restoration, and logout handling
metadata:
  version: 1.0.0
---

## Provides

- Login session handling in the frontend
- Token storage and retrieval
- Protected route checks
- Session restore on app load
- Logout and auth cleanup flow

## Use When

- Implementing user authentication in a frontend app
- Building login and logout flows
- Protecting pages for signed-in users only
- Persisting auth state across refreshes

---

## Instructions

### 1. Store Auth State

- Keep auth state in a shared place such as context, global store, or top-level state
- Track at least:
  - `user`
  - `token`
  - `isAuthenticated`
  - `isLoading`

Example:

```javascript
const [auth, setAuth] = useState({
  user: null,
  token: null,
  isAuthenticated: false,
  isLoading: true,
});
```

---

### 2. Handle Login

- Submit credentials to the backend login endpoint
- On success, store the returned token
- Update auth state with user details
- Mark the session as authenticated

Standard flow:

1. User submits login form
2. Frontend calls login API
3. Save token in storage
4. Update auth state
5. Redirect to protected area

Example:

```javascript
const login = async (credentials) => {
  const res = await fetch("/api/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(credentials),
  });

  if (!res.ok) {
    throw new Error("Login failed");
  }

  const data = await res.json();

  localStorage.setItem("token", data.token);

  setAuth({
    user: data.user,
    token: data.token,
    isAuthenticated: true,
    isLoading: false,
  });
};
```

---

### 3. Restore Session on App Load

- Read stored token when the app starts
- If a token exists, restore auth state or validate it with the backend
- Finish initialization before rendering protected content

Example:

```javascript
useEffect(() => {
  const token = localStorage.getItem("token");

  if (!token) {
    setAuth((prev) => ({ ...prev, isLoading: false }));
    return;
  }

  setAuth({
    user: null,
    token,
    isAuthenticated: true,
    isLoading: false,
  });
}, []);
```

---

### 4. Protect Routes

- Block access to private routes when the user is not authenticated
- Redirect unauthenticated users to the login page
- Wait for auth initialization before deciding access

Example:

```javascript
const ProtectedRoute = ({ children }) => {
  if (auth.isLoading) return <div>Loading...</div>;

  if (!auth.isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return children;
};
```

---

### 5. Attach Token to API Requests

- Include the token in authenticated API requests
- Send it in the `Authorization` header when required by the backend

Example:

```javascript
const fetchProfile = async () => {
  const token = localStorage.getItem("token");

  const res = await fetch("/api/profile", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!res.ok) {
    throw new Error("Unauthorized request");
  }

  return res.json();
};
```

---

### 6. Handle Logout

- Remove stored token
- Clear user and auth state
- Redirect to login or public page

Example:

```javascript
const logout = () => {
  localStorage.removeItem("token");

  setAuth({
    user: null,
    token: null,
    isAuthenticated: false,
    isLoading: false,
  });
};
```

---

### 7. Safety Notes

- Prefer secure, short-lived tokens from the backend
- If the app uses cookies instead of local storage, follow the backend session strategy
- Handle expired tokens by clearing auth state and redirecting to login
- Avoid rendering protected content before auth loading completes

## Standard Flow

```javascript
app starts
-> restore token
-> mark user authenticated if valid
-> guard private routes
-> send token with protected API calls
-> clear session on logout
```
