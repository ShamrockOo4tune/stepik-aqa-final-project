import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage

@pytest.mark.login_guest
class TestLoginFromMainPage():                       
    link = "http://selenium1py.pythonanywhere.com/"
    def test_guest_can_go_to_login_page(self, browser):     
        page = MainPage(browser=browser, url=self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser=browser, url=browser.current_url)
        login_page.should_be_login_page() 

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser=browser, url=self.link)
        page.open()
        page.should_be_login_link()
        
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает главную страницу 
    # Переходит в корзину по кнопке в шапке сайта
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста 
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser=browser, url=link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser=browser, url=browser.current_url)
    basket_page.shoud_not_be_goods_in_the_basket()
    basket_page.should_be_empty_basket_message()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    # Переходит в корзину по кнопке в шапке 
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.go_to_basket()
    basket_page = BasketPage(browser=browser, url=browser.current_url)
    basket_page.shoud_not_be_goods_in_the_basket()
    basket_page.should_be_empty_basket_message()
