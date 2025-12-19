from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalcPage:
    """
    PageObject для страницы «Slow Calculator».
    Обеспечивает управление задержкой, вводом значений,
    нажатием кнопок калькулятора и получением результата.
    """

    DELAY_INPUT = (By.ID, "delay")
    RESULT = (By.CSS_SELECTOR, "div.screen")

    def __init__(self, driver: WebDriver):
        """
        Инициализация класса страницы.

        :param driver: WebDriver — экземпляр браузера.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        :return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, value: int) -> None:
        """
        Устанавливает задержку в секундах перед отображением результата.

        :param value: int — количество секунд.
        :return: None
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(value))

    def click_button(self, label: str) -> None:
        """
        Нажимает кнопку калькулятора с указанной надписью.

        :param label: str — текст кнопки, например '1', '+', '='.
        :return: None
        """
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{label}']"))
        )
        btn.click()

    def get_result(self) -> str:
        """
        Возвращает текст результата, отображённый на экране калькулятора.

        :return: str — текст результата.
        """
        return self.wait.until(
            EC.presence_of_element_located(self.RESULT)
        ).text

    def wait_for_result(self, expected: str) -> str:
        """
        Ожидает, пока на экране появится ожидаемое значение результата,
        затем возвращает фактический текст.

        :param expected: str — ожидаемое значение.
        :return: str — результат на экране после ожидания.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT, expected)
        )
        return self.get_result()
