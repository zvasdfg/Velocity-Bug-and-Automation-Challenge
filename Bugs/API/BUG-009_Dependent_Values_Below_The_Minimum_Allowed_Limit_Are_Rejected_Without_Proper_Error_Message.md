ID: BUG-009
Title: Dependent values below the minimum allowed limit are rejected without proper error message
Component: Employees API
Environment: Prod
Severity: Medium
Priority: Medium

Preconditions:
API is available and reachable.

Steps to Reproduce:

Send a POST or PUT request with dependants = -1.

Expected Result:
The API should return HTTP 400 with a clear validation message indicating the minimum allowed value is 0.

Actual Result:
The request is rejected but no descriptive validation error is returned.

Impact:
Users do not understand why the request failed.

Notes:
Input validation feedback is missing.