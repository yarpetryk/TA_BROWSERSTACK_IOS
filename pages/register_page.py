import allure
from pages.locators import RegisterPageLocators
from pages.base_pages import BasePage


class RegisterPage(BasePage):
    """Description """
    @allure.step("And user click register button")
    def click_register_button(self):
        self.find_element_and_click(RegisterPageLocators.REGISTER_BUTTON)

    @allure.step("And user enter username")
    def enter_username(self, text):
        el = self.find_all_elements(RegisterPageLocators.USERNAME_FIELD)[0]
        el.clear() and el.send_keys(text)

    @allure.step("And user enter password")
    def enter_password(self, text):
        el = self.find_all_elements(RegisterPageLocators.PASSWORD_FIELD)[0]
        el.clear() and el.send_keys(text)

    @allure.step("And user click login button")
    def click_login_button(self):
        self.find_element_and_click(RegisterPageLocators.LOGIN_BUTTON)

    @allure.step("And user see pop up")
    def pop_up_is_visible(self, message):
        el = self.find_element(RegisterPageLocators.POP_UP_TITLE)
        if el.text == message:
            return True

    @allure.step("And user see error pop up")
    def error_message_is_visible(self, error_message):
        el = self.find_element(RegisterPageLocators.ERROR_MESSAGE)
        if el.text == error_message:
            return True

    @allure.step("And user accept Terms and Conditions")
    def accept_terms(self):
        self.find_element_and_click(RegisterPageLocators.TERMS_CHECKBOX)

