
from selenium.webdriver.common.by import By

from base_page import BasePage


# - Зайти на сайт https://www.thesaurus.com/
# - В поле поиска ввести love
# - Нажать иконку поиска
# - Найти 6 синоним слова love
# - вывести его в консоль
# * Для любителей полазить по верстке: вывести на экран все синонимы слова love

class MainPage(BasePage):
    SEARCH_FIELD = (By.XPATH, "//input[@id='global-search']/parent::div")
    SEARCH_BUTTON = (By.XPATH, "//input[@id='global-search']/parent::div/child::button")

    def search_word(self, word):
        self.find_element(self.SEARCH_FIELD).send_keys(word)

    def click_search_button(self):
        self.find_element(self.SEARCH_BUTTON).click()

