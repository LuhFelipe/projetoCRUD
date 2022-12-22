# Importando SQLite
import sqlite3 as lite

# Criando conexão
con = lite.connect("dados.db")

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, diaEm DATA, estado TEXT, assunto TEXT)")
