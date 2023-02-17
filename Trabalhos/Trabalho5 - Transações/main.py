'''
    Utilizando Property e Setter
    Autor: Letícia Vitória dos Santos
    Ultima aulteração: 06/11/2022
'''
from abc import ABC, abstractmethod

# Criação de classe
class Transacao():
    def __init__(self, data, valor, descricao):
        self.data = data
        self.valor = valor
        self.descricao = descricao
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
    
    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

# Criação de classe abstrata, superclasse/classe pai   
class Conta(ABC):
    def __init__(self, numConta, nome, saldo) -> None:
        self.__numConta = numConta
        self.__nome = nome
        self.saldo = saldo
        self.__listaTransacao = []
    
    @property
    def numConta(self):
        return self.__numConta
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
        
    @property
    def listaTransacao(self):
        return self.__listaTransacao
    
    # Função para depositar (aumentar o saldo)
    def depositarConta(self, transacao):
        self.saldo += transacao.valor
        self.__listaTransacao.append(transacao)
    
    # Função para retirar (diminui o saldo ou diminui o saldo e o limite, ou não é possível)
    def retirarConta(self, transacao):
        if transacao.valor > self.saldo:
            print(f'Não é possível retirar {transacao.valor}')
        else:
            self.__listaTransacao.append(transacao)
        
    # Função abstrata
    @abstractmethod
    def imprimirExtrato(self):
        pass

# Classe que herda os atributos e funções da Classe Pessoa/ Subclasse ou Classe Filha
class ContaPoupanca(Conta):
    def __init__(self, numConta, nome, saldo, aniverConta):
        super().__init__(numConta, nome, saldo)
        self.__aniverConta = aniverConta
    
    @property
    def aniverConta(self):
        return self.__aniverConta
    
    # Função herdada da superclasse/classe pai
    def depositarConta(self, transacao):
        return super().depositarConta(transacao)
    
    # Função herdada da superclasse/classe pai
    def retirarConta(self, transacao):
        return super().retirarConta(transacao)
    
    # Função abstrata herdada da superclasse/classe pai
    def imprimirExtrato(self):
        print('Número da Conta: {}'. format(self.numConta))
        print('Nome Corretista: {}'. format(self.nome))
        print('Saldo: {}'. format(self.saldo))
        print('Aniversário da Conta: {}'. format(self.aniverConta))
        print('****Transações***')
        for list in self.listaTransacao:
            print('Data: {} - Valor: {} - Descrição: {}'. format(list.data, list.valor, list.descricao))
        print()

# Classe que herda os atributos e funções da Classe Pessoa/ Subclasse ou Classe Filha 
class ContaCorrenteComum(Conta):
    def __init__(self, numConta, nome, saldo):
        super().__init__(numConta, nome, saldo)
    
    # Função herdada da superclasse/classe pai
    def depositarConta(self, transacao):
        return super().depositarConta(transacao)
    
    # Função herdada da superclasse/classe pai
    def retirarConta(self, transacao):
        return super().retirarConta(transacao)
    
    # Função abstrata herdada da superclasse/classe pai
    def imprimirExtrato(self):
        print('Número da Conta: {}'. format(self.numConta))
        print('Nome Corretista: {}'. format(self.nome))
        print('Saldo: {}'. format(self.saldo))
        print('****Transações***')
        for list in self.listaTransacao:
            print('Data: {} - Valor: {} - Descrição: {}'. format(list.data, list.valor, list.descricao))
        print()

# Classe que herda os atributos e funções da Classe Pessoa/ Subclasse ou Classe Filha
class ContaCorrenteLimite(Conta):
    def __init__(self, numConta, nome, saldo, limite):
        super().__init__(numConta, nome, saldo)
        self.__limite = limite
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    # Função herdada da superclasse/classe pai
    def depositarConta(self, transacao):
        return super().depositarConta(transacao)
    
    # Função herdada da superclasse/classe pai, mas sobrescrita pois necessita de tratamento diferente
    def retirarConta(self, transacao):
        if transacao.valor > (self.saldo + self.__limite):
            print(f'Não é possível retirar {transacao.valor}')
        else:
            if transacao.valor < self.saldo:
                self.saldo -= transacao.valor
                self.listaTransacao.append(transacao)
            else:
                self.__limite = (transacao.valor - self.saldo)
                self.saldo = 0
                self.listaTransacao.append(transacao)
    
    # Função abstrata herdada da superclasse/classe pai
    def imprimirExtrato(self):
        print('Número da Conta: {}'. format(self.numConta))
        print('Nome Corretista: {}'. format(self.nome))
        print('Saldo: {}'. format(self.saldo))
        print('Limite: {}'. format(self.limite))
        print('****Transações***')
        for list in self.listaTransacao:
            print('Data: {} - Valor: {} - Descrição: {}'. format(list.data, list.valor, list.descricao))
        print()

# Início da main
if __name__ == "__main__":
    # Criação das instancias das contas (poupança, corrente e corrente com limite)
    contaP = ContaPoupanca(123, 'Letícia Santos', 4500, '03')
    contaCC = ContaCorrenteComum(456, 'Matheus Menezes', 9800)
    contaCL = ContaCorrenteLimite(789, 'Flavia Menezes', 2000, 200)
    # Criação de lista contendo as instâncias
    listaContas = [contaP, contaCC, contaCL]

    # Impressão das transações realizadas nas contas
    for list in listaContas:
        list.imprimirExtrato()
    print()

    # Criação de instâncias das transações
    trans1 = Transacao('03/12/2021', 400, 'Depósito')
    trans2 = Transacao('31/12/2021', 500, 'Depósito')
    trans3 = Transacao('03/08/2021', 400, 'Depósito')

    # Depositando dinheiro nass contas
    contaP.depositarConta(trans1)
    contaCC.depositarConta(trans2)
    contaCL.depositarConta(trans3)

    # Impressão das transações realizadas nas contas
    for list in listaContas:
        list.imprimirExtrato()
    print()

    # Criação de instâncias das transações
    trans4 = Transacao('07/01/2022', 2000, 'Retirada')
    trans5 = Transacao('22/01/2022', 11000, 'Retirada')
    trans6 = Transacao('11/01/2022', 2500, 'Retirada')

    # Retirando dinheiro das contas, caso possível (caso não uma mensagem é printada)
    contaP.retirarConta(trans4)
    contaCC.retirarConta(trans5)
    contaCL.retirarConta(trans6)
    print()

    # Impressão das transações realizadas nas contas
    for list in listaContas:
        list.imprimirExtrato()
    print()

# Fim da main
    