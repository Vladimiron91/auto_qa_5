'''Задание 1: Проверка наличия текста в iframe
Открыть страницу
Перейти по ссылке: https://bonigarcia.dev/selenium-webdriver-java/iframes.html.
Проверить наличие текста
Найти фрейм (iframe), в котором содержится искомый текст.
Переключиться в этот iframe.
Найти элемент, содержащий текст "semper posuere integer et senectus justo curabitur.".
Убедиться, что текст отображается на странице.'''

###############################################################################################

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_iframe_text(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    WebDriverWait(browser, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "my-iframe"))
    )

    expected_text = "semper posuere integer et senectus justo curabitur."

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"),
            expected_text
        )
    )

    body_text = browser.find_element(By.TAG_NAME, "body").text

    assert expected_text in body_text, "Текст не найден внутри iframe"