import unittest

from selenium import webdriver

from config.test_settings import TestSettings
from test_shop.page_object import main_page, login_page, my_account_page, cart_page

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.shop_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_item_to_cart(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.is_item_in_cart(self.driver))

    def test_remove_item_from_cart(self):
        main_page.add_item_to_cart(self.driver)
        main_page.go_to_cart_page(self.driver)
        self.assertTrue(cart_page.is_item_in_cart(self.driver))
        cart_page.remove_item_from_cart(self.driver)
        self.assertTrue(cart_page.is_item_removed_from_cart(self.driver))
