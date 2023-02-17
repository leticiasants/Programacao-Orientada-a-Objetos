import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Playlist():
    def __init__(self, nome, musicas) -> None:
        self.__nome = nome

        self.__musicas = musicas

    @property
    def nome(self):
        return self.__nome
    
    @property
    def musicas(self):
        return self.__musicas

class LimiteInserePlaylist(tk.Toplevel):
    def __init__(self, controle, listaNomeArtistas, listaArtistas):

        tk.Toplevel.__init__(self)
        self.geometry('350x300+400+200')
        self.title('Playlist')
        self.controle = controle

        self.framePlaylist = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameMusicas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.framePlaylist.pack()
        self.frameArtista.pack()
        self.frameMusicas.pack()        
        self.frameButton.pack()

        self.labelPlaylist = tk.Label(self.framePlaylist,text='Nome da Playlist: ')
        self.labelPlaylist.pack(side="left")

        self.inputPlaylist = tk.Entry(self.framePlaylist, width=20)
        self.inputPlaylist.pack(side="left")

        self.labelArtista = tk.Label(self.frameArtista,text='Escolha o artista: ')
        self.labelArtista.pack(side="left")
        self.escolhaArtista = tk.StringVar()
        self.comboboxArtista = ttk.Combobox(self.frameArtista, width = 15 , textvariable = self.escolhaArtista)
        self.comboboxArtista.pack(side="left")
        self.comboboxArtista['values'] = listaNomeArtistas

        self.labelMusicas = tk.Label(self.frameMusicas,text='Escolha a música: ')
        self.labelMusicas.pack(side="left") 
        self.listbox = tk.Listbox(self.frameMusicas)
        self.listbox.pack(side="left")
        for art in listaArtistas:
            if self.escolhaArtista.get() == art:
                for mus in art.listaMusicas:
                    self.listbox.insert(tk.END, mus.titulo)

        self.buttonBusca = tk.Button(self.frameButton ,text='Buscar músicas do artista')           
        self.buttonBusca.pack(side="left")
        self.buttonBusca.bind("<Button>", controle.buscaMusicasArtista)

        self.buttonInsere = tk.Button(self.frameButton ,text='Adicionar música')           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereMusica)

        self.buttonCria = tk.Button(self.frameButton ,text='Cria Playlist')           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaPlaylist)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg) 

class LimiteMostraPlaylist():
    def __init__(self, str):
        messagebox.showinfo('Lista de Playlists', str)

class LimiteConsultaPlaylist(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x200+500+200')
        self.title("Consulta Playlist")
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

class CtrlPlaylist():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal

        self.listaMusicasPlaylist = []
        self.listaMusicasArtista = []
        self.listaPlaylists =  []
    
    def inserePlaylist(self):        
        listaNomeArtistas = self.ctrlPrincipal.ctrlArtista.getListaNomesArtistas()
        listaArtistas = self.ctrlPrincipal.ctrlArtista.getInsArtistas()

        self.limiteIns = LimiteInserePlaylist(self, listaNomeArtistas, listaArtistas)

    def mostraPlaylist(self):
        str = 'Playlists: \n\n'
        for play in self.listaPlaylists:
            str += play.nome + '\n'      
        self.limiteLista = LimiteMostraPlaylist(str)

    def consultaPlaylist(self):
        self.limiteIns = LimiteConsultaPlaylist(self)

    def buscaMusicasArtista(self, event):
        self.limiteIns.listbox.delete(0, tk.END)
        artSel = self.limiteIns.escolhaArtista.get()
        listaMusicasArt = self.ctrlPrincipal.ctrlArtista.getMusicasArtista(artSel)
        for mus in listaMusicasArt:
            self.limiteIns.listbox.insert(tk.END, mus)

    def insereMusica(self, event):
        musicaSel = self.limiteIns.listbox.get(tk.ACTIVE)
        musica = self.ctrlPrincipal.ctrlMusica.getMusica(musicaSel)
        self.listaMusicasPlaylist.append(musica)
        self.limiteIns.mostraJanela('Sucesso', 'Música adicionada')
        self.limiteIns.listbox.delete(tk.ACTIVE)

    def criaPlaylist(self, event):
        nome = self.limiteIns.inputPlaylist.get()
        playlist = Playlist(nome, self.listaMusicasPlaylist)
        self.listaPlaylists.append(playlist)
        self.limiteIns.mostraJanela('Sucesso', 'Playlist criada com sucesso')
        self.limiteIns.destroy()

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def consultarHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        cont = 0
        for play in self.listaPlaylists:
            cont += 1
            if  play.nome  == nome:
                msg = 'Playlist: ' + play.nome + '\n\n'
                for mus in self.listaMusicasPlaylist:
                    msg += str(mus.nroFaixa) + ' - ' + mus.titulo + '\n'
                self.limiteIns.mostraJanela('Dados da Playlist', msg)
                break
            elif cont == len(self.listaArtista):
                self.limiteIns.mostraJanela('Erro', 'Playlist não encontrado!')
                break

    def fechaHandler(self, event):
        self.limiteIns.destroy()