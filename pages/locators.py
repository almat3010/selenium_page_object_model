from selenium.webdriver.common.by import By

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MSG_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_INPUT_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")
    CONFIRM_REGISTRATION = (By.CSS_SELECTOR, "div#messages>div.alert-success>div.alertinner.wicon>i.icon-ok-sign")

class ProductPageLocators():
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MSG = (By.CSS_SELECTOR, "div.alertinner>strong")
    TITLE_OF_BOOK = (By.CSS_SELECTOR, "h1")
    PRICE_OF_BASKET = (By.CSS_SELECTOR, "div.alertinner>p>strong")
    PRICE_OF_BOOK = (By.CSS_SELECTOR, "div.product_main>p.price_color")

class BasePageLocators():
    BASKET_BTN = (By.CSS_SELECTOR, "div.basket-mini>span>a.btn")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")