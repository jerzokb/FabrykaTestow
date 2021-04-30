from tests.helpers.HelpersFunctions import *

iframe_tab = 'iframe-header'
iframe_content = 'iframe-content'
iframe_main = 'iframe'
button1 = 'simpleButton1'
button2 = 'simpleButton2'
message = 'whichButtonIsClickedMessage'


def click_iframe_tab(driver_instance):
    elem = driver_instance.find_element_by_id(iframe_tab)
    elem.click()


def iframe_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, iframe_content)
    return elem.is_displayed()


def click_inside_iframe_one(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, iframe_main)
    driver_instance.switch_to.frame(driver_instance.find_element_by_tag_name("iframe"))
    driver_instance.find_element_by_id(button1).click()
    output = driver_instance.find_element_by_id(message).text
    if output == 'Button 1 was clicked!':
        return True
    else:
        return False


def click_inside_iframe_two(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, iframe_main)
    driver_instance.switch_to.frame(driver_instance.find_element_by_tag_name("iframe"))
    driver_instance.find_element_by_id(button2).click()
    output = driver_instance.find_element_by_id(message).text
    if output == 'Button 2 was clicked!':
        return True
    else:
        return False