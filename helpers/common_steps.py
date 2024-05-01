import time
from helpers.config_importer import ConfigImporter


def uninstall_app(driver):
    config_importer = ConfigImporter()
    driver.remove_app(str(config_importer.config_package_name()))


def terminate_app(driver):
    config_importer = ConfigImporter()
    driver.terminate_app(str(config_importer.config_package_name()))


def reset_app(driver):
    driver.reset()


def is_installed(driver):
    config_importer = ConfigImporter()
    return driver.is_app_installed(str(config_importer.config_package_name()))


def activate_app(driver):
    config_importer = ConfigImporter()
    driver.activate_app(str(config_importer.config_package_name()))
    time.sleep(2)


def open_notification(driver):
    driver.open_notifications()
