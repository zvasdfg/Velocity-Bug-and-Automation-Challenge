ID: BUG-002
Title: Updating salary via PUT is ignored without returning any validation error
Component: Employees API
Environment: Prod
Severity: High
Priority: High

Preconditions:
An employee already exists in the system.

Steps to Reproduce:

Create an employee with a valid salary.

Send a PUT request to /api/Employees attempting to update the salary field.

Expected Result:
The API should either update the salary successfully or return a validation error explaining that the salary field is not editable.

Actual Result:
The salary value is not updated and no error or warning message is returned.

Impact:
Client applications assume the update succeeded, causing data inconsistency and incorrect financial calculations.

Notes:
Salary mutability is not documented in the API contract.