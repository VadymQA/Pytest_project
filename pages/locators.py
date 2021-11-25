from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, ".js-menu-setting")
    # LOGIN_LINK2 = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    TITLE_OF_PRODUCT_AFTER_ADDING_TO_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_MSG = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
