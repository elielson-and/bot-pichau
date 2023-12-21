import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://voidseek.com/login')

button = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/form/div[4]/button')
button.click()


time.sleep(10)

