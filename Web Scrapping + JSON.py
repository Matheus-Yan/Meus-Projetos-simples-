from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from time import sleep
import json

def pegar_elementos(quote):
    frase = quote.find_element(By.CLASS_NAME, 'text').text
    autor = quote.find_element(By.CLASS_NAME, 'author').text
    tags_sujo = quote.find_elements(By.CLASS_NAME, 'tag')
    tags = [tag.text for tag in tags_sujo]
    return frase,autor,tags

def iniciar_driver():
    chrome_options = Options()
    chrome_options.binary_location = '/home/matheus-yan/Downloads/chrome-linux64/chrome'
    chrome_options.add_argument('--window-size=2000,2000')
    chrome_options.add_argument("--force-device-scale-factor=0.30")
    service = Service('/usr/bin/chromedriver')

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

driver = iniciar_driver()
driver.get('https://quotes.toscrape.com/')
sleep(0.3)


dicionario = []
while True:
    quotes = driver.find_elements(By.CLASS_NAME,'quote')
    sleep(0.3)

    for quote in quotes:
        frase,autor,tags = pegar_elementos(quote)
        entrada = {
            'frase': frase,
            'autor': autor,
            'tags': tags
        }

        sleep(0.3)
        dicionario.append(entrada)
    try:
        link = driver.find_element(By.CLASS_NAME, 'next')
        clicke = link.find_element(By.TAG_NAME, 'a')
        clicke.click()
    except:
        break
with open('scrap.json','w', encoding='utf-8') as f:
    json.dump(dicionario, f, ensure_ascii=False, indent=4)
