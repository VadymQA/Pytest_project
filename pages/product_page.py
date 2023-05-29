from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        btn_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        btn_add_to_cart.click()

    def verify_product_that_was_added(self):
        assert self.browser.find_element(*ProductPageLocators.TITLE_OF_PRODUCT_AFTER_ADDING_TO_CART).text == "Coders at Work", "Bla-bla"

    def should_not_be_success_msg(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG) , "WARNING! Element is presented, but it shoulndn't!"

    def should_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MSG) , "WARNING! Not Dissapered!"

