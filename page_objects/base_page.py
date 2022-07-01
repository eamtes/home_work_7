from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def _verify_element_presence(self, wait: float, locator: tuple):
        try:
            return WebDriverWait(self.browser, wait).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Cant find element by locator: {locator}")

    def _element(self, wait, locator: tuple):
        return self._verify_element_presence(wait, locator)

    def _elements(self, locator: tuple):
        return self.browser.find_elements(*locator)

    def _element_in_elements(self, elements, locator: tuple):
        return elements.find_element(*locator)

    def _move_to_element(self, wait, element):
        ActionChains(self.browser).pause(wait).move_to_element(element).perform()

    def _click_element(self, wait, element):
        ActionChains(self.browser).pause(wait).move_to_element(element).click().perform()

    def _click_in_element(self, wait, element, locator: tuple, index: int = 0):
        element = element.find_elements(*locator)[index]
        self._click_element(wait, element)

    def check_text(self, xpath):
        try:
            self.browser.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
