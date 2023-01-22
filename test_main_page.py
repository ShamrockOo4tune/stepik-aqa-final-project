from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser=browser, url=link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser=browser, url="http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
    login_page.should_be_login_page()
    