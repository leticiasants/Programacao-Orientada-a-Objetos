palavra = input('Digite uma palavra: ').upper()
palindromo = True
for i in range(0, int(len(palavra)/2)):
    if palavra[i] != palavra[len(palavra)-i-1]:
        palindromo = False
        break
if palindromo: 
    print(palavra + ' é um palíndromo!')
else:
    print(palavra + ' não é um palíndromo!')
