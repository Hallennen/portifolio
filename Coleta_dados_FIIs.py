import requests
from bs4 import BeautifulSoup
import os
import time

site_base = 'https://www.fundsexplorer.com.br/funds/'

fundo = 'S'

while fundo != 'n' :
    os.system('cls')
    fundo = input('Escolha qual fundo deseja consultar a cotação: ').upper()
    if fundo == 'N':
        break
    else:
        try:

            site = site_base+fundo

            conteudo = requests.get(site).content

            leitor = BeautifulSoup(conteudo,'html.parser')

            preco = leitor.find("span", class_ ="price")
            nome = leitor.find("h1", class_="section-title")
            dividendo = leitor.find_all("span", class_= "indicator-value")
            print('Fundo: ',nome.text)
            print('Preço: ',preco.text[19:27])
            print('Ultimo dividendo: ', dividendo[1].text[17:24])
            print('Patrimonio L: ', dividendo[3].text[17:26])
            print('P/VP: ', dividendo[6].text[17:24])

            fundo = input('Tecle enter para continuar ou "n" para sair: ')
        except:
            print('\033[1;31m NÃO ENCONTRADO FUNDO COM ESSA ABREVIAÇÃO \033[m \n')
            time.sleep(2)