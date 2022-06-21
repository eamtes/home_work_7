from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class MainPage(BasePage):
    BUTTON_MY_ACCOUNT = (By.CSS_SELECTOR, "[title$=Account]")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "[href$='account/login']")
    BUTTON_LOGOUT = (By.CSS_SELECTOR, "[href$='account/logout']")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "[href$='account/register']")
    BUTTON_DESKTOPS = (By.CSS_SELECTOR, "[href$=desktops].dropdown-toggle")
    BUTTON_SHOW_ALL_DESKTOPS = (By.CSS_SELECTOR, "[href$=desktops].see-all")
    BUTTON_CURRENCY = (By.CSS_SELECTOR, "[class=btn-group] [data-toggle=dropdown]")
    CURRENCY_EURO = (By.CSS_SELECTOR, "[name=EUR]")
    CURRENCY_POUND_STERLING = (By.CSS_SELECTOR, "[name=GBP]")
    CURRENCY_US_DOLLAR = (By.CSS_SELECTOR, "[name=USD]")
    IMG_MACBOOK = (By.CSS_SELECTOR, "img[title*=MacBook]")
    IMG_IPHONE = (By.CSS_SELECTOR, "img[title*=iPhone]")
    SEARCH = (By.NAME, "search")
    CART_TOTAL = (By.ID, "cart-total")
    LINK_TEXT_OPENCART = (By.LINK_TEXT, "OpenCart")
    _WAIT = 0.5

    FEATURE_PRODUCT = (By.CSS_SELECTOR, "#content > div.row .product-layout")
    FEATURE_PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")

    def visibility_of_element_on_main_page(self,  locator, wait=_WAIT):
        return self._verify_element_presence(wait, locator)

    def click_featured_product_on_main_page(self, number, wait=_WAIT):
        feature_product = self._elements(self.FEATURE_PRODUCT)[number]
        product_name = self._element_in_elements(feature_product, self.FEATURE_PRODUCT_NAME).text
        self._click_element(wait, feature_product)
        return product_name

    def click_element_on_main_page(self, element, wait=_WAIT):
        self._click_element(wait, self._element(wait, element))

    def move_to_element_on_main_page(self, element, wait=_WAIT):
        self._move_to_element(wait, self._element(wait, element))

    def check_text_on_main_page(self, xpath):
        self.check_text(xpath)
