ID: BUG-001
Title: Retrieve employee by non-existing ID returns server error instead of 404
Component: Employees API
Environment: Prod
Severity: High
Priority: High

Preconditions:
API is available and reachable.

Steps to Reproduce:

Send a GET request to /api/Employees/{id} using a valid UUID that does not exist in the system.

Expected Result:
The API should return HTTP 404 Not Found with a descriptive error message indicating that the employee does not exist.

Actual Result:
The API returns a server error (5xx).

Impact:
API consumers cannot distinguish between a system failure and a missing resource, which leads to incorrect error handling and unreliable automation results.

Notes:
This behavior violates RESTful principles for resource retrieval.