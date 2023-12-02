# from Pages.base_page import BasePage
from Pages.main_page import MainPage
from Pages.result_page import ResultPage


def test_synonyms(driver):

    main_page = MainPage(driver)
    result_page = ResultPage(driver)
    driver.get('https://www.thesaurus.com/')
    main_page.search_word("love")
    main_page.click_search_button()
    synonyms = result_page.get_six_synonyms()
    result_page.print_synonyms(synonyms)
