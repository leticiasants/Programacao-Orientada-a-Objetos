class Curso:
    def __init__(self, nome):
        self.__nome = nome

        self.__grade = None
        self.__lstAlunos = []
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def grade(self):
        return self.__grade
    
    @property
    def lstAlunos(self):
        return self.__lstAlunos
    
    def addGrade(self, grade):
        self.__grade = grade

    def addLstAlunos(self, aluno):
        self.__lstAlunos.append(aluno)


class Grade:
    def __init__(self, ano, curso):
        self.__ano = ano
        self.__curso = curso

        self.__lstDisciplinas = []
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def curso(self):
        return self.__curso
    
    @property
    def lstDisciplinas(self):
        return self.__lstDisciplinas
    
    def addDisciplina(self, disciplina):
        self.__lstDisciplinas.append(disciplina)


class Disciplina:
    def __init__(self, codigo, nome, cargaHoraria, grade):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
        self.__grade = grade
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cargaHoraria(self):
        return self.__cargaHoraria

    @property
    def grade(self):
        return self.__grade

    def curso(self):
        return self.__grade.curso

class Aluno:
    def __init__(self, nroMatricula, nome, curso):
        self.__nroMatricula = nroMatricula
        self.__nome = nome
        self.__curso = curso

        self.__historico = Historico(self)
    
    @property
    def nroMatricula(self):
        return self.__nroMatricula
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def curso(self):
        return self.__curso
    
    def addLtsDisc(self, disciplina):
        if (disciplina.curso() == self.__curso):
            self.__historico.addDiscObrigatoria(disciplina)
        else:
            self.__historico.addDiscEletiva(disciplina)
        
    @property
    def historico(self):
        return self.__historico
    

class Historico:
    def __init__(self, aluno):
        self.__aluno = aluno

        self.__lstDiscObrigatorias = []
        self.__lstDiscEletiva = []
    
    @property
    def aluno(self):
        return self.__aluno

    @property
    def lstDiscObrigatorias(self):
        return self.__lstDiscObrigatorias
    
    @property
    def lstDiscEletiva(self):
        return self.__lstDiscEletiva
    
    def nomeAluno(self):
        return self.aluno.nome()
    
    def addDiscObrigatoria(self, disciplina):
        self.__lstDiscObrigatorias.append(disciplina)
    
    def addDiscEletiva(self, disciplina):
        self.__lstDiscEletiva.append(disciplina)



if __name__ == "__main__":
    curso1 = Curso('Sistemas de Informa????o')
    curso2 = Curso('Ci??ncia da Computa????o')
    grade1 = Grade(2022, curso1)
    grade2 = Grade(2016, curso2)

    disc1 = Disciplina('XDES01', 'Fundamentos de Programa????o', 64, grade1)
    disc2 = Disciplina('XDES02', 'Programa????o OO', 64, grade1)
    disc3 = Disciplina('STCO01', 'Algoritmos e Programa????o I', 64, grade1)
    disc4 = Disciplina('ECOX21', 'Maratona de Programa????o I', 48, grade1)
    disc5 = Disciplina('XMCO03', 'M??todos Exatos', 64, grade1)
    disc6 = Disciplina('CIC130', 'Introdu????o ?? CCO', 32, grade2)
    disc7 = Disciplina('MAT050', 'Fundamentos de Matem??tica', 64, grade2)
    disc8 = Disciplina('MAT001', 'C??lculo I', 96, grade2)
    disc9 = Disciplina('SPAD06', 'Mineira????o de Dados', 64, grade2)
    disc10 = Disciplina('XDES15', 'Reutiliza????o de Software', 64, grade2)

    aluno1 = Aluno(2022002542, 'Let??cia Santos', curso1)
    aluno2 = Aluno(2019018630, 'Matheus Menezes', curso2)

    curso1.addLstAlunos(aluno1)
    curso2.addLstAlunos(aluno2)

    aluno1.addLtsDisc(disc1)
    aluno1.addLtsDisc(disc2)
    aluno1.addLtsDisc(disc3)
    aluno1.addLtsDisc(disc9)
    aluno1.addLtsDisc(disc10)
    aluno2.addLtsDisc(disc6)
    aluno2.addLtsDisc(disc7)
    aluno2.addLtsDisc(disc8)
    aluno2.addLtsDisc(disc4)
    aluno2.addLtsDisc(disc5)

    historico1 = aluno1.historico
    historico2 = aluno2.historico

    lstHistorico = [historico1, historico2]

    print('****************** HIST??RICO DOS ALUNOS ******************')
    print()
    for his in lstHistorico:
        print(f'Aluno: {his.aluno.nome} - Matr??cula: {his.aluno.nroMatricula}')
        print('*** Disciplinas Obrogat??rias ***')
        totalCgHObrig = 0
        for dis in his.lstDiscObrigatorias:
            print(f'{dis.codigo} - {dis.nome} - Carga Horaria: {dis.cargaHoraria}hrs')
            totalCgHObrig += dis.cargaHoraria
        print()
        print(f'Carga hor??ria brigat??ria total: {totalCgHObrig}')
        print()
        print('*** Disciplinas Eletiva ***')
        totalCgHEle = 0
        for dis in his.lstDiscEletiva:
            print(f'{dis.codigo} - {dis.nome} - Carga Horaria: {dis.cargaHoraria}hrs')
            totalCgHEle += dis.cargaHoraria
        print()
        print(f'Carga hor??ria brigat??ria total: {totalCgHEle}')
        print()
        print('-------------------------------------------------------')
        print()
