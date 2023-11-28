import pytest
from selenium import webdriver


@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome()
    print('Chrome was used')
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox()
    print('Firefox was used')
    yield driver
    driver.quit()