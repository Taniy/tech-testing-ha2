__author__ = 'tan'

from tests.helpers.page_component import Page, Component
from selenium.webdriver.support.ui import WebDriverWait


class CreatePage(Page):
    PATH = '/ads/create'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def advertise_campany(self):
        return AdvertiseCampany(self.driver)

    @property
    def create_advertise(self):
        return CreateAdvertise(self.driver)

    @property
    def create_campany(self):
        return CreateCampany(self.driver)

    @property
    def settings_level(self):
        return SettingsLevel(self.driver)

    @property
    def settings_country(self):
        return SettingsCountry(self.driver)


class TopMenu(Component):
    EMAIL = '#PH_user-email'

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )


class AdvertiseCampany(Component):
    CAMP_NAME = '.base-setting__campaign-name__input'
    ADVERTISE_TYPE = '#product-type-6039'
    ADVERTISE_ITEM = '#pad-mobile_app_feed'

    def set_campany(self, name_of_campaign):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CAMP_NAME)
        )
        element.clear()
        element.send_keys(name_of_campaign)

    def set_advertise_type(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.ADVERTISE_TYPE)
        )
        element.click()

    def set_advertise_item(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.ADVERTISE_ITEM)
        )
        element.click()


class CreateCampany(Component):
    SUBMIT ='.main-button__label'

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()


class SettingsLevel(Component):
    LEVEL = '.campaign-setting__wrapper_income_group > span:nth-child(1)'
    LOW_LEVEL = '#income_group-9286'
    AVERAGE_LEVEL = '#income_group-9287'
    HIGH_LEVEL = '#income_group-9288'

    def click_level(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.LEVEL)
        )
        element.click()

    def set_low_high_level(self):
        self.driver.find_element_by_css_selector(self.LOW_LEVEL).click()
        self.driver.find_element_by_css_selector(self.HIGH_LEVEL).click()

    def set_average_level(self):
        self.driver.find_element_by_css_selector(self.AVERAGE_LEVEL).click()


class SettingsCountry(Component):
    OPEN_USSR = '#regions100001 > span:nth-child(1)'
    USSR = '#regions100001 > label:nth-child(3)'
    CHILD = '#regions399 > label:nth-child(3)'
    COUNTRY= []
    COUNTRY.append('#regions219 > label:nth-child(3)')
    COUNTRY.append('#regions34 > label:nth-child(3)')
    COUNTRY.append('#regions17 > label:nth-child(3)')
    COUNTRY.append('#regions29 > label:nth-child(3)')
    COUNTRY.append('#regions28 > label:nth-child(3)')
    COUNTRY.append('#regions398 > span:nth-child(1)')

    def open_ussr(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.OPEN_USSR)
        )
        element.click()

    def set_all_ussr(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.USSR)
        )
        element.click()

    def set_child_country(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.COUNTRY[5])
        )
        button.click()
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CHILD)
        )
        element.click()

    def set_some_countries(self):
        for i in range(4):
            element = WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_element_by_css_selector(self.COUNTRY[i])
            )
            element.click()


class CreateAdvertise(Component):
    REF = 'input[data-name="url"]'
    TITLE = 'input[data-name="title"]'
    TEXT = 'textarea[data-name="text"]'
    SMALL_IMAGE = 'input[data-name="image"]'
    BIG_IMAGE = 'input[data-name="promo_image"]'
    SUBMIT ='.banner-form__save-button'

    def set_reference(self, reference):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.REF)
        )
        element.send_keys(reference)

    def set_title(self, notice_title):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.TITLE)
        )
        element.send_keys(notice_title)

    def set_text(self, notice_text):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.TEXT)
        )
        element.send_keys(notice_text)

    def set_small_image(self, small_image):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SMALL_IMAGE)
        )
        element.send_keys(small_image)

    def set_big_image(self, big_image):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BIG_IMAGE)
        )
        element.send_keys(big_image)

    def submit(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SUBMIT)
        )
        element.click()