from abc import ABC, abstractmethod

class Professor(ABC):
    def __init__(self, nome, matricula, cargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.cargaHoraria = cargaHoraria

    @property
    def nome(self):
        return self.__nome
    @property
    def matricula(self):
        return self.__matricula

    @property
    def cargaHoraria(self):
        return self.__cargaHoraria

    @cargaHoraria.setter
    def cargaHoraria(self, valor):
        if valor > 160:
            print('Ajustando valor da carga horária.')
            self.__cargaHoraria = 160
        else:
            self.__cargaHoraria = valor

    @abstractmethod
    def calculaSalario(self):
        pass

    @abstractmethod
    def imprimeDados(self):
        pass

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salario):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        if valor < 1100:
            print('Proibido pagar menos que o salário mínimo')
            self.__salario = 1100
        else:
            self.__salario = valor
    
    def calculaSalario(self):
        return self.__salario

    def imprimeDados(self):
        print('Nome: {}'. format(self.nome))
        print('Matrícula: {}'. format(self.matricula))
        print('Carga Horária: {}'. format(self.cargaHoraria))
        print('Salário Líquido: {}'. format(self.calculaSalario()))
        print()
    

class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioHora = salarioHora

    @property
    def salarioHora(self):
        return self.__salarioHora

    @salarioHora.setter
    def salarioHora(self, salarioHora):
        self.__salarioHora = salarioHora 

    def calculaSalario(self):
        return self.__salarioHora * self.cargaHoraria

    def imprimeDados(self):
        print('Nome: {}'. format(self.nome))
        print('Matrícula: {}'. format(self.matricula))
        print('Carga Horária: {}'. format(self.cargaHoraria))
        print('Salário Hora: {}'. format(self.__salarioHora))
        print('Salário Líquido: {}'. format(self.calculaSalario()))
        print()

if __name__ == "__main__":
    prof1 = ProfDE('Joao', 12345, 40, 5000)
    prof2 = ProfHorista('Paulo', 54321, 30, 75)
    prof3 = ProfHorista('Ana', 56789, 38, 95)
    profs = [prof1, prof2, prof3]
    for prof in profs:
        prof.imprimeDados()
    prof1.salario = 1000
    prof2.salarioHora = 100
    prof3.salarioHora = 120
    for prof in profs:
        prof.imprimeDados()