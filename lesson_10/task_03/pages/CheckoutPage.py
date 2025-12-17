import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа (Checkout).

    Attributes:
        driver: webdriver
        wait: WebDriverWait
    """
    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        Args:
            driver (webdriver): экземпляр браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнение формы на странице Checkout: {first} {last}, {zip_code}")
    def fill_form(self, first: str, last: str, zip_code: str) -> None:
        """
        Заполняет форму пользователя и нажимает кнопку Continue.

        Args:
            first (str): имя
            last (str): фамилия
            zip_code (str): почтовый индекс
        """
        self.wait.until(EC.presence_of_element_located(self.FIRST)).send_keys(first)
        self.driver.find_element(*self.LAST).send_keys(last)
        self.driver.find_element(*self.ZIP).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE_BTN).click()

    @allure.step("Получение общей суммы заказа")
    def get_total(self) -> str:
        """
        Получает общую сумму заказа на странице Checkout.

        Returns:
            str: сумма заказа без текста "Total: $"
        """
        total_text = self.wait.until(
            EC.presence_of_element_located(self.TOTAL)
        ).text
        return total_text.replace("Total: $", "")
