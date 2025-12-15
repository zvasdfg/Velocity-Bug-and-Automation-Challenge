ID: BUG-004
Title: Updating employee without ID is not allowed but API does not return descriptive error
Component: Employees API
Environment: Prod
Severity: Medium
Priority: Medium

Preconditions:
API is available and reachable.

Steps to Reproduce:

Send a PUT request to /api/Employees without including the id field in the request body.

Expected Result:
The API should return HTTP 400 Bad Request with a descriptive error message indicating that the employee ID is required.

Actual Result:
The request is rejected but the response does not include a meaningful error description.

Impact:
Developers and testers cannot easily determine why the request failed, increasing debugging time.

Notes:
Error contract is missing or incomplete.