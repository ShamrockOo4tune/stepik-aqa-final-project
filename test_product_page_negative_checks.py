import pytest
from pages.product_page import ProductPage
   
@pytest.mark.xfail(reason="designed to fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара 
    # Добавляем товар в корзину 
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара 
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.should_not_be_success_message()
    

@pytest.mark.xfail(reason="designed to fail")
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_disappear()
