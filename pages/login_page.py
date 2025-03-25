from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage, LoginPageLocators):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_FIELD)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_FIELD)
        password_input.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_FIELD)
        confirm_password.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "no login in link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
