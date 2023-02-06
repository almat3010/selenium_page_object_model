from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.click(*ProductPageLocators.BUTTON_ADD_BASKET)
        #solve = self.solve_quiz_and_get_code()

    def should_be_add_in_basket(self):
        msg_add_to_basket = self.browser.find_element(*ProductPageLocators.ALERT_INNER)
        title_of_book = self.browser.find_element(*ProductPageLocators.TITLE_OF_BOOK)
        print(msg_add_to_basket.text)
        print(title_of_book.text)
        assert msg_add_to_basket.text == title_of_book.text, "title is not same"

    def should_be_same_price(self):
        msg_price_of_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET)
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        assert msg_price_of_basket.text == price_of_book.text, "price is not same"