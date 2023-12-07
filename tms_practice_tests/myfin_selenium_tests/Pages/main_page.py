from selenium.webdriver.common.by import By

from .base_page import BasePage


# 1. Открыть сайт https://myfin.by/ +
# 2. Навестись на раздел "Карты" в хедере +
# 3. Нажать "Красная карта 2.0" +
# 4. В поле "Номер мобильного телефона" ввести 299402265
# 5. Нажать кнопку "Подтвердить"+
# Ожидаемый результат:
# - Появилась надпись "Пройдите идентификацию"
# - Появилась кнопка "Перейти в МСИ"
# --- со звездочкой ---
# - Проверить, что кнопка "Перейти в МСИ" цвета #ef3124


class MainPage(BasePage):
    CARD_BUTTON = (By.XPATH, "//a[@href='/cards']")
    RED_CARD_2_0_BUTTON = (By.XPATH, "//*[.='Онлайн оформление карты']/parent::div//li[1]")
    NUMBER_FIELD = (By.XPATH, "//*[@type='tel']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@type='submit']")
    IDENTIFICATION_TEXT_locator = (By.XPATH, "//span[@class='title']")
    GO_TO_MSI_BUTTON = (By.XPATH, "//button[@type='button']")
    PHONE_NUMBER = '299402265'
    # Exptected values
    GO_TO_MSI_BUTTON_COLOR = 'rgba(239, 49, 36, 1)'
    IDENTIFICATION_TEXT = 'Пройдите идентификацию'

    def hover_card_button(self):
        self.do_hover(self.CARD_BUTTON)

    def click_red_card_button(self):
        self.click(self.RED_CARD_2_0_BUTTON)

    def fill_in_the_number_field(self):
        self.input(self.NUMBER_FIELD, self.PHONE_NUMBER)

    def verify_identification_text(self):
        identification_text = self.find_element(self.IDENTIFICATION_TEXT_locator)
        assert identification_text.text == self.IDENTIFICATION_TEXT

    def verify_msi_button(self):
        msi_button = self.find_element(self.GO_TO_MSI_BUTTON)
        assert msi_button.is_displayed()
        button_color = self.get_color(self.GO_TO_MSI_BUTTON)
        print(button_color)
        assert button_color == self.GO_TO_MSI_BUTTON_COLOR, f"Button color is {button_color} "
