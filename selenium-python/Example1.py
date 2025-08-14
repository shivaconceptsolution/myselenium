from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://shivaconceptsolution.com")
time.sleep(1)
driver.close()
