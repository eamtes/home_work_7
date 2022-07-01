from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    BUTTON_CONTINUE_FOR_LOGOUT = (By.CSS_SELECTOR, ".pull-right [href$='common/home']")
    TEXT_ACCOUNT_LOGOUT = "//div[@id='content']//h1[text()='Account Logout']"
    LINK_REGISTER = (By.CSS_SELECTOR, "a[href$='register'].btn")
    INPUT_LOGIN = (By.CSS_SELECTOR, "input[value='Login']")
    PLACEHOLDER_MAIL = (By.CSS_SELECTOR, "[placeholder='E-Mail Address']")
    PLACEHOLDER_PASSWORD = (By.CSS_SELECTOR, "[placeholder='Password']")
    LINK_FORGOTTEN = (By.CSS_SELECTOR, "div.form-group>a[href$='forgotten']")
    _WAIT = 0.5

    def visibility_of_element_on_login_page(self, locator, wait=_WAIT):
        return self._verify_element_presence(wait, locator)
