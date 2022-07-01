from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class UserLoginForm(BasePage):
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value=Login]")
    _WAIT = 0.5

    def login_with(self, username, password, wait=_WAIT):
        self._verify_element_presence(wait, self.INPUT_EMAIL).send_keys(username)
        self._verify_element_presence(wait, self.INPUT_PASSWORD).send_keys(password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()
