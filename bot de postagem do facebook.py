from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=900,800', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument) 
    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': 'E:\\Storage\\Desktop',
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values_automatic_dowloads': 1, 
    })
    driver = webdriver.Chrome(options=chrome_options) 
    return driver
driver = iniciar_driver()
driver.get('https://facebook.com') 
sleep(2)

# ações repetitivas:
def preencher_campo(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep((randint(1, 5)/40))

# ELEMENTOS da tela de LOGIN:
try:
    campo_email = driver.find_element(By.ID, 'email')
    campo_senha = driver.find_element(By.ID, 'pass')
    botao_entrar = driver.find_element(By.XPATH, '//button[@name="login"]')

except:
    print('Não localizamos os elementos necessários para concluir o cadastro.')
    exit()

# LOGIN-EMAIL:
email = '' # -> VOCE DEVE PREENCHER AS INFORMAÇÕES AQUI
preencher_campo(email, campo_email)
sleep(0.8)

# LOGIN-SENHA
senha = '' # -> VOCE DEVE PREENCHER AS INFORMAÇÕES AQUI
preencher_campo(senha, campo_senha)
sleep(0.8)

# CLICANDO ENTER:
botao_entrar.click()

# CAPTCHA! --> PASSO MANUAL!
print('Pressione Enter após concluir o CAPTCHA!!')
input('')
sleep(2)

# --------------------------------------------------------------------------------------

# ELEMENTO PAGINA INICIAL
try:
    campo_publicação = driver.find_element(By.XPATH, "//div[@tabindex='0']//span[@style='-webkit-box-orient:vertical;-webkit-line-clamp:2;display:-webkit-box']")
except:
    print('Não foi possível encontrar os elementos do menu principal do Facebook')
    exit()
sleep(0.5)

# CLICANDO PARA IR AO CAMPO PARA DIGITAR:
campo_publicação.click()
sleep(1)

# ELEMENTO PARA DIGITAR
try:
    campo_escrever_publicação = driver.find_element(By.XPATH, "//div[@style='user-select: text; white-space: pre-wrap; word-break: break-word; font-size: 24px;']")
except:
    print('Não foi possível encontrar os elementos do menu principal do Facebook')

# ESCREVENDO PUBLICAÇÃO:
texto_publicação = 'Oi, isso foi feito por um robô!' # PUBLICAÇÃO A SER FEITA-> 
preencher_campo(texto_publicação, campo_escrever_publicação)
campo_escrever_publicação.send_keys(Keys.ENTER)
