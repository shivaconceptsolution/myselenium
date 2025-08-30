from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/selenium-python/frameexample.html")
driver.refresh()
driver.switch_to.frame("second")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"SHIVA").click()
time.sleep(5)