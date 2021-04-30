from tests.helpers.HelpersFunctions import *

basic_auth_header = 'basicauth-header'
basic_auth_content = 'basicauth-content'
ba_username = 'ba_username'
ba_password = 'ba_password'
username = 'admin'
password = 'admin'
incorrect_password = 'password'
ba_button = '//*[@id="content"]/button'
loggedInMessage = 'loggedInMessage'
loginFormMessage = 'loginFormMessage'


def click_basic_auth_tab(driver_instance):
    elem = driver_instance.find_element_by_id(basic_auth_header)
    elem.click()


def is_basic_auth_content_visible(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, basic_auth_content)
    elem = driver_instance.find_element_by_id(basic_auth_content)
    return elem.is_displayed()


def enter_correct_credentials(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, basic_auth_content)
    input_username = driver_instance.find_element_by_id(ba_username)
    input_password = driver_instance.find_element_by_id(ba_password)
    button_login = driver_instance.find_element_by_xpath(ba_button)
    input_username.send_keys(username)
    input_password.send_keys(password)
    button_login.click()
    wait_for_visibility_of_element_id(driver_instance, loggedInMessage)
    message_text = driver_instance.find_element_by_id(loggedInMessage)
    if message_text.is_displayed():
        return True
    else:
        return False


def enter_incorrect_credentials(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, basic_auth_content)
    input_username = driver_instance.find_element_by_id(ba_username)
    input_password = driver_instance.find_element_by_id(ba_password)
    button_login = driver_instance.find_element_by_xpath(ba_button)
    input_username.send_keys(username)
    input_password.send_keys(incorrect_password)
    button_login.click()
    wait_for_visibility_of_element_id(driver_instance, loginFormMessage)
    message_text = driver_instance.find_element_by_id(loginFormMessage)
    if message_text.is_displayed():
        return True
    else:
        return False