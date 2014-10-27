#coding=utf-8
__author__ = 'tan'

from tests.helpers.page_component import Page, Component
from selenium.webdriver.support.ui import WebDriverWait
import tests.helpers.utils as utils


class EditPage(Page):
    PATH = ''

    @property
    def check_level(self):
        return CheckLevel(self.driver)

    @property
    def check_country(self):
        return CheckCountry(self.driver)


class CheckLevel(Component):
    LEVEL_BUTTON = '.campaign-setting__wrapper_income_group > span:nth-child(1)'
    HIGH_LEVEL = '#income_group-9288'
    LOW_LEVEL = '#income_group-9286'
    AVERAGE_LEVEL = '#income_group-9287'
    LAST_ELEMENT = '/html/body/div[8]'

    def wait_for_edit_page_load(self):
        WebDriverWait(self.driver, 30, 2).until(
            lambda d: d.find_element_by_xpath(self.LAST_ELEMENT)

        )

    def click_level(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda d: d.find_element_by_css_selector(self.LEVEL_BUTTON)
        )
        element.click()

    def low_high(self):
        elem_high = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.HIGH_LEVEL)
        )
        elem_low = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.LOW_LEVEL)
        )
        if not (elem_high.get_attribute("checked") or elem_low.get_attribute("checked")):
            return False
        return True

    def average(self):
        element = WebDriverWait(self.driver, 30, 2).until(
            lambda d: d.find_element_by_css_selector(self.AVERAGE_LEVEL)
        )
        if not (element.get_attribute("checked")):
            return False
        return True


class CheckCountry(Component):
    BUTTON_COUNTRIES = '#regions100001 > span:nth-child(1)'
    LAST_ELEMENT = '/html/body/div[8]'
    USSR ='#regions100001 > label:nth-child(3)'
    CHILD = '#regions399 > label:nth-child(3)'
    COUNTRY= []
    COUNTRY.append('#regions219 > label:nth-child(3)')
    COUNTRY.append('#regions34 > label:nth-child(3)')
    COUNTRY.append('#regions17 > label:nth-child(3)')
    COUNTRY.append('#regions29 > label:nth-child(3)')
    COUNTRY.append('#regions28 > label:nth-child(3)')
    COUNTRY.append('#regions398 > span:nth-child(1)')

    def wait_for_edit_page_load(self):
        WebDriverWait(self.driver, 30, 2).until(
            lambda d: d.find_element_by_xpath(self.LAST_ELEMENT)
        )

    def click_countries(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BUTTON_COUNTRIES)
        )
        element.click()

    def all_ussr_checked(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.USSR)
        )
        if not ("checked" in (element.get_attribute("class"))):
            return False
        return True

    def child_child_checked(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.COUNTRY[5])
        )
        button.click()
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CHILD)
        )
        print element.get_attribute("class")
        if not ("checked" in (element.get_attribute("class"))):
            return False
        return True

    def some_countries_checked(self):
        for i in range(4):
            element = WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_css_selector(self.COUNTRY[i])
            )
            if not ("checked" in (element.get_attribute("class"))):
                return False
        return True
