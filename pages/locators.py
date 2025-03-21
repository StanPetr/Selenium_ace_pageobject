from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.LINK_TEXT, "View basket")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1:nth-child(1)")
    ADD_BTN = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_IN_CONFIRMATION = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    BASKET_TOTAL = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
