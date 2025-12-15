ID: BUG-009
Title: Login with unauthorized user results in HTTP 405 error instead of proper access handling
Type: Bug / Authentication / Error Handling
Priority: High
Severity: High

Preconditions:

Application is available

User is on the Login screen

Steps to Reproduce:

Navigate to the application login page

Enter valid credentials for a user that is not allowed to access the system

Submit the login form

Expected Result:

The system should:

Reject the login attempt gracefully

Display a clear and user-friendly error message (e.g., “User is not authorized to access this application”)

Return an appropriate HTTP status code (e.g., 401 Unauthorized or 403 Forbidden)

Actual Result:

The application crashes and returns an HTTP 405 (Method Not Allowed) error

Business Impact:

Poor user experience and lack of clarity

Incorrect HTTP status code complicates API and UI error handling

Potential security concern by exposing improper error responses

Increased support and troubleshooting effort

Evidence:
![alt text](image-8.png)