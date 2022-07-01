from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ProductPage(BasePage):
    WISH_LIST_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[type=button]#button-cart")
    ADD_TO_COMPARISON = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")
    _WAIT = 0.5

    def click_element_on_product_page(self, element, wait=_WAIT):
        self._click_element(wait, self._element(wait, element))
