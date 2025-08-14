#this script will set textfield value
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.shivaconceptsolution.com/backupmain/test.html")
txt=driver.find_element("id","txt1")
txt.send_keys("FIRST TEXT FIELD")
time.sleep(1)
driver.close()
