from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    TITLE_OF_PRODUCT_AFTER_ADDING_TO_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_MSG = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

class BasketPageLocator():
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocator():
    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "#register_form > button")

