import pytest
import allure
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест: проверка суммы заказа на SauceDemo")
@allure.description(
    "Тест выполняет полный сценарий покупки: авторизация, добавление товаров, оформление заказа и проверка суммы")
@allure.feature("Shop Page")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_total(driver):
    with allure.step("Авторизация пользователя"):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        inventory = InventoryPage(driver)
        inventory.add_to_cart("Sauce Labs Backpack")
        inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory.add_to_cart("Sauce Labs Onesie")

    with allure.step("Переход в корзину"):
        inventory.go_to_cart()

    with allure.step("Нажатие кнопки Checkout"):
        cart = CartPage(driver)
        cart.click_checkout()

    with allure.step("Заполнение формы и продолжение"):
        checkout = CheckoutPage(driver)
        checkout.fill_form("Mikhail", "Belyaev", "12345")

    with allure.step("Получение и проверка итоговой суммы заказа"):
        total = checkout.get_total()
        assert total == "58.29", f"Ожидалось 58.29, получено {total}"
