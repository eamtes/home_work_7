from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class SuccessAlert(BasePage):
    SELF = (By.CSS_SELECTOR, ".alert-success")
    LOGIN = (By.LINK_TEXT, "login")
    SOPPING_CART = (By.PARTIAL_LINK_TEXT, "shopping cart")
    PRODUCT_COMPARISON = (By.LINK_TEXT, "product comparison")
    _WAIT = 1

    def click_element_on_success_alert(self, element, wait=_WAIT):
        self._click_element(wait, self._element(wait, element))
