from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def should_not_be_any_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
        "Basket should be empty, but it is not"

    def shoold_be_message_basket_is_empty_language_ru(self):
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY)
        assert message.text == "Продолжить покупки", "Text about empty basket is not presented, but should be"
