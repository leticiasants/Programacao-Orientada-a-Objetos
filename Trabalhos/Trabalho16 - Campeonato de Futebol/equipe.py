import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from math import *
import os.path
import pickle

class Estudante():
    def __init__(self, nroMatric, nome, curso) -> None:
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso

    @property
    def nroMatric(self):
        return self.__nroMatric
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def curso(self):
        return self.__curso

class Curso():
    def __init__(self, sigla, nome) -> None:
        self.__sigla = sigla
        self.__nome = nome

    @property
    def sigla(self):
        return self.__sigla
    
    @property
    def nome(self):
        return self.__nome
    
class Equipe:
    def __init__(self, curso, listaEstudantes):
        self.__curso = curso
        self.__listaEstudantes = listaEstudantes
    
    
    @property
    def curso(self):
        return self.__curso

    @property
    def listaEstudantes(self):
        return self.__listaEstudantes

class LimiteInsereEquipe(tk.Toplevel):
    def __init__(self, controle, listaCurso):

        tk.Toplevel.__init__(self)
        self.geometry('250x200+500+200')
        self.title("Equipe")
        self.controle = controle

        self.frameCurso = tk.Frame(self)
        self.frameEstudante = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCurso.pack()
        self.frameEstudante.pack()
        self.frameButton.pack()
      
        self.labelCurso = tk.Label(self.frameCurso,text='Curso: ')
        self.labelCurso.pack(side="left")
        self.escolhaCurso = tk.StringVar()
        self.comboboxCurso = ttk.Combobox(self.frameCurso, width = 15 , textvariable = self.escolhaCurso)
        self.comboboxCurso.pack(side="left")
        listaNomeCursos = []
        for cus in listaCurso:
            listaNomeCursos.append(cus.nome)
        self.comboboxCurso['values'] = listaNomeCursos

        self.labelEstudante = tk.Label(self.frameEstudante, text="Matric. Estudante: ")
        self.labelEstudante.pack(side="left")
        self.inputEstudante = tk.Entry(self.frameEstudante, width=10)
        self.inputEstudante.pack(side="left")
        
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Adicionar Estudante")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.addHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Criar Equipe")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.criarHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaEquipe(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200+500+200')
        self.title("Consultar Equipes")
        self.ctrl = controle

        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCurso.pack()
        self.frameButton.pack()

        self.labelCurso = tk.Label(self.frameCurso, text="Sigla do curso: ")
        self.labelCurso.pack(side="left")
        self.inputCurso = tk.Entry(self.frameCurso, width=10)
        self.inputCurso.pack(side="left")

        self.buttonConsulta = tk.Button(self.frameButton ,text="Consultar Equipe")      
        self.buttonConsulta.pack(side="left")
        self.buttonConsulta.bind("<Button>", controle.cunsultaHandler)

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteImprimeDados():
    def __init__(self, str):
        messagebox.showinfo('Lista de Playlists', str)
    
class CtrlEquipe():
    def __init__(self, controlador):
        self.ctrlPrincipal = controlador
        if not os.path.isfile("/Users/Letícia/Documents/Development/Orientada_a_Objetos/Trabalhos/Trabalho16 - Campeonato de Futebol/equipe.pickle"):
            self.listaEquipe =  []
        else:
            with open("/Users/Letícia/Documents/Development/Orientada_a_Objetos/Trabalhos/Trabalho16 - Campeonato de Futebol/equipe.pickle", "rb") as f:
                self.listaEquipe = pickle.load(f)
        
        self.listaEstEquipe = []
        
    c1 = Curso("CCO", "Ciência da Computação")
    c2 = Curso("SIN", "Sistemas de Informação")
    c3 = Curso("EEL", "Engenharia Elétrica")
    listaCurso = []
    listaCurso.append(c1)
    listaCurso.append(c2)
    listaCurso.append(c3)
    #Inserir mais cursos, se quiser
    listaEstudante = []
    listaEstudante.append(Estudante(1001, "José da Silva", c1))
    listaEstudante.append(Estudante(1002, "João de Souza", c1))
    listaEstudante.append(Estudante(1003, "Rui Santos", c2))

    listaEstudante.append(Estudante(1004, "Ana Castro", c2))
    listaEstudante.append(Estudante(1005, "Maria Costa", c2))
    listaEstudante.append(Estudante(1006, "Marcos Alves", c3))
    listaEstudante.append(Estudante(1007, "Lucas Gonçalves", c3))
    listaEstudante.append(Estudante(1008, "Patricia Machado", c3))
    listaEstudante.append(Estudante(1009, "Camila Pereira", c1))
    listaEstudante.append(Estudante(1010, "Luis Ferreira", c3))
    #Inserir mais 7 alunos, totalizando pelo menos 10 na lista

    def criarEquipe(self):
        self.limiteIns = LimiteInsereEquipe(self, self.listaCurso)
    
    def consultarEquipe(self):
        self.limiteCons = LimiteConsultaEquipe(self)

    def imprimirDados(self):      
        contEq = 0
        contEstEq = 0

        for eq in self.listaEquipe:
            contEq += 1
            for est in eq.listaEstudantes:
                contEstEq += 1
        
        media = round(contEstEq/contEq)

        msg = 'Número de equipes: ' + str(contEq) + '\n'
        msg += 'Número total de estudantes: ' + str(contEstEq) + '\n'
        msg += 'Média de estudantes por equipe: ' + str(media)

        self.limiteImp = LimiteImprimeDados(msg)


    def salvaEquipes(self):
        if len(self.listaEquipe) != 0:
            with open("/Users/Letícia/Documents/Development/Orientada_a_Objetos/Trabalhos/Trabalho16 - Campeonato de Futebol/equipe.pickle","wb") as f:
                pickle.dump(self.listaEquipe, f)
    
    def addHandler(self, event):
        cursoSel = self.limiteIns.escolhaCurso.get()
        estSel = int(self.limiteIns.inputEstudante.get())
        aux1 = 0
        aux2 = 0
        for est in self.listaEstudante:
            if est.nroMatric == estSel:
                aux1 += 1
                if est.curso.nome == cursoSel:
                    aux2 += 1
                    self.listaEstEquipe.append(est)
                    self.limiteIns.mostraJanela('Sucesso', 'Aluno adicionado com sucesso')
                    break        
            
        if aux1 == 0:
            self.limiteIns.mostraJanela('Erro', 'Aluno não matriculado!')
            aux2 += 1
        
        if aux2 == 0:
            self.limiteIns.mostraJanela('Erro', 'Aluno não está matriculado no curso selecionado!')
  
    def clearHandler(self, event):
        self.limiteIns.inputEstudante.delete(0, len(self.limiteIns.inputEstudante.get()))
        self.limiteIns.comboboxCurso.set('---')
    
    def criarHandler(self, event):
        cursoSel = self.limiteIns.escolhaCurso.get()
        for cur in self.listaCurso:
            if cur.nome == cursoSel:
                curso = cur
                break

        self.listaEquipe.append(Equipe(curso, self.listaEstEquipe))
        self.listaEstEquipe = []

        self.limiteIns.destroy()

    def cunsultaHandler(self, event):
        cursoSel = self.limiteCons.inputCurso.get()
        aux1 = 0
        aux2 = 0
        aux3 = 0
        for cur in self.listaCurso:
            if cur.sigla == cursoSel:
                aux1 += 1
                break
        
        for eq in self.listaEquipe:
            if eq.curso.sigla == cursoSel:
                aux2 += 1
                msg = eq.curso.sigla + ' - ' + eq.curso.nome + ':\n\n'
                for est in eq.listaEstudantes:
                    aux3 += 1
                    msg += est.nome + '\n'
        
        if aux3 > 0:
            self.limiteCons.mostraJanela('Equipe', msg)
        
        if aux1 == 0:
            self.limiteCons.mostraJanela('Erro', 'Esta sigla de curso não existe')

        if aux2 == 0:
            self.limiteCons.mostraJanela('Erro', 'Não existe equipe desse curso')
        
    def fechaHandler(self, event):
        self.limiteCons.destroy()
