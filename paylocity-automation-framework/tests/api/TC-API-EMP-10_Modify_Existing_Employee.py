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
def update_payload():
    return {
        "username": "jdoe",
        "firstName": "John",
        "lastName": "Doe",
        "salary": 60000,
        "dependants": 0
    }


def test_tc_api_emp_001_create_employee_success(auth, headers, update_payload):
    """
    TC-API-EMP-001
    Create employee with valid mandatory data
    """

    url = f"{BASEURL}{EMPLOYEE_ENDPOINT}{'98da3eb4-46b1-4d5b-ba44-8766fbc9cf97'}"

    response = requests.put(
        url,
        json=update_payload,
        headers=headers,
        auth=auth
    )

    assert response.status_code == 200, (
        f"Expected status 200, got {response.status_code}\n"
        f"Response body:\n{response.text}"
    )

    response_json = response.json()

    # Validate updated data
    assert response_json["salary"] == 60000
    assert response_json["dependents"] == 2

    # Calculated fields recalculated
    assert "gross" in response_json
    assert "benefitsCost" in response_json
    assert "net" in response_json

    # Business rule sanity check
    assert response_json["net"] < response_json["gross"]