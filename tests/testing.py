import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from tests.helpers.page_create import CreatePage
from tests.helpers.page_campany import CampanyPage
from tests.helpers.page_auth import AuthPage
import tests.helpers.utils as utils
from tests.helpers.config import *
from tests.helpers.page_edit import EditPage


class ExampleTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(DOMAIN)
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)

        auth_form.submit()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):

        create_page = CreatePage(self.driver)
        create_page.open()
        email = create_page.top_menu.get_email()

        self.assertEqual(USERNAME, email)

    def test_average_level(self):

        create_page = CreatePage(self.driver)
        create_page.open()
        create_page.top_menu.get_email()
        create_page.advertise_campany.set_campany(CAMPAIGN)
        create_page.advertise_campany.set_advertise_type()
        create_page.advertise_campany.set_advertise_item()

        create_page.create_advertise.set_reference(REF)
        utils.wait_load_ref(self.driver)
        create_page.create_advertise.set_title(TITLE)
        create_page.create_advertise.set_text(TEXT)
        create_page.create_advertise.set_small_image(SMALL_IMAGE)
        create_page.create_advertise.set_big_image(BIG_IMAGE)
        utils.wait_loading(self.driver)
        create_page.create_advertise.submit()

        utils.wait_loading(self.driver)
        create_page.settings_level.click_level()
        create_page.settings_level.set_average_level()
        utils.wait_loading(self.driver)
        create_page.create_campany.submit()
        utils.wait_loading(self.driver)

        campany_page = CampanyPage(self.driver)
        campany_page.open()
        utils.wait_loading(self.driver)
        campany_page.checking.edit()

        edit_page = EditPage(self.driver)
        edit_page.check_level.wait_for_edit_page_load()
        utils.wait_loading(self.driver)
        edit_page.check_level.click_level()
        check_average = edit_page.check_level.average()

        self.assertTrue(check_average)

    def test_low_high_level(self):

        create_page = CreatePage(self.driver)
        create_page.open()
        create_page.top_menu.get_email()
        create_page.advertise_campany.set_campany(CAMPAIGN)
        create_page.advertise_campany.set_advertise_type()
        create_page.advertise_campany.set_advertise_item()

        create_page.create_advertise.set_reference(REF)
        utils.wait_load_ref(self.driver)
        create_page.create_advertise.set_title(TITLE)
        create_page.create_advertise.set_text(TEXT)
        create_page.create_advertise.set_small_image(SMALL_IMAGE)
        create_page.create_advertise.set_big_image(BIG_IMAGE)
        utils.wait_loading(self.driver)
        create_page.create_advertise.submit()

        utils.wait_loading(self.driver)
        create_page.settings_level.click_level()
        create_page.settings_level.set_low_high_level()
        utils.wait_loading(self.driver)
        create_page.create_campany.submit()
        utils.wait_loading(self.driver)

        campany_page = CampanyPage(self.driver)
        campany_page.open()

        utils.wait_loading(self.driver)
        campany_page.checking.edit()

        edit_page = EditPage(self.driver)
        edit_page.check_level.wait_for_edit_page_load()
        utils.wait_loading(self.driver)
        edit_page.check_level.click_level()
        check_low_high = edit_page.check_level.low_high()

        self.assertTrue(check_low_high)

    def test_all_ussr(self):

        create_page = CreatePage(self.driver)
        create_page.open()
        create_page.top_menu.get_email()
        create_page.advertise_campany.set_campany(CAMPAIGN)
        create_page.advertise_campany.set_advertise_type()
        create_page.advertise_campany.set_advertise_item()

        create_page.create_advertise.set_reference(REF)
        utils.wait_load_ref(self.driver)
        create_page.create_advertise.set_title(TITLE)
        create_page.create_advertise.set_text(TEXT)
        create_page.create_advertise.set_small_image(SMALL_IMAGE)
        create_page.create_advertise.set_big_image(BIG_IMAGE)
        utils.wait_loading(self.driver)
        create_page.create_advertise.submit()

        utils.wait_loading(self.driver)
        create_page.settings_country.set_all_ussr()
        utils.wait_loading(self.driver)
        create_page.create_campany.submit()
        utils.wait_loading(self.driver)

        campany_page = CampanyPage(self.driver)
        campany_page.open()

        utils.wait_loading(self.driver)
        campany_page.checking.edit()

        edit_page = EditPage(self.driver)
        edit_page.check_level.wait_for_edit_page_load()
        utils.wait_loading(self.driver)
        ussr_select = edit_page.check_country.all_ussr_checked()
        edit_page.check_country.click_countries()
        other_countries_in_ussr = edit_page.check_country.some_countries_checked()
        self.assertTrue(ussr_select)
        self.assertTrue(other_countries_in_ussr)

    def test_country_child(self):

        create_page = CreatePage(self.driver)
        create_page.open()
        create_page.top_menu.get_email()
        create_page.advertise_campany.set_campany(CAMPAIGN)
        create_page.advertise_campany.set_advertise_type()
        create_page.advertise_campany.set_advertise_item()

        create_page.create_advertise.set_reference(REF)
        utils.wait_load_ref(self.driver)
        create_page.create_advertise.set_title(TITLE)
        create_page.create_advertise.set_text(TEXT)
        create_page.create_advertise.set_small_image(SMALL_IMAGE)
        create_page.create_advertise.set_big_image(BIG_IMAGE)
        utils.wait_loading(self.driver)
        create_page.create_advertise.submit()

        utils.wait_loading(self.driver)
        create_page.settings_country.open_ussr()
        create_page.settings_country.set_child_country()
        utils.wait_loading(self.driver)
        create_page.create_campany.submit()
        utils.wait_loading(self.driver)

        campany_page = CampanyPage(self.driver)
        campany_page.checking.wait_for_edit_page_load()

        campany_page.open()

        utils.wait_loading(self.driver)
        campany_page.checking.edit()

        edit_page = EditPage(self.driver)
        edit_page.check_level.wait_for_edit_page_load()
        utils.wait_loading(self.driver)
        edit_page.check_country.click_countries()
        ussr_child_check = edit_page.check_country.child_child_checked()
        other_countries_in_ussr = edit_page.check_country.some_countries_checked()

        self.assertTrue(ussr_child_check)
        self.assertFalse(other_countries_in_ussr)

    def test_click_some_countries(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        create_page.top_menu.get_email()
        create_page.advertise_campany.set_campany(CAMPAIGN)
        create_page.advertise_campany.set_advertise_type()
        create_page.advertise_campany.set_advertise_item()

        create_page.create_advertise.set_reference(REF)
        utils.wait_load_ref(self.driver)
        create_page.create_advertise.set_title(TITLE)
        create_page.create_advertise.set_text(TEXT)
        create_page.create_advertise.set_small_image(SMALL_IMAGE)
        create_page.create_advertise.set_big_image(BIG_IMAGE)
        utils.wait_loading(self.driver)
        create_page.create_advertise.submit()

        utils.wait_loading(self.driver)
        create_page.settings_country.open_ussr()
        create_page.settings_country.set_some_countries()
        utils.wait_loading(self.driver)
        create_page.create_campany.submit()
        utils.wait_loading(self.driver)

        campany_page = CampanyPage(self.driver)
        campany_page.checking.wait_for_edit_page_load()
        campany_page.open()

        utils.wait_loading(self.driver)
        campany_page.checking.edit()

        edit_page = EditPage(self.driver)
        edit_page.check_level.wait_for_edit_page_load()
        utils.wait_loading(self.driver)
        edit_page.check_country.click_countries()
        some_countries_check = edit_page.check_country.some_countries_checked()
        ussr_child_check = edit_page.check_country.child_child_checked()

        self.assertTrue(some_countries_check)
        self.assertFalse(ussr_child_check)
