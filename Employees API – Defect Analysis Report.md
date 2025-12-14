Employees API – Defect Analysis Report
1. Purpose of This Report

This report summarizes the defects identified during functional and exploratory testing of the Employees API. The intent is to provide developers with clear, actionable information about current issues, their impact, and recommended focus areas for remediation. The level of detail reflects what would typically be shared directly with an engineering team to support efficient triage and fixes.

2. Scope

System Under Test: Employees API

Environment: Production (as provided)

Testing Focus:

CRUD operations on employees

Input validation and business rules enforcement

Error handling and API contract consistency

RESTful behavior and HTTP semantics

3. Executive Summary

Testing revealed multiple critical and high-severity defects that directly affect data integrity, business rule enforcement, and API reliability. The most severe issues involve:

Salary handling that contradicts core business assumptions

Incorrect HTTP responses for non-existing resources

Missing or inconsistent validation feedback

In addition, several medium-severity issues degrade developer experience and make automation and client-side error handling unreliable.

Overall risk assessment: High – The API is currently vulnerable to invalid financial data, ambiguous client behavior, and broken REST contracts.

4. Defect Overview
4.1 Critical & High-Severity Defects
BUG-003 – Salary can be overridden via PUT despite fixed business rules

Severity: Critical | Priority: High

Summary: The API allows salary modification even though salary is assumed to be fixed.

Impact: Breaks core payroll and benefits calculations, leading to incorrect gross, net, and benefits cost values.

Risk: Very high – Direct violation of business rules and assumptions.

BUG-001 – Retrieve employee by non-existing ID returns server error instead of 404

Severity: High | Priority: High

Summary: GET requests for non-existing employees return 5xx errors.

Impact: Clients cannot distinguish between system failures and missing resources.

Risk: High – Causes unreliable automation and incorrect error handling logic.

BUG-002 – Updating salary via PUT is ignored without validation feedback

Severity: High | Priority: High

Summary: Salary updates are silently ignored without error or warning.

Impact: Clients assume updates succeeded, leading to data inconsistencies.

Risk: High – Silent failures are difficult to detect and debug.

BUG-006 – API allows negative salary values without validation error

Severity: High | Priority: High

Summary: Negative salary values are accepted and processed.

Impact: Invalid financial data propagates into calculations.

Risk: High – Corrupts core financial logic.

4.2 Medium-Severity Defects
BUG-005 – Deleting employee with non-existing ID returns success

Severity: Medium | Priority: Medium

Summary: DELETE returns success even when the resource does not exist.

Impact: Clients cannot confirm whether a deletion actually occurred.

REST Concern: Violates standard DELETE semantics.

BUG-004 – Updating employee without ID returns non-descriptive error

Severity: Medium | Priority: Medium

Summary: PUT without ID fails without a clear error message.

Impact: Increases debugging time and confusion for API consumers.

BUG-007 – Read-only fields accepted in requests without feedback

Severity: Medium | Priority: Medium

Summary: Fields such as gross, net, and benefitsCost can be sent without validation or warnings.

Impact: Clients may assume these values are controllable from the request.

Contract Concern: Read-only constraints are not enforced or documented.

BUG-008 – API error responses are inconsistent

Severity: Medium | Priority: Medium

Summary: Error responses vary in structure and content.

Impact: Automation frameworks and frontends cannot reliably parse errors.

Root Cause: Missing standardized error schema.

BUG-009 – Dependent values below minimum rejected without clear error

Severity: Medium | Priority: Medium

Summary: Negative dependent values fail without descriptive feedback.

Impact: Users do not understand validation rules.

BUG-010 – Dependent values above maximum rejected without clear error

Severity: Medium | Priority: Medium

Summary: Values above the allowed maximum (32) are rejected silently or with vague errors.

Impact: Poor developer experience and unclear constraints.

5. Cross-Cutting Observations
5.1 Business Rules vs. Implementation

There is a clear inconsistency between documented or assumed business rules (e.g., fixed salary) and actual API behavior. In some cases, the API both allows and ignores updates to the same field, depending on the scenario.

5.2 Validation and Error Handling Gaps

Missing minimum/maximum constraints in schema definitions

Validation failures without meaningful messages

Silent rejections or ignored fields

These issues significantly increase the cost of integration and testing.

5.3 REST and API Contract Issues

Incorrect HTTP status codes (5xx instead of 404)

DELETE operations returning success for non-existing resources

No standardized error response format

6. Recommendations
Short-Term (High Priority)

Enforce salary business rules consistently (either fully immutable or explicitly editable)

Fix GET and DELETE endpoints to return correct HTTP status codes

Add validation for negative and out-of-range numeric values

Medium-Term

Define and enforce a standardized error response schema

Explicitly mark read-only fields and reject them when sent in requests

Improve validation messages across all endpoints

Long-Term

Update and align OpenAPI specification with actual behavior

Add contract tests to prevent regression in business rules and error handling

7. Conclusion

The Employees API currently exposes several high-risk defects that can lead to incorrect financial data, unreliable client behavior, and increased maintenance cost. Addressing the critical and high-severity issues should be prioritized before extending functionality or onboarding additional consumers. Standardizing validation and error handling will significantly improve API robustness and developer experience.