BUG-008

ID: BUG-008
Title: API error responses are inconsistent and lack a standard structure
Component: Employees API
Environment: Prod
Severity: Medium
Priority: Medium

Preconditions:
API is available and reachable.

Steps to Reproduce:

Trigger different types of errors (validation, not found, server error).

Expected Result:
All error responses should follow a consistent schema including error code, message, and details.

Actual Result:
Error responses vary and often lack descriptive information.

Impact:
Automation frameworks and frontend applications cannot handle errors reliably.

Notes:
No error schema is defined in the OpenAPI specification.