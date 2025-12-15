import allure
from src.utils.logger import get_logger

logger = get_logger(__name__)


def assert_equals(actual, expected, message: str = ""):
    """
    Generic equality assertion with logging
    """
    logger.info("Asserting equality | Expected: %s | Actual: %s", expected, actual)

    try:
        assert actual == expected
    except AssertionError:
        _attach_to_allure(actual, expected)
        raise AssertionError(
            message or f"Assertion failed: expected '{expected}', but got '{actual}'"
        )


def assert_not_equals(actual, expected, message: str = ""):
    logger.info(
        "Asserting inequality | Expected not equal to: %s | Actual: %s",
        expected, actual
    )

    try:
        assert actual != expected
    except AssertionError:
        _attach_to_allure(actual, expected)
        raise AssertionError(
            message or f"Assertion failed: values should not be equal -> '{actual}'"
        )


def assert_true(condition, message: str = ""):
    logger.info("Asserting condition is TRUE")

    try:
        assert condition is True
    except AssertionError:
        raise AssertionError(
            message or "Assertion failed: condition is not True"
        )


def assert_false(condition, message: str = ""):
    logger.info("Asserting condition is FALSE")

    try:
        assert condition is False
    except AssertionError:
        raise AssertionError(
            message or "Assertion failed: condition is not False"
        )


def assert_contains(container, value, message: str = ""):
    logger.info(
        "Asserting container contains value | Container: %s | Value: %s",
        container, value
    )

    try:
        assert value in container
    except AssertionError:
        raise AssertionError(
            message or f"Assertion failed: '{value}' not found in '{container}'"
        )


def assert_status_code(response, expected_code: int):
    """
    API-specific assertion
    """
    actual_code = response.status_code
    logger.info(
        "Asserting HTTP status code | Expected: %s | Actual: %s",
        expected_code, actual_code
    )

    try:
        assert actual_code == expected_code
    except AssertionError:
        _attach_api_response(response)
        raise AssertionError(
            f"Expected status code {expected_code}, but got {actual_code}"
        )


def _attach_to_allure(actual, expected):
    """
    Attach assertion values to Allure report
    """
    try:
        allure.attach(
            f"Expected: {expected}\nActual: {actual}",
            name="Assertion Details",
            attachment_type=allure.attachment_type.TEXT
        )
    except Exception:
        pass


def _attach_api_response(response):
    try:
        allure.attach(
            response.text,
            name="API Response",
            attachment_type=allure.attachment_type.JSON
        )
    except Exception:
        pass
