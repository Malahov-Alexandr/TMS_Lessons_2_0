# 1. Открыть сайт https://blizko.by/
# 2. Перейти на страницу "Каталог"
# 3. Развернуть выпадашку "Дом"
# 4. Выбрать "Товары для дома"
# 5. Нажать на кнопку "Телефоны" у первого мазагазина
# Ожидаемый результат
# На появившейся модалке есть заголовок, адрес, несколько телефонов,
# кнопка закрытия и фраза "Пожалуйста, сообщите администратору, что нашли этот телефон на Blizko.by" в футере
# === Со звездочкой ===
# - проверить, что заголовок жирный (только не говорите ему :) )
# - проверить, что телефон в формате 8(ХХХ) ХХХ-ХХ-ХХ
# - проверить, что телефон - это не просто текст

from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from tms_practice_tests.playwright_practice.assert_data import *


class TestExample:
    def test_example(self, page: Page):
        home_page = HomePage(page)
        catalog_page = CatalogPage(page)
        product_page = ProductPage(page)

        home_page.go_to('https://blizko.by/')
        home_page.goto_catalog()
        catalog_page.select_by_text("Дом")
        catalog_page.select_by_text("Товары для дома")
        catalog_page.select_by_role("Телефоны")

        title_text = product_page.get_title()
        address_text = product_page.get_address()
        say_to_admin_text = product_page.say_to_admin_text()
        assert title_text == title_for_order_page
        assert address_text == address_for_order_page
        assert say_to_admin_text.strip() == say_to_admin




