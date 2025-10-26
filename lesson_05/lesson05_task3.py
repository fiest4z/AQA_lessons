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
driver.get('http://the-internet.herokuapp.com/inputs')
search_item = 'input'
search_input = driver.find_element(By.CSS_SELECTOR, search_item)
search_input.send_keys("Sky")
sleep(1)
search_input.clear()
search_input.send_keys("Pro")

sleep(3)
driver.quit()
