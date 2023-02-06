from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ALERT_INNER = (By.CSS_SELECTOR, "div.alertinner>strong")
    TITLE_OF_BOOK = (By.CSS_SELECTOR, "h1")
    PRICE_OF_BASKET = (By.CSS_SELECTOR, "div.alertinner>p>strong")
    PRICE_OF_BOOK = (By.CSS_SELECTOR, "div.product_main>p.price_color")