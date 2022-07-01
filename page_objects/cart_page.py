from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CartPage(BasePage):
    BUTTON_REMOVE = (By.CSS_SELECTOR, "[data-toggle=tooltip][onclick^=cart]")
    BUTTONS = (By.CSS_SELECTOR, ".buttons")
    TEXT_CART_IS_EMPTY = "//div[@id='content']//p[text()='Your shopping cart is empty!']"
    CHECKOUT_LINK = (By.LINK_TEXT, "Checkout")
    CONTENT = (By.CSS_SELECTOR, "#content")
    _WAIT = 0.5

    def go_to_checkout(self, wait=_WAIT):
        self._click_in_element(wait, self._element(wait, self.BUTTONS), self.CHECKOUT_LINK)

    def verify_product(self, product_name, wait=_WAIT):
        self._verify_element_presence(wait, self.CONTENT)
        self._verify_element_presence(wait, (By.LINK_TEXT, product_name))

    def click_element_on_cart_page(self, element, wait=_WAIT):
        self._click_element(wait, self._element(wait, element))

    def check_text_on_cart_page(self, xpath):
        self.check_text(xpath)
