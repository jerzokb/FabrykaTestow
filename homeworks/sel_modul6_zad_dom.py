import time

from selenium import webdriver
from helpers import HelpersFunctions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

url = 'https://fabrykatestow.pl'
menu_link_text = 'KURSY'
button_xpath = '//a[@href="https://fabrykatestow.pl/taps"]'
image_xpath = '//*[@id="content"]/div/div/div/div/div/div/div/section[5]/div[2]/div/div/div/div/section/div/div/div[1]/div/div/div[1]/div/div/img'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

menu_link = driver.find_element_by_partial_link_text(menu_link_text)
menu_link.click()

button_strona_kursu = driver.find_element_by_xpath(button_xpath)
button_strona_kursu.click()

picture_section = driver.find_element_by_xpath(image_xpath)

HelpersFunctions.scroll_to_element(driver, picture_section)

driver.get_screenshot_as_file('PawelZwierzchpwski.png')

driver.close()