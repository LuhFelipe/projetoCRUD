#importando SQLite
import sqlite3 as lite

#criar conexão com banco de dados
con = lite.connect("dados.db")
    #como está na mesma pasta so colocar o nome

#CRUD
#C CREATE
#R READ
#U UPDATE
#D DELETE

lista = ['Joao Futi Muanda','joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente']
"""
#inserir Informações
with con:
    cur = con.cursor()
    query = "INSERT INTO formulario (nome, email, telefone, diaEm, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
    cur.execute(query, lista)
"""
#acessar Informações
with con:
    cur = con.cursor()
    query = "SELECT * FROM formulario"
    cur.execute(query)
    info = cur.fetchall()
    print(info)

"""
lista = ["joao", 1]
#atualizar Informações
with con:
    cur = con.cursor()
    query = "UPDATE formulario SET nome = ? WHERE id = ?"
    cur.execute(query, lista)
"""
"""
lista = [1]
#deletar Informações
with con:
    cur = con.cursor()
    query = "DELETE FROM formulario WHERE id = ?"
    cur.execute(query, lista)
    """