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

waiter = WebDriverWait(driver, 5)
driver.get('http://uitestingplayground.com/textinput')

driver.find_element(By.CSS_SELECTOR, '#newButtonName').send_keys('SkyPro')
driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#updatingButton'), 'SkyPro')
)
text_message = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

print(text_message)

driver.quit()
