import time

from .pages.product_page import ProductPage


def test_guest_can_go_to_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()


def test_guest_should_see_promo_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_promo_code_in_url()


def test_guest_should_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)


def test_guest_should_see_add_in_basket_confirmation(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_be_product_name_in_confirmation()


def test_guest_should_see_right_prices_in_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_be_equal_product_price_and_basket_total()
