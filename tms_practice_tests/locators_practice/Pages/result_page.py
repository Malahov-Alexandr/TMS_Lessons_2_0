from selenium.webdriver.common.by import By

from .base_page import BasePage

# - Зайти на сайт https://www.thesaurus.com/
# - В поле поиска ввести love
# - Нажать иконку поиска
# - Найти 6 синоним слова love
# - вывести его в консоль
# * Для любителей полазить по верстке: вывести на экран все синонимы слова love

class ResultPage(BasePage):
    ALL_SYNONYMS = (By.XPATH, "//*[@data-type='thesaurus-synonyms-card']//li")

    def get_all_synonyms(self):
        synonyms = self.find_elements(self.ALL_SYNONYMS)
        return synonyms

    def get_six_synonyms(self):
        synonyms = self.find_elements(self.ALL_SYNONYMS)
        for synonym in synonyms[:6]:
            print(synonym.text)
        return synonyms[:6]
