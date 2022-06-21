import pytest
import pathlib
from pathlib import Path
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=f"{Path(pathlib.Path.home())}/drivers")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", "-U", default="http://192.168.1.74:8081/")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(executable_path=f"{drivers}/chromedriver.exe", options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(executable_path=f"{drivers}/geckodriver.exe", options=options)
    else:
        raise ValueError("Browser not supported!")

    def open_browser():
        return driver.get(url)

    driver.open = open_browser
    driver.open()

    driver.maximize_window()
    request.addfinalizer(driver.close)

    return driver
