from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    INPUT_LIMIT = (By.ID, "input-limit")
    INPUT_SORT = (By.ID, "input-sort")
    LIST_VIEV = (By.ID, "list-view")
    GRID_VIEV = (By.ID, "grid-view")
    COLUMN_LEFT = (By.ID, "column-left")
    LAPTOP_HP_3065 = (By.CSS_SELECTOR, "[alt$='3065']")
    _WAIT = 0.5

    def visibility_of_element_on_cp(self, locator, wait=_WAIT):
        return self._verify_element_presence(wait, locator)

    def click_element_on_cp(self, locator, wait=_WAIT):
        self._click_element(wait, self._element(wait, locator))

    def move_to_element_on_cp(self, element, wait=_WAIT):
        self._move_to_element(wait, self._element(wait, element))
