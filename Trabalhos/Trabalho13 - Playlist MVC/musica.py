class Musica():
    def __init__(self, titulo, artista, album, nroFaixa) -> None:
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def album(self):
        return self.__album

    @property
    def nroFaixa(self):
        return self.__nroFaixa


class CtrlMusica:
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal
        self.listaMusicas = []

    def getMusica(self, nomeMusica):
        musicaSel = None
        for mus in self.listaMusicas:
            if mus.titulo == nomeMusica:
                musicaSel = mus
        return musicaSel 

    def gravaMusica(self, titulo, artista, album):
        nroFaixa = len(self.listaMusicas)
        musica = Musica(titulo, artista, album, (nroFaixa+1))
        self.listaMusicas.append(musica)
        return musica