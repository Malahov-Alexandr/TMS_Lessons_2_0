import pytest
from selenium import webdriver


@pytest.fixture
def chrome_driver(request):
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    driver = webdriver.Chrome(options=option)

    def take_screenshot():
        if request.node.rep_call.failed:
            driver.save_screenshot(f"screenshot_after_test.png")

    yield driver
    # driver.save_screenshot(f"screenshot.png")
    take_screenshot()
    driver.quit()


@pytest.fixture()
def firefox_driver(request):
    option = webdriver.FirefoxOptions()
    option.add_argument("--headless")
    driver = webdriver.Firefox(options=option)

    def take_screenshot():
        if request.node.rep_call.failed:
            driver.save_screenshot(f"screenshot.png")

    yield driver
    #driver.save_screenshot(f"screenshot_after_test.png")
    take_screenshot()
    driver.quit()