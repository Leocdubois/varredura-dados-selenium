from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep

# Abrir navegador e entrar no site  
navegador = webdriver.Chrome()
navegador.get('https://devaprender-play.netlify.app/')

sleep(3)


# Anotar os nomes e os valores dos produtos
produtos = navegador.find_elements(By.XPATH, "//h3[@class='text-lg font-semibold text-gray-900 group-hover:text-indigo-600']")
valores = navegador.find_elements(By.XPATH, "//p[@class='text-2xl font-bold text-indigo-600']")

for produto, valor in zip(produtos, valores):
    with open('preços.csv', 'a' , encoding='utf-8') as arquivo: 
        arquivo.write(f'{produto.text},{valor.text}{os.linesep}')

input('') 