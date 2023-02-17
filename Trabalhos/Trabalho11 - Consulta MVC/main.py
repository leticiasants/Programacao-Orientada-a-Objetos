import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ModelCliente():
    def __init__(self, nome, codigo, email):
        self.__nome = nome
        self.__codigo = codigo
        self.__email = email

    @property
    def nome(self):
        return self.__nome
    
    @property
    def codigo(self):
        return self.__codigo

    @property
    def email(self):
        return self.__email

class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
      
        self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2,text="Código: ")
        self.labelInfo3 = tk.Label(self.frame3,text="Email: ")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")  
        self.labelInfo3.pack(side="left") 

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")  
        self.inputText3 = tk.Entry(self.frame3, width=20)
        self.inputText3.pack(side="left")            
      
        self.buttonSubmit = tk.Button(self.janela,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.enterHandler)
      
        self.buttonClear = tk.Button(self.janela,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)  
           
        self.buttonCliente = tk.Button(self.janela,text="Listar Clientes")      
        self.buttonCliente.pack(side="left")
        self.buttonCliente.bind("<Button>", controller.clientesHandler) 

        self.buttonConsulta = tk.Button(self.janela,text="Consultar Cliente")      
        self.buttonConsulta.pack(side="left")
        self.buttonConsulta.bind("<Button>", controller.consultarHandler)

    def mostraJanela(self, titulo, mensagem):
        if titulo == 'Erro':
            messagebox.showerror(titulo, mensagem)

        messagebox.showinfo(titulo, mensagem)
         
      
class Controller():       
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x100')
        self.listaClientes = []

        self.view = View(self.root, self) 

        self.root.title("Exemplo MVC")
        
        self.root.mainloop()

    def enterHandler(self, event):
        nomeCli = self.view.inputText1.get()
        codCli = self.view.inputText2.get()
        emailCli = self.view.inputText3.get()
        cliente = ModelCliente(nomeCli, codCli, emailCli)
        self.listaClientes.append(cliente)
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))
        self.view.inputText3.delete(0, len(self.view.inputText3.get()))

    def clientesHandler(self, event):
        if (len(self.listaClientes) == 0):
            self.view.mostraJanela('Clientes', 'Não possuem clientes cadastrados!')
        else:
            self.msg = 'Clientes Cadastrados:\n'
            for cliente in self.listaClientes:
                self.msg += cliente.codigo + ' - ' + cliente.nome + ' - ' + cliente.email + '\n'
            self.view.mostraJanela('Clientes', self.msg)
    
    def consultarHandler(self, event):
        codigo = simpledialog.askstring('Consulta de Cliente', 'Código:')
        cont = 0
        for cli in self.listaClientes:
            cont += 1
            if cli.codigo == codigo:
                self.dados = cli.nome + ' - ' + cli.email
                self.view.mostraJanela('Dados do Cliente', self.dados)
                break
            elif cont == len(self.listaClientes):
                self.view.mostraJanela('Erro', 'Código não cadastrado')
                break
            

if __name__ == '__main__':
    c = Controller()