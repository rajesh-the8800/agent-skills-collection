---
name: api-security-review
description: Checks REST and GraphQL APIs for security misconfigurations including authentication flaws, authorization gaps, rate limiting issues, insecure endpoints, and data exposure risks
metadata:
  version: 1.0.0
---

## Provides

- Authentication and authorization review points
- Rate limiting and abuse protection checks
- Response data exposure checks
- Insecure endpoint review guidance

## Use When

- Building REST or GraphQL APIs
- Auditing backend APIs for security weaknesses
- Reviewing API authentication and access control
- Checking whether responses expose unnecessary data

---

## Instructions

### 1. Identify Sensitive Endpoints

- List endpoints that handle authentication, user data, admin actions, payments, uploads, or internal operations
- Mark which endpoints are public, authenticated, privileged, or internal-only
- Review both REST routes and GraphQL queries or mutations

---

### 2. Check Authentication Controls

- Verify protected endpoints require valid authentication
- Review token, session, API key, or signed request handling
- Check whether expired, invalid, or missing credentials are rejected consistently
- Confirm login and token refresh flows do not expose excessive information

Review targets:

- Login endpoints
- Session creation and refresh
- API key validation
- GraphQL mutations with user impact

---

### 3. Check Authorization Logic

- Confirm users can access only their own data unless broader access is explicitly allowed
- Review object-level and role-based authorization, not just route-level checks
- Test whether changing IDs, tenant values, or query inputs exposes another user's data
- Ensure admin actions cannot be triggered by normal users

Common risks:

- IDOR or BOLA issues
- Missing role checks
- Tenant isolation failures
- Client-controlled privilege flags

---

### 4. Review Rate Limiting and Abuse Protection

- Check whether login, signup, password reset, search, and expensive endpoints are rate limited
- Review protections against brute force, scraping, and denial-of-service patterns
- Confirm limits apply per user, token, IP, or other appropriate scope

Example targets:

- Authentication endpoints
- OTP or verification flows
- GraphQL introspection or deep query execution
- Bulk export endpoints

---

### 5. Check Response Data Exposure

- Inspect API responses for unnecessary fields, internal identifiers, secrets, or debugging data
- Return the minimum data needed by the client
- Ensure errors do not leak stack traces, SQL details, internal paths, or security-sensitive metadata

Review targets:

- User profile responses
- Admin endpoints
- Validation error responses
- GraphQL schema fields and nested resolvers

---

### 6. Review Endpoint Security

- Verify sensitive endpoints use HTTPS in deployment
- Check CORS configuration for unnecessary origins, methods, headers, or credential exposure
- Confirm unsafe methods such as `PUT`, `PATCH`, or `DELETE` are protected properly
- Review whether deprecated, test, or internal endpoints remain exposed

---

### 7. Review Input Handling

- Validate and constrain all request inputs including headers, params, body fields, and GraphQL variables
- Reject malformed, oversized, or unexpected input early
- Check whether filtering, sorting, and query-building logic could enable injection or excessive data access

---

### 8. Review GraphQL-Specific Risks

- Restrict introspection in production if appropriate for the system
- Check resolver-level authorization, not just schema visibility
- Review query depth, complexity, and nested expansion controls
- Ensure mutations and sensitive queries follow the same auth rules as REST endpoints

---

### 9. Report Findings by Severity

- Mark issues as critical, high, medium, or low based on exploitability and impact
- Include the affected endpoint, risky behavior, likely impact, and safer fix
- Prioritize broken auth, broken access control, and sensitive data exposure first

Standard review flow:

1. Inventory endpoints and trust levels
2. Check authentication requirements
3. Verify authorization on objects and roles
4. Review rate limiting and abuse controls
5. Inspect responses, errors, and exposed endpoints

---

### 10. Safety Notes

- API security depends on both code and deployment configuration
- Passing client-side checks does not prove backend authorization is correct
- Security reviews should include normal, invalid, and malicious request paths
- Production-safe defaults matter for CORS, errors, introspection, and logging

## Standard Flow

```javascript
inventory endpoints
-> verify authentication
-> verify authorization
-> inspect rate limiting and abuse controls
-> review responses and endpoint exposure
-> report risks and fixes
```
