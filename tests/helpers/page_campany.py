__author__ = 'tan'

from tests.helpers.page_component import Page, Component
from selenium.webdriver.support.ui import WebDriverWait


class CampanyPage(Page):
    PATH = '/ads/campaigns/'

    @property
    def checking(self):
        return Checking(self.driver)

    @property
    def top_menu(self):
        return TopMenu(self.driver)


class Checking(Component):
    EDIT_BUTTON = '.control__link_edit'
    CAMPANY = 'li.campaign-row:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)'
    LAST_ELEMENT = '/html/body/div[8]'

    def wait_for_edit_page_load(self):
        WebDriverWait(self.driver, 30, 2).until(
            lambda d: d.find_element_by_xpath(self.LAST_ELEMENT)

        )

    def edit(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EDIT_BUTTON)
        )
        element.click()

    def get_campany(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CAMPANY).text
        )


class TopMenu(Component):
    EMAIL = '#PH_user-email'

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )

