from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_01_form():
    options = Options()

    driver = webdriver.Edge(
        service=Service(r"C:\Users\Михаил\PycharmProjects\edgedriver\msedgedriver.exe"),
        options=options,
    )
    wait = WebDriverWait(driver, 5)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").send_keys(
        Keys.RETURN
    )

    assert "alert-danger" in driver.find_element(By.ID, "zip-code").get_attribute(
        "class"
    )

    green_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]
    for field_id in green_fields:
        assert "alert-success" in driver.find_element(By.ID, field_id).get_attribute(
            "class"
        )

    driver.quit()
