import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from pages.locators import HomePageLocators
from pages.base_pages import BasePage


class HomePage(BasePage):
    """Description """
    @allure.step("And user click on the user icon")
    def click_user_icon(self):
        self.find_element_and_click(HomePageLocators.USER_ICON)

    @allure.step("And user see current date")
    def date_is_visible(self, date):
        self.is_element_enabled((By.XPATH, HomePageLocators.CURRENT_DATE.format(date=date)))
        return True

    @allure.step("And user see navigation bar")
    def bottom_navigation_bar_is_visible(self):
        self.is_element_enabled(HomePageLocators.NAV_BAR)
        return True

    @allure.step("And user select prosumer device")
    def select_prosumer_device(self):
        self.find_element_and_click(HomePageLocators.DEVICE_PROSUMER)

    @allure.step("And user select generator device")
    def select_generator_device(self):
        self.find_element_and_click(HomePageLocators.DEVICE_PICKER)
        self.find_element_and_click(HomePageLocators.DEVICE_GENERATOR)

    @allure.step("And user select power group")
    def select_power_group(self):
        self.find_element_and_click(HomePageLocators.DEVICE_POWER_GROUP)

    @allure.step("And user wait the spinner finished")
    def wait_until_spinner_will_be_invisible(self):
        self.wait_until_element_will_be_invisible(HomePageLocators.SPINNER)

    @allure.step("And user is log in")
    def user_is_log_in(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(HomePageLocators.USER_ICON))
        except TimeoutException:
            return False
        else:
            return True

    @allure.step("And user select the Analytics tab")
    def select_analytics_tab(self):
        self.find_element_and_click(HomePageLocators.ANALYTICS_TAB)


    @allure.step("And user select the Budget tab")
    def select_budget_tab(self):
        self.find_element_and_click(HomePageLocators.BUDGET_TAB)
