from selenium.webdriver.common.by import By
from src.core.base_page import BasePage
from src.utils.logger import get_logger
import re

def money_to_float(value: str) -> float:
    """
    Converts '$1,538.46' -> 1538.46
    """
    if value is None:
        return 0.0

    clean_value = re.sub(r"[^\d.]", "", value)
    return float(clean_value)

logger = get_logger(__name__)

class DashboardPage(BasePage):

    EMPLOYEE_ROWS = (By.CSS_SELECTOR, "table tbody tr")
    ADD_EMPLOYEE_BTN = (By.CSS_SELECTOR, "button[type='button']")
    EDIT_EMPLOYEE_BTN = (By.CSS_SELECTOR, '#employeesTable > tbody > tr:nth-child(2) > td:nth-child(9) > i.fas.fa-edit')
    DELETE_EMPLOYEE_BTN = (By.CSS_SELECTOR, '#employeesTable > tbody > tr:nth-child(2) > td:nth-child(9) > i.fas.fa-times')
    FIRTSNAME = (By.ID, "firstName")
    LASTNAME = (By.ID, "lastName")
    DEPENDENTS = (By.ID, "dependants")
    ADD_BTN = (By.ID, "addEmployee")
    UPDATE_BTN = (By.CSS_SELECTOR, '#updateEmployee')
    DELETE_BTN = (By.CSS_SELECTOR, '#deleteEmployee')
    ##CANCEL_BTN = (By.XPATH,"//*[@id="employeeModal"]/div/div/div[3]/button[3]")

    GROSS = (By.CSS_SELECTOR,'#employeesTable > tbody > tr:nth-child(6) > td:nth-child(6)')
    COST = (By.CSS_SELECTOR,'#employeesTable > tbody > tr:nth-child(6) > td:nth-child(7)')
    NET = (By.CSS_SELECTOR,'#employeesTable > tbody > tr:nth-child(6) > td:nth-child(8)')

    def get_employee_count(self):
        return len(self.driver.find_elements(*self.EMPLOYEE_ROWS))

    def is_loaded(self):
        return self.wait.until(
            lambda d: d.find_element(*self.ADD_EMPLOYEE_BTN).is_displayed()
        )

    def add_employe(self,firstName,lastName,dependants):
        self.click(self.ADD_EMPLOYEE_BTN)
        logger.info("Click on Add Employee BTN")
        self.type(self.FIRTSNAME, firstName)
        logger.info("firstname set")
        self.type(self.LASTNAME, lastName)
        logger.info("Lastname set")
        self.type(self.DEPENDENTS, dependants)
        logger.info("Dependants Set")
        self.click(self.ADD_BTN)
        logger.info("Click on Add BTN")
        logger.info("Employee succesfully added")

    def edit_employe(self,firstName,lastName,dependants):
        self.click(self.EDIT_EMPLOYEE_BTN)
        logger.info("Click on Edit Employee BTN")
        self.type(self.FIRTSNAME, firstName)
        logger.info("firstname set")
        self.type(self.LASTNAME, lastName)
        logger.info("Lastname set")
        self.type(self.DEPENDENTS, dependants)
        logger.info("Dependants Set")
        self.click(self.UPDATE_BTN)
        logger.info("Click on Update BTN")
        logger.info("Employee succesfully updated")

    def delete_employe(self,firstName,lastName,dependants):
        self.click(self.DELETE_EMPLOYEE_BTN)
        logger.info("Click on Edit Employee BTN")
        self.click(self.DELETE_BTN)
        logger.info("Click on Edit Employee BTN")
        logger.info("Employee succesfully deleted")
        
    
    def assert_info(self):
        grossPay = money_to_float(self.get_text(self.GROSS))
        benefitsCost = money_to_float(self.get_text(self.COST))
        netPay = money_to_float(self.get_text(self.NET))
        if netPay != grossPay - benefitsCost:
            raise AssertionError(
                f"Net pay mismatch | net={netPay} gross={grossPay} benefits={benefitsCost}"
    )
        else:
            logger.info(
                f"Net pay validated successfully | net={netPay} gross={grossPay} benefits={benefitsCost}"
    )
