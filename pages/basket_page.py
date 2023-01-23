from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def shoud_not_be_goods_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_THE_BASKET), "Items to buy in the basket message should not be presented, but it is"
     
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "No empty basket message present"
