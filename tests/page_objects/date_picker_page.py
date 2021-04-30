from datetime import date
from time import sleep

from tests.helpers.HelpersFunctions import *

datepicker_header = 'datepicker-header'
datepicker_content = 'datepicker-content'
datepicker_element = '//*[@id="start"]'
button = 'reset-button'


def click_date_picker_tab(driver_instance):
    element = driver_instance.find_element_by_id(datepicker_header)
    element.click()


def date_picker_content_visible(driver_instance):
    element = wait_for_visibility_of_element_id(driver_instance, datepicker_content)
    return element.is_displayed()


def click_date_picker_element(driver_instance):
    element = driver_instance.find_element_by_id(datepicker_element)
    element.click()


def get_date_picker_value(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, datepicker_element)
    element = driver_instance.find_element_by_xpath(datepicker_element)
    datepicker_value = element.get_attribute("value")
    expected_value = "2020-07-22"
    if datepicker_value == expected_value:
        return True
    else:
        return False


def send_correct_date(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, datepicker_element)
    element = driver_instance.find_element_by_xpath(datepicker_element)
    today = "2020-07-22"
    element.send_keys(today)
    datepicker_value = element.get_attribute("value")
    print('Actual value: ' + datepicker_value + ' expected value: ' + today)
    if datepicker_value == today:
        return True
    else:
        return False


def send_incorrect_date(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, datepicker_element)
    element = driver_instance.find_element_by_xpath(datepicker_element)
    today = "1313-FRIDAY-13"
    element.send_keys(today)
    datepicker_value = element.get_attribute("value")
    if datepicker_value == today:
        return False
    else:
        return True
