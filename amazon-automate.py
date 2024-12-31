from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
time.sleep(5)
try:
    driver.get("https://www.amazon.in/")
    time.sleep(5)
    check_element=driver.find_element(By.ID,"twotabsearchtextbox")
    check_element.send_keys("iphone 15")
    time.sleep(6)
    check_element.send_keys(Keys.ENTER)
    print("Test Passed")
finally:
    driver.quit()