from selenium.webdriver.common.by import By

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
class ProductPageLocators():
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SELECTED_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SELECTED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
