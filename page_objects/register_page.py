from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class RegisterPage(BasePage):
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, "[name=firstname]")
    FIRST_NAME = "Аня"
    FIELD_LAST_NAME = (By.CSS_SELECTOR, "[name=lastname]")
    LAST_NAME = "Петрова"
    FIELD_EMAIL = (By.CSS_SELECTOR, "[name=email]")
    EMAIL = "test.test6@mail.ru"
    FIELD_TELEPHONE = (By.CSS_SELECTOR, "[name=telephone]")
    TELEPHONE = 89991002929
    FIELD_PASSWORD = (By.CSS_SELECTOR, "[name=password]")
    PASSWORD = "qwerty123"
    FIELD_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "[name=confirm]")
    PASSWORD_CONFIRM = "qwerty123"
    CHECKBOX_PRIVACY_POLICY = (By.CSS_SELECTOR, "[name=agree]")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "[value=Continue]")
    BUTTON_CONTINUE_AFTER_REGISTRATION = (By.CSS_SELECTOR, ".buttons [href$='account/account']")
    BUTTON_SUCCESS = (By.CSS_SELECTOR, "[href$='account/success']")
    SUBSCRIBE_YES = (By.CSS_SELECTOR, "input[name='newsletter'][value='1']")
    SUBSCRIBE_NO = (By.CSS_SELECTOR, "input[name='newsletter'][value='0']")
    LINK_PRIVACY_POLICY = (By.CSS_SELECTOR, ".agree")
    _WAIT = 0.5

    def visibility_of_element_on_register_page(self, locator, wait=_WAIT):
        return self._verify_element_presence(wait, locator)

    def send_key_on_register_page(self, key, element, wait=_WAIT):
        self._verify_element_presence(wait, element).send_keys(key)

    def click_element_on_register_page(self, element, wait=_WAIT):
        self._click_element(wait, self._element(wait, element))
