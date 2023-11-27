from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_pop():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://onliner.by")
    driver.find_element(By.XPATH, "//div[@class='auth-bar__item auth-bar__item--text']").click()
    driver.find_element(By.XPATH, "//input[@placeholder='Ник или e-mail']").send_keys('Name')
    driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys('name')
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    time.sleep(4)

    test = "//div[@class='auth-form__title auth-form__title_base auth-form__title_condensed-other']"
    assert test == "Помогите нам улучшить  безопасность"
