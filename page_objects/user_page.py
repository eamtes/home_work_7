from selenium.webdriver.common.by import By
from page_objects.elements.user_login_form import UserLoginForm
from page_objects.base_page import BasePage


class UserPage(BasePage):
    SHOPPING_CART = (By.CSS_SELECTOR, "[title='Shopping Cart']")
    BACK_TO_MAIN_PAGE = (By.CSS_SELECTOR, "[href$='common/home'] [title='Your Store']")
    PAYMENT_FORM = (By.CSS_SELECTOR, "#payment-new")
    LOGIN = "test2@mail.ru"
    PASSWORD = "test"
    _WAIT = 1

    def login_with(self, username, password):
        UserLoginForm(self.browser).login_with(username, password)

    def click_link(self, link_text, wait=_WAIT):
        self._click_element(wait, (By.LINK_TEXT, link_text))

    def verify_pay_form(self, wait=_WAIT):
        self._verify_element_presence(wait, self.PAYMENT_FORM)

    def verify_product_link(self, product_name, wait=_WAIT):
        self._verify_element_presence(wait, (By.LINK_TEXT, product_name))

    def click_element_on_user_page(self, element, wait=_WAIT):
        self._click_element(wait, self._element(wait, element))
