from selenium.webdriver.common.by import By


class PowerMeterLocators(object):
    """A class for Power Dashboard page locators. All Power Dashboard locators should come here"""
    CURRENT_POWER = (By.XPATH, "//*[contains(@name,'CurrentOperatingText')]/child::*[position()=1]")
    MIN_POWER = (By.XPATH, "//*[contains(@name,'MinOperatingElement')]/child::*[position()=2]/child::*[position()=1]")
    AVG_POWER = (By.XPATH, "//*[contains(@name,'AvgOperatingElement')]/child::*[position()=2]/child::*[position()=1]")
    MAX_POWER = (By.XPATH, "//*[contains(@name,'MaxOperatingElement')]/child::*[position()=2]/child::*[position()=1]")
    CONSUMPTION_SUM = (By.XPATH, "//*[contains(@name,'VerbrauchCard')]/child::*[position()=4]/child::*[position()=1]")
    CONSUMPTION_CURRENCY = (By.XPATH, "//*[contains(@name,'VerbrauchCard')]/child::*[position()=6]")
    CONSUMPTION_READINGS = (By.XPATH, "//*[contains(@name,'VerbrauchCard')]/child::*[position()=7]/child::*[position()=1]")
    FEED_SUM = (By.XPATH, "//*[contains(@name,'EinspeisungCard')]/child::*[position()=4]/child::*[position()=1]")
    FEED_CURRENCY = (By.XPATH, "//*[contains(@name,'EinspeisungCard')]/child::*[position()=6]")
    FEED_READINGS = (By.XPATH, "//*[contains(@name,'EinspeisungCard')]/child::*[position()=7]/child::*[position()=1]")
    GENERATION_SUM = (By.XPATH, "//*[contains(@name,'ProduktionCard')]/child::*[position()=4]/child::*[position()=1]")
    GENERATION_CURRENCY = (By.XPATH, "//*[contains(@name,'ProduktionCard')]/child::*[position()=5]")
    GENERATION_READINGS = (By.XPATH, "//*[contains(@name,'ProduktionCard')]/child::*[position()=5]/child::*[position()=1]")


class HomePageLocators(object):
    """A class for Start page locators. All Start page locators should come here"""
    USER_ICON = (By.XPATH, "//*[contains(@name,'user')]")
    CURRENT_DATE = "//*[@name = '{date}']"
    NAV_BAR = (By.XPATH, "//*[contains(@name,'Start')]")
    DEVICE_PROSUMER = (By.XPATH, "//*[contains(@name,'prosumer')]")
    DEVICE_GENERATOR = (By.XPATH, "//*[contains(@name,'generator')]")
    DEVICE_POWER_GROUP = (By.XPATH, "//*[contains(@name,'Alle Strom')]")
    SPINNER = (By.XPATH, "//*[contains(@name,'LoaderPopup')]")
    ANALYTICS_TAB = (By.XPATH, "//*[contains(@name,'Analytik')]")
    DEVICE_PICKER = (By.XPATH, "//*[contains(@name,'chevron-down')]")
    BUDGET_TAB = (By.XPATH, "//*[contains(@name,'Abschlag')]")


class AnalyticsPageLocators(object):
    """A class for Start page locators. All Start page locators should come here"""
    DATE_PICKER = (By.XPATH, "//*[contains(@name,'AnalyticDateLabel')]/child::*[position()=1]")
    DEVICE_PICKER = (By.XPATH, "//*[contains(@resource-id,'')]/")
    CALENDAR_DAY_TAB = (By.XPATH, "//*[contains(@name,'DateTypeSelectionBar')]/child::*[position()=1]/child::*[position()=2]")
    DAY = "//*[contains(@name,'DateTypeSelectionBar')]/following-sibling::*[position()=4]/child::*[@name='{day}']"
    SAVE_BUTTON = (By.XPATH, "//*[contains(@name,'OK')]")
    PREVIOUS_MONTH = (By.XPATH, "//*[contains(@name,'Zurück')]")
    FIRST_TILE = (By.XPATH, "//*[contains(@name,'AnalyticLeftCard')]/child::*[position()=2]/child::*[position()=1]")
    SECOND_TILE = (By.XPATH, "//*[contains(@name,'AnalyticMiddleCard')]/child::*[position()=2]/child::*[position()=1]")
    THIRD_TILE = (By.XPATH, "//*[contains(@name,'AnalyticRightCard')]/child::*[position()=2]/child::*[position()=1]")


