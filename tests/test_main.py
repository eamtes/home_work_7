import time
import pytest
from page_objects.register_page import RegisterPage
from page_objects.cart_page import CartPage
from page_objects.product_page import ProductPage
from page_objects.user_page import UserPage
from page_objects.catalog_page import CatalogPage
from page_objects.elements.success_alert import SuccessAlert
from page_objects.main_page import MainPage
from page_objects.cart_product_page import CartProductPage
from page_objects.login_page import LoginPage


@pytest.mark.parametrize("CSS_SELECTORS", [MainPage.IMG_MACBOOK,
                                           MainPage.IMG_IPHONE,
                                           MainPage.SEARCH,
                                           MainPage.CART_TOTAL,
                                           MainPage.LINK_TEXT_OPENCART])
def test_main_page(browser, CSS_SELECTORS):
    MainPage(browser).visibility_of_element_on_main_page(CSS_SELECTORS)


@pytest.mark.parametrize("CSS_SELECTORS", [CatalogPage.INPUT_LIMIT,
                                           CatalogPage.INPUT_SORT,
                                           CatalogPage.LIST_VIEV,
                                           CatalogPage.GRID_VIEV,
                                           CatalogPage.COLUMN_LEFT])
def test_catalog_page(browser, CSS_SELECTORS):
    MainPage(browser).move_to_element_on_main_page(MainPage.BUTTON_DESKTOPS)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_SHOW_ALL_DESKTOPS)
    CatalogPage(browser).visibility_of_element_on_cp(CSS_SELECTORS)


@pytest.mark.parametrize("CSS_SELECTORS", [CartProductPage.DOT,
                                           CartProductPage.LINK_HP,
                                           CartProductPage.BUTTON_CART,
                                           CartProductPage.INPUT_OPTION_255,
                                           CartProductPage.BUTTON_ONCLICK_COMPARE])
def test_cart_product_page(browser, CSS_SELECTORS):
    MainPage(browser).move_to_element_on_main_page(MainPage.BUTTON_DESKTOPS)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_SHOW_ALL_DESKTOPS)
    CatalogPage(browser).click_element_on_cp(CatalogPage.LAPTOP_HP_3065)
    CartProductPage(browser).visibility_of_element_on_cart_product_page(CSS_SELECTORS)


@pytest.mark.parametrize("CSS_SELECTORS", [LoginPage.LINK_REGISTER,
                                           LoginPage.INPUT_LOGIN,
                                           LoginPage.PLACEHOLDER_MAIL,
                                           LoginPage.PLACEHOLDER_PASSWORD,
                                           LoginPage.LINK_FORGOTTEN])
def test_login_page(browser, CSS_SELECTORS):
    # Здесь без sleep не работает, не понимаю почему. Обрывается на первом шаге. Как будто
    # страница не успевает подгрузится
    time.sleep(1)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_MY_ACCOUNT)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_LOGIN)
    LoginPage(browser).visibility_of_element_on_login_page(CSS_SELECTORS)


@pytest.mark.parametrize("CSS_SELECTORS", [RegisterPage.SUBSCRIBE_YES,
                                           RegisterPage.SUBSCRIBE_NO,
                                           RegisterPage.CHECKBOX_PRIVACY_POLICY,
                                           RegisterPage.BUTTON_CONTINUE,
                                           RegisterPage.LINK_PRIVACY_POLICY])
def test_register_page(browser, CSS_SELECTORS):
    time.sleep(1)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_MY_ACCOUNT)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_REGISTER)
    RegisterPage(browser).visibility_of_element_on_register_page(CSS_SELECTORS)


def test_adding_new_product(browser):
    # Здесь без sleep не работает, не понимаю почему. Обрывается на первом шаге. Как будто
    # страница не успевает подгрузится
    time.sleep(1)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_MY_ACCOUNT)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_LOGIN)
    UserPage(browser).login_with(UserPage.LOGIN, UserPage.PASSWORD)
    MainPage(browser).click_element_on_main_page(UserPage.BACK_TO_MAIN_PAGE)
    product_name = MainPage(browser).click_featured_product_on_main_page(0)
    ProductPage(browser).click_element_on_product_page(ProductPage.ADD_TO_CART_BUTTON)
    SuccessAlert(browser).click_element_on_success_alert(SuccessAlert.SOPPING_CART)
    CartPage(browser).verify_product(product_name)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_MY_ACCOUNT)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_LOGOUT)
    MainPage(browser).check_text_on_main_page(LoginPage.TEXT_ACCOUNT_LOGOUT)
    MainPage(browser).click_element_on_main_page(LoginPage.BUTTON_CONTINUE_FOR_LOGOUT)


