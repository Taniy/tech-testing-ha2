__author__ = 'tan'

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException


def ajax_complete(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")
    except WebDriverException:
        pass


def wait_for_ajax_complete(driver):
    WebDriverWait(driver, 30, 2).until(ajax_complete, 'AJAX')


def ajax_complete_ref(driver):
    try:
        return driver.execute_script('return document.querySelector("input[data-name=title]").className.indexOf("disable")<0')
    except WebDriverException:
        pass


def wait_for_ajax_complete_ref(driver):
    WebDriverWait(driver, 30, 2).until(ajax_complete_ref, 'AJAX')