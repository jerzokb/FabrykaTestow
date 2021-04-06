from selenium import webdriver
import time

driver = webdriver.Chrome()
# get - przechodzi na stronę, którą podamy
driver.get('https://google.pl')
search_box = driver.find_element_by_name('q')
search_box.send_keys('selenium python')
search_box.submit()
time.sleep(5)
# zamknie wszystkie okna przeglądarek
driver.quit()
# zamknie okno, na którym wykonywały się testy
driver.close()

# selenium commands
