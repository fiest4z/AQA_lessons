from selenium import webdriver
from CalcPage import CalcPage


def test_calc_sum():
    driver = webdriver.Firefox()
    driver.maximize_window()

    page = CalcPage(driver)
    page.open()


    page.set_delay(45)


    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.wait_for_result("15")
    assert result == "15"

    driver.quit()
