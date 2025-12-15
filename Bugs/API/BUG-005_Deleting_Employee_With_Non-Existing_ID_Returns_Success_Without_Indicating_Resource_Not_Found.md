ID: BUG-005
Title: Deleting employee with non-existing ID returns success without indicating resource not found
Component: Employees API
Environment: Prod
Severity: Medium
Priority: Medium

Preconditions:
API is available and reachable.

Steps to Reproduce:

Send a DELETE request to /api/Employees/{id} using a valid UUID that does not exist.

Expected Result:
The API should return HTTP 404 Not Found indicating the employee does not exist.

Actual Result:
The API returns a success response, but no record is deleted.

Impact:
Consumers cannot reliably determine whether a delete operation actually removed a resource.

Notes:
Violates RESTful semantics for DELETE operations.