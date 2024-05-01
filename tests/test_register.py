import pytest
from helpers.common_steps import reset_app
from api.api_validate_profile import validate_profile
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.register_page import RegisterPage
from pages.home_page import HomePage
from helpers.config_env import config_env
from helpers.config_importer import ConfigImporter
from helpers.data_generator import GenerateUserData
from helpers.error_message import error_message
from helpers.success_message import success_message
from helpers.config_env import config_env


# Global variable
pytest.login = None
pytest.password = None


class TestRegister:
    # Setting up the initialization
    def init(self, driver):
        self.driver = driver
        self.config_env = config_env()
        self.config_importer = ConfigImporter()
        self.register_page = RegisterPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.error = error_message()
        self.success = success_message()
        self.faker = GenerateUserData()
        self.login = self.config_env['login']

    # Mark test as a "register_negative" to run marked tests in the future
    @pytest.mark.register_negative
    def test_register_username_empty(self, driver):
        # Initialization
        self.init(driver)

        # The user log out
        if self.home_page.user_is_log_in():
            self.home_page.wait_until_spinner_will_be_invisible()
            self.home_page.click_user_icon()
            self.home_page.wait_until_spinner_will_be_invisible()
            self.profile_page.click_log_out_item()

        # The user accept Terms and Conditions
        self.register_page.accept_terms()

        # The user click Register button
        self.register_page.click_register_button()

        # The User see 'username is empty' error message
        assert self.login_page.error_message_is_visible(self.error['error_message'])


    # Mark test as a "register_negative" to run marked tests in the future
    @pytest.mark.register_negative
    def test_register_password_empty(self, driver):
        # Initialization
        reset_app(driver)
        self.init(driver)

        # The user enter username
        self.register_page.enter_username(self.config_importer.config_username_invalid())

        # The user accept Terms and Conditions
        self.register_page.accept_terms()

        # The user click Register button
        self.register_page.click_register_button()

        # The User see 'username is empty' error message
        assert self.login_page.error_message_is_visible(self.error['error_message'])

    # Mark test as a "register_negative" to run marked tests in the future
    @pytest.mark.register_negative
    def test_register_username_incorrect(self, driver):
        # Initialization
        reset_app(driver)
        self.init(driver)

        # The user enter incorrect username
        self.register_page.enter_username(self.config_importer.config_username_incorrect())
        
        # The user accept Terms and Conditions
        self.register_page.accept_terms()

        # The user click Register button
        self.register_page.click_register_button()

        # The User see 'username is empty' error message
        assert self.login_page.error_message_is_visible(self.error['username_incorrect'])

    # Mark test as a "register_negative" to run marked tests in the future
    @pytest.mark.register_negative
    def test_register_password_short(self, driver):
        # Initialization
        reset_app(driver)
        self.init(driver)

        # The user enter username already exists
        self.register_page.enter_username(self.config_importer.config_username_invalid())

        # The user enter username already exists
        self.register_page.enter_password(self.config_importer.config_user_password_short())
        
        # The user accept Terms and Conditions
        self.register_page.accept_terms()

        # The user click Register button
        self.register_page.click_register_button()

        # The User see 'username is empty' error message
        assert self.login_page.error_message_is_visible(self.error['short_password'])

    """
    # Mark test as a "register_negative" to run marked tests in the future
    @pytest.mark.register_negative
    def test_register_username_exists(self, driver):
        # Initialization
        reset_app(driver)
        self.init(driver)

        # The user enter username already exists
        self.register_page.enter_username(self.login)

        # The user enter password
        self.register_page.enter_password(self.config_importer.config_user_password_invalid())
        
        # The user accept Terms and Conditions
        self.register_page.accept_terms()

        # The user click Register button
        self.register_page.click_register_button()
        time.sleep(2)

        # The User see 'username is empty' error message
        assert self.register_page.pop_up_is_visible(self.error['user_exists_pop_up_title'])
        time.sleep(2)
    """
    # Mark test as a "register_positive" to run marked tests in the future
    @pytest.mark.register_positive
    def test_register(self, driver):
        # Initialization
        reset_app(driver)
        self.init(driver)
        pytest.login = self.faker.email()
        pytest.password = self.faker.password()

        # The user enter username
        self.register_page.enter_username(pytest.login)

        # The user enter password
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

        # The User see the bottom navigation bar
        assert self.home_page.bottom_navigation_bar_is_visible()

