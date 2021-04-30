from tests.helpers.HelpersFunctions import *
from selenium.webdriver import ActionChains
import os
from time import sleep

drag_tab = 'draganddrop-header'
drag_content = 'draganddrop-content'
rectangleA = 'column-a'
rectangleB = 'column-b'


def click_drag_and_drop_tab(driver_instance):
    elem = driver_instance.find_element_by_id(drag_tab)
    elem.click()

def drag_and_drop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, drag_content)
    return elem.is_displayed()


def check_drag_and_drop(driver_instance):
    driver_instance.implicitly_wait(10)
    driver_instance.get('http://simpletestsite.fabrykatestow.pl/')

    with open(os.path.abspath('drag_and_drop_helper.js'), 'r') as js_file:
        line = js_file.readline()
        script = ''
        while line:
            script += line
            line = js_file.readline()

    driver_instance.execute_script(script + "jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
    sleep(2)
    return True