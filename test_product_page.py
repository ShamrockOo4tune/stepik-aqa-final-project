from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser=browser, url=link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
