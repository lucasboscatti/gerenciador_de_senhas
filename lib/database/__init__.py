import sqlite3

conn = sqlite3.connect('senhas.db')
c = conn.cursor()


def connect():
    try:
        c.execute('''CREATE TABLE senhas(site,login,senha)''')
    except sqlite3.OperationalError:
        return False
    else:
        return True


def disconnect():
    conn.close()


def data(nome, login, senha):
    c.execute(f"INSERT INTO senhas VALUES ('{nome}','{login}','{senha}')")
    conn.commit()


def readData(site):
    c.execute('SELECT * from senhas')
    for row in c:
        if row[0] == site:
            print(f'Login = {row[1]} / Senha = {row[2]}')


def checkDatas(txt):
    while True:
        site = str(input(txt)).upper().strip()
        c.execute(f'SELECT * FROM senhas')
        for row in c:
            if row[0] == site:
                return site
        else:
            print(f"\033[1;31mERRO! Digite uma conta existe no gerenciador.\033[m")


def seeDatas():
    c.execute('SELECT * from senhas')
    cont = 0
    for row in c:
        print(row[0])
        cont += 1
    return cont


def deleteData(site):
    c.execute('''DELETE FROM senhas WHERE site=?''', (site,))
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

