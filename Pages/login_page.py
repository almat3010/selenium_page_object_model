from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "registration form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_REGISTRATION)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_REGISTRATION)
        password_input.send_keys(password)
        repeatPassword = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT_REGISTRATION)
        repeatPassword.send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit.click()
        assert self.is_element_present(*LoginPageLocators.CONFIRM_REGISTRATION), "registration failed"