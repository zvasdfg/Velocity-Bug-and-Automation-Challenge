ID: BUG-006
Title: API allows negative salary values without validation error
Component: Employees API
Environment: Prod
Severity: High
Priority: High

Preconditions:
API is available and reachable.

Steps to Reproduce:

Send a POST or PUT request including a negative value in the salary field.

Expected Result:
The API should reject the request with a validation error indicating that salary must be a positive value.

Actual Result:
The API accepts the negative salary and processes the request.

Impact:
Invalid financial data is stored and used for benefit and net pay calculations.

Notes:
The OpenAPI schema does not define a minimum value for salary.