import allure
from selenium.webdriver.common.by import By
from pages.locators import ResetPasswordLocators
from pages.base_pages import BasePage


class ResetPasswordPage(BasePage):
    """Description """
    @allure.step("And user see 'reset password' pop up")
    def title_is_visible(self, title):
        self.is_element_enabled((By.XPATH, ResetPasswordLocators.TITLE.format(title=title)))
        return True

    @allure.step("And user click on the user icon")
    def click_save_button(self):
        self.find_element_and_click(ResetPasswordLocators.SAVE_BUTTON)

    @allure.step("And user enter new password")
    def enter_new_password(self, text):
        el = self.find_all_elements(ResetPasswordLocators.INPUT_FIELD)[0]
        el.clear() and el.send_keys(text)

    @allure.step("And user enter new password again")
    def enter_new_password_again(self, text):
        el = self.find_all_elements(ResetPasswordLocators.INPUT_FIELD)[1]
        el.clear() and el.send_keys(text)

    @allure.step("And user see success message pop up")
    def password_updated(self, success_message):
        el = self.find_element(ResetPasswordLocators.PASSWORD_UPDATED_POP_UP_TITLE)
        if el.text == success_message:
            return True
