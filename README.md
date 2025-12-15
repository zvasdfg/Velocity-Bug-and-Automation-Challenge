# Paylocity Automation Framework

## 📌 Overview

Paylocity Automation Framework is a **Python-based test automation framework** designed to validate both **UI and API layers** using best practices in test architecture.

The framework follows:

* **Page Object Model (POM)** for UI automation
* **Service / Client abstraction** for API automation
* **Pytest** as the test runner
* **Selenium WebDriver** for UI tests
* **Requests** for API tests
* **Allure** for reporting

It is intentionally kept **simple, scalable, and CI/CD friendly**, suitable for technical assessments and real-world projects.

---

## ⚠️ IMPORTANT NOTE

I am aware that it is **not a security best practice** to publish sensitive files such as `.env` files (and other artifacts that should normally be included in `.gitignore`).

However, **for the purpose of facilitating installation, execution, and review of this assessment**, these files have been intentionally included in the repository.

In a real production or enterprise environment, all sensitive configuration files would be:
- Properly excluded from version control
- Managed through secure secret management solutions
- Injected via environment variables or CI/CD pipelines
---

## 📊 Defect Analysis Reports

At the **root of this repository**, you will find the following defect analysis documents:

- **Employees API – Defect Analysis Report**
- **Benefits Dashboard – UX & Business Rule Defect Report**

These documents provide:
- A consolidated view of the identified issues
- Description of functional, technical, and business rule defects
- Expected vs actual behavior
- Impact and observations

---

## 🐞 Individual Bug Evidence

Detailed bug reports with supporting evidence (screenshots, logs, request/response samples) are available in the following directories:
```text
Bugs/
├── API/
└── UI/
```

Each bug includes:
- Clear reproduction steps
- Evidence
- Observed behavior
- Expected behavior

---

## 🧪 Automated Test Cases

The test cases that were automated as part of this project are also available in **test case format** for review and traceability.

They can be found here:
```text
Test Cases/
├── API/
└── UI/
```
These documents describe:
- Test objectives
- Preconditions
- Steps
- Expected results

---


## 🧱 Tech Stack

* Python 3.9+
* Pytest
* Selenium
* Requests
* Allure Reports
* WebDriver Manager

---

## 📂 Project Structure

