from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import math
import time
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.click_add_to_basket_button()
        self.solve_quiz_and_get_code()
        self.selected_product_added_to_basket()
        self.basket_price_should_be_selected_product_price()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_LINK), "'Add to busket button' is not presented"

    def click_add_to_basket_button(self):
        product_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        product_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        time.sleep(7)

    def selected_product_added_to_basket(self):
        selected_product_name = self.browser.find_element(*ProductPageLocators.SELECTED_PRODUCT_NAME)
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        assert selected_product_name.text == added_product_name.text, "Название выбранного товара НЕ совпадает с названием товара в корзине"

    def basket_price_should_be_selected_product_price(self):
        selected_product_price = self.browser.find_element(*ProductPageLocators.SELECTED_PRODUCT_PRICE)
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE)
        assert added_product_price.text == selected_product_price.text, "Стоимость корзины НЕ совпадает со стоимостью выбранного товара"
