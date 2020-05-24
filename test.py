import sqlite3

conn = sqlite3.connect('senhas.db')
c = conn.cursor()
try:
    c.execute('''CREATE TABLE senhas(site,login,senha)''')
except sqlite3.OperationalError:
    print('Tabela já criada')
else:
    print("Tabela criada")

c.execute('SELECT * from senhas')
for row in c:
    if row[0] == 'FIBRAOT':
        print(row)

conn.commit()
conn.close()