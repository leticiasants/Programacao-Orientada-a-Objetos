import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os.path
import pickle

class CupomFiscal():
    def __init__(self, nroCupom, itensCupons, quantProd) -> None:
        self.__nroCupom = nroCupom
        self.__itensCupom = itensCupons
        self.__quantProd = quantProd
    
    @property
    def nroCupom (self):
        return self.__nroCupom
    
    @property
    def itensCupons (self):
        return self.__itensCupom
    
    @property
    def quantProd (self):
        return self.__quantProd
    

class LimiteInsereCupom(tk.Toplevel):
    def __init__(self, controle, listaProdutos):

        tk.Toplevel.__init__(self)
        self.geometry('300x250+500+200')
        self.title("Cupom Fiscal")
        self.controle = controle

        self.frameNroCupom = tk.Frame(self)
        self.frameProduto = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNroCupom.pack()
        self.frameProduto.pack()
        self.frameButton.pack()        

        self.labelNroCupom = tk.Label(self.frameNroCupom,text="Número do cupom: ")
        self.labelNroCupom.pack(side="left")
        self.inputNroCupom = tk.Entry(self.frameNroCupom, width=20)
        self.inputNroCupom.pack(side="left")
          
        self.labelProduto = tk.Label(self.frameProduto,text="Adicione os produtos: ")
        self.labelProduto.pack(side="left") 
        self.listbox = tk.Listbox(self.frameProduto)
        self.listbox.pack(side="left")
        scrollbar = Scrollbar(self.frameProduto) 
        scrollbar.pack(side = RIGHT, fill = BOTH)
        for prod in listaProdutos:
            self.listbox.insert(tk.END, prod)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Produto")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereProduto)

        self.buttonCria = tk.Button(self.frameButton ,text="Fechar Cupom")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaCupom)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraCupom():
    def __init__(self, str):
        messagebox.showinfo('Lista de Cupons', str)

# Falta implementar
class LimiteConsultaCupom(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x200+500+200')
        self.title("Consulta Cupons")
        self.controle = controle 

        self.frameNroCupom = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNroCupom.pack()
        self.frameButton.pack()
      
        self.labelNroCupom = tk.Label(self.frameNroCupom,text="Número do cupom: ")
        self.labelNroCupom.pack(side="left")  

        self.inputNroCupom = tk.Entry(self.frameNroCupom, width=20)
        self.inputNroCupom.pack(side="left")             

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

class CtrlCupomFiscal():
    def __init__(self, ControlePrincipal):
        self.ctrlPrincipal = ControlePrincipal
        if not os.path.isfile("/Users/Letícia/Documents/Development/Orientada_a_Objetos/Trabalhos/Trabalho14 - Cupom Fiscal/cupom.pickle"):
            self.listaCupons =  []
        else:
            with open("/Users/Letícia/Documents/Development/Orientada_a_Objetos/Trabalhos/Trabalho14 - Cupom Fiscal/cupom.pickle", "rb") as f:
                self.listaCupons = pickle.load(f)
        
        self.listaProdutosCupom = []
        self.listaQuantProd = []

    def salvaCupons(self):
        if len(self.listaCupons) != 0:
            with open("/Users/Letícia/Documents/Development/Orientada_a_Objetos/Trabalhos/Trabalho14 - Cupom Fiscal/cupom.pickle","wb") as f:
                pickle.dump(self.listaCupons, f)

    def insereCupom(self):        
        self.listaCodProduto = self.ctrlPrincipal.ctrlProduto.getListaCodigo()
        self.limiteIns = LimiteInsereCupom(self, self.listaCodProduto)

    def mostraCupom(self):
        str = 'Cupom: \n\n'
        for cpm in self.listaCupons:
            str += cpm.nroCupom + '\n'       
        self.limiteLista = LimiteMostraCupom(str)
    
    def consultaCupom(self):
        self.limiteIns = LimiteConsultaCupom(self)

    def insereProduto(self, event):
        prodSel = self.limiteIns.listbox.get(tk.ACTIVE)
        prod = self.ctrlPrincipal.ctrlProduto.getProduto(prodSel)
        cont = 0
        if len(self.listaProdutosCupom) == 0:
           self.listaProdutosCupom.append(prod)
           self.listaQuantProd.append(1)
        else: 
            for pdt in self.listaProdutosCupom:
                if prod.codigo == pdt.codigo:
                    self.listaQuantProd[cont] = (self.listaQuantProd[cont] + 1)
                    break
                elif cont == (len(self.listaProdutosCupom)-1): 
                    self.listaProdutosCupom.append(prod)
                    self.listaQuantProd.append(1)
                    break
                cont +=1
        self.limiteIns.mostraJanela('Sucesso', 'Produto incluso')
        
    def criaCupom(self, event):
        nroCupom = self.limiteIns.inputNroCupom.get()
        cupom = CupomFiscal(nroCupom, self.listaProdutosCupom, self.listaQuantProd)
        self.listaCupons.append(cupom)
        self.listaProdutosCupom = []
        self.listaQuantProd = []
        self.limiteIns.mostraJanela('Sucesso', 'Cupom Fiscal criado com sucesso')
        self.limiteIns.destroy()

    def consultarHandler(self,event):
        nroCupom = self.limiteIns.inputNroCupom.get()
        cont = 0
        cont2 = 0
        valorPro = 0
        valorTotal = 0
        msg = 'Cupom: '
        for cpm in self.listaCupons:
            cont += 1
            if  cpm.nroCupom  == nroCupom:
                msg += str(cpm.nroCupom) + '\n\n'
                for x in cpm.itensCupons:
                    valorPro = float(cpm.quantProd[cont2]) * float(x.valorUnitario)
                    msg += str(cpm.quantProd[cont2]) + ' - ' + str(x.codigo) + ' - ' + x.descricao + ' - ' + str(valorPro) + '\n'
                    valorTotal += valorPro
                    cont2 += 1          
                msg += 'Valor total: ' + str(valorTotal)
                self.limiteIns.mostraJanela('Dados do Cupom', msg)
                break 
            elif cont == len(self.listaCupons):
                self.limiteIns.mostraJanela('Erro', 'Cupom não encontrado!')
                break
    
    
    def limparHandler(self, event):
        self.limiteIns.inputNroCupom.delete(0, len(self.limiteIns.inputNroCupom.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()
