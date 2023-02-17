'''
    Tratando exceções em Python
    Autor: Letícia Vitória dos Santos
    Ultima aulteração: 06/11/2022
'''
from abc import ABC, abstractmethod

# Classes do tipo exception
class IdadeMenorQuePermitida(Exception):
    pass

class IdadeInvalida(Exception):
    pass

class TitulacaoInvalida(Exception):
    pass

class CursoInvalido(Exception):
    pass

class CPFJaCadatrado(Exception):
    pass

# Classe abstrata/ Superclasse ou Classe Pai
class Pessoa(ABC):
    def __init__(self, nome, cpf, endereco, idade) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__idade = idade
        
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def idade(self):
        return self.__idade
    
    # Função abstrata
    @abstractmethod
    def printDescricao(self):
        pass

# Classe que herda os atributos e funções da Classe Pessoa/ Subclasse ou Classe Filha
class Professor(Pessoa):
    def __init__(self, nome, cpf, endereco, idade, titulacao) -> None:
        super().__init__(nome, cpf, endereco, idade)
        self.__titulacao = titulacao
    
    @property
    def titulacao(self):
        return self.__titulacao
    
    # Definição da função abstrata herdada (Imprime os dados pertencentos a Classe Professor)
    def printDescricao(self):
        print(f'Professor: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'CPF: {self.cpf}')
        print(f'Endereço: {self.endereco}')
        print(f'Titulação: {self.__titulacao}')
        
# Classe que herda os atributos e funções da Classe Pessoa/ Subclasse ou Classe Filha
class Aluno(Pessoa):
    def __init__(self, nome, cpf, endereco, idade, curso) -> None:
        super().__init__(nome, cpf, endereco, idade)
        self.__curso = curso
    
    @property
    def curso(self):
        return self.__curso
    
    # Definição da função abstrata herdada (Imprime os dados pertencentos a Classe Aluno)
    def printDescricao(self):
        print(f'Aluno: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'CPF: {self.cpf}')
        print(f'Endereço: {self.endereco}')
        print(f'Curso: {self.__curso}')
    
# Início da main
if __name__ == '__main__':
    # Criação das instancias do tipo Professor e do Tipo Aluno
    prof1 = Professor('Pedro Henrique', 12345, 'Av. BPS, 32', 33, 'doutor')
    prof2 = Professor('João Luiz', 65432, 'Av JK, 65', 25, 'doutor')
    prof3 = Professor('Ana Maria', 78945, 'Rua Major Belo Lisboa, 22', 37, 'mestre')
    aluno1 = Aluno('Letícia Santos', 65498, 'Açude, 21', 21, 'SIN')
    aluno2 = Aluno('Matheus Menezes', 65498, 'Carneiros, 30', 24, 'SIN')
    aluno3 = Aluno('Flavia Souza', 12456, 'Medicina, 65', 30, 'Pedagogia')
    aluno4 = Aluno('Vitoria Silva', 96385, 'Centro, 985', 16, 'CCO')
    aluno5 = Aluno('Maria Eduarda', 98732, 'Pinheirinho, 564', -19, 'SIN')
    
    # Criação de lista contendo as instâncias criadas
    listaPessoas = [prof1, prof2, prof3, aluno1, aluno2, aluno3, aluno4, aluno5]

    # Criação de lista que armazenara as instâncias sem erros ou invalidações
    cadastro = []
    
    # For para percorrer toda a lista contande as instâncias
    for list in listaPessoas:

        # Código a ser executado
        try:
            # Verificação de duplicação de CPF
            for pes in cadastro:
                if list.cpf == pes.cpf:
                    # Chamada de Exception
                    raise CPFJaCadatrado()
            # Verificação de validade de idade
            if list.idade < 0:
                # Chamada de Exception
                raise IdadeInvalida()
            # Verificação para instâncias do tipo Professor
            if (type(list) == Professor):
                # Verificação de idade apropriada 
                if list.idade < 30:
                    # Chamada de Exception
                    raise IdadeMenorQuePermitida()
                # Verificação de validade de titulação
                if list.titulacao != 'doutor':
                    # Chamada de Exception
                    raise TitulacaoInvalida()
            # Verificação para instâncias do tipo Aluno
            else:
                # Verificação de idade apropriada 
                if list.idade < 18:
                    # Chamada de Exception
                    raise IdadeMenorQuePermitida()
                # Verificação de validade de curso
                if (list.curso != 'SIN') and (list.curso != 'CCO'):
                    # Chamada de Exception
                    raise CursoInvalido()
        # Excepts a serem executadas caso chamadas
        except CPFJaCadatrado:
            print(f'O CPF {list.cpf} já se encontra cadastrado!')
        except IdadeInvalida:
            print('A idade digitada é invalida!')
        except IdadeMenorQuePermitida:
            print(f'A idade {list.idade} é menor do que a permitida para esse tipo de cadastro!')
        except TitulacaoInvalida:
            print(f'A titulação "{list.titulacao}" não é permitida para esse cadastro!')
        except CursoInvalido:
            print(f'O curso "{list.curso}" não está disponível para cadastro!')
        # Caso nenhuma except sejá executada, a instância é adicionada a lista de cadastro
        else:
            cadastro.append(list)

    # Print da descrição das instâncias adicionadas na lista cadastro
    print()
    for cad in cadastro:
        cad.printDescricao()
        print()

# Fim da main