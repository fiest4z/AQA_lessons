from time import sleep

from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

firefox_path = "/usr/lib/firefox/firefox"  # Путь к версии .deb
options = Options()
options.binary_location = firefox_path
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)
driver.get("https://the-internet.herokuapp.com/login")

username_field = driver.find_element(By.CSS_SELECTOR, "input#username")
username_field.send_keys("tomsmith")

oassword_field = driver.find_element(By.CSS_SELECTOR, "input#password")
oassword_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

flash_message = driver.find_element(By.CSS_SELECTOR, '#flash').text
print(flash_message)

sleep(5)

driver.quit()
