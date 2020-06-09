from lib.interface import *
from lib.database import *
from time import sleep

acessPasswordsUser()
cabecalho('GERENCIADOR DE SENHAS')
while True:
    name = str(input(f'{cor(3)}Login {cor(4)}(0 para criar nova conta){cor(0)}: '))
    if name == '0':
        createUser()
    else:
        check = checkUser(name)
        if check != 0:
            while True:
                senha = str(input(f'{cor(3)}senha{cor(0)}: '))
                checks = checkSenha(senha)
                if checks != 0:
                    break
                else:
                    print(f'{cor(1)}Senha incorreta! Tente novamente.{cor(0)}')
                    continue
            break
        else:
            print(f'{cor(1)}Usuário não encontrado ou erro de digitação{cor(0)}')
            continue
cabecalho(f'{cor(3)}BEM VINDO {name.upper()}!{cor(0)}')
while True:
    menu()
    print(linha())
    d = escolha(f'{cor(3)}SUA OPÇÃO:{cor(0)} ', name)
    print(linha())
    sleep(2)
    if d == 'disconnect':
        break

disconnect()
