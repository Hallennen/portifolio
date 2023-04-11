import random
import time
from win10toast import ToastNotifier

toaster = ToastNotifier()

lista= (1,2,3,4,5,6,7,8,9)
pin = 0
num = 1

while pin != num:
    num = random.choice(lista)

    toaster.show_toast(
        "notificação",
        'SEU CODIGO DE ACESSO É: '+  str(num),
        threaded=True,
        icon_path=None,
        duration=4
    )

    pin = int(input('informe o pin: '))

    if pin == num:
        print('está correto!')
    else:
        print("PIN incorreto")

input()



    
