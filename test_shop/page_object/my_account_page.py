from tests.helpers.HelpersFunctions import *

my_account_header = '//*[@id="post-9"]/header/h1'

def is_header_visible(driver_instance):
    elem = wait_for_visibility_of_element_xpath(driver_instance, my_account_header)
    return elem.is_displayed()
