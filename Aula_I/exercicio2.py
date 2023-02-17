import random
num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o segundo numero: ")
# gerar numero aleatório entre os números estabelecidos
# int() é utilizado para converter a variavel dentro dos () para o tipo inteiro
print(random.randrange(int(num1), int(num2)))
