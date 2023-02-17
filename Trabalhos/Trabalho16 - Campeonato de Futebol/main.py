import tkinter as tk
import equipe as eq

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.gameMenu = tk.Menu(self.menubar)
        self.salvaMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar) 

        self.gameMenu.add_command(label="Criar Equipe", command=self.controle.criarEquipe)
        self.gameMenu.add_command(label="Consultar Equipe", command=self.controle.consultarEquipe)
        self.gameMenu.add_command(label="Imprimir Dados", command=self.controle.imprimirDados)
        self.menubar.add_cascade(label="Equipe", menu=self.gameMenu)

        self.sairMenu.add_command(label="Salva", command=self.controle.salvaEquipes)
        self.menubar.add_cascade(label="Sair", menu=self.sairMenu)
               
        self.root.config(menu=self.menubar)

class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.CtrlEquipe = eq.CtrlEquipe(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Campeonato de Futebol")
        # Inicia o mainloop
        self.root.mainloop()
    
    def criarEquipe(self):
        self.CtrlEquipe.criarEquipe()

    def consultarEquipe(self):
        self.CtrlEquipe.consultarEquipe()
    
    def imprimirDados(self):
        self.CtrlEquipe.imprimirDados()

    def salvaEquipes(self):
        self.CtrlEquipe.salvaEquipes()
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()