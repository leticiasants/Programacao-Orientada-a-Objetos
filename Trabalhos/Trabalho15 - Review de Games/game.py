import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from math import *
import os.path
import pickle

class Jogo:
    def __init__(self, codigo, titulo, console, genero, preco):
        self.__codigo = codigo
        self.__titulo = titulo
        self.console = console
        self.genero = genero
        self.preco = preco
        self.__avaliacoes = []
    
    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def console(self):
        return self.__console

    @console.setter
    def console(self, valor):
        self.consoles = ["XBox", "PlayStation", "Switch", "PC"]
        if not valor in self.consoles:
            raise ValueError("Tipo inválido: {}".format(valor))
        else:
            self.__console = valor

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, valor):
        self.generos = ["Ação", "Aventura", "Estratégia", "RPG", "Esporte", "Simulação"]
        if not valor in self.generos:
            raise ValueError("Variedade inválida: {}".format(valor))
        else:
            self.__genero = valor
            
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor < 0 or valor > 500:
            raise ValueError("Valor inválido: {}".format(valor))
        else:
            self.__preco = valor
    
    @property
    def avaliacoes(self):
        return self.__avaliacoes

    def addAvaliacoes(self, avaliacao):
        self.__avaliacoes.append(avaliacao)

    def mediaAvaliacoes(self):
        cont1 = 0
        cont2 = 0
        for aval in self.__avaliacoes:
            cont1 += aval
            cont2 += 1
        media = cont1/cont2
        if media >= 0 and media <= 1: return 1
        if media > 1 and media <= 2: return 2
        if media > 2 and media <= 3: return 3
        if media > 3 and media <= 4: return 4
        if media > 4 and media <= 5: return 5

    def getJogo(self):
        return "Titulo: " + str(self.titulo)\
        + "\nCodigo: " + str(self.codigo)\
        + "\nConsole: " + str(self.console)\
        + "\nGênero: " + str(self.genero)\
        + "\nPreço: " + str(self.preco)\
        + "\nAvaliações: " + str(self.mediaAvaliacoes())
    
class LimiteInsereGame(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200+500+200')
        self.title("Jogo")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameTitulo = tk.Frame(self)
        self.frameConsole = tk.Frame(self)
        self.frameGenero = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCodigo.pack()
        self.frameTitulo.pack()
        self.frameConsole.pack()
        self.frameGenero.pack()
        self.framePreco.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelTitulo = tk.Label(self.frameTitulo,text="Título: ")
        self.labelConsole = tk.Label(self.frameConsole, text="Console: ")
        self.labelGenero = tk.Label(self.frameGenero, text="Gênero: ")
        self.labelPreco = tk.Label(self.framePreco, text="Preco: ")
        self.labelCodigo.pack(side="left")
        self.labelTitulo.pack(side="left")
        self.labelConsole.pack(side="left")
        self.labelGenero.pack(side="left")
        self.labelPreco.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputConsole = tk.Entry(self.frameConsole, width=15)
        self.inputGenero = tk.Entry(self.frameGenero, width=20)
        self.inputPreco = tk.Entry(self.framePreco, width=10)
        self.inputCodigo.pack(side="left")
        self.inputTitulo.pack(side="left")
        self.inputConsole.pack(side="left")
        self.inputGenero.pack(side="left")
        self.inputPreco.pack(side="left")
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteAvaliaGame(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200+500+200')
        self.title("Avalia Jogo")
        self.controle = controle 

        self.frameCodigo = tk.Frame(self)
        self.frameAvaliacao = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodigo.pack()
        self.frameAvaliacao.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelCodigo.pack(side="left")
        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)
        self.inputCodigo.pack(side="left")

        self.labelAvaliacao = tk.Label(self.frameAvaliacao,text='Avaliação: ')
        self.labelAvaliacao.pack(side="left")
        self.escolhaAvaliacao = tk.StringVar()
        self.comboboxAvaliacao = ttk.Combobox(self.frameAvaliacao, width = 15 , textvariable = self.escolhaAvaliacao)
        self.comboboxAvaliacao.pack(side="left")
        listaAvaliacoes = ['1 estrela', '2 estrelas', '3 estrelas', '4 estrelas', '5 estrelas'] 
        self.comboboxAvaliacao['values'] = listaAvaliacoes

        self.buttonSubmit = tk.Button(self.frameButton ,text="Adicionar avaliação")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.addHandler)
      
        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaGame(tk.Toplevel):
    def __init__(self, avaliacoes, controle):

        tk.Toplevel.__init__(self)
        self.geometry('400x250+500+200')
        self.title("Consultar Jogos")
        self.ctrl = controle

        self.frameCombo = tk.Frame(self)
        self.frameCombo.pack(pady=3)

        self.labelAvaliacao = tk.Label(self.frameCombo,text="Avaliações: ")
        self.labelAvaliacao.pack(side="left")
        self.escolhaAvaliacao = tk.StringVar()
        self.comboboxAvaliacao = ttk.Combobox(self.frameCombo, width = 15 ,values=avaliacoes, textvariable = self.escolhaAvaliacao)
        self.comboboxAvaliacao.pack(side="left")
        self.comboboxAvaliacao.bind("<<ComboboxSelected>>", self.ctrl.exibeAvaliacao)

        self.frameJogos = tk.Frame(self)
        self.frameJogos.pack()
        self.textJogos = tk.Text(self.frameJogos, height=20,width=40)
        self.textJogos.pack()
        self.textJogos.config(state=tk.DISABLED)

