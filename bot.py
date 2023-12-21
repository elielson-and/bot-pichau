import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from core.environment.MainEnv import MainEnv as Env
env = Env()
credentials = env.credentials()
# Carregar os seletores XPath do arquivo JSON
with open('core/components/LoginComponents.json', 'r') as file:
    selectors = json.load(file)

chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://voidseek.com/login')

env = Env()

email_field = driver.find_element(By.XPATH, selectors['email_field']).send_keys(credentials['email'])
password_field = driver.find_element(By.XPATH, selectors['password_field']).send_keys(credentials['password'])
login_button = driver.find_element(By.XPATH, selectors['login_button']).click()

time.sleep(10)
