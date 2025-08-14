from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://technokri.com/regitration_page")
#txt=driver.find_element(By.XPATH,"//html/body/div/input[1]")
#txt=driver.find_element(By.XPATH,"//div[@id='abc']/input[1]")

txt=driver.find_element(By.XPATH,"//*[@class='list']/li")
print(txt.text)

