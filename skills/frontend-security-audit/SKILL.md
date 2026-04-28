---
name: frontend-security-audit
description: Analyzes frontend code for client-side security weaknesses including XSS prevention, secure storage choices, safe DOM handling, and secure API consumption
metadata:
  version: 1.0.0
---

## Provides

- XSS prevention checks
- Secure storage usage guidance
- Safe DOM handling review points
- Secure API consumption checks

## Use When

- Building frontend applications that handle user data
- Reviewing frontend code for security weaknesses
- Validating client-side handling of user input
- Checking browser-side API and storage patterns

---

## Instructions

### 1. Identify User-Controlled Inputs

- Trace any value that can come from users, URLs, query params, local storage, or external APIs
- Treat all dynamic content as untrusted until it is validated or safely rendered
- Focus first on values that reach the DOM, navigation, or network requests

---

### 2. Check for XSS Risks

- Prefer framework-safe rendering patterns such as normal JSX text rendering
- Flag direct HTML injection patterns such as `dangerouslySetInnerHTML`, `innerHTML`, or unsafe template insertion
- Require sanitization before rendering rich HTML from untrusted sources

Review targets:

- Search results
- Comments or user profiles
- CMS content
- Query-string-driven UI

---

### 3. Review DOM Handling

- Use safe DOM APIs and framework bindings instead of manual string-based DOM updates
- Avoid inserting untrusted values into HTML, script URLs, inline event handlers, or style attributes
- Prefer `textContent` or framework-managed rendering when displaying plain text

Unsafe example:

```javascript
element.innerHTML = userBio;
```

Safer example:

```javascript
element.textContent = userBio;
```

---

### 4. Review Storage Usage

- Check whether sensitive data is stored in `localStorage`, `sessionStorage`, or other browser-accessible storage
- Avoid storing secrets, long-lived tokens, or highly sensitive user data in plain frontend storage
- Prefer safer backend-driven session approaches when the application requires stronger protection

Review targets:

- Access tokens
- Refresh tokens
- Personal profile data
- Payment or account details

---

### 5. Review Secure API Consumption

- Ensure API requests use HTTPS endpoints in real deployments
- Verify auth headers, tokens, and user identifiers are handled carefully in the client
- Avoid exposing private API keys or secret credentials in frontend code or env files
- Check error handling so sensitive server responses are not leaked into the UI or logs

Example checks:

- No hardcoded secrets in source files
- No private server endpoints exposed as public client config
- No trust in client-side authorization alone

---

### 6. Validate Navigation and URL Handling

- Review redirects and navigation targets derived from query params or external input
- Avoid open redirect patterns and unsafe URL construction
- Validate or restrict allowed destinations when redirecting after login or logout

---

### 7. Check Third-Party and Browser Integrations

- Review third-party scripts, embeds, and analytics usage for unnecessary exposure of user data
- Limit access to browser features and storage when not required
- Confirm external libraries do not receive sensitive data unless needed

---

### 8. Report Findings by Severity

- Mark issues as critical, high, medium, or low based on exploitability and data exposure
- Include the risky pattern, why it is dangerous, and the safer alternative
- Prioritize fixes that reduce XSS risk, secret exposure, and insecure token handling first

Standard review flow:

1. Trace untrusted inputs
2. Check rendering and DOM usage
3. Review storage and token handling
4. Inspect API usage and config exposure
5. Summarize findings with recommended fixes

---

### 9. Safety Notes

- Client-side checks improve safety but do not replace backend authorization and validation
- Sanitization is required when rendering any untrusted HTML
- Frontend code should assume browser storage and source code are visible to attackers
- Security reviews should include both code paths and configuration choices

## Standard Flow

```javascript
trace untrusted input
-> inspect rendering and DOM updates
-> review storage and token usage
-> inspect API calls and config exposure
-> report risks and safer alternatives
```
