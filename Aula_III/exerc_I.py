quant = int(input('Quantos nomes você deseja digitar? '))
lista_nome = []
lista_altura = []
maior = 0

for i in range(quant):
    nome = input('Digite o nome: ')
    lista_nome.append(nome)
    altura = int(input('Digite a altura(cm): '))
    lista_altura.append(altura)

for i in range(quant):
    if maior < lista_altura[i]:
        maior = lista_altura[i]
        num_maior = i
    
menor = maior 

for i in range(quant):
    if menor > lista_altura[i]:
        menor = lista_altura[i]
        num_menor = i
    
print('A pessoa mais alta é ' + lista_nome[num_maior] + ' com ' + str(lista_altura[num_maior]) + 'cm de altura')
print('A pessoa mais baixa é ' + lista_nome[num_menor] + ' com ' + str(lista_altura[num_menor]) + 'cm de altura')