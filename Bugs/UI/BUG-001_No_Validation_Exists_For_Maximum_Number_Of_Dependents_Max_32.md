ID: BUG-001
Title: No validation exists for maximum number of dependents (Max 32)
Type: Bug / Business Rule
Priority: High
Severity: High

Preconditions:

User is authenticated

User has access to the Benefits Dashboard

Steps to Reproduce:

    Create or edit an employee

    Enter a high number of dependents (e.g., 32)

    Save the employee

    Observe the calculated Benefits Cost and Net Pay

Expected Result:

The system should:

Enforce a reasonable maximum number of dependents, or

Display a validation error or warning for unrealistic values

Actual Result:

The system accepts up to 32 dependents without validation

Business Impact:

Allows unrealistic scenarios

May cause incorrect payroll calculations

Poses financial and compliance risks

Evidence:
![alt text](image.png)