```text
<<<<<<< HEAD
Paylocity/
├── Bugs/
│   ├── API/
│   │   ├── BUG-001.txt
│   │   ├── BUG-002.txt
│   │   ├── BUG-003.txt
│   │   ├── BUG-004.txt
│   │   ├── BUG-005.txt
│   │   ├── BUG-006.txt
│   │   ├── BUG-007.txt
│   │   ├── BUG-008.txt
│   │   ├── BUG-009.txt
│   │   ├── BUG-010.txt
│   ├── UI/
│   │   ├── BUG-001.txt
│   │   ├── BUG-002.txt
│   │   ├── BUG-003.txt
│   │   ├── BUG-004.txt
│   │   ├── BUG-005.txt
│   │   ├── BUG-006.txt
│   │   ├── BUG-007.txt
│   │   ├── BUG-008.txt
├── Test Cases/
│   ├── API/
│   │   ├── TC-API-EMP-001.xlsx
│   │   ├── TC-API-EMP-002.xlsx
│   │   ├── TC-API-EMP-003.xlsx
│   │   ├── TC-API-EMP-004.xlsx
│   │   ├── TC-API-EMP-005.xlsx
│   │   ├── TC-API-EMP-006.xlsx
│   │   ├── TC-API-EMP-007.xlsx
│   │   ├── TC-API-EMP-008.xlsx
│   │   ├── TC-API-EMP-009.xlsx
│   │   ├── TC-API-EMP-010.xlsx
│   │   ├── TC-API-EMP-011.xlsx
│   │   ├── TC-API-EMP-012.xlsx
│   │   ├── TC-API-EMP-013.xlsx
│   │   ├── TC-API-EMP-014.xlsx
│   │   ├── TC-API-EMP-015.xlsx
│   ├── UI/
│   │   ├── TC-01 Add employee with no dependents.xlsx
│   │   ├── TC-02 Add employee with one dependent.xlsx
│   │   ├── TC-03 Add employee with multiple dependents.xlsx
│   │   ├── TC-04 Validate paycheck deduction calculation.xlsx
│   │   ├── TC-05 Edit employee dependents.xlsx
│   │   ├── TC-06 Delete employee.xlsx
│   │   ├── TC-07 Add employee with negative dependents.xlsx
│   │   ├── TC-08 Add employee with very large number of dependents.xlsx
├── Paylocity-automation-framework/
│   ├── .env
│   ├── pytest.ini
│   ├── README.md
│   ├── requirements.txt
│   ├── src/
│   │   ├── config/
│   │   │   ├── config.yaml
│   │   │   ├── environment.py
│   │   ├── core/
│   │   │   ├── api_client.py
│   │   │   ├── base_page.py
│   │   │   ├── driver_factory.py
│   │   │   ├── __init__.py
│   │   ├── pages/
│   │   │   ├── dashboard_page.py
│   │   │   ├── login_page.py
│   │   ├── services/
│   │   │   ├── employee_api.py
│   │   ├── utils/
│   │   │   ├── assertions.py
│   │   │   ├── logger.py
│   │   ├── __init__.py
│   ├── tests/
│   │   ├── api/
│   │   │   ├── TC-API-EMP-01.py
│   │   │   ├── TC-API-EMP-02.py
│   │   │   ├── TC-API-EMP-03.py
│   │   │   ├── TC-API-EMP-04.py
│   │   │   ├── TC-API-EMP-05.py
│   │   │   ├── TC-API-EMP-07.py
│   │   │   ├── TC-API-EMP-08.py
│   │   │   ├── TC-API-EMP-10.py
│   │   ├── ui/
│   │   │   ├── TC-01.py
│   │   │   ├── TC-02.py
│   │   │   ├── TC-03.py
│   │   │   ├── TC-04.py
│   │   │   ├── TC-05.py
│   │   │   ├── TC-06.py
│   │   │   ├── test_login.py

=======
├── src/
│   ├── config/
│   ├── core/
│   │   ├── __init__.py (0.0 KB)
│   │   ├── base_page.py (0.6 KB)
│   │   └── driver_factory.py (0.6 KB)
│   ├── pages/
│   │   ├── dashboard_page.py (3.5 KB)
│   │   └── login_page.py (0.5 KB)
│   ├── utils/
│   │   ├── assertions.py (3.0 KB)
│   │   └── logger.py (1.2 KB)
│   └── __init__.py (0.0 KB)
├── tests/
│   ├── api/
│   │   ├── TC-API-EMP-01_Create_Employee_Mandatory_Data.py (1.9 KB)
│   │   ├── TC-API-EMP-02_Create_Employee_Max_Dependants.py (1.9 KB)
│   │   ├── TC-API-EMP-03_Create_Employee_Negative_Dependants.py (1.3 KB)
│   │   ├── TC-API-EMP-04_Create_Employee_Overflow_Dependants.py (1.3 KB)
│   │   ├── TC-API-EMP-05_Get_Employee_List.py (1.2 KB)
│   │   ├── TC-API-EMP-07_Create_Employee_WIthout_Mandatory_Data.py (1.8 KB)
│   │   ├── TC-API-EMP-08_Get_Single_Employee.py (1.6 KB)
│   │   └── TC-API-EMP-10_Modify_Existing_Employee.py (1.6 KB)
│   └── ui/
│       ├── TC-01_Add_Employee_No_Deps.py (0.9 KB)
│       ├── TC-02_Add_Employee_SIngle_Dep.py (0.9 KB)
│       ├── TC-03_Add_Employee_Multiple_Deps.py (0.9 KB)
│       ├── TC-04_Validate_Information.py (0.9 KB)
│       ├── TC-05_Edit_Employee.py (0.9 KB)
│       └── TC-06_Delete_Employee.py (1.0 KB)
├── conftest.py (0.2 KB)
├── pytest.ini (0.9 KB)
└── requirements.txt (0.7 KB)
>>>>>>> 74ba17043a5b629f768b856dd8c0854999b03b51



```

---

## ⚙️ Setup Instructions

### 1️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Chrome WebDriver

ChromeDriver is managed automatically using **webdriver-manager**.
Make sure you have **Google Chrome installed**.

---

## ▶️ Running Tests

### Make sure to be in the right location:

```bash
velocity-automation-framework
```
### Run all tests

```bash
pytest
```

---

### Run UI tests only

```bash
pytest -m ui
```

---

### Run API tests only

```bash
pytest -m api
```

---

### Run a single test

```bash
pytest tests/api/test_employee_api.py::test_get_all_employees
```

---

## 📊 Allure Reporting

### Run tests with Allure results

```bash
pytest --alluredir=allure-results
```

### Open report

```bash
allure serve allure-results
```

The report includes:

* Test steps
* Logs
* Attachments (API responses, UI data)

---

## 🧪 Test Design Principles

* Clear separation between **test logic** and **automation logic**
* No business logic inside tests
* Reusable assertions and helpers
* Explicit fixtures instead of hidden state

---

## 🧠 Best Practices Applied

✔ Page Object Model (POM)
✔ Single Responsibility Principle
✔ Explicit pytest fixtures
✔ Logging instead of print statements
✔ API and UI validation in the same framework
✔ CI/CD ready

---

## 🚀 Possible Enhancements

* API authentication handling
* Schema validation (JSON Schema)
* UI ↔ API data comparison
* Docker support
* Parallel execution
* Contract testing

---

## 👤 Author

**Isaac Arellano**
Senior / Principal QA Engineer

---

## 📜 License

This project is for educational and assessment purposes.
