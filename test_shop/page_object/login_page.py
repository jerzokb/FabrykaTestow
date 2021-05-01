from test_shop.helpers.HelpersFunctions import *
from test_shop.helpers.DataGenerator import *
from faker import Faker

fake = Faker()

random_password = fake.password()
input_username = 'username'
input_password = 'password'
button_login = '//*[@id="customer_login"]/div[1]/form/p[3]/button'
login_error = '//*[@id="content"]/div/div[1]/ul'

email1 = 'cotaga1249@maillei.net'
password1 = 'VRrMhK8MqFyd'

email2 = 'wowen49501@maillei.net'
password2 = 'lxsg#GAqH$Ke'

email3 = 'bomineg967@onmail3.com'
password3 = 'zedvu@##)CZy'

email4 = 'wacog70401@tinkmail.net'
password4 = 'Lk*3Q9&am3zL'

email5 = 'calose2528@maillei.net'
password5 = 'lkSb&SAJwLWo'


def correct_login(driver_instance):
    username = driver_instance.find_element_by_id(input_username)
    username.send_keys(email1)
    password = driver_instance.find_element_by_id(input_password)
    password.send_keys(password1)
    button = driver_instance.find_element_by_xpath(button_login)
    button.click()

def incorrect_login(driver_instance):
    username = driver_instance.find_element_by_id(input_username)
    username.send_keys(DataGenerator.generateWrongEmail())
    password = driver_instance.find_element_by_id(input_password)
    password.send_keys(random_password)
    button = driver_instance.find_element_by_xpath(button_login)
    button.click()
    try:
        wait_for_visibility_of_element_xpath(driver_instance, login_error)
        return button.is_displayed()
    except StaleElementReferenceException:
        print('ERROR: Incorrect username or password.')
        return True