from tests.helpers.HelpersFunctions import *
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.switch_to import SwitchTo

formHeader = 'form-header'
formContent = 'form-content'
inputFirstName = 'fname'
inputLastName = 'lname'
buttonSubmit = 'formSubmitButton'


def click_form_tab(driver_instance):
    elem = driver_instance.find_element_by_id(formHeader)
    elem.click()


def is_form_content_visible(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, formContent)
    elem = driver_instance.find_element_by_id(formContent)
    return elem.is_displayed()


def send_first_name_and_last_name(driver_instance, firstName, lastName):
    wait_for_visibility_of_element_id(driver_instance, inputFirstName)
    first_name = driver_instance.find_element_by_id(inputFirstName)
    first_name.send_keys(firstName)
    last_name = driver_instance.find_element_by_id(inputLastName)
    last_name.send_keys(lastName)
    submit_button = driver_instance.find_element_by_id(buttonSubmit)
    submit_button.click()
    alert = Alert(driver_instance)
    value = "success"
    if value == alert.text:
        return True
    else:
        return False


def send_only_first_name(driver_instance, firstName):
    wait_for_visibility_of_element_id(driver_instance, inputFirstName)
    first_name = driver_instance.find_element_by_id(inputFirstName)
    submit_button = driver_instance.find_element_by_id(buttonSubmit)
    first_name.send_keys(firstName)
    submit_button.click()
    toast = driver_instance.switch_to.active_element.get_attribute("text")
    value = "Wypełnij to pole."
    if value == toast:
        return True
    else:
        return False


def send_only_last_name(driver_instance, lastName):
    wait_for_visibility_of_element_id(driver_instance, inputLastName)
    last_name = driver_instance.find_element_by_id(inputLastName)
    submit_button = driver_instance.find_element_by_id(buttonSubmit)
    last_name.send_keys(lastName)
    submit_button.click()
    toast = driver_instance.switch_to.active_element.get_attribute("text")
    value = "Wypełnij to pole."
    if value == toast:
        return True
    else:
        return False