import pytest
import requests
from requests.auth import HTTPBasicAuth
from src.config.environment import Settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

BASEURL = Settings.API_BASE_URL
USER = 'TestUser845'
PASSWORD = Settings.PASSWORD
EMPLOYEE_ENDPOINT = "/api/Employees/"


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

    url = f"{BASEURL}{EMPLOYEE_ENDPOINT}{'98da3eb4-46b1-4d5b-ba44-8766fbc9cf97'}"

    response = requests.get(
        url,
        headers=headers,
        auth=auth
    )

    assert response.status_code == 200, (
        f"Expected status 200, got {response.status_code}\n"
        f"Response body:\n{response.text}"
    )

    response_json = response.json()

    # Validate employee data

    assert "firstName" in response_json
    assert "lastName" in response_json
    assert "dependants" in response_json

    # Calculated fields
    assert "gross" in response_json
    assert "benefitsCost" in response_json
    assert "net" in response_json

    # Business rule sanity check
    assert response_json["net"] < response_json["gross"]