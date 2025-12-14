# Velocity Automation Framework

## 📌 Overview

Velocity Automation Framework is a **Python-based test automation framework** designed to validate both **UI and API layers** using best practices in test architecture.

The framework follows:

* **Page Object Model (POM)** for UI automation
* **Service / Client abstraction** for API automation
* **Pytest** as the test runner
* **Selenium WebDriver** for UI tests
* **Requests** for API tests
* **Allure** for reporting

It is intentionally kept **simple, scalable, and CI/CD friendly**, suitable for technical assessments and real-world projects.

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
Velocity/
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
├── velocity-automation-framework/
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