class CtrlGame():
    def __init__(self, controlador):
        self.ctrlPrincipal = controlador
        if not os.path.isfile("/Users/Letícia/Documents/Development/Orientada_a_Objetos/Trabalhos/Trabalho15 - Review de Games/game.pickle"):
            self.listaJogos =  []
        else:
            with open("/Users/Letícia/Documents/Development/Orientada_a_Objetos/Trabalhos/Trabalho15 - Review de Games/game.pickle", "rb") as f:
                self.listaJogos = pickle.load(f)

    def cadastraGame(self):
        self.limiteIns = LimiteInsereGame(self)
    
    def avaliaGame(self):
        self.limiteIns = LimiteAvaliaGame(self)

    def consultaGame(self):
        self.avaliacoes = ['1 estrela', '2 estrelas', '3 estrelas', '4 estrelas', '5 estrelas']           
        self.limiteCons = LimiteConsultaGame(self.avaliacoes, self)

    def salvaJogos(self):
        if len(self.listaJogos) != 0:
            with open("/Users/Letícia/Documents/Development/Orientada_a_Objetos/Trabalhos/Trabalho15 - Review de Games/game.pickle","wb") as f:
                pickle.dump(self.listaJogos, f)
    
    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        titulo = self.limiteIns.inputTitulo.get()
        console = self.limiteIns.inputConsole.get()
        genero = self.limiteIns.inputGenero.get()
        preco = int(self.limiteIns.inputPreco.get())

        try:
            jogo = Jogo(codigo, titulo, console, genero, preco)
            self.listaJogos.append(jogo)            
            self.limiteIns.mostraJanela('Sucesso', 'Jogo cadastrado com sucesso')
            self.clearHandler(event)
        except ValueError as error:
            self.limiteIns.mostraJanela('Erro', error)            
    
    def addHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        avalSel  = self.limiteIns.escolhaAvaliacao.get()
        cont1 = 0
        if avalSel == '1 estrela': aval = 1
        elif avalSel == '2 estrelas': aval = 2
        elif avalSel == '3 estrelas': aval = 3
        elif avalSel == '4 estrelas': aval = 4
        else: aval = 5

        for jogo in self.listaJogos:
            cont1 += 1
            if jogo.codigo == codigo:
                jogo.addAvaliacoes(aval)
                self.limiteIns.mostraJanela('Sucesso', 'Avaliação adicionada com sucesso')
                break
            elif cont1 == len(self.listaJogos):
                self.limiteIns.mostraJanela('Erro', 'Jogo não cadastrado')
        
  
    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.inputConsole.delete(0, len(self.limiteIns.inputConsole.get()))
        self.limiteIns.inputGenero.delete(0, len(self.limiteIns.inputGenero.get()))
        self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def exibeAvaliacao(self,event):
        avalSel = self.limiteCons.comboboxAvaliacao.get()
        aval = int(avalSel[0])
        self.limiteCons.textJogos.config(state='normal')
        self.limiteCons.textJogos.delete("1.0", tk.END)
        for jogo in self.listaJogos:
            if(jogo.mediaAvaliacoes() == aval):
                jogoSel = jogo.getJogo() + '\n\n'
                self.limiteCons.textJogos.insert(1.0, jogoSel)
        self.limiteCons.textJogos.config(state='disable')
