import random
import time
from win10toast import ToastNotifier

toaster = ToastNotifier()

lista = 2

def num_aleatorio():
    global lista
    lista= random.randint(1,100)
    return lista

pin = 0


while pin != lista:
    num_aleatorio()

    toaster.show_toast(
        "notificação",
        'SEU CODIGO DE ACESSO É: '+  str(lista),
        threaded=True,
        icon_path=None,
        duration=4
    )

    pin = int(input('informe o pin: '))

    if pin == lista:
        print('está correto!')
    else:
        print("PIN incorreto")

input()



    
