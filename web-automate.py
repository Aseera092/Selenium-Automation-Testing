import time
from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
try:
    driver.get("http://127.0.0.1:5500/index.html")
    time.sleep(5)
    check_element=driver.find_element(By.TAG_NAME,"h3")
    if check_element.text.strip()=="FISAT":
        nameTextBox=driver.find_element(By.NAME,"fname")
        # rowTextBox=driver.find_element(By.NAME,"")
        nameTextBox.send_keys("Asee")
        time.sleep(3)
        print("Test Passed")
    else:
        print("Test Failed")
finally:
    driver.quit()