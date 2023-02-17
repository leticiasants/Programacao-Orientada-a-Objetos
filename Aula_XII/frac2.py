def mdc(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def mesmaFracao(f1, f2):
    return (f1.num == f2.num) and (f1.den == f2.den)


class Fracao():
    
    def __init__(self, num, den):
        self.__num = num        
        self.__den = den     

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den       

    def simplifica(self):
        divComum = mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum   

    def __add__(self,outraFrac):
        novoNum = self.__num * outraFrac.den + self.__den * outraFrac.num
        novoDen = self.__den * outraFrac.den
        divComum = mdc(novoNum, novoDen)
        return Fracao(novoNum//divComum, novoDen//divComum)        

class FracaoMista():
    def __init__(self, num, den, inteiro = None):
        if inteiro is None:
            self.__inteiro = 0
        else: 
            self.__inteiro = inteiro
        self.__num = num
        self.__den = den
    
    @property
    def num(self):
        return self.__num
    
    @property
    def den(self):
        return self.__den
    
    @property
    def inteiro(self):
        return self.__inteiro
    
    def __str__(self):
        return str (self.__inteiro) + " " + str(self.__num) + "/" + str(self.__den)
    
    def __add__(self, outraFrac):
        novoInteiro = self.__inteiro + outraFrac.inteiro
        novoNum = self.__num * outraFrac.den + self.__den * outraFrac.num
        novoDen = self.__den * outraFrac.den
        divComum = mdc(novoNum, novoDen)
        resultNum = novoNum//divComum
        resultDen = novoDen//divComum
        inteiro = resultNum//resultDen
        inteiro += self.__inteiro
        if(type(outraFrac) is FracaoMista):
            inteiro += outraFrac.inteiro
        if resultNum > resultDen:
            resultNum = resultNum % resultDen
        
        if resultNum == resultDen:
            return inteiro
        
        if inteiro == 0:
            return Fracao(resultNum, resultDen)
        
        return FracaoMista(inteiro=inteiro, num=resultNum, den=resultDen)

        
if __name__ == "__main__":
    fracMista1 = FracaoMista(num=7, den=6)
    fracMista2 = FracaoMista(num=13, den=7)
    fracMista3 = fracMista1 + fracMista2

    print(fracMista3)
    print()

    fracMista1 = FracaoMista(num=1, den=3)
    fracMista2 = FracaoMista(num=2, den=3)
    fracMista3 = fracMista1 + fracMista2

    print(fracMista3)
    print()

    fracMista1 = FracaoMista(inteiro=3, num=1, den=2)
    fracMista2 = FracaoMista(inteiro=4, num=2, den=3)
    fracMista3 = fracMista1 + fracMista2

    print(fracMista3)
    print()
