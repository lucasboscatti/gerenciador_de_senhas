import sqlite3

# funcoes para database dos usuários


def acessPasswordsUser():
    global conn, c
    conn = sqlite3.connect('userPasswords.db')
    c = conn.cursor()
    try:
        c.execute(f'''CREATE TABLE user(username,userpass)''')
    except sqlite3.OperationalError:
        return False
    else:
        return True


def dataUser(login, senha):
    c.execute(f"INSERT INTO user(username,userpass) VALUES (?,?)", (login, senha))
    conn.commit()


def createUser():
    while True:
        register_name = str(input('Digite seu nome de usuário: ')).strip()
        exist = checkUser(register_name)
        if exist == 0:
            confirm_register_name = str(input(f'Deseja confirmar {register_name}? (S/N)')).upper()
            if confirm_register_name in ['N', 'NÃO', 'NAO']:
                continue
            elif confirm_register_name in ['S', 'SIM']:
                while True:
                    register_senha_master = str(input('Digite uma senha: '))
                    confirm_register_senha = str(input('Confirme sua senha: '))
                    if register_senha_master == confirm_register_senha:
                        dataUser(register_name, register_senha_master)
                        c.execute(f'''CREATE TABLE {register_name}passwords(site,login,senha)''')
                        print('Conta criada com sucesso!')
                        break
                    else:
                        print('\033[1;31mAs senhas são incompatíveis!\033[m')
                break
            else:
                print('\033[1;31mDigite apenas SIM ou NÃO (S/N)!\033[m')
        elif exist > 0:
            print(f'Usuário {register_name} já existe!')


def checkUser(name):
    c.execute(f'SELECT * FROM user')
    cont = 0
    for row in c:
        if row[0] == name:
            cont += 1
    return cont


def checkSenha(senha):
    c.execute(f'SELECT * FROM user')
    cont = 0
    for row in c:
        if row[1] == senha:
            cont += 1
    return cont


# funções para database de senhas do usuário

def data(name, nome, login, senha):
    c.execute(f"INSERT INTO {name}passwords(site,login,senha) VALUES (?,?,?)", (nome, login, senha))
    conn.commit()


def readData(name, site):
    c.execute(f'SELECT * from {name}passwords')
    for row in c:
        if row[0] == site:
            print(f'Login = {row[1]} / Senha = {row[2]}')


def checkDatas(txt, name):
    while True:
        site = str(input(txt)).upper().strip()
        c.execute(f'SELECT * FROM {name}passwords')
        for row in c:
            if row[0] == site:
                return site
        else:
            print(f"\033[1;31mERRO! Digite uma conta existe no gerenciador.\033[m")


def seeDatas(name):
    c.execute(f'SELECT * from {name}passwords')
    cont = 0
    for row in c:
        if row[0] is None:
            cont = 0
        else:
            print(row[0])
            cont += 1
    return cont


def deleteData(name, site):
    c.execute(f'''DELETE FROM {name}passwords WHERE site=?''', (site,))
    print(f'conta do {site} deletada com sucesso!')
    conn.commit()


def corrigir(txt):
    while True:
        nome = str(input(txt)).strip()
        certeza = str(input('Deseja confirmar essa informação? (S/N) ')).upper().strip()
        if certeza in ['S', 'SIM']:
            return nome
        elif certeza in ['N', 'NÃO', 'NAO']:
            continue
        else:
            print(f'\033[1;31mERRO! Digite apenas SIM ou NÃO (S/N)!\033[m')


def disconnect():
    conn.close()
