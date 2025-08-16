from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.python.org/")
driver.maximize_window()
ele1=driver.find_element("name","q")
ele1.send_keys("loop")
#ele1.send_keys(Keys.RETURN)
time.sleep(5)
driver.quit()