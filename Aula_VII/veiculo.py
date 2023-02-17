class Veiculo:

    # construtor
    def __init__(self, marca, cor, motorLigado):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorLigado

    #getters

    def getMarca(self):
        return self.__marca
    
    def getCor(self):
        return self.__cor
    
    #is usado para booleano
    def isMotorLigado(self):
        return self.__motorLigado

    # método
    def ligaMotor(self):
        if(self.__motorLigado):
            print('O motor já está ligado!')
        else: 
            self.__motorLigado = True
            print('O motor acaba de ser ligado!')

class Motocicleta(Veiculo):

    #construtor
    def __init__(self, marca, cor, motorLigado, estilo):
        super().__init__(marca, cor, motorLigado)
        self.__estilo = estilo

    #getters

    def getEstilo(self):
        return self.__estilo

    #método
    def mostraAtributos(self):
        print('Esta motocicleta é uma {} {} estilo {}'.format(self.getMarca(), self.getCor(), self.getEstilo()))
        if(self.isMotorLigado()):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')

class Carro(Veiculo):

    #construtor
    def __init__(self, marca, cor, motorLigado, portaMalasCheio):
        super().__init__(marca, cor, motorLigado)
        self.__portaMalasCheio = portaMalasCheio
    
    #getters
    def istPortaMalasCheio(self):
        return self.__portaMalasCheio

    #método
    def enchePortaMalas(self):
        if (self.__portaMalasCheio == True):
            return True
        else:
            self.__portaMalasCheio = True
            return False
            

    def mostraAtributos(self):
        print('Este carro é um {} {}'.format(self.getMarca(), self.getCor()))
        if(self.isMotorLigado()):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')
        if(self.enchePortaMalas()):
            print('O porta malas está cheio!')
        else:
            print('Seu porta malas está vazio!')

m = Motocicleta('Honda', 'azul', False, 'naked')
m.mostraAtributos()
m.ligaMotor()
m.mostraAtributos()
print('---------------------------------')
c = Carro('Chevrolet', 'branco', False, False)
c.mostraAtributos()
c.enchePortaMalas()
c.ligaMotor()
c.mostraAtributos()