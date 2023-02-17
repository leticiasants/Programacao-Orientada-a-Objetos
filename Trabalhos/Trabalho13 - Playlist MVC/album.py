import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog

class Album():
    def __init__(self, titulo, ano, artista) -> None:
        self.__titulo = titulo
        self.__ano = ano
        self.__artistas = artista
        self.__listaMusicas = []

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def artistas(self):
        return self.__artistas

    @property
    def listaMusicas(self):
        return self.__listaMusicas

    def addFaixa(self, musica):
        self.__listaMusicas.append(musica)

class LimiteInsereAlbuns(tk.Toplevel):
    def __init__(self, controle, listaArtistas):

        tk.Toplevel.__init__(self)
        self.geometry('250x150+400+200')
        self.title('Álbum')
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameTitulo.pack()
        self.frameArtista.pack()
        self.frameAno.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo,text='Título: ')
        self.labelTitulo.pack(side="left") 
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")             

        self.labelArtista = tk.Label(self.frameArtista,text='Artista: ')
        self.labelArtista.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameArtista, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        listaArtistas.append('Varios artistas')
        self.combobox['values'] = listaArtistas

        self.labelAno = tk.Label(self.frameAno,text='Ano: ')
        self.labelAno.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")           

        self.buttonSubmit = tk.Button(self.frameButton ,text='Criar Álbum')      
        self.buttonSubmit.pack(side="top")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonAdd= tk.Button(self.frameButton ,text='Adicionar Música')      
        self.buttonAdd.pack(side="left")
        self.buttonAdd.bind("<Button>", controle.inserirMusica)

        self.buttonFecha = tk.Button(self.frameButton ,text='Concluído')      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraAlbuns():
    def __init__(self, str):
        messagebox.showinfo('Lista de Albuns', str)

class LimiteConsultaAlbum(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x200+500+200')
        self.title("Consulta Album")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameButton.pack()
      
        self.labelTitulo = tk.Label(self.frameTitulo,text="Titulo: ")
        self.labelTitulo.pack(side="left")  

        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")             

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

class CtrlAlbum():
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal
        self.listaAlbuns =  []

    def insereAlbuns(self):
        listaArtistas = self.ctrlPrincipal.ctrlArtista.getListaNomesArtistas()
        self.limiteIns = LimiteInsereAlbuns(self, listaArtistas)
    
    def mostraAlbuns(self):
        str = 'Albuns: \n\n'
        for alb in self.listaAlbuns:
            str += alb.titulo + '\n'      
        self.limiteLista = LimiteMostraAlbuns(str)

    def consultaAlbuns(self):
        self.limiteIns = LimiteConsultaAlbum(self)

    def getAlbunsArtista(self, artista):
        listaTituloAlbuns = []
        for alb in self.listaAlbuns:
            if alb.getArtista().nome == artista:
                listaTituloAlbuns.append(alb.titulo)
        return listaTituloAlbuns

    def getAlbumByName(self, titAlbum):
        AlbSele = None
        for alb in self.listaAlbuns:
            if alb.titulo == titAlbum:
                AlbSele = alb
        return AlbSele

    def inserirMusica(self, event):
        art = self.limiteIns.escolhaCombo.get()
        if art == 'Varios artistas':

            tituloMusica = simpledialog.askstring('Música', 'Título:')
            nomeArt = simpledialog.askstring(tituloMusica, 'Artista: ')

            artista = self.ctrlPrincipal.ctrlArtista.getArtista(nomeArt)

            tituloAlbum = self.limiteIns.inputTitulo.get()
            
            album = self.ctrlPrincipal.ctrlAlbum.getAlbumByName(tituloAlbum)
            
            musica = self.ctrlPrincipal.ctrlMusica.gravaMusica(tituloMusica, artista, album)

            album.addFaixa(musica)
            artista.AddMusica(musica)
            self.ctrlPrincipal.ctrlArtista.addAlbum(nomeArt, album)
            self.limiteIns.mostraJanela('Sucesso', 'Música gravada com sucesso')
        
        else: 
            tituloMusica = simpledialog.askstring('Música', 'Título:')
            tituloAlbum = self.limiteIns.inputTitulo.get()
            
            album = self.ctrlPrincipal.ctrlAlbum.getAlbumByName(tituloAlbum)
            artista = self.ctrlPrincipal.ctrlArtista.getArtista(art)

            musica = self.ctrlPrincipal.ctrlMusica.gravaMusica(tituloMusica, artista, album)

            album.addFaixa(musica)
            artista.AddMusica(musica)
            self.limiteIns.mostraJanela('Sucesso', 'Música gravada com sucesso')

    def enterHandler(self, event):
        titulo = self.limiteIns.inputTitulo.get()
        nomeArtista = self.limiteIns.escolhaCombo.get()
        ano = self.limiteIns.inputAno.get()
        artista = self.ctrlPrincipal.ctrlArtista.getArtista(nomeArtista)
        album = Album(titulo, ano, artista)
        self.listaAlbuns.append(album)
        self.ctrlPrincipal.ctrlArtista.addAlbum(nomeArtista, album)
        self.limiteIns.mostraJanela('Sucesso', 'Álbum criado com sucesso')

    def clearHandler(self, event):
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
            
    def consultarHandler(self, event):
        titulo = self.limiteIns.inputTitulo.get()
        cont = 0
        msg = 'Album: ' + titulo + '\n\n'
        for alb in self.listaAlbuns:
            cont += 1
            if alb.titulo == titulo:
                for mus in alb.listaMusicas:
                    msg += str(mus.nroFaixa) + ' - ' + mus.titulo + '\n'
                self.limiteIns.mostraJanela('Album', msg)
                break
            elif cont == len(self.listaAlbuns):
                self.limiteIns.mostraJanela('Erro', 'Album não encontrado!')
                break

    def fechaHandler(self, event):
        self.limiteIns.destroy()