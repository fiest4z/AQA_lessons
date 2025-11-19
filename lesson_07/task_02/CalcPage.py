from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    DELAY_INPUT = (By.ID, "delay")
    RESULT = (By.CSS_SELECTOR, "div.screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, value):
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(value))

    def click_button(self, label: str):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{label}']"))
        )
        btn.click()
    def get_result(self):
        return self.wait.until(
            EC.presence_of_element_located(self.RESULT)
        ).text

    def wait_for_result(self, expected):
        self.wait.until(EC.text_to_be_present_in_element(self.RESULT, expected))
        return self.get_result()
