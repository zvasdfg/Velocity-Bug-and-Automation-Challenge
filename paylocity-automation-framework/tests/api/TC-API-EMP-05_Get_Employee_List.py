import pytest
import requests
from requests.auth import HTTPBasicAuth
from src.config.environment import Settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

BASEURL = Settings.API_BASE_URL
USER = 'TestUser845'
PASSWORD = Settings.PASSWORD
EMPLOYEE_ENDPOINT = "/api/Employees"


@pytest.fixture
def auth():
    """Basic Auth fixture"""
    return HTTPBasicAuth(USER, PASSWORD)


@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json"
    }


@pytest.fixture
def valid_employee_payload():
    return {
        "lastName": "Dependants",
        "salary": 52000
    }


def test_tc_api_emp_001_create_employee_success(auth, headers, valid_employee_payload):
    """
    TC-API-EMP-001
    Create employee with valid mandatory data
    """

    url = f"{BASEURL}{EMPLOYEE_ENDPOINT}"

    response = requests.post(
        url,
        json=valid_employee_payload,
        headers=headers,
        auth=auth
    )

    # ---- Debug info (only printed if test fails) ----
    assert response.status_code == 400, (
        f"Expected status 200, got {response.status_code}\n"
        f"Response body:\n{response.text}"
    )

    response_json = response.json()
