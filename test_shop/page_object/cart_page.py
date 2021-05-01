from test_shop.helpers.HelpersFunctions import *

item_in_cart = '//*[@id="post-7"]/div/div/form/table/tbody/tr[1]'
remove_item_from_cart_button = '//*[@id="post-7"]/div/div/form/table/tbody/tr[1]/td[1]/a'
submit_cart_button = '//*[@id="post-7"]/div/div/div[2]/div/div/a'


def is_item_in_cart(driver_instance):
    elem = wait_for_visibility_of_element_xpath(driver_instance, item_in_cart)
    return elem.is_displayed()


def remove_item_from_cart(driver_instance):
    elem = wait_for_visibility_of_element_xpath(driver_instance, remove_item_from_cart_button)
    elem.click()


def is_item_removed_from_cart(driver_instance):
    try:
        wait_for_invisibility_of_element_xpath(driver_instance, item_in_cart)
        return True
    except NoSuchElementException:
        return False


def submit_cart(driver_instance):
    elem = driver_instance.find_element_by_xpath(submit_cart_button)
    elem.click()