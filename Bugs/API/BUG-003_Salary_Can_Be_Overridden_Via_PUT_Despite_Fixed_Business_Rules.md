ID: BUG-003
Title: Salary can be overridden via PUT despite fixed business rules
Component: Employees API
Environment: Prod
Severity: Critical
Priority: High

Preconditions:
An employee already exists in the system.

Steps to Reproduce:

Send a PUT request to /api/Employees with a different salary value.

Expected Result:
Salary should remain fixed or the API should reject the request with a clear validation error.

Actual Result:
The salary value is successfully overwritten.

Impact:
This breaks core business assumptions and leads to incorrect gross pay, benefits cost, and net pay calculations.

Notes:
This behavior directly contradicts documented assumptions regarding fixed salary values.