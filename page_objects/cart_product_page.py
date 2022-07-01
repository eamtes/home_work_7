from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CartProductPage(BasePage):
    DOT = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    LINK_HP = (By.CSS_SELECTOR, "a[href$='hewlett-packard']")
    BUTTON_CART = (By.CSS_SELECTOR, "button#button-cart")
    INPUT_OPTION_255 = (By.CSS_SELECTOR, "#input-option225")
    BUTTON_ONCLICK_COMPARE = (By.CSS_SELECTOR, "button[onclick^='compare']")
    _WAIT = 0.5

    def visibility_of_element_on_cart_product_page(self, locator, wait=_WAIT):
        return self._verify_element_presence(wait, locator)
