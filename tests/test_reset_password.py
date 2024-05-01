import pytest
from api.api_validate_profile import validate_profile
from helpers.common_steps import reset_app
from helpers.config_importer import ConfigImporter
from helpers.data_generator import GenerateUserData
from helpers.error_message import error_message
from helpers.success_message import success_message
from pages.home_page import HomePage
from pages.benchmark_page import BenchmarkPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.profile_settings_page import ProfileSettingsPage
from pages.reset_password_page import ResetPasswordPage
from tests.test_login_and_select_prosumer_device import test_login


# Global variable
pytest.login = None
pytest.password = None


class TestResetPassword:
    # Setting up the initialization
    def init(self, driver):
        self.driver = driver
        self.config_importer = ConfigImporter()
        self.home_page = HomePage(self.driver)
        self.register_page = RegisterPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.benchmark_page = BenchmarkPage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.profile_settings_page = ProfileSettingsPage(self.driver)
        self.reset_password_page = ResetPasswordPage(self.driver)
        self.faker = GenerateUserData()
        self.error = error_message()
        self.success = success_message()


    # Mark test as a "register_positive" to run marked tests in the future
    @pytest.mark.register_positive
    def test_register(self, driver):
        # Initialization
        self.init(driver)
        pytest.login = self.faker.email()
        pytest.password = self.faker.password()

        # The user log out
        if self.home_page.user_is_log_in():
            self.home_page.wait_until_spinner_will_be_invisible()
            self.home_page.click_user_icon()
            self.home_page.wait_until_spinner_will_be_invisible()
            self.profile_page.click_log_out_item()

        # The user enter username
        self.register_page.enter_username(pytest.login)

        # The user enter username already exists
        self.register_page.enter_password(pytest.password)

        # The user accept Terms and Conditions
        self.register_page.accept_terms()

        # The user click Register button
        self.register_page.click_register_button()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User see confirmation pop-up
        assert self.register_page.pop_up_is_visible(self.success['user_registered_pop_up_title'])

        # The User validate account
        validate_profile(pytest.login, pytest.password)


    # Mark test as a "register_login" to run marked tests in the future
    @pytest.mark.register_login
    def test_login(self, driver):
        # Initialization
        reset_app(driver)
        self.init(driver)

        # The User click on Login button
        self.register_page.click_login_button()

        # The User enter username
        self.login_page.enter_username(pytest.login)

        # The User enter password
        self.login_page.enter_password(pytest.password)

        # The user hide keyboard
        self.login_page.hide_keyboard()

        # The User click on Login button
        self.login_page.click_login_button()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User see the bottom navigation bar
        assert self.home_page.bottom_navigation_bar_is_visible()


    # Mark test as a "reset_password" to run marked tests in the future
    @pytest.mark.reset_password
    def test_reset_password_title(self, driver):
        # Initialization
        self.init(driver)

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The User click on User icon
        self.home_page.click_user_icon()

        # The User click on Gear icon
        self.profile_page.click_gear_icon()

        # The user swipe down
        #swipe_down(self.driver)

        # The User click on reset password item
        self.profile_settings_page.click_reset_password_item()

        # The user see "reset password" pop up
        assert self.reset_password_page.title_is_visible(self.success['reset_password_pop_up_title'])


    @pytest.mark.reset_password_negative
    def test_password_empty_input(self, driver):
        # Initialization
        self.init(driver)

        # The User click on save button
        self.reset_password_page.click_save_button()

        # The User see error message
        assert self.login_page.error_message_is_visible(self.error['error_message'])


    @pytest.mark.reset_password_negative
    def test_password_is_short(self, driver):
        # Initialization
        self.init(driver)

        # The user enter short password
        self.reset_password_page.enter_new_password(self.config_importer.config_user_password_short())

        # The user enter short password again
        self.reset_password_page.enter_new_password_again(self.config_importer.config_user_password_short())

        # The User click on save button
        self.reset_password_page.click_save_button()

        # The User see error message
        assert self.login_page.error_message_is_visible(self.error['short_password'])

    @pytest.mark.reset_password_negative
    def test_password_no_match(self, driver):
        # Initialization
        self.init(driver)

        # The user enter password
        self.reset_password_page.enter_new_password(self.config_importer.config_user_password_invalid())

        # The user enter short password again
        self.reset_password_page.enter_new_password_again(self.config_importer.config_user_password_no_match())

        # The User click on save button
        self.reset_password_page.click_save_button()

        # The User see error message
        assert self.login_page.error_message_is_visible(self.error['no_match_password'])

    @pytest.mark.reset_password_positive
    def test_password_positive(self, driver):
        # Initialization
        self.init(driver)
        pytest.password = self.faker.password()

        # The user enter password
        self.reset_password_page.enter_new_password(pytest.password)

        # The user enter short password again
        self.reset_password_page.enter_new_password_again(pytest.password)

        # The User click on save button
        self.reset_password_page.click_save_button()

        # The user wait when spinner is finished
        self.home_page.wait_until_spinner_will_be_invisible()

        # The user click on "OK" button
        self.benchmark_page.close_pop_up()

        # The user login with new password
        self.test_login(driver)
