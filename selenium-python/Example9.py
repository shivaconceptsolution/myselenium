from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("http://127.0.0.1:5500/cssselectorexample.html")
driver.find_element(By.CSS_SELECTOR,"input[type=text]").send_keys("RAMKUMAR SHARMA")
driver.find_element(By.CSS_SELECTOR,"input[type=date]").send_keys("12-12-2000")
driver.find_element(By.CSS_SELECTOR,"input[type=number]").send_keys(25)
time.sleep(5)
driver.close()