class RegisterPageLocators(object):
    """A class for Bot page locators. All Start page locators should come here"""
    USERNAME_FIELD = (By.XPATH, "//*[contains(@type,'XCUIElementTypeTextField')]")
    PASSWORD_FIELD = (By.XPATH, "//*[contains(@type,'XCUIElementTypeSecureTextField')]")
    REGISTER_BUTTON = (By.XPATH, "//*[contains(@name,'Jetzt registrieren')]")
    LOGIN_BUTTON = (By.XPATH, "//*[contains(@name,'Anmelden')]")
    ERROR_MESSAGE = "//*[@name = '{error}']"
    TERMS_CHECKBOX = (By.XPATH, "//*[contains(@name, 'Ausblenden')]/following-sibling::*[position()=1]")
    POP_UP_TITLE = (By.XPATH, "//*[contains(@name,'Registrierung bestätigen')]")


class LoginPageLocators(object):
    """A class for Bot page locators. All Login page locators should come here"""
    #USERNAME_FIELD = (By.XPATH, "//*[contains(@resource-id,'Username')]")
    #PASSWORD_FIELD = (By.XPATH, "//*[contains(@resource-id,'Password')]")
    #LOGIN_BUTTON = (By.CLASS_NAME, "android.widget.Button")
    USERNAME_FIELD = (By.XPATH, "//*[contains(@name, 'E-Mail')]/following-sibling::*[position()=2]")
    PASSWORD_FIELD = (By.XPATH, "//*[contains(@name,'Passwort')]/following-sibling::*[position()=2]")
    LOGIN_BUTTON = (By.XPATH, "//*[contains(@name,'Hier Anmelden')]")
    ERROR_MESSAGE = "//*[@name = '{name}']"
    HIDE_KEYBOARD_BUTTON = (By.XPATH, "//*[contains(@name,'eye')]/following-sibling::*[position()=2]")
    SKIP_BUTTON = (By.XPATH, "//*[contains(@name,'Überspringen')]")
    SKIP_ACTIVATION_BUTTON = (By.XPATH, "//*[contains(@name,'Jetzt aktivieren')]/following-sibling::*[position()=1]")


class ProfilePageLocators(object):
    """A class for Bot page locators. All Profile page locators should come here"""
    LOG_OUT_ITEM = (By.XPATH, "//*[contains(@name,'Abmelden')]")
    GEAR_ICON = (By.XPATH, "//*[contains(@name,'settings')]")
    HOUSE_ITEM = (By.XPATH, "//*[contains(@name,'Haushalt')]")
    HOUSE_ITEM_INFO = (By.XPATH, "//*[contains(@name,'Haushalt')]/following-sibling::*[position()=1]")
    TARIFF_ITEM = (By.XPATH, "//*[contains(@name,'Tarife')]")


class ProfileSettingsPageLocators(object):
    """A class for Bot page locators. All Edit Profile page locators should come here"""
    RESET_PASSWORD_ITEM = (By.XPATH, "//*[contains(@name,'Passwort ändern')]")
    BACK_BUTTON = (By.XPATH, "//*[contains(@name,'Arrow-left')]")


class ResetPasswordLocators(object):
    """A class for Bot page locators. All Reset password locators should come here"""
    TITLE = "//*[@name = '{title}']"
    INPUT_FIELD = (By.XPATH, "//*[contains(@type, 'XCUIElementTypeSecureTextField')]")
    SAVE_BUTTON = (By.XPATH, "//*[contains(@name,'Speichern')]")


class BenchmarkPageLocators(object):
    """A class for Bot page locators. All Benchmark locators should come here"""
    MENU_ITEM = (By.XPATH, "//*[contains(@name,'Haustyp')]/following-sibling::*[position()=1]")
    TYPE_OF_LIVING_OPTION = (By.XPATH, "//*[contains(@type,'XCUIElementTypeCollectionView')]/child::*[position()=5]/child::*[position()=1]")
    SPACE_INPUT_FIELD = (By.XPATH, "//*[contains(@type,'XCUIElementTypeTextField')]")
    SAVE_BUTTON = (By.XPATH, "//*[contains(@name,'Speichern')]")
    CLOSE_POP_UP = (By.XPATH, "//*[contains(@name,'OK')]")


