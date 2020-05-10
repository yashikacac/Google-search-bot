from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")

time.sleep(3)
search_element = driver.find_element_by_name('q')


name=input("enter something to search")
search_element.send_keys(name)

search_element.send_keys(Keys.ENTER)