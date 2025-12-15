ID: BUG-008
Title: Dependent values above the maximum allowed limit are rejected without user feedback
Type: Bug / Validation / UX
Priority: High
Severity: Medium–High

Preconditions:

User is authenticated

User has access to create or edit an employee

Steps to Reproduce:

    Create or edit an employee

    Enter a number of dependents greater than the allowed maximum (e.g., 33)

    Attempt to save the employee

Expected Result:

The system should prevent saving and

Display a clear validation error explaining the maximum allowed number of dependents (e.g., 32)

Actual Result:

The system blocks the value

No validation message or explanation is shown to the user

Business Impact:

Users are unaware of system constraints

Creates a poor user experience

Increases support and onboarding costs

Evidence:
![alt text](image-7.png)