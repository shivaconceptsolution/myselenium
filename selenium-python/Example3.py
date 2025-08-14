#this script will set textfield value
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.shivaconceptsolution.com/backupmain/test.html")
txt=driver.find_element(By.CSS_SELECTOR,"input[placeholder='enter date']")
txt.send_keys("11-11-2001")
time.sleep(1)
#driver.close()
