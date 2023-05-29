from .locators import BasketPageLocator, BasePageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def verify_basket_is_empty(self):
        text = self.browser.find_element(*BasketPageLocator.TEXT_EMPTY_BASKET).text
        print(text)
        assert text == "Your basket is empty. Continue shopping"



