from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first, last, zip_code):
        self.wait.until(EC.presence_of_element_located(self.FIRST)).send_keys(first)
        self.driver.find_element(*self.LAST).send_keys(last)
        self.driver.find_element(*self.ZIP).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def get_total(self):
        total_text = self.wait.until(
            EC.presence_of_element_located(self.TOTAL)
        ).text
        return total_text.replace("Total: $", "")
