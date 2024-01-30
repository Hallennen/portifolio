import requests, os , time
from bs4 import BeautifulSoup

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

            ticker = leitor.find("h1", class_="headerTicker__content__title")
            nome = leitor.find(class_="headerTicker__content__name")
            preco = leitor.find(class_ ="headerTicker__content__price")
            informacoes = leitor.find_all(id="indicators")
            print('FUNDO: ', ticker.text,' - ', nome.text)
            print('\nPreço: ',preco.text[1:9])
            print(informacoes[1].text)

            fundo = input('Tecle enter para continuar ou "n" para sair: ')
        except:
            print('\033[1;31m NÃO ENCONTRADO FUNDO COM ESSA ABREVIAÇÃO \033[m \n')
            time.sleep(2)