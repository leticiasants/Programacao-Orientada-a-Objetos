import tkinter as tk
import artista as art
import album as alb
import playlist as play
import musica as mus

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250+50+100')
        self.menubar = tk.Menu(self.root)        
        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)

        self.artistaMenu.add_command(label="Cadastrar", command=self.controle.insereArtista)
        self.artistaMenu.add_command(label="Mostrar", command=self.controle.mostraArtista)
        self.artistaMenu.add_command(label="Consultar", command=self.controle.consultarArtista)
        self.menubar.add_cascade(label="Artista", menu=self.artistaMenu)

        self.albumMenu.add_command(label="Cadastrar", command=self.controle.insereAlbuns)
        self.albumMenu.add_command(label="Mostrar", command=self.controle.mostraAlbuns)
        self.albumMenu.add_command(label="Consultar", command=self.controle.consultarAlbum)       
        self.menubar.add_cascade(label="Álbum", menu=self.albumMenu)

        self.playlistMenu.add_command(label="Cadastrar", command=self.controle.inserePlaylist)
        self.playlistMenu.add_command(label="Mostrar", command=self.controle.mostraPlaylist)
        self.playlistMenu.add_command(label="Consultar", command=self.controle.consultarPlaylist)                        
        self.menubar.add_cascade(label="Playlist", menu=self.playlistMenu)        

        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlArtista = art.CtrlArtista(self)
        self.ctrlAlbum = alb.CtrlAlbum(self)
        self.ctrlPlaylist = play.CtrlPlaylist(self)
        self.ctrlMusica = mus.CtrlMusica(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Streaming de áudio")
        self.root.mainloop()

    def insereArtista(self):
        self.ctrlArtista.insereArtista()

    def mostraArtista(self):
        self.ctrlArtista.mostraArtista()

    def consultarArtista(self):
        self.ctrlArtista.consultaArtista()

    def insereAlbuns(self):
        self.ctrlAlbum.insereAlbuns()
    
    def mostraAlbuns(self):
        self.ctrlAlbum.mostraAlbuns()

    def consultarAlbum(self):
        self.ctrlAlbum.consultaAlbuns()

    def inserePlaylist(self):
        self.ctrlPlaylist.inserePlaylist()
    
    def mostraPlaylist(self):
        self.ctrlPlaylist.mostraPlaylist()

    def consultarPlaylist(self):
        self.ctrlPlaylist.consultaPlaylist()

if __name__ == '__main__':
    c = ControlePrincipal()