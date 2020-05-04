import time

def test_is_element_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)
    browser.implicitly_wait(10)
    assert len(browser.find_elements_by_xpath
               ("//form[@id='add_to_basket_form']//button[@type='submit']")) == 1, "Корзина не найдена"
