import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """
    Класс для работы со страницей списка товаров (Inventory).

    Attributes:
        driver: webdriver
        wait: WebDriverWait
    """

    def __init__(self, driver):
        """
        Инициализация страницы Inventory.

        Args:
            driver (webdriver): экземпляр браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавление товара в корзину: {item_name}")
    def add_to_cart(self, item_name: str) -> None:
        """
        Добавляет товар в корзину по его названию.

        Args:
            item_name (str): название товара
        """
        item_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
            )
        )
        item_btn.click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Нажимает на иконку корзины и переходит на страницу Cart.
        """
        cart_icon = self.wait.until(
            EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
        )
        cart_icon.click()
