ID: BUG-007
Title: Negative dependent values are not allowed but no validation error is displayed
Type: Bug / Validation / UX
Priority: High
Severity: Medium–High

Preconditions:

User is authenticated

User has access to create or edit an employee

Steps to Reproduce:

    Create or edit an employee

    Enter a negative number in the Dependents field (e.g., -1)

    Attempt to save the employee

Expected Result:

The system should prevent saving and

Display a clear validation error indicating that dependent values cannot be negative

Actual Result:

The system prevents the value from being saved

No error message, warning, or visual feedback is shown

Business Impact:

Users do not understand why the action failed

Causes confusion and repeated failed attempts

Violates basic form validation and usability standards

Evidence:
![alt text](image-6.png)