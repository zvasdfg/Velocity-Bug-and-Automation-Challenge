ID: BUG-002
Title: Missing warning when benefits significantly reduce Net Pay
Type: Bug / UX / Business Rule
Priority: High
Severity: Medium–High

Preconditions:

Employee with multiple dependents

Steps to Reproduce:

    Create or edit an employee with a large number of dependents

    Review Gross Pay, Benefits Cost, and Net Pay values

Expected Result:

The system should display:

A warning message, or

A confirmation prompt when Net Pay falls below a defined threshold

Actual Result:

Net Pay is reduced without any warning or user confirmation

Business Impact:

Lack of financial transparency

Increased risk of employee disputes

Poor user trust in payroll accuracy

Evidence:
![alt text](image-2.png)