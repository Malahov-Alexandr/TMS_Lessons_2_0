# Написать параметризированный тест, который:
# 1 - открывает в любом браузере* сайты https://www.amazon.com/, https://www.apple.com/, https://www.google.com/
# 2 - Проверяет, что на сайте заголовке окна для сайта Амазона - Amazon, для Эпла - Apple, для Гугла - Google
# 3 - тест должен быть параметризированным. Т.е. должны быть две переменные url и page_title, которые меняются
# 4 - на каждый сайт запускается новый тест
# * Можете попробовать запускать разные браузеры на разные сайты, например: для Амазона и Эпла - Firefox, для Гугла - хром
# ** В конце теста можно делать скриншот страницы. Делается это через driver. save_screenshot()
# *** (для самых отчаянных!) Попробуйте написать фикстуру драйвера так, чтобы скриншот делался при падении. Падение можно организовать через raise Exception("Something is wrong") в теле теста


import pytest


@pytest.mark.parametrize("url, page_title", [
    ("https://www.amazon.com/", "Amazon"),
    ("https://www.apple.com/", "Apple"),
    ("https://www.google.com/", "Google"),
])
def test_check_title(chrome_driver, firefox_driver, url, page_title):
    if 'amazon' or 'apple' in url:
        firefox_driver.get(url)
        current_title = firefox_driver.title
        assert current_title == page_title, firefox_driver.save_screenshot('screenshot_for_failed_test.png')
    else:
        chrome_driver.get(url)
        current_driver = chrome_driver.title
        assert current_driver == page_title
