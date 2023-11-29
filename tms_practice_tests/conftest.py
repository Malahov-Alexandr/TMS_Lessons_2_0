import pytest
from selenium import webdriver


class CustomDriver:
    driver = None

    def __init__(self, x):
        self.x = x

    def custom_driver(self):
        print('x = ', self.x)

        if ('apple' in self.x) or ('amazon' in self.x):
            self.driver = webdriver.Firefox()
            print('firefox')
        else:
            self.driver = webdriver.Chrome()
            print('chrome')
        return self.driver


@pytest.fixture
def driver(test_arg, request):
    new_webdriver = CustomDriver(test_arg)
    driver = new_webdriver.custom_driver()

    def take_screenshot():
        if request.node.rep_call.failed:
            driver.save_screenshot(f"screenshot_after_test.png")

    yield driver
    # take_screenshot()
    driver.quit()
