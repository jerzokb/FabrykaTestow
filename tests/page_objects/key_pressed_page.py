from tests.helpers.HelpersFunctions import *
from selenium.webdriver.common.keys import Keys

key_pressed_tab = 'keypresses-header'
key_pressed_content = 'keypresses-content'
input_field = 'target'
key_pressed_result = 'keyPressResult'


def click_key_presses_tab(driver_instance):
    elem = driver_instance.find_element_by_id(key_pressed_tab)
    elem.click()


def key_presses_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, key_pressed_content)
    return elem.is_displayed()


def key_pressed_correct_value(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, input_field)
    elem = driver_instance.find_element_by_id(input_field)
    elem_result = driver_instance.find_element_by_id(key_pressed_result)
    elem.send_keys("K")
    value = "K"
    if value == (elem_result.text[13:]):
        return True
    else:
        return False