import pytest
import allure
from selenium import webdriver

from CalcPage import CalcPage


@pytest.fixture
def driver():
    """
    Фикстура: создание и закрытие драйвера Firefox.

    :return: WebDriver — экземпляр браузера Firefox.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


@allure.title("Проверка сложения 7 + 8 в Slow Calculator")
@allure.description("""
Тест проверяет корректность работы 'slow calculator':
1. Открываем страницу.
2. Устанавливаем задержку вычисления.
3. Вводим выражение 7 + 8.
4. Ожидаем появления результата.
5. Проверяем, что результат равен 15.
""")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calc_sum(driver):
    """
    Тест выполнения суммирования 7 + 8 с задержкой отображения результата.
    """
    page = CalcPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        page.open()

    with allure.step("Устанавливаем задержку вычисления: 45 секунд"):
        page.set_delay(45)

    with allure.step("Вводим выражение 7 + 8"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Ожидаем появления результата '15'"):
        result = page.wait_for_result("15")

    with allure.step("Проверяем корректность результата"):
        assert result == "15", f"Ожидалось значение '15', получено '{result}'"
