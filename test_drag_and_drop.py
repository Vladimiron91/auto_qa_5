'''Задание 2: Тестирование Drag & Drop (Перетаскивание изображения в корзину)
Открыть страницу Drag & Drop Demo.
Перейти по ссылке: https://www.globalsqa.com/demo-site/draganddrop/.
Выполнить следующие шаги:
Захватить первую фотографию (верхний левый элемент).
Перетащить её в область корзины (Trash).
Проверить, что после перемещения:
В корзине появилась одна фотография.
В основной области осталось 3 фотографии.
Ожидаемый результат:
Фотография успешно перемещается в корзину.
Вне корзины остаются 3 фотографии.'''

#########################################################################################

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_drag_and_drop(browser):
    browser.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(browser, 10)

    # ---- Закрываем cookie попап ----
    try:
        consent_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.fc-button.fc-cta-consent.fc-primary-button")
            )
        )
        consent_button.click()
    except:
        pass  # если попап может не появился

    #Переход iframe
    iframe = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame"))
    )
    browser.switch_to.frame(iframe)

    #Фото CSS, как требовал ментор)))
    source = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#gallery > li:nth-child(1)")
        )
    )

    # Корзина
    target = wait.until(
        EC.presence_of_element_located((By.ID, "trash"))
    )

    #Drag & drop
    ActionChains(browser).drag_and_drop(source, target).perform()

    # ЖДУ, пока в корзине появится 1 фотография
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#trash ul li")) == 1)

    # ЖДУ, пока в галерее останется 3 фотографии
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3)

    # Проверка
    photos_in_trash = browser.find_elements(By.CSS_SELECTOR, "#trash ul li")
    photos_in_gallery = browser.find_elements(By.CSS_SELECTOR, "#gallery li")

    assert len(photos_in_trash) == 1, "В корзине должно быть 1 фото"
    assert len(photos_in_gallery) == 3, "В галерее должно остаться 3 фото"

    browser.switch_to.default_content()