import random

lista = "abcdefghijklmnopqrstuvwxyz123456789!@##$%&*()_+"

tam_senha = int(input('Digite o tamanho da senha que deseja: '))

senha = "".join(random.sample(lista,tam_senha))
print('senha: ', senha)

input('tecle enter para encerrar')
