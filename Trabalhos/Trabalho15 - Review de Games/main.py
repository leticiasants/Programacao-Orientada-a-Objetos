import tkinter as tk
import game as gm

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.gameMenu = tk.Menu(self.menubar)
        self.salvaMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar) 

        self.gameMenu.add_command(label="Cadastrar", command=self.controle.cadastraGame)
        self.gameMenu.add_command(label="Avaliar", command=self.controle.avaliaGame)
        self.gameMenu.add_command(label="Consultar", command=self.controle.consultaGame)
        self.menubar.add_cascade(label="Jogo", menu=self.gameMenu)

        self.sairMenu.add_command(label="Salva", command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", menu=self.sairMenu)
               
        self.root.config(menu=self.menubar)

class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.CtrlGame = gm.CtrlGame(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Jogos")
        # Inicia o mainloop
        self.root.mainloop()
    
    def cadastraGame(self):
        self.CtrlGame.cadastraGame()

    def avaliaGame(self):
        self.CtrlGame.avaliaGame()
    
    def consultaGame(self):
        self.CtrlGame.consultaGame()

    def salvaDados(self):
        self.CtrlGame.salvaJogos()
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()