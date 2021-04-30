from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def hover_over_element(driver_instance, element):
    hover = ActionChains(driver_instance).move_to_element(element)
    hover.perform()


def wait_for_visibility_of_element_xpath(driver_instance, xpath):
    try:
        elem = WebDriverWait(driver_instance, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_visibility_of_element_id(driver_instance, id):
    try:
        elem = WebDriverWait(driver_instance, 10).until(EC.visibility_of_element_located((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem


def visibility_of_element_wait(driver, id):
    """Checking if element specified by xpath is visible on page

    :param driver: webdriver instance
    :param xpath: xpath of webelement
    :param timeout: time after looking for element will be stopped (default: 10)
    : return: first element in list of found elements
    """
    timeout_message = f"Element for xpath: '{id}' and url: {driver.current_url} not found in 10 seconds"

    locator = (By.ID, id)
    element_located = EC.visibility_of_element_located((locator))
    # visibility_of_all_elements_located()
    wait = WebDriverWait(driver, 10).until(
        element_located,
        timeout_message)

    return element_located


def wait_for_invisibility_of_element(inv_driver_instance, xpath):
    inv_element = WebDriverWait(inv_driver_instance, 8).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
    return inv_element


def scroll_to_element(driver_instance, element):
    action = ActionChains(driver_instance)
    action.move_to_element(element)
    action.perform()


def isDisplayed(driver_instance, locator):
    try:
        driver_instance.find_element_by_xpath("//*[text()='find text vwhis in page']")
    except NoSuchElementException:
        return False
    return True
