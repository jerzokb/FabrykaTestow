from test_shop.helpers.HelpersFunctions import *

page_header = '//*[@id="post-8"]/header/h1'

def is_header_visible(driver_instance):
    elem = wait_for_visibility_of_element_xpath(driver_instance, page_header)
    return elem.is_displayed()