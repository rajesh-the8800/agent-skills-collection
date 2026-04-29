---
name: database-query-analyzer
description: Detects inefficient database queries, missing indexes, and performance bottlenecks when optimizing application and database performance
metadata:
  version: 1.0.0
---

# Database Query Analyzer

## Provides

- Inefficient query detection
- Missing or weak index review
- Query pattern and data-access bottleneck analysis
- Database performance optimization guidance

## Use When

- Optimizing database performance
- Investigating slow endpoints or reports
- Reviewing ORM or raw SQL query behavior
- Looking for performance bottlenecks in data access paths

---

## Instructions

### 1. Start with the Slow Path

- Identify the endpoint, job, report, or service affected by database slowness
- Trace the code path to the exact query or ORM call before reviewing unrelated database code
- Focus first on the highest-cost or highest-frequency queries

---

### 2. Review Query Shape

- Check whether queries fetch only the needed rows and columns
- Look for unnecessary joins, broad selects, repeated filters, and unbounded scans
- Flag patterns that load excessive data before filtering in application code

Examples:

- `SELECT *` when only a few columns are needed
- filtering large datasets in memory after broad queries
- repeated per-row lookup queries

---

### 3. Check for Missing or Weak Indexing

- Review filter, join, sort, and lookup fields for indexing needs
- Check whether composite indexes match actual query patterns
- Flag indexes that are missing on high-traffic lookup paths
- Note when indexes may exist but not match the query order or predicates well

---

### 4. Look for N+1 and Repeated Query Patterns

- Check whether related records are fetched one row at a time instead of in batches
- Review ORM lazy-loading behavior, resolver patterns, and nested loops
- Look for duplicate queries across the same request or job execution

---

### 5. Review Pagination and Large Result Sets

- Check whether list endpoints use bounded pagination
- Flag full-table reads, large offsets, or unbounded exports on hot paths
- Review whether cursor-based approaches would be safer for large or frequently changing datasets

---

### 6. Review Transactions and Write Patterns

- Look for long-running transactions, repeated writes, and unnecessary round trips
- Check whether writes are grouped efficiently when safe
- Review lock-heavy operations, retry patterns, and contention risks when visible

---

### 7. Review ORM and Query Builder Usage

- Check whether the ORM generates inefficient SQL for relationships, counts, or nested loads
- Look for hidden query multiplication, repeated eager loading, or unnecessary hydration of full model objects
- Confirm raw SQL or query builder usage matches the intended access pattern

---

### 8. Use Performance Evidence When Available

- Prefer query plans, logs, timings, slow-query reports, and metrics when available
- Separate proven bottlenecks from likely inefficiencies seen in code
- If no runtime evidence is available, state that the finding is a likely optimization target rather than a confirmed bottleneck

---

### 9. Report Findings Clearly

- Group issues by severity, cost, or impact
- Include:
  - issue
  - query or code path
  - explanation
  - suggested improvement
- Separate confirmed bottlenecks from likely risks

Standard workflow:

1. Identify the slow path
2. Trace the responsible query or ORM call
3. Review query shape, indexes, and repeated access patterns
4. Check pagination, transactions, and ORM behavior
5. Summarize bottlenecks and improvements

---

### 10. Safety Notes

- Do not recommend indexes blindly without considering write cost and actual query shape
- Query performance depends on data distribution, scale, and execution plans, not just code appearance
- A suspicious query is not automatically a real bottleneck without evidence
- Prefer targeted changes over broad database tuning advice when the issue is localized

## Output Format

### Overview

- Short summary of database performance health

### Confirmed Bottlenecks

- Issue
- Query or path
- Evidence
- Suggested fix

### Likely Risks

- Query or pattern that may become a bottleneck

### Index Recommendations

- Missing or improved indexes to consider

### Recommendations

- High-impact changes to improve performance
