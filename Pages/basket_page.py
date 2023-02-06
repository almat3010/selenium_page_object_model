from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_not_be_item_in_basket(self):
       assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "items present"
    def should_be_msg_about_empty_items(self):
        assert self.is_element_present(*BasketPageLocators.MSG_EMPTY_BASKET), "msg is not present"
        