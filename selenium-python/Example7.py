from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://eroomrent.in/index.php")
driver.maximize_window()
dropdown = Select(driver.find_element("name","ddlcat"))
# Select by visible text
dropdown.select_by_visible_text("Flat")
time.sleep(5)
dropdown = Select(driver.find_element("id","subcat"))
# Select by visible text
dropdown.select_by_index(2)
time.sleep(3)
dropdown = Select(driver.find_element("id","location"))
# Select by visible text
dropdown.select_by_index(2)
time.sleep(3)
element = driver.find_element(By.CLASS_NAME, "btn-one")
element.click()
time.sleep(3)
driver.quit()

