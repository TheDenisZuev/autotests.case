from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_xpath("//button[@id='book']")
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x = browser.find_element_by_xpath("//span[@id='input_value']").text
    input1 = browser.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(calc(x))

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



