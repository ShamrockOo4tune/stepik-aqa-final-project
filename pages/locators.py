from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "article.product_page h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "article.product_page p.price_color")
    HAS_BEEN_ADDED_TO_YOUR_BASKET = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) > .alertinner > strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) > .alertinner")
    