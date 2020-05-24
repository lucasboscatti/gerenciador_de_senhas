from lib.database import *
from time import sleep


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu():
    print(f'''{cor(3)}1{cor(0)} -{cor(4)} Adicionar nova conta
{cor(3)}2{cor(0)} -{cor(4)} Resgatar os dados de uma conta
{cor(3)}3{cor(0)} -{cor(4)} Ver sites/jogos cadastrados
{cor(3)}4{cor(0)} -{cor(4)} Deletar uma conta
{cor(3)}5{cor(0)} -{cor(4)} Sair do gerenciador de senhas{cor(0)}''')


def escolha(txt):
    while True:
        op = str(input(txt)).strip()
        if op not in ['1', '2', '3', '4', '5']:
            print(f'{cor(1)}ERRO! Digite uma opção válida!{cor(0)}')
        else:
            if op == '1':
                linha()
                nome = corrigir('Conta de qual site/jogo? ')
                login = corrigir('Qual login? ')
                senha = corrigir('Qual a senha?')
                linha()
                data(nome.upper(), login, senha)
                print(f'Conta do {nome} salva com sucesso!')
            elif op == '2':
                conta = checkDatas('Você quer informação de qual conta?')
                readData(conta)
            elif op == '3':
                cont = seeDatas()
                if cont == 0:
                    print('Ainda não há contas cadastradas!')
            elif op == '4':
                conta = checkDatas('Você quer deletar qual conta?')
                deleteData(conta)
            elif op == '5':
                print('Encerrando o gerenciador de senhas...')
                return 'disconnect'
            break


def cor(nome):
    cores = {'0': '\033[m',  # 0 - sem cores
             '1': '\033[1;31m',  # 1 - vermelho
             '2': '\033[1;32m',  # 2 - verde
             '3': '\033[1;33m',  # 3 - amarelo
             '4': '\033[1;34m',  # 4 - azul
             '5': '\033[1;35m',  # 5 - roxo
             '6': '\033[7;30m'  # 6 - branco
             }
    return cores[f'{nome}']