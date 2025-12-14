# Benefits Dashboard – UX & Business Rule Defect Report

## 1. Purpose of This Report

This document consolidates the defects identified during UI and business-rule validation of the **Benefits Dashboard**. The goal is to communicate issues to the development team with sufficient clarity and context to support prioritization, design decisions, and implementation fixes.

Unlike purely technical API defects, the findings in this report focus on **user experience, financial transparency, accessibility, and business rule enforcement**, all of which directly affect user trust and regulatory risk.

## 2. Scope

* **System Under Test:** Benefits Dashboard (UI)
* **Environment:** Production (as tested)
* **Testing Focus:**

  * Financial data presentation and clarity
  * Business rule visibility and enforcement
  * Accessibility and usability
  * Risk of user misinterpretation

## 3. Executive Summary

Testing revealed several **high-impact UX and business-rule gaps** that, while not always causing functional failures, significantly increase the risk of **financial misunderstanding, user disputes, and accessibility non-compliance**.

Key themes identified:

* Lack of transparency in financial calculations
* Missing validation or warnings for extreme but allowed values
* Ambiguous labeling of monetary amounts
* Accessibility gaps that may violate WCAG standards

**Overall risk assessment:** Medium–High. While calculations appear internally consistent, the lack of clarity and safeguards can lead to incorrect decisions and loss of user confidence.

## 4. Defect Analysis

This section includes all previously identified defects **plus additional UX, validation, and authentication issues** discovered in subsequent testing rounds. The newly added defects reinforce existing themes around missing feedback, unclear constraints, and error-handling gaps.

### 4.1 High-Priority Defects

#### BUG-001 – No validation exists for maximum number of dependents (Max 32)

* **Type:** Bug / Business Rule
* **Severity:** High | **Priority:** High
* **Summary:** The system allows up to 32 dependents without warnings or validation.
* **Impact:** Enables unrealistic employee scenarios and inflated benefits costs.
* **Risk:** High – Financial and compliance implications if used incorrectly.

#### BUG-002 – Missing warning when benefits significantly reduce Net Pay

* **Type:** Bug / UX / Business Rule
* **Severity:** Medium–High | **Priority:** High
* **Summary:** Net Pay can drop significantly due to benefits costs without user awareness.
* **Impact:** Users may unknowingly accept payroll outcomes that heavily reduce take-home pay.
* **Risk:** High – Potential employee disputes and loss of trust.

### 4.2 Medium-Priority Defects

#### BUG-006 – Full GUID displayed in ID column reduces table readability

* **Type:** Bug / UX
* **Severity:** Low | **Priority:** Low
* **Summary:** The UI displays full GUID values in the ID column instead of a truncated or friendly identifier.
* **Impact:** Makes tables harder to scan and slows down user navigation.
* **Risk:** Low – Cosmetic but affects usability at scale.

#### BUG-007 – Negative dependent values are blocked without validation feedback

* **Type:** Bug / Validation / UX
* **Severity:** Medium–High | **Priority:** High
* **Summary:** Negative dependent values cannot be saved, but no error or visual feedback is shown.
* **Impact:** Users do not understand why the action failed and may repeatedly retry.
* **Risk:** Medium–High – Violates basic form validation and usability principles.

#### BUG-008 – Dependent values above the maximum limit are rejected without feedback

* **Type:** Bug / Validation / UX
* **Severity:** Medium–High | **Priority:** High
* **Summary:** Values above the allowed maximum (e.g., 32) are blocked silently.
* **Impact:** Users are unaware of system constraints and rules.
* **Risk:** Medium–High – Increases frustration, onboarding friction, and support costs.

#### BUG-009 – Unauthorized login returns HTTP 405 instead of proper access error

* **Type:** Bug / Authentication / Error Handling
* **Severity:** High | **Priority:** High
* **Summary:** Logging in with a valid but unauthorized user results in a 405 error.
* **Impact:** Poor user experience, incorrect HTTP semantics, and potential security concerns.
* **Risk:** High – Authentication and authorization flows must be explicit and predictable.

#### BUG-003 – Ambiguity in financial field pay-period labeling

* **Type:** Bug / UX
* **Severity:** Medium | **Priority:** Medium
* **Summary:** Financial fields mix annual and per-paycheck values without clear labels.
* **Impact:** Users may misinterpret amounts and draw incorrect conclusions.
* **Risk:** Medium – Especially problematic for first-time users.

#### BUG-004 – No breakdown provided for Benefits Cost calculation

* **Type:** Bug / UX
* **Severity:** Medium | **Priority:** Medium
* **Summary:** Only final benefits cost is shown, with no explanation of how it is calculated.
* **Impact:** Reduces transparency and complicates audits or employee inquiries.
* **Risk:** Medium – Affects credibility of payroll calculations.

#### BUG-005 – Action icons lack text labels and accessibility support

* **Type:** Bug / Accessibility / UX
* **Severity:** Medium | **Priority:** Medium
* **Summary:** Icons have no tooltips, aria-labels, or keyboard navigation support.
* **Impact:** Poor usability for assistive technology users and accessibility compliance risk.
* **Risk:** Medium – Potential WCAG violations.

## 5. Cross-Cutting Observations

### 5.1 Financial Transparency

Multiple defects indicate that while calculations are technically correct, the **user is not given enough context** to understand how values are derived or what they represent.

### 5.2 Business Rule Visibility

Key constraints (e.g., maximum dependents, acceptable net pay thresholds) exist implicitly but are not communicated or enforced clearly at the UI level.

### 5.3 Accessibility and Inclusivity

Missing accessibility attributes suggest accessibility was not considered as part of the initial design, increasing legal and usability risks.

## 6. Recommendations

### Short-Term

* Add warnings or confirmation dialogs when Net Pay drops below a defined threshold
* Clearly label all monetary fields as annual or per-paycheck
* Enforce or explicitly warn about maximum dependent values

### Medium-Term

* Provide a detailed benefits cost breakdown within the UI
* Standardize accessibility support for all actionable icons

### Long-Term

* Define UX standards for financial transparency across the product
* Include accessibility checks in the definition of done
* Add usability testing focused on financial comprehension

## 7. Conclusion

The Benefits Dashboard functions correctly from a calculation standpoint but lacks essential UX, accessibility, and business-rule safeguards. Addressing these issues will significantly improve user trust, reduce financial disputes, and strengthen compliance posture. The defects outlined should be treated as product quality concerns rather than cosmetic issues.
