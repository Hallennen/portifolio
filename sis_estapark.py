import os
from datetime import datetime
import psycopg2
import time

#SISTEMA DE ESTACIONAMENTO """ESTAPARK"""
def menu():
    os.system('cls')
    print('''\t**** ESCOLHA A OPÇÃO DESEJADA: ****\n
            0 - FECHAR APLICAÇÃO
            1 - ENTRADA
            2 - SAIDA''')

def conect_bd():
    global cursor
    global conexao
    conexao = psycopg2.connect (host='127.0.0.1', database='estapark',user='postgres',password='1804')
    cursor = conexao.cursor()


def data_hora():
    global data
    global date
    global hora_entrada
    date = datetime.now()
    data = date.strftime('%d/%m/%y - %H:%M')
    hora_entrada = date.strftime('%H:%M')



def text_padrao_entrada():
    data_hora()
    os.system('cls')
    print('\t   ****ESTAPARK****\n\n',
        'Rua Mexi-cu, n69 - Centro.\n',
        'São Paulo, CNPJ: 89.878.789/0001-02\n',
        'Whatsapp CEL: 11 91234-5678\n\n'
        ' PLACA: ',formataca_placa,
        '\n MODELO: ', modelo,
        '\n ENTRADA: ', data,
        '\n\n ABERTO DE SEG A SEX DAS 9h AS 19h.',
        '\n OBRIGADO PELA PREFERENCIA, VOLTE SEMPRE!',)



def text_padrao_saida():
    data_hora()
    os.system('cls')
    print('\t   ****ESTAPARK****\n\n',
        'Rua Mexi-cu, n69 - Centro.\n',
        'São Paulo, CNPJ: 89.878.789/0001-02\n',
        'Whatsapp CEL: 11 91234-5678\n\n'
        ' PLACA: ', formataca_placa,
        '\n MODELO: ', modelo,
        '\n SAIDA: ', data)




def tempo():
    data_hora()
    global tempo_de_permanencia
    global hora_permanencia
    primeirapt_hora_entrada = horah[:2]
    segundapt_hora_entrada = horah[3:5]

    primeirapt_hora_saida = hora_saida[:2]
    segundapt_hora_saida = hora_saida[3:5]
    
    hora_permanencia = int(primeirapt_hora_saida) - int(primeirapt_hora_entrada)
    minuto_permanencia = int(segundapt_hora_saida) - int(segundapt_hora_entrada)
    tempo_de_permanencia = str(hora_permanencia) + ':' + str(minuto_permanencia)

    if hora_permanencia >= 0:
        valor = 5
    elif hora_permanencia > 2:
        valor = 7
    elif hora_permanencia > 4:
        valor = 10
    elif hora_permanencia > 5:
        valor = 12
    elif hora_permanencia > 12:
        valor = 25

    print(' TEMPO DE PERMANENCIA: ',tempo_de_permanencia,
            '\n     ',horah + '-' + hora_saida,
            '\n VALOR: ', valor ,'REAIS'
            '\n\n ABERTO DE SEG A SEX DAS 9h AS 19h.',
            '\n OBRIGADO PELA PREFERENCIA, VOLTE SEMPRE!')

    

def salvarbd():
    conect_bd()
    insert = """INSERT INTO estapark (placa_car, modelo_car, hora_entrada, hora_saida)
                    VALUES ('{}','{}','{}','{}')""".format(formataca_placa,modelo,hora_entrada,hora_entrada)
    cursor.execute(insert)
    conexao.commit()
    conexao.close()
    print('deu certo')


resposta_menu = 4
while resposta_menu != 0:
    menu()
    resposta_menu = int(input('Opção: '))
    while len(str(resposta_menu)) == 0 or resposta_menu <0 or resposta_menu >2 :
        print('OPÇÃO INVALIDA')
        resposta_menu = int(input('Opção: '))
        

    if resposta_menu == 1:
        #ENTRADA
        placa_veiculo = input(str('INFORME A PLACA DO VEICULO: ')).upper()
        while len(placa_veiculo) !=7 :
            print('placa invalida, informe novamente')
            placa_veiculo = input(str('INFORME A PLACA DO VEICULO: ')).upper()

        modelo= input('INFORME O MODELO DO VEICULO: ').upper()
        formataca_placa = placa_veiculo[0:3] + '-' + placa_veiculo[3:8]
        text_padrao_entrada()
        salvarbd()
        input('PRESSIONE QUALQUER TECLA PARA SEGUIR')

    elif resposta_menu == 2:
        #SAIDA
        try:
            data_hora()
            placa_veiculo = input(str('INFORME A PLACA DO VEICULO: ')).upper()
            while len(placa_veiculo) !=7 :
                print('placa invalida, informe novamente')
                placa_veiculo = input(str('INFORME A PLACA DO VEICULO: ')).upper()
            formataca_placa = placa_veiculo[0:3] + '-' + placa_veiculo[3:8]
            hora_saida = date.strftime('%H:%M')
            
            
            conect_bd()
            busca_placa = """SELECT placa_car, modelo_car, hora_entrada FROM estapark WHERE placa_car = '{}'""".format(formataca_placa)
            cursor.execute(busca_placa)
            atualiza_hora_saida = """UPDATE estapark
                                        SET hora_saida = '{}'
                                        WHERE placa_car = '{}'""".format(str(hora_saida),formataca_placa)
            cursor.execute(atualiza_hora_saida,busca_placa)
            cursor.execute(busca_placa)
            retorno_info = cursor.fetchone()
            conexao.commit()
            conexao.close()
            placa_validada = retorno_info[0]
            modelo = retorno_info[1]
            horah = retorno_info[2]
         
        

            if formataca_placa == placa_validada:
                text_padrao_saida()
                tempo()
                print('veiculo saindo!!')
                input('PRESSIONE QUALQUER TECLA PARA SEGUIR')


        except:
            print('Placa do veiculo não encontrada.')
            time.sleep(3)

    else:
        break

print('fechando')

