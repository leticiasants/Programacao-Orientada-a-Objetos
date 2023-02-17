import tkinter as tk
from tkinter import messagebox

class Artista():
    def __init__(self, nome) -> None:
        self.__nome = nome

        self.__listaMusicas = []
        self.__listaAlbuns = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def listaMusicas(self):
        return self.__listaMusicas

    @property
    def listaAlbuns(self):
        return self.__listaAlbuns

    def AddMusica(self, musica):
        self.__listaMusicas.append(musica)

    def AddAlbum(self, album):
        self.__listaAlbuns.append(album)

class LimiteInsereArtista(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100+500+200')
        self.title("Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNome.pack(side="left")  

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
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

class LimiteMostraArtistas():
    def __init__(self, str):
        messagebox.showinfo('Lista de Artistas', str)

class LimiteConsultaArtista(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x200+500+200')
        self.title("Consulta Artista")
        self.controle = controle 

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNome.pack(side="left")  

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             

        self.buttonConsultar = tk.Button(self.frameButton ,text="Consultar")      
        self.buttonConsultar.pack(side="left")
        self.buttonConsultar.bind("<Button>", controle.consultarHandler)

        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler) 

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlArtista():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaArtista = []

    def insereArtista(self):
        self.limiteIns = LimiteInsereArtista(self) 

    def mostraArtista(self):
        str = 'Artistas: \n\n'
        for art in self.listaArtista:
            str += art.nome + '\n'       
        self.limiteLista = LimiteMostraArtistas(str)
    
    def consultaArtista(self):
        self.limiteIns = LimiteConsultaArtista(self)

    def getArtista(self, nome):
        artCad = None
        for art in self.listaArtista:
            if art.nome == nome:
                artCad = art
        return artCad

    def getListaNomesArtistas(self):
        listaNomes = []
        for art in self.listaArtista:
            listaNomes.append(art.nome)
        return listaNomes
    
    def getInsArtistas(self):
        art = []
        for artis in self.listaArtista:
            art.append(artis)
        return art

    def getMusicasArtista(self, nomeArtista):
        listaMusicas = []
        for art in self.listaArtista:
            if art.nome == nomeArtista:
                for mus in art.listaMusicas:
                    listaMusicas.append(mus.titulo)
        return listaMusicas

    def addAlbum(self, nomeArtista, album):
        for art in self.listaArtista:
            if art.nome == nomeArtista:
                art.AddAlbum(album)

    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        artista = Artista(nome)
        self.listaArtista.append(artista)
        self.limiteIns.mostraJanela('Sucesso', 'Artista cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def consultarHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        cont = 0
        for art in self.listaArtista:
            cont += 1
            if  art.nome  == nome:
                msg = art.nome + '\n\n'
                for alb in art.listaAlbuns:
                    msg += 'Album: ' + alb.titulo + '\n'
                    for mus in alb.listaMusicas:
                        for mus2 in art.listaMusicas:
                            if mus == mus2:
                                msg += str(mus.nroFaixa) + ' - ' + mus.titulo + '\n'
                    msg += '\n\n'
                self.limiteIns.mostraJanela('Dados do Artista', msg)
                break 
            elif cont == len(self.listaArtista):
                self.limiteIns.mostraJanela('Erro', 'Artista não encontrado!')
                break

    def fechaHandler(self, event):
        self.limiteIns.destroy()
