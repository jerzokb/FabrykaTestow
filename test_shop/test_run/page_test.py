import unittest

from selenium import webdriver

from config.test_settings import TestSettings
from test_shop.page_object import main_page, login_page, my_account_page

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.shop_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_is_taps_logo_visible(self):
        self.assertTrue(main_page.is_taps_logo_visible(self.driver))

    def test_correct_login(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
        self.assertTrue(my_account_page.is_header_visible(self.driver))

    def test_incorrect_login(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.incorrect_login(self.driver))