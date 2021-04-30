import unittest
from faker import Faker

from selenium import webdriver

from config.test_settings import TestSettings
from tests.page_objects import main_page, checkboxes_page, hovers_page, users_page, inputs_page, dropdown_page, add_remove_page, date_picker_page, basic_auth_page, drag_and_drop_page, form_page, key_pressed_page, status_code_page, iframe_page

fake = Faker()
firstName = fake.first_name()
lastName = fake.last_name()

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test3_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test4_inputs_visibilty(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.input_content_visible(self.driver))

    def test5_inputs_correct_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_keys_to_input(self.driver))

    def test6_inputs_incorrect_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test8_add_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)

    def test9_delete_element(self):
        add_remove_page.click_and_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

    #Date Picker Tests
    def test_is_date_picker_content_visible(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.date_picker_content_visible(self.driver))

    def test_date_picker_check_value(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.get_date_picker_value(self.driver))

    def test_date_picker_send_correct_data(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.send_correct_date(self.driver))

    def test_date_picker_send_incorrect_data(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.send_incorrect_date(self.driver))

    #Basic Auth Tests
    def test_is_basic_auth_content_visible(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.is_basic_auth_content_visible(self.driver))

    def test_correct_login_credentials(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.enter_correct_credentials(self.driver))

    def test_incorrect_login_credentials(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.enter_incorrect_credentials(self.driver))

    #Form Tests
    def test_is_form_content_visible(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.is_form_content_visible(self.driver))

    def test_send_correct_values(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.send_first_name_and_last_name(self.driver, firstName, lastName))

    def test_send_only_first_name(self):
        form_page.click_form_tab(self.driver)
        self.assertFalse(form_page.send_only_first_name(self.driver, firstName))

    def test_send_only_last_name(self):
        form_page.click_form_tab(self.driver)
        self.assertFalse(form_page.send_only_last_name(self.driver, lastName))

    #Key Pressed Page Tests
    def test_key_pressed_content_visible(self):
        key_pressed_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_pressed_page.key_presses_content_visible(self.driver))

    def test_key_pressed_values(self):
        key_pressed_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_pressed_page.key_pressed_correct_value(self.driver))

    #Drag and Drop Tests
    def test_drag_and_drop_content_visible(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.drag_and_drop_content_visible(self.driver))

    def test_drag_and_drop(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.check_drag_and_drop(self.driver))

    #Status Code Tests
    def test_is_status_code_content_visible(self):
        status_code_page.click_codes_tab(self.driver)
        self.assertTrue(status_code_page.codes_content_visible(self.driver))

    def test_code_200(self):
        status_code_page.click_codes_tab(self.driver)
        self.assertTrue(status_code_page.code_200(self.driver))

    def test_code_305(self):
        status_code_page.click_codes_tab(self.driver)
        self.assertTrue(status_code_page.code_305(self.driver))

    def test_code_404(self):
        status_code_page.click_codes_tab(self.driver)
        self.assertTrue(status_code_page.code_404(self.driver))

    def test_code_500(self):
        status_code_page.click_codes_tab(self.driver)
        self.assertTrue(status_code_page.code_500(self.driver))

    #iFrame Tests
    def test_is_iframe_content_visible(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.iframe_content_visible(self.driver))

    def test_inside_iframe_one(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.click_inside_iframe_one(self.driver))

    def test_inside_iframe_two(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.click_inside_iframe_two(self.driver))

