import pytest
from selenium import webdriver

from .Pages.base_page import BasePage
from .Pages.main_page import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def setup(driver):
    base = BasePage(driver)
    main = MainPage(driver)
    yield base, main
