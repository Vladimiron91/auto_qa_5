'''Задание 1: Проверка наличия текста в iframe
Открыть страницу
Перейти по ссылке: https://bonigarcia.dev/selenium-webdriver-java/iframes.html.
Проверить наличие текста
Найти фрейм (iframe), в котором содержится искомый текст.
Переключиться в этот iframe.
Найти элемент, содержащий текст "semper posuere integer et senectus justo curabitur.".
Убедиться, что текст отображается на странице.'''

###############################################################################################

'''import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


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

    sleep(1)

    expected_text = "semper posuere integer et senectus justo curabitur."

    paragraphs = browser.find_elements(By.TAG_NAME, "p")

    found = any(expected_text in p.text for p in paragraphs)

    browser.switch_to.default_content()

    assert found, "Текст не найден внутри iframe"'''

##############################################################################

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


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_drag_and_drop(browser):
    browser.get("https://www.globalsqa.com/demo-site/draganddrop/")

    wait = WebDriverWait(browser, 10)

    # iframe
    iframe = wait.until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe.demo-frame")
        )
    )

    sleep(3)

    # первая фотография
    photo = wait.until(
        EC.presence_of_element_located((By.XPATH, "//ul[@id='gallery']/li[1]"))
    )

    # корзина
    trash = wait.until(EC.presence_of_element_located((By.ID, "trash")))

    sleep(3)

    # проверяем
    photos_in_trash = browser.find_elements(By.CSS_SELECTOR, "#trash ul li")
    photos_in_gallery = browser.find_elements(By.CSS_SELECTOR, "#gallery li")

    assert len(photos_in_trash) == 1, "В корзине должно быть 1 фото"
    assert len(photos_in_gallery) == 3, "В галерее должно остаться 3 фото"