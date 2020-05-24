from lib.interface import *
from lib.database import *
from time import sleep

connect()
cabecalho('GERENCIADOR DE SENHAS')
senha_master = '123456'
senha = str(input('Insira sua senha master: '))
if senha == senha_master:
    cabecalho(f'{cor(3)}BEM VINDO!{cor(0)}')

    while True:
        menu()
        print(linha())
        d = escolha(f'{cor(3)}SUA OPÇÃO:{cor(0)} ')
        print(linha())
        sleep(2)
        if d == 'disconnect':
            break
else:
    cabecalho(f'''{cor(1)}SENHA INVÁLIDA!{cor(0)} Encerrando...''')

disconnect()
