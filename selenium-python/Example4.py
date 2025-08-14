from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://127.0.0.1:5500/practice.html")
#txt=driver.find_element(By.XPATH,"//html/body/div/input[1]")
#txt=driver.find_element(By.XPATH,"//div[@id='abc']/input[1]")
txt=driver.find_element(By.XPATH,"//*[@id='abc']/input[1]")
txt.send_keys("SET PATH BY REL XPATH")
txt=driver.find_element(By.XPATH,"//*[@class='xyz']/input[1]")
txt.send_keys("SET PATH BY REL XPATH")
time.sleep(3)
