from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://eroomrent.in/index.php")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"FAQ").click()
time.sleep(5)
driver.close()