---
name: api-design-validator
description: Reviews API structure for REST best practices, naming consistency, resource design, and proper HTTP status code usage when designing or reviewing APIs
metadata:
  version: 1.0.0
---

# API Design Validator

## Provides

- REST design review guidance
- Endpoint naming consistency checks
- HTTP method and status code validation
- Resource structure and response-shape review

## Use When

- Designing a new API
- Reviewing an existing API
- Checking REST conventions and consistency
- Validating endpoint behavior before implementation or release

---

## Instructions

### 1. Review Resource Modeling

- Check whether endpoints are organized around resources rather than actions
- Prefer clear, stable nouns in paths
- Identify whether related resources use consistent nesting and naming

Examples:

- Prefer `/users` over `/getUsers`
- Prefer `/orders/{id}` over `/orderDetailsById`

---

### 2. Validate Naming Consistency

- Check path naming, parameter naming, and payload field naming for consistency
- Prefer one casing style and one pluralization approach across the API
- Review whether similar resources follow similar conventions

Examples:

- consistent use of `userId` versus `user_id`
- consistent use of `/users` and `/users/{id}`

---

### 3. Validate HTTP Method Usage

- Check whether methods match intended behavior
- Use `GET` for reads, `POST` for creation, `PUT` or `PATCH` for updates, and `DELETE` for removal
- Flag designs that overload one method for unrelated actions

Review targets:

- safe versus mutating operations
- idempotent versus non-idempotent behavior
- bulk operations and action-style endpoints

---

### 4. Validate Status Codes

- Check whether responses use appropriate HTTP status codes
- Prefer `200`, `201`, `204`, `400`, `401`, `403`, `404`, `409`, `422`, and `500` according to actual behavior
- Flag endpoints that always return `200` even when the result is an error

Examples:

- `201 Created` after successful resource creation
- `204 No Content` for successful delete without response body
- `404 Not Found` when a requested resource does not exist

---

### 5. Review Request and Response Shapes

- Check whether request bodies and response payloads are consistent and predictable
- Prefer stable envelope patterns only when the API uses them consistently
- Ensure error responses follow a clear and reusable format

Review targets:

- pagination shape
- filter and sort parameters
- validation error format
- success versus error payload consistency

---

### 6. Review Query and Filtering Design

- Check whether filtering, sorting, searching, and pagination use predictable query parameters
- Avoid mixing unrelated behaviors into inconsistent parameter schemes
- Confirm that collection endpoints and detail endpoints have clearly different responsibilities

---

### 7. Check Versioning and Evolution

- Review whether the API has a clear versioning approach when needed
- Check whether breaking changes are isolated and documented consistently
- Identify endpoints that may be difficult to evolve because of ambiguous contracts

---

### 8. Flag Common API Design Issues

- Verb-based paths instead of resource-based paths
- Inconsistent naming between similar endpoints
- Incorrect or overly generic status codes
- Inconsistent pagination or filtering patterns
- Response shapes that vary without clear reason
- Leaky internal implementation details in public contracts

---

### 9. Report Findings Clearly

- Group findings by severity or impact
- Include:
  - issue
  - endpoint
  - explanation
  - suggested improvement
- Separate confirmed inconsistencies from design preferences

Standard workflow:

1. Review resources and path structure
2. Validate naming consistency
3. Check HTTP methods and status codes
4. Review request and response contracts
5. Summarize design issues and improvements

---

### 10. Safety Notes

- Prefer consistency within the API over blindly following one convention in isolation
- Do not label a design choice as wrong unless it creates confusion, misuse, or inconsistency
- Status code validation should reflect actual endpoint behavior, not just naming intent
- Public API design should avoid exposing internal storage or service implementation details

## Output Format

### Overview

- Short summary of API design quality

### Strong Areas

- Conventions that are applied well

### Issues

- Issue
- Endpoint
- Explanation
- Suggested improvement

### Consistency Risks

- Naming, status code, or contract mismatches to standardize

### Recommendations

- High-value improvements to make the API easier to use and maintain
