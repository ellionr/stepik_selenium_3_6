import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_page_have_adding_button(browser):
    browser.get(link)
    #time.sleep(10)
    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        is_button = True
    except NoSuchElementException:
        is_button = False

    assert is_button, 'Button is not found'
