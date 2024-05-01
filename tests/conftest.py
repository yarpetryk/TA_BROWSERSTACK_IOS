import pytest
from appium import webdriver
from helpers.config_importer import ConfigImporter


config_importer = ConfigImporter()

@pytest.fixture(scope="function")
def driver():
    locale = str(config_importer.config_locale())
    language = str(config_importer.config_language())
    capabilities = {
        'language': language,
        'locale': locale,
    }
    url = 'https://hub-cloud.browserstack.com/wd/hub'
    appium_driver = webdriver.Remote(url, capabilities)

    yield appium_driver
    appium_driver.quit()

