from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

def hover_over_element(driver_instance, element):
    hover = ActionChains(driver_instance).move_to_element(element)
    hover.perform()

def wait_for_visibility_of_element_xpath(driver_instance, ID, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located(By.ID, ID))
    except TimeoutException:
        elem = False
    return elem

def wait_for_visibility_of_element_id(driver_instance, xpath, time_to_wait=10):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located(By.XPATH, xpath))
    except TimeoutException:
        elem = False
    return elem

def wait_for_invisibility_of_element(inv_driver_instance, xpath, time_to_wait=8):
    inv_element = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element_located(By.XPATH, xpath))
    return inv_element

def scroll_to_element(driver_instance, element):
    action = ActionChains(driver_instance)
    action.move_to_element(element)
    action.perform()