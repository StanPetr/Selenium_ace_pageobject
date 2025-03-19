import time
import pytest
from .pages.product_page import ProductPage


def test_guest_can_go_to_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()


def test_guest_can_see_promo_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_promo_code_in_url()


@pytest.mark.parametrize('promo', ["?promo=offer0", "?promo=offer1", "?promo=offer2",  "?promo=offer3", "?promo=offer4",
                                   "?promo=offer5", "?promo=offer6", "?promo=offer7", "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_be_product_name_in_confirmation()


@pytest.mark.parametrize('promo', ["?promo=offer0", "?promo=offer1", "?promo=offer2",  "?promo=offer3", "?promo=offer4",
                                   "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                   "?promo=offer8", "?promo=offer9"])
def test_guest_can_see_add_in_basket_confirmation(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_be_product_name_in_confirmation()


@pytest.mark.parametrize('promo', ["?promo=offer0", "?promo=offer1", "?promo=offer2",  "?promo=offer3", "?promo=offer4",
                                   "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                   "?promo=offer8", "?promo=offer9"])
def test_guest_should_see_right_prices_in_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_be_equal_product_price_and_basket_total()
