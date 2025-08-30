#this script will set textfield value
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.shivaconceptsolution.com")
l=driver.find_elements(By.TAG_NAME,"img")
f=open("imagepath.txt","w")
for data in l:
    print("image name is ",data.get_attribute("src"))
    f.write(data.get_attribute("src")+"\n")
f.close()
print("total images are",len(l))
time.sleep(1)
#driver.close()
