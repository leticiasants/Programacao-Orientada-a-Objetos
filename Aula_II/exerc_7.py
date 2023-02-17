lista_num = []
num = 1
soma = 0

while num != 0:
    num = int(input('Diga um número: '))
    if num != 0:
        lista_num.append(num)

for i in range(int(len(lista_num))):
    soma = soma + lista_num[i]

media = soma/int(len(lista_num))

print('A média dos números digitados é: ' + str(media))