class DevicePageLocators(object):
    """A class for Bot page locators. All Device locators should come here"""
    ADD_DEVICE_ITEM = (By.XPATH, "//*[contains(@text,'+')]")


class BudgetPageLocators(object):
    """A class for Budget page locators. All DBudget locators should come here"""
    PREPAYMENT = (By.XPATH, "//*[contains(@name,'Monatsabschlag')]/parent::*[position()=1]/following-sibling::*[position()=2]/child::*[position()=1]")
    CONSUMPTION = (By.XPATH, "//*[contains(@name,'Monatskosten')]/parent::*[position()=1]/following-sibling::*[position()=2]/child::*[position()=1]")
    PERCENTAGE = (By.XPATH, "//*[contains(@name,'+/-')]/parent::*[position()=1]/following-sibling::*[position()=2]/child::*[position()=1]")
    DATE_PICKER = "//*[@name = '{month}']"
    PREV_MONTH = (By.XPATH, "//*[contains(@name,'DateTypeSelectionBar')]/following-sibling::*[position()=1]/child::*[position()=1]")
    CLOSE_CALENDAR = (By.XPATH, "//*[contains(@name,'OK')]")


class TariffPageLocators(object):
    """A class for Budget page locators. All DBudget locators should come here"""
    NEW_TARIFF_BUTTON = (By.XPATH, "//*[contains(@name,'Neuen Tarif')]")
    VENDOR_NAME_INPUT = (By.XPATH, "//*[contains(@name,'Anbietername')]/following-sibling::*[position()=1]")
    TARIFF_NAME_INPUT = (By.XPATH, "//*[contains(@name,'Tarifbezeichnung')]/following-sibling::*[position()=1]")
    BASIC_PRICE_INPUT = (By.XPATH, "//*[contains(@name,'Basispreis')]/following-sibling::*[position()=2]")
    WORKING_PRICE_INPUT = (By.XPATH, "//*[contains(@name,'Arbeitspreis')]/following-sibling::*[position()=2]")
    PREPAYMENT_INPUT = (By.XPATH, "//*[contains(@name,'Abschlag')]/following-sibling::*[position()=2]")
    NEXT_BUTTON = (By.XPATH, "//*[contains(@name,'Abbrechen')]/following-sibling::*[position()=1]")
    CALENDAR = (By.XPATH, "//*[contains(@name,'Datumsauswahl')]")
    PREV_MONTH_BUTTON = (By.XPATH, "//*[contains(@name,'Vorheriger Monat')]")
    SELECT_DAY = "//*[contains(@name,'1. {month}')]"
    CREATE_TARIFF_BUTTON = (By.XPATH, "//*[contains(@name,'Tarif speichern')]")
    CLOSE_POP_UP = (By.XPATH, "//*[contains(@name,'OK')]")
    DEVICE_PICKER = (By.XPATH, "//*[contains(@name,'Gerät')]/following-sibling::*[position()=1]")
    PROSUMER_DEVICE = (By.XPATH, "//*[contains(@name,'prosumer')]")
    VENDOR_NAME = (By.XPATH, "//*[contains(@name,'prosumer')]/following-sibling::*[position()=3]")
    TARIFF_NAME = (By.XPATH, "//*[contains(@name,'prosumer')]/following-sibling::*[position()=4]")
    TARIFF_START_DATE = (By.XPATH, "//*[contains(@name,'prosumer')]/following-sibling::*[position()=5]")
    BASIC_PRICE = (By.XPATH, "//*[contains(@name,'prosumer')]/following-sibling::*[position()=9]")
    WORKING_PRICE = (By.XPATH, "//*[contains(@name,'prosumer')]/following-sibling::*[position()=10]")
    PREPAYMENT = (By.XPATH, "//*[contains(@name,'prosumer')]/following-sibling::*[position()=15]")
    SETTINGS_ICON = (By.XPATH, "//*[contains(@name,'settings')]")
    DELETE_BUTTON = (By.XPATH, "//*[contains(@name,'Löschen')]")
    YES_BUTTON = (By.XPATH, "//*[contains(@name,'Ja')]")
    CLOSE_CALENDAR = (By.XPATH, "//*[contains(@name,'PopoverDismissRegion')]")
