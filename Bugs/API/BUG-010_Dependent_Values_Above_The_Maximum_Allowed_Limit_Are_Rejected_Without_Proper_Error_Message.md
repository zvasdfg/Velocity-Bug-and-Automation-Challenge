ID: BUG-010
Title: Dependent values above the maximum allowed limit are rejected without proper error message
Component: Employees API
Environment: Prod
Severity: Medium
Priority: Medium

Preconditions:
API is available and reachable.

Steps to Reproduce:

Send a POST or PUT request with dependants = 33.

Expected Result:
The API should return HTTP 400 with a clear message indicating the maximum allowed value is 32.

Actual Result:
The request is rejected silently or with a non-descriptive error.

Impact:
Poor developer experience and unclear validation rules.

Notes:
Maximum constraint exists in schema but is not properly surfaced to consumers.