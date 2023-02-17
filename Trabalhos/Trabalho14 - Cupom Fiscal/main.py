import tkinter as tk
from tkinter import messagebox
import produto as prod
import cupomfiscal as cpm

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.produtoMenu = tk.Menu(self.menubar)
        self.cupomMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)    

        self.produtoMenu.add_command(label="Cadastrar", \
                    command=self.controle.insereProduto)
        self.produtoMenu.add_command(label="Produtos Cadastrados", \
                    command=self.controle.mostraProduto)
        self.produtoMenu.add_command(label="Consultar", \
                    command=self.controle.consultaProduto)
        self.menubar.add_cascade(label="Produto", \
                    menu=self.produtoMenu)

        self.cupomMenu.add_command(label="Criar", \
                    command=self.controle.insereCupom)
        self.cupomMenu.add_command(label="Cupons Criados", \
                    command=self.controle.mostraCupom)
        self.cupomMenu.add_command(label="Consultar", \
                    command=self.controle.consultaCupom)        
        self.menubar.add_cascade(label="Cupom Fiscal", \
                    menu=self.cupomMenu)

        self.sairMenu.add_command(label="Salva", \
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProduto = prod.CtrlProduto()
        self.ctrlCupom = cpm.CtrlCupomFiscal(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Cupom Fiscal")
        # Inicia o mainloop
        self.root.mainloop()
       
    def insereProduto(self):
        self.ctrlProduto.insereProduto()

    def mostraProduto(self):
        self.ctrlProduto.mostraProduto()
    
    def consultaProduto(self):
        self.ctrlProduto.consultaProduto()

    def insereCupom(self):
        self.ctrlCupom.insereCupom()
    
    def mostraCupom(self):
        self.ctrlCupom.mostraCupom()

    def consultaCupom(self):
        self.ctrlCupom.consultaCupom()

    def salvaDados(self):
        self.ctrlProduto.salvaProdutos()
        self.ctrlCupom.salvaCupons()
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()