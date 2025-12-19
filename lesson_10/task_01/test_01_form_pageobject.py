import pytest
import allure
from selenium import webdriver

from FormPage import FormPage


@pytest.fixture
def driver():
    """
    Фикстура инициализации веб-драйвера.

    :return: WebDriver — экземпляр браузера Chrome.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка отправки формы с некорректным ZIP-кодом")
@allure.description("""
Пошаговая проверка заполнения формы:
1. Открываем страницу.
2. Заполняем все поля.
3. Отправляем форму.
4. Проверяем, что ZIP-код подсвечен красным, а остальные поля — зелёным.
""")
@allure.feature("Форма ввода данных")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow(driver):
    """
    Основной тест проверки валидации формы.
    """
    form_page = FormPage(driver)

    with allure.step("Открываем страницу формы"):
        form_page.open()

    with allure.step("Заполняем поля формы"):
        form_page.fill_form()

    with allure.step("Отправляем форму"):
        form_page.submit_form()

    with allure.step("Проверяем, что ZIP-код подсвечен как ошибка"):
        assert form_page.check_zip_code_error(), "Ожидалась ошибка валидации ZIP"

    with allure.step("Проверяем, что остальные поля валидны"):
        assert form_page.check_fields_success(), "Ожидались корректные значения полей"
