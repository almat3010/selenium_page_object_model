import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def click(self, by, selector):
        element = self.browser.find_element(by,selector)
        element.click()

    def is_element_present(self, by, selector):
        try:
            self.browser.find_element(by,selector)
        except(NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, by, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by, selector)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, by, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((by, selector)))
        except TimeoutException:
            return False
        return True

    def go_to_basket(self):
        self.click(*BasePageLocators.BASKET_BTN)
        assert "basket" in self.browser.current_url

    def go_to_login_page(self):
        self.click(*BasePageLocators.LOGIN_LINK)
        assert "login" in self.browser.current_url

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

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
            return alert_text
        except NoAlertPresentException:
            print("No second alert presented")