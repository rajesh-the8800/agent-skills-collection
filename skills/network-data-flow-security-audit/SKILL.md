---
name: network-data-flow-security-audit
description: Analyzes data movement across frontend, backend, and network layers to detect insecure transport, CORS issues, sensitive data exposure, interception risks, and logging leaks
metadata:
  version: 1.0.0
---

## Provides

- HTTPS and TLS review points
- CORS misconfiguration checks
- Sensitive data exposure review for URLs and headers
- Request, response, and transport-layer leak checks

## Use When

- Checking end-to-end data security across application and network layers
- Reviewing how frontend and backend exchange sensitive data
- Auditing transport and browser security behavior
- Investigating where data may leak in transit or logs

---

## Instructions

### 1. Trace Data Flow End to End

- Map how data moves from the browser to APIs, services, storage, logs, and third parties
- Identify where sensitive values appear, including tokens, identifiers, personal data, and internal metadata
- Review both successful and failed request paths

---

### 2. Check HTTPS and TLS Usage

- Ensure all sensitive traffic uses HTTPS in real deployments
- Flag mixed-content behavior, insecure redirects, or fallback to plain HTTP
- Review whether security-sensitive endpoints, assets, and API calls are consistently protected in transit

Review targets:

- Login and signup flows
- Payment or account endpoints
- File upload and download flows
- Internal admin tools

---

### 3. Review CORS Configuration

- Check allowed origins, methods, headers, and credential settings
- Flag wildcard or overly broad origin rules on sensitive APIs
- Ensure credentialed requests are restricted to trusted origins
- Review whether preflight handling exposes unnecessary access

Common risks:

- `Access-Control-Allow-Origin: *` on sensitive endpoints
- Overbroad allowed headers or methods
- Cookies or auth headers exposed to unintended origins

---

### 4. Check Sensitive Data in URLs and Headers

- Review whether secrets, tokens, emails, or internal identifiers appear in query strings, fragments, or logs
- Avoid putting sensitive values in URLs because they can leak through browser history, referrers, proxies, and logs
- Check headers for unintended exposure of internal tokens or debugging values

Review targets:

- Password reset links
- OAuth callbacks
- Search and filter URLs
- Custom auth headers

---

### 5. Review Request and Response Exposure

- Inspect request payloads and responses for unnecessary sensitive fields
- Return only the data needed by the caller
- Ensure errors and debug responses do not expose stack traces, internal hosts, or secret values
- Check whether caching layers or proxies might store sensitive responses

---

### 6. Consider Interception Risks

- Review whether tokens or session identifiers can be stolen through insecure storage, weak transport, or exposed logs
- Check whether APIs rely on transport assumptions that fail behind proxies or misconfigured environments
- Confirm sensitive requests are not downgraded, replayed, or exposed through insecure client behavior

---

### 7. Review Logging and Monitoring Leaks

- Check frontend, backend, proxy, and observability logs for sensitive request or response data
- Avoid logging secrets, tokens, cookies, full payloads, or personal data unless absolutely required and protected
- Review analytics and monitoring tools for accidental data capture

Review targets:

- Browser console logs
- Server application logs
- Reverse proxy or CDN logs
- Error tracking payloads

---

### 8. Review Third-Party Handoffs

- Identify external APIs, SDKs, analytics tools, and embedded services that receive application data
- Confirm only necessary fields are shared with each third party
- Check whether outbound requests leak internal identifiers or sensitive metadata

---

### 9. Report Findings by Severity

- Mark issues as critical, high, medium, or low based on exploitability and data impact
- Include where the data leaks or travels insecurely, why it matters, and the safer alternative
- Prioritize insecure transport, overbroad CORS, and sensitive data leakage first

Standard review flow:

1. Trace data movement across layers
2. Verify secure transport and redirects
3. Review CORS and origin trust boundaries
4. Inspect URLs, headers, requests, responses, and logs
5. Summarize leaks, risks, and fixes

---

### 10. Safety Notes

- Secure transport alone is not enough if sensitive data is overexposed in logs or browser-visible locations
- Client-side protections do not replace backend authorization and server-side validation
- Logging, proxy, and analytics systems are part of the security surface
- End-to-end reviews should include normal, failure, and edge-case flows

## Standard Flow

```javascript
trace data flow
-> verify HTTPS and TLS behavior
-> inspect CORS and origin access
-> review URLs, headers, requests, responses, and logs
-> identify leaks and insecure transmission paths
-> report risks and fixes
```
