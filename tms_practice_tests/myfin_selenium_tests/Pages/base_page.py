import colorsys

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# 1. Открыть сайт https://myfin.by/
# 2. Навестись на раздел "Карты" в хедере
# 3. Нажать "Красная карта 2.0"
# 4. В поле "Номер мобильного телефона" ввести 299402265
# 5. Нажать кнопку "Подтвердить"
# Ожидаемый результат:
# - Появилась надпись "Пройдите идентификацию"
# - Появилась кнопка "Перейти в МСИ"
# --- со звездочкой ---
# - Проверить, что кнопка "Перейти в МСИ" цвета #ef3124


class BasePage:
    URL = 'https://www.myfin.by/'

    def __init__(self, driver):
        self.window_handler = None
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):

        if self.wait.until(EC.element_to_be_clickable(locator)):
            return self.driver.find_element(*locator)
        else:
            print(f"Element {locator} not found")

    def do_hover(self, locator):
        ActionChains(self.driver).move_to_element(self.find_element(locator)).perform()

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.find_element(locator).click()

    def input(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        text = self.find_element(locator).text
        return text

    def get_attr(self, locator, attribute):
        attr = self.find_element(locator).get_attribute(attribute)
        return attr

    def get_color(self, locator):
        color = self.find_element(locator).value_of_css_property('background-color')
        return color

    def go_to_another_page(self):
        self.window_handler = self.driver.window_handles
        if len(self.window_handler) > 1:
            self.driver.switch_to.window(self.window_handler[1])
        else:
            raise Exception("No other window to switch to")

