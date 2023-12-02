from .Pages.base_page import BasePage,save
from .Pages.main_page import MainPage
from .Pages.result_page import ResultPage


def test_synonyms(driver):
    main_page = MainPage(driver)
    result_page = ResultPage(driver)
    driver.get(BasePage.URL)
    main_page.cookies_pass()
    main_page.search_word_field("love")
    main_page.click_search_button()
    result_page.get_six_synonyms()
    all_results = result_page.get_all_synonyms()
    save(all_results)

