__author__ = 'tan'

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException


def loading(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")
    except WebDriverException:
        pass


def wait_loading(driver):
    WebDriverWait(driver, 30, 1).until(loading, 'AJAX')


def loading_ref(driver):
    try:
        return driver.execute_script('return document.querySelector("input[data-name=title]").className.indexOf("disable")<0')
    except WebDriverException:
        pass


def wait_load_ref(driver):
    WebDriverWait(driver, 30, 1).until(loading_ref, 'AJAX')