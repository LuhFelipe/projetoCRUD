#Importando o Tkinder
from cgitb import text
from tkinter import *
from tkinter import font

from tkinter import ttk

#Importando o Tkcalendar
from tkcalendar import Calendar, DateEntry


################# cores ###############
cor0 = "#f0f3f5"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#4fa882"  # verde
cor3 = "#38576b"  # valor
cor4 = "#403d3d"   # letra
cor5 = "#e06636"   # - profit
cor6 = "#038cfc"   # azul
cor7 = "#ef5350"   # vermelha
cor8 = "#263238"   # + verde
cor9 = "#e9edf5"   # sky blue

################# criando Janela ###############
janela = Tk()
janela.title()
janela.geometry("1043x453")
janela.configure(background = cor9)
janela.resizable(width = FALSE, height = FALSE)

################# dividindo Janela ###############
frameCima = Frame(janela, width = 310, height = 50, bg = cor2, relief = "flat")
frameCima.grid(row = 0, column = 0)

frameBaixo = Frame(janela, width = 310, height = 403, bg = cor1, relief = "flat")
frameBaixo.grid(row = 1, column = 0, sticky = NSEW, padx = 0, pady = 1,) 

frameDireita = Frame(janela, width = 588, height = 403, bg = cor1, relief = "flat")
frameDireita.grid(row = 0, column = 1, rowspan = 2, padx = 1, pady = 0, sticky = NSEW) 

################# label Cima ###############
appNome = Label(frameCima, text = "Formulário de Consultoria", anchor = NW, font = ("Ivy 13 bold"), bg = cor2, fg = cor1, relief = "flat")
appNome.place(x = 15, y = 20)
#pesquisar o que é label

################# Configurando frame Baixo ###############
#Nome
lNome = Label(frameBaixo, text = "Nome *", anchor = NW, font = ("Ivy 9 bold"), bg = cor1, fg = cor4, relief = "flat")
lNome.place(x = 15, y = 10)
#entrada
eNome = Entry(frameBaixo, width = 45, justify = "left", relief = "solid")
eNome.place(x = 15, y = 40)
#==
#Email
lEmail = Label(frameBaixo, text = "Email *", anchor = NW, font = ("Ivy 9 bold"), bg = cor1, fg = cor4, relief = "flat")
lEmail.place(x = 15, y = 70)
#entrada
eEmail = Entry(frameBaixo, width = 45, justify = "left", relief = "solid")
eEmail.place(x = 15, y = 100)
#==
#Telefone
lTelefone = Label(frameBaixo, text = "Telefone *", anchor = NW, font = ("Ivy 9 bold"), bg = cor1, fg = cor4, relief = "flat")
lTelefone.place(x = 15, y = 130)
#entrada
eTelefone = Entry(frameBaixo, width = 45, justify = "left", relief = "solid")
eTelefone.place(x = 15, y = 160)
#==
#Data da Consulta
lCal = Label(frameBaixo, text = "Data da Consulta *", anchor = NW, font = ("Ivy 9 bold"), bg = cor1, fg = cor4, relief = "flat")
lCal.place(x = 15, y = 190)
#entrada
eCal = DateEntry(frameBaixo, width = 12, background = "dackblue", foreground = "white", borderwidth = 2, year = 2022)
eCal.place(x = 15, y = 219)
#==
#Estado
lEstado = Label(frameBaixo, text = "Estado da Consulta *", anchor = NW, font = ("Ivy 9 bold"), bg = cor1, fg = cor4, relief = "flat")
lEstado.place(x = 160, y = 190)
#entrada
eEstado = Entry(frameBaixo, width = 20, justify = "left", relief = "solid")
eEstado.place(x = 160, y = 220)
#==
#Sobre
lSobre = Label(frameBaixo, text = "Informações extras *", anchor = NW, font = ("Ivy 9 bold"), bg = cor1, fg = cor4, relief = "flat")
lSobre.place(x = 15, y = 260)
#entrada
eSobre = Entry(frameBaixo, width = 45, justify = "left", relief = "solid")
eSobre.place(x = 15, y = 290)
#==

#Botão Inserir
bInserir = Button(frameBaixo, text = "Inserir", width = 10, font = ("Ivy 9 bold"), bg = cor6, fg = cor1, relief = "raised", overrelief = "ridge")
bInserir.place(x = 15, y = 340)

#Botão Atualizar
bAtualizar = Button(frameBaixo, text = "Atualizar", width = 10, font = ("Ivy 9 bold"), bg = cor2, fg = cor1, relief = "raised", overrelief = "ridge")
bAtualizar.place(x = 110, y = 340)

#Botão Deletar
bDeletar = Button(frameBaixo, text = "Deletar", width = 10, font = ("Ivy 9 bold"), bg = cor7, fg = cor1, relief = "raised", overrelief = "ridge")
bDeletar.place(x = 205, y = 340)



################# frame Direita ###############

lista = [[1,'Joao Futi Muanda','joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
           [2,'Fortnato Mpngo', 'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
           [3,'Usando Python',  'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
           [4,'Clinton Berclidio', 'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
           [5,'A traicao da Julieta','joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente']
           ]

#lista para cabeçario
tabelaHead = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']


#criando a Tabela
tree = ttk.Treeview(frameDireita, selectmode="extended", columns=tabelaHead, show="headings")

#vertical Scrollbar
vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

#horizontal Scrollbar
hsb = ttk.Scrollbar( frameDireita, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

frameDireita.grid_rowconfigure(0, weight=12)


hd=["nw","nw","nw","nw","nw","center","center"]
h=[30,170,140,100,120,50,100]
n=0

for col in tabelaHead:
    tree.heading(col, text=col.title(), anchor=CENTER)
    # adjust the column's width to the header string
    tree.column(col, width=h[n],anchor=hd[n])
    
    n+=1

for item in lista:
    tree.insert('', 'end', values=item)









janela.mainloop()