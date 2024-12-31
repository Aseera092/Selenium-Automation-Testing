import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
try:
    driver.get("https://www.google.com/")
    time.sleep(5)
    check_element=driver.find_element(By.ID,"APjFqb")
    check_element.send_keys("FISAT")
    time.sleep(6)
    check_element.send_keys(Keys.ENTER)
    print("Test passed")
finally:
    driver.quit()
