from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage, BasketPageLocators):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def guest_should_see_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Basket is not empty"

    def guest_should_see_basket_not_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Basket is not empty"

    def guest_should_see_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HAS_ITEMS), \
            "Basket is empty"

    def guest_should_see_no_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_HAS_ITEMS), \
            "Basket is empty"