# Тест использует шаги добавления товара, так как тесты должны быть независимы от других тестов
def test_removing_product_from_the_list(browser):
    # Здесь без sleep не работает, не понимаю почему. Обрывается на первом шаге. Как будто
    # страница не успевает подгрузится
    time.sleep(1)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_MY_ACCOUNT)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_LOGIN)
    UserPage(browser).login_with(UserPage.LOGIN, UserPage.PASSWORD)
    MainPage(browser).click_element_on_main_page(UserPage.BACK_TO_MAIN_PAGE)
    product_name = MainPage(browser).click_featured_product_on_main_page(0)
    ProductPage(browser).click_element_on_product_page(ProductPage.ADD_TO_CART_BUTTON)
    SuccessAlert(browser).click_element_on_success_alert(SuccessAlert.SOPPING_CART)
    CartPage(browser).verify_product(product_name)
    CartPage(browser).click_element_on_cart_page(CartPage.BUTTON_REMOVE)
    CartPage(browser).check_text_on_cart_page(CartPage.TEXT_CART_IS_EMPTY)
    # Здесь без sleep не работает, не понимаю почему. Обрывается на первом шаге. Как будто
    # страница не успевает подгрузится
    time.sleep(1)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_MY_ACCOUNT)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_LOGOUT)
    MainPage(browser).check_text_on_main_page(LoginPage.TEXT_ACCOUNT_LOGOUT)
    MainPage(browser).click_element_on_main_page(LoginPage.BUTTON_CONTINUE_FOR_LOGOUT)


def test_new_user_registration(browser):
    # Здесь без sleep не работает, не понимаю почему. Обрывается на первом шаге. Как будто
    # страница не успевает подгрузится
    time.sleep(1)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_MY_ACCOUNT)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_REGISTER)
    RegisterPage(browser).send_key_on_register_page(RegisterPage.FIRST_NAME, RegisterPage.FIELD_FIRST_NAME)
    RegisterPage(browser).send_key_on_register_page(RegisterPage.LAST_NAME, RegisterPage.FIELD_LAST_NAME)
    RegisterPage(browser).send_key_on_register_page(RegisterPage.EMAIL, RegisterPage.FIELD_EMAIL)
    RegisterPage(browser).send_key_on_register_page(RegisterPage.TELEPHONE, RegisterPage.FIELD_TELEPHONE)
    RegisterPage(browser).send_key_on_register_page(RegisterPage.PASSWORD, RegisterPage.FIELD_PASSWORD)
    RegisterPage(browser).send_key_on_register_page(RegisterPage.PASSWORD_CONFIRM, RegisterPage.FIELD_PASSWORD_CONFIRM)
    RegisterPage(browser).click_element_on_register_page(RegisterPage.CHECKBOX_PRIVACY_POLICY)
    RegisterPage(browser).click_element_on_register_page(RegisterPage.BUTTON_CONTINUE)
    RegisterPage(browser).visibility_of_element_on_register_page(RegisterPage.BUTTON_SUCCESS)
    RegisterPage(browser).click_element_on_register_page(RegisterPage.BUTTON_CONTINUE_AFTER_REGISTRATION)


def test_currency_switching(browser):
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_CURRENCY)
    MainPage(browser).click_element_on_main_page(MainPage.CURRENCY_POUND_STERLING)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_CURRENCY)
    MainPage(browser).click_element_on_main_page(MainPage.CURRENCY_US_DOLLAR)
    MainPage(browser).click_element_on_main_page(MainPage.BUTTON_CURRENCY)
    MainPage(browser).click_element_on_main_page(MainPage.CURRENCY_EURO)
