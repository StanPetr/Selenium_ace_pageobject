from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage, ProductPageLocators):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def should_be_promo_code_in_url(self):  # 1.1 check promo in URL
        assert "/?promo=newYear" in self.browser.current_url, "promo code missed"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_CONFIRMATION), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_CONFIRMATION), \
            "Success message is presented, but should not be"

    def click_button_add_to_basket(self):  # 2 click button
        button = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        button.click()

    def should_be_product_name_in_confirmation(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        conf_name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_CONFIRMATION)
        print(product_name.text)
        print(conf_name.text)
        assert conf_name.text == product_name.text, "name of product hasn't found"

    def should_be_equal_product_price_and_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        print(product_price.text)
        print(basket_total.text)
        assert product_price.text == basket_total.text, "prices are not equal"
