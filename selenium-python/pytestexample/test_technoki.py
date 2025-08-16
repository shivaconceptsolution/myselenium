from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def testxyz():
   driver = webdriver.Chrome()
   driver.maximize_window()
   driver.get("https://technokri.com/regitration_page")
   txt=driver.find_elements(By.XPATH,"//*[@class='list']/li")
   for opt in txt:
      value = opt.get_attribute("innerText").strip()
      print(value) 
   driver.close()
   
