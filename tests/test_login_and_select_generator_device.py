import time
from helpers.config_env import config_env
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage


def test_login(driver):
    # # # # # # # # # Initialization # # # # # # # # # # # # #
    config_environment = config_env()
    register_page = RegisterPage(driver)
    home_page = HomePage(driver)
    profile_page = ProfilePage(driver)
    login_page = LoginPage(driver)
    login = config_environment['login']
    password = config_environment['password']
    # # # # # # # # # Initialization # # # # # # # # # # # # #

    # The User log out
    if home_page.user_is_log_in():
        home_page.wait_until_spinner_will_be_invisible()
        home_page.click_user_icon()
        home_page.wait_until_spinner_will_be_invisible()
        profile_page.click_log_out_item()

    # The User click on Login button
    register_page.click_login_button()

    # The User enter username
    login_page.enter_username(login)

    # The User enter password
    login_page.enter_password(password)

    # The user hide keyboard
    login_page.hide_keyboard()

    # The User click on Login button
    login_page.click_login_button()

    # The User click on Skip button
    login_page.click_skip_button()

    # The User click on Skip button
    login_page.click_skip_button()

    # The User click on Skip activation button
    login_page.click_skip_activation_button()

    # The user select device
    home_page.select_generator_device()

    # The user wait when spinner is finished
    home_page.wait_until_spinner_will_be_invisible()

    # The User see the bottom navigation bar
    assert home_page.bottom_navigation_bar_is_visible()
