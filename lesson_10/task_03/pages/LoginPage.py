import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Класс для работы со страницей авторизации (Login).

    Attributes:
        driver: webdriver
        wait: WebDriverWait
    """
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver):
        """
        Инициализация страницы Login.

        Args:
            driver (webdriver): экземпляр браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы логина")
    def open(self) -> None:
        """
        Открывает страницу логина.
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Вход на сайт с логином: {username}")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход на сайт.

        Args:
            username (str): имя пользователя
            password (str): пароль пользователя
        """
        self.wait.until(EC.presence_of_element_located(self.USERNAME)).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()
