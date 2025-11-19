from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

firefox_path = "/usr/lib/firefox/firefox"  # Путь к версии .deb
options = Options()
options.binary_location = firefox_path
service = FirefoxService(GeckoDriverManager().install())

driver = webdriver.Firefox(service=service, options=options)

waiter = WebDriverWait(driver, 15)
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

third_image = waiter.until(
    EC.visibility_of_element_located((By.ID, "award")))

print(third_image.get_attribute("src"))

driver.quit()
