from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from time import sleep

def iniciar_driver():
    chrome_options = Options()
    chrome_options.binary_location = '/home/matheus-yan/Downloads/chrome-linux64/chrome'
    chrome_options.add_argument('--window-size=1000,1000')
    service = Service('/usr/bin/chromedriver')

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

driver = iniciar_driver()
driver.get('https://10fastfingers.com/typing-test/portuguese')

div_element = driver.find_element(By.ID, 'row1')
texto = div_element.find_elements(By.TAG_NAME, 'span')
campo = driver.find_element(By.ID,'inputfield')

for span in texto:
    temp = span.text
    campo.send_keys(temp)
    campo.send_keys(' ')

input()
driver.quit()
