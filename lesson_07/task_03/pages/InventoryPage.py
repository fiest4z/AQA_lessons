from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, item_name: str):
        """Добавляет товар по его названию."""
        item_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
            )
        )
        item_btn.click()

    def go_to_cart(self):
        cart_icon = self.wait.until(
            EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
        )
        cart_icon.click()
