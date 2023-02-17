'''
    Criando Superclasses/Classe pai e subclasses/Classe filha
    Autor: Letícia Vitória dos Santos
    Ultima aulteração: 06/11/2022
'''
from abc import ABC, abstractmethod

# Criação de classe abstrata, superclasse/classe pai
class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone
    
    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome

    def getTelefone(self):
        return self.__telefone
    
    def setTelefone(self, telefone):
        self.__telefone = telefone

    # Criação de função abstrata
    @abstractmethod
    def getSalario(self):
        pass

# Classe que herda os atributos e funções da Classe Pessoa/ Subclasse ou Classe Filha
class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorHora = valorHora
    
    def getHorasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    def getValorHora(self):
        return self.__valorHora
    
    # Definição da função herdada (calculo do salario de empregada domestica do tipo horista)
    def getSalario(self):
        return self.__horasTrabalhadas * self.__valorHora
    
# Classe que herda os atributos e funções da Classe Pessoa/ Subclasse ou Classe Filha
class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorDia = valorDia
    
    def getDiasTrabalhados(self):
        return self.__diasTrabalhados
    
    def getValorDia(self):
        return self.__valorDia
    
    # Definição da função herdada (calculo do salario de empregada domestica do tipo diarista)
    def getSalario(self):
        return self.__diasTrabalhados * self.__valorDia

# Classe que herda os atributos e funções da Classe Pessoa/ Subclasse ou Classe Filha   
class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, salario):
        super().__init__(nome, telefone)
        self.__salario = salario
    
    # Definição da função herdada (calculo do salario de empregada domestica do tipo mensalista)
    def getSalario(self):
        return self.__salario

# Início da main
if __name__ == "__main__":
    # Criação das instâncias das subclasses/ classes filhas
    empHorista = Horista('Maria', 35999887766, 160, 12)
    empDiarista = Diarista('Ana', 35999554433, 20, 65)
    empMensalista = Mensalista('Carla', 35999443322, 1200)
    # Criação de lista com as instâncias criadas
    empsDomesticas = [empHorista, empDiarista, empMensalista]
    # Criação de variável que ira representar o menor salário entre as empregadas
    menorSalario = empHorista.getSalario()
    # Verificação de cada uma das empregadas
    for emp in empsDomesticas:
        print('Nome: {} - Salario: {}'. format(emp.getNome(), emp.getSalario()))
        if (emp.getSalario() < menorSalario):
            menorSalario = emp.getSalario()
            tel = emp.getTelefone()
            nome = emp.getNome()
    
    # Print da empregada com o menor custo de salário
    print('\n----Opção mais barata----\n')
    print('Nome: {}\nTel: {}\nSalário: {}'. format(nome, tel, menorSalario))

# Fim da main
    