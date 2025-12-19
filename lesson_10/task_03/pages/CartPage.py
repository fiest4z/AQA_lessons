from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """
    PageObject для страницы корзины интернет-магазина.
    Содержит методы для перехода к оформлению заказа.
    """

    CHECKOUT_BTN = (By.ID, "checkout")

    def __init__(self, driver: WebDriver):
        """
        Инициализация объекта страницы.

        :param driver: WebDriver — экземпляр браузера.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self) -> None:
        """
        Нажимает кнопку 'Checkout' для перехода к оформлению заказа.

        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BTN)
        ).click()
