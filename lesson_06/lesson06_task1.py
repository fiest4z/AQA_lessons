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

waiter = WebDriverWait(driver, 20, 1)
driver.get('http://uitestingplayground.com/ajax')
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
content = driver.find_element(By.CSS_SELECTOR, "#content")

text_message = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success")))

print(text_message.text)

driver.quit()
