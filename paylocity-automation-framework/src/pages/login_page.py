from selenium.webdriver.common.by import By
from src.core.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = (By.ID, "Username")
    PASSWORD = (By.ID, "Password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    LOGOUT_LBL = (By.CSS_SELECTOR, 'body > header > nav > div > ul > li > a')

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def logout(self):
        self.click(self.LOGOUT_LBL)
