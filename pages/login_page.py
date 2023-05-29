from .base_page import BasePage
from .locators import LoginPageLocator

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocator.INPUT_EMAIL)
        email_input.send_keys(email)
        input_pass = self.browser.find_element(*LoginPageLocator.INPUT_PASSWORD)
        input_pass.send_keys(password)
        input_confirm = self.browser.find_element(*LoginPageLocator.INPUT_PASSWORD_CONFIRM)
        input_confirm.send_keys(password)
        self.browser.find_element(*LoginPageLocator.BUTTON_REGISTER).click()
