from abc import ABC, abstractmethod

class Vendedor(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome

        self.__vendas = []

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def vendas(self):
        return self.__vendas
    
    def adicionaVenda(self, codImovel, mes, ano, valor):
        self.__vendas.append(Venda(codImovel, mes, ano, valor))


    @abstractmethod
    def getDados(self):
        pass

    @abstractmethod
    def calculaRenda(self):
        pass

class Contratado(Vendedor):
    def __init__(self, codigo, nome, salarioFixo, nroCartTrabalho):
        super().__init__(codigo, nome)
        self.__salarioFixo = salarioFixo
        self.__nroCartTrabalho = nroCartTrabalho
        self.__comissao = 1/100

    @property
    def salarioFixo(self):
        return self.__salarioFixo

    @property
    def nroCartTrabalho(self):
        return self.__nroCartTrabalho
    
    @property
    def comissao(self):
        return self.__comissao
    
    def getDados(self):
        return f'Nome: {self.nome} - Nro Carteira: {self.nroCartTrabalho}'
        
    def calculaRenda(self, mes, ano):
        totalComissao = 0

        for x in self.vendas:
            if (x.mesVenda == mes and x.anoVenda == ano):
                totalComissao += x.valorVenda
        
        comissaoFinal = self.__salarioFixo + (totalComissao * self.__comissao)

        return comissaoFinal


class Comissionado(Vendedor):
    def __init__(self, codigo, nome, nroCPF, comissao):
        super().__init__(codigo, nome)
        self.__nroCPF = nroCPF
        self.__comissao = comissao
    
    @property
    def nroCPF(self):
        return self.__nroCPF
    
    @property
    def comissao(self):
        return self.__comissao
    
    def getDados(self):
        return f'Nome: {self.nome} - Nro CPF: {self.nroCPF}'
    
    def calculaRenda(self, mes, ano):
        totalComissao = 0

        for x in self.vendas:
            if (x.mesVenda == mes and x.anoVenda == ano):
                totalComissao += x.valorVenda
        
        comissaoFinal = totalComissao * (self.__comissao/100)
        
        return comissaoFinal
    

class Venda():
    def __init__ (self, codImovel, mesVenda, anoVenda, valorVenda):
        self.__codImovel = codImovel
        self.__mesVenda = mesVenda
        self.__anoVenda = anoVenda
        self.__valorVenda = valorVenda

    @property
    def codImovel(self):
        return self.__codImovel
    
    @property
    def mesVenda(self):
        return self.__mesVenda
    
    @property
    def anoVenda(self):
        return self.__anoVenda
    
    @property
    def valorVenda(self):
        return self.__valorVenda


# c??digo disponibilizado (n??o alterado)
if __name__ == "__main__":
    funcContratado = Contratado(1001, 'Jo??o da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)
    funcComissionado = Comissionado(1002, 'Jos?? Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        print (func.getDados())
        print ("Renda no m??s 3 de 2022: ")
        print (func.calculaRenda(3, 2022))
