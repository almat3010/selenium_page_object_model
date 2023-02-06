from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.click(*ProductPageLocators.BUTTON_ADD_BASKET)
        self.solve_quiz_and_get_code()

    def should_be_add_in_basket(self):
        msg_add_to_basket = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG)
        title_of_book = self.browser.find_element(*ProductPageLocators.TITLE_OF_BOOK)
        assert msg_add_to_basket.text == title_of_book.text, "title is not same"

    def should_be_same_price(self):
        msg_price_of_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET)
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        assert msg_price_of_basket.text == price_of_book.text, "price is not same"

    def should_be_disappearing_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MSG), "success message is not disappear"
    
    def should_not_be_success_message_after_adding_in_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG)

    def should_not_be_success_message_without_adding_in_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG)