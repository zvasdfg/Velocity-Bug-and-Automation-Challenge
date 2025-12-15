import allure
import time
from src.core.driver_factory import DriverFactory
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import *
from src.core.base_page import *
from src.config.environment import Settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

BASEURL = Settings.UI_BASE_URL
USER = 'TestUser845'
PASSWORD = Settings.PASSWORD

@allure.feature("Login")
def test_valid_login():
    driver = DriverFactory.create_driver()
    driver.get(BASEURL)
    with allure.step("Open login page"):
        login = LoginPage(driver)
        login.login(USER, PASSWORD)
    
    with allure.step("Add Employee no deps"):
        dashboard= DashboardPage(driver)
        dashboard.add_employe("Natahsa","Romanoff","0")
        time.sleep(5)

    with allure.step("Logout"):
        login = LoginPage(driver)
        login.logout()

   ## driver.quit()
