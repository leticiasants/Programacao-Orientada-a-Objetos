class Musica:
    def __init__(self, titulo, artista, album, nroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa

        artista.addMusica(self)

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

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano

        self.__faixas = []
        artista.addAlbum(self)

    @property
    def titulo(self):
        return self.__titulo

    @property
    def artista(self):
        return self.__artista

    @property
    def ano(self):
        return self.__ano

    @property
    def faixas(self):
        return self.__faixas

    def addFaixa(self, titulo, artista=None):
        if artista is None:
            artista = self.__artista
        nroFaixa = len(self.__faixas)
        musica = Musica(titulo, artista, self, nroFaixa)
        self.__faixas.append(musica)

class Artista:
    def __init__(self, nome):
        self.__nome = nome

        self.__albuns = []
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def albuns(self):
        return self.__albuns

    @property
    def musicas(self):
        return self.__musicas

    def addAlbum(self, album):
        self.__albuns.append(album)

    def addMusica(self, musica):
        self.__musicas.append(musica)


class Playlist:
    def __init__(self, nome):
        self.__nome = nome

        self.__musicas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def musicas(self):
        return self.__musicas

    def addMusica(self, musica):
        self.__musicas.append(musica)


if __name__ == "__main__":    
    listaAlbuns = []
    art1 = Artista('Coldplay')
    album1 = Album('Mylo Xyloto', art1, 2011)
    album1.addFaixa('Paradise')
    album1.addFaixa('Hurts Like Heaven')
    album1.addFaixa('Charlie Brown') 
    listaAlbuns.append(album1)

    album2 = Album('A Head Full of Dreams', art1, 2015)
    album2.addFaixa('A Head Full of Dreams')
    album2.addFaixa('Birds')
    album2.addFaixa('Everglow')
    listaAlbuns.append(album2)

    art2 = Artista('Skank')
    album3 = Album('Siderado', art2, 1998)
    album3.addFaixa('Resposta')
    album3.addFaixa('Saideira')
    album3.addFaixa('Romance Noir')
    listaAlbuns.append(album3)

    # Criar e exibir uma playlist com as músicas do album "Mylo Xyloto"
    playlist1 = Playlist('Playlist Mylo Xyloto')

    for mus in album1.faixas:
        playlist1.addMusica(mus)
    
    print(playlist1.nome)

    for mus in playlist1.musicas:
        print(f'Música: {mus.titulo}')
    
    print()

    # Criar e exibir uma playlist com todas as músicas do Coldplay   
    playlist2 = Playlist('Playlist Codplay') 

    for mus in art1.musicas:
        playlist2.addMusica(mus)   
    
    print(playlist2.nome)

    for mus in playlist2.musicas:
        print(f'Música: {mus.titulo}')

    print()

    # Criar e exibir uma playlist contendo uma música de cada album
    playlist3 = Playlist('Playlist 3')

    for album in listaAlbuns:
            playlist3.addMusica(album.faixas[0])

    print(playlist3.nome)

    for mus in playlist3.musicas:
        print(f'Música: {mus.titulo}')

    print()