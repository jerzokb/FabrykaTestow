import unittest

from selenium import webdriver

from config.test_settings import TestSettings
from test_shop.page_object import main_page, login_page, my_account_page, cart_page, order_page, order_received_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.shop_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_process(self):
        self.assertTrue(main_page.is_taps_logo_visible(self.driver))
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.is_item_in_cart(self.driver))
        cart_page.submit_cart(self.driver)
        order_page.proper_fill_all_form_areas(self.driver)
        order_page.submit_order(self.driver)
        self.assertTrue(order_received_page.is_header_visible(self.driver))