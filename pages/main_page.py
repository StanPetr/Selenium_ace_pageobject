from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_basket(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_LINK)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
