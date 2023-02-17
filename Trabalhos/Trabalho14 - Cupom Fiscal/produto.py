import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

class Produto():
    def __init__(self, codigo, descricao, valorUnitario) -> None:
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valorUnitario = valorUnitario

    @property
    def codigo (self):
        return self.__codigo
    
    @property
    def descricao (self):
        return self.__descricao

    @property
    def valorUnitario (self):
        return self.__valorUnitario

class LimiteInsereProduto(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100+500+200')
        self.title("Produto")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.frameValor = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameDescricao.pack()
        self.frameValor.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.labelDescricao = tk.Label(self.frameDescricao,text="Descrição: ")
        self.labelValor = tk.Label(self.frameValor,text="Valor Unitario: ")
        self.labelCodigo.pack(side="left")
        self.labelDescricao.pack(side="left")
        self.labelValor.pack(side="left")  

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputDescricao = tk.Entry(self.frameDescricao, width=20)
        self.inputDescricao.pack(side="left")  
        self.inputValor = tk.Entry(self.frameValor, width=20)
        self.inputValor.pack(side="left")            
      
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

class LimiteMostraProduto():
    def __init__(self, str):
        messagebox.showinfo('Lista de Produtos', str)

class LimiteConsultaProduto(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x200+500+200')
        self.title("Consulta Produtos")
        self.controle = controle 

        self.frameCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.labelCodigo.pack(side="left")  

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")             

        self.buttonConsultar = tk.Button(self.frameButton ,text="Consultar")      
        self.buttonConsultar.pack(side="left")
        self.buttonConsultar.bind("<Button>", controle.consultarHandler)

        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.limparHandler) 

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlProduto():
    def __init__(self):
        if not os.path.isfile("/Users/Letícia/Documents/Development/Orientada_a_Objetos/Trabalhos/Trabalho14 - Cupom Fiscal/produto.pickle"):
            self.listaProdutos =  []
        else:
            with open("/Users/Letícia/Documents/Development/Orientada_a_Objetos/Trabalhos/Trabalho14 - Cupom Fiscal/produto.pickle", "rb") as f:
                self.listaProdutos = pickle.load(f)

    def salvaProdutos(self):
        if len(self.listaProdutos) != 0:
            with open("/Users/Letícia/Documents/Development/Orientada_a_Objetos/Trabalhos/Trabalho14 - Cupom Fiscal/produto.pickle","wb") as f:
                pickle.dump(self.listaProdutos, f)

    def insereProduto(self):
        self.limiteIns = LimiteInsereProduto(self) 
    
    def mostraProduto(self):
        msg = 'Produto: \n\n'
        for prod in self.listaProdutos:
            msg += str(prod.codigo) + ' - ' + prod.descricao + ' - ' + str(prod.valorUnitario) + '\n'    
        self.limiteLista = LimiteMostraProduto(msg)
    
    def consultaProduto(self):
        self.limiteIns = LimiteConsultaProduto(self)

    def getProduto(self, codigo):
        prodReg = None
        for prod in self.listaProdutos:
            if prod.codigo == codigo:
                prodReg = prod
        return prodReg

    def getListaCodigo(self):
        listaCod = []
        for prod in self.listaProdutos:
            listaCod.append(prod.codigo)
        return listaCod

    def enterHandler(self, event):
        cod = self.limiteIns.inputCodigo.get()
        desc = self.limiteIns.inputDescricao.get()
        valUni = self.limiteIns.inputValor.get()
        produto = Produto(cod, desc, valUni)
        self.listaProdutos.append(produto)
        self.limiteIns.mostraJanela('Sucesso', 'Produto cadastrado com sucesso')
        self.clearHandler(event)

    def consultarHandler(self,event):
        cod = self.limiteIns.inputCodigo.get()
        cont = 0
        for prod in self.listaProdutos:
            cont += 1
            if  prod.codigo  == cod:
                msg = str(prod.codigo) + ' - ' + prod.descricao + ' - ' + str(prod.valorUnitario)
                self.limiteIns.mostraJanela('Dados do Produto', msg)
                break 
            elif cont == len(self.listaProdutos):
                self.limiteIns.mostraJanela('Erro', 'Produto não encontrado!')
                break
    
    def limparHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputDescricao.delete(0, len(self.limiteIns.inputDescricao.get()))
        self.limiteIns.inputValor.delete(0, len(self.limiteIns.inputValor.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()