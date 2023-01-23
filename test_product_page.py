import pytest
import random
import string
from pages.product_page import ProductPage
from pages.login_page import LoginPage
                               
def test_guest_can_add_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.product_added_with_correct_product_name(product_name=product_name)
    product_page.product_price_match_basket_total(product_price=product_price)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.product_user
class TestUserAddToBasketFromProductPage():
    link = "https://selenium1py.pythonanywhere.com/accounts/login/"
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser=browser, url=self.link)
        login_page.open()
        email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@testers.com"
        password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        login_page.register_new_user(email=email, password=password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser=browser, url=self.product_link)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser=browser, url=self.product_link)
        product_page.open()
        product_page.should_be_add_to_basket_button()
        product_name = product_page.get_product_name()
        product_price = product_page.get_product_price()
        product_page.add_to_basket()
        product_page.product_added_with_correct_product_name(product_name=product_name)
        product_page.product_price_match_basket_total(product_price=product_price)
