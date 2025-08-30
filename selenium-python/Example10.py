from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")
driver.switch_to.frame(0)
source = driver.find_element(By.ID,"draggable")
destination =  driver.find_element(By.ID,"droppable")
actions2 = ActionChains(driver)
actions2. drag_and_drop(source,destination).perform()
time.sleep(5)
driver.close()

