tamanho = int(input('Diga quantos nomes deseja digitar: '))
lista_nome = []
for cont in range(tamanho):
    lista_nome.append(input('Digite o nome: '))

nome = input('Digite um nome: ')

if nome in lista_nome:
    print('O nome ' + nome + ' está entre os nomes listados!')
else: 
    print('O nome ' + nome + ' não está entre os nomes listados!')
