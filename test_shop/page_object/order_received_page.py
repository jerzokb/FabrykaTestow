import time

from test_shop.helpers.HelpersFunctions import *

page_header = '//*[@id="post-8"]/header/h1'
total_price = '//*[@id="post-8"]/div/div/div/ul/li[3]/strong/span/bdi'


def is_header_visible(driver_instance):
    elem = wait_for_visibility_of_element_xpath(driver_instance, page_header)
    return elem.is_displayed()


def is_total_price_correct(driver_instance, price):
    wait_for_visibility_of_element_xpath(driver_instance, total_price)
    time.sleep(10)
    elem = driver_instance.find_element_by_xpath(total_price)
    total_amount = elem.text
    print(total_amount)
    if (total_amount == price):
        return True
    else:
        return False