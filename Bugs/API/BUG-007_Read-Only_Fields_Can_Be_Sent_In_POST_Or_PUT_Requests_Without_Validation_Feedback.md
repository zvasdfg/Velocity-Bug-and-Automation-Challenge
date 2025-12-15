ID: BUG-007
Title: Read-only fields can be sent in POST or PUT requests without validation feedback
Component: Employees API
Environment: Prod
Severity: Medium
Priority: Medium

Preconditions:
API is available and reachable.

Steps to Reproduce:

Send a POST or PUT request including read-only fields such as gross, net, or benefitsCost.

Expected Result:
The API should reject the request or explicitly ignore the fields and return a warning.

Actual Result:
The fields are silently ignored or recalculated without any feedback.

Impact:
API consumers may incorrectly assume these fields can be controlled from the client side.

Notes:
Read-only behavior is not enforced or documented in the API contract.