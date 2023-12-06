from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# сделано только для теста, по правильному нужно создать отдельный класс
def save(text):
    with open('synonyms.txt', 'w') as file:
        for line in text:
            file.write(line.text+'\n')


class BasePage:
    URL = 'https://www.thesaurus.com/'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):

        if self.wait.until(EC.element_to_be_clickable(locator)):
            return self.driver.find_element(*locator)
        else:
            print(f"Element {locator} not found")

    def presence_locator(self, locator):
        accept_button = self.driver.find_element(*locator)
        if accept_button.is_displayed():
            accept_button.click()


    def find_elements(self, locator):
        if self.wait.until(EC.presence_of_element_located(locator)):
            return self.driver.find_elements(*locator)
        else:
            raise Exception(f"Elements {locator} not found")

    # сделано только для теста, по правильному нужно создать отдельный класс

