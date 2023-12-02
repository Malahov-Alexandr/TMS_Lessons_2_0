from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    URL = 'https://www.thesaurus.com/'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        if self.wait.until(EC.presence_of_element_located(locator)):
            return self.driver.find_element(*locator)
        else:
            raise Exception(f"Element {locator} not found")

    def find_elements(self, locator):
        if self.wait.until(EC.presence_of_element_located(locator)):
            return self.driver.find_elements(*locator)
        else:
            raise Exception(f"Elements {locator} not found")


