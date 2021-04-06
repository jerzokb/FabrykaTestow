from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

def hover_over_element(driver_instance, element):
    hover = ActionChains(driver_instance).move_to_element(element)
    hover.perform()

def wait_for_element(driver_instance, element, time_to_wait = 10):
    try:
        element = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of(element))
    except TimeoutException:
        element = False
    return element

def scroll_to_element(driver_instance, element):
    action = ActionChains(driver_instance)
    action.move_to_element(element)
    action.perform()