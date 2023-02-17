def palindromo(str):
    palin = True
    for i in range(int(len(str)/2)):
        if str[i] != str[int(len(str)-i-1)]:
            palin = False
    if palin:
        return True
    else:
        return False

#capitalize() -> primeira letra maiúscula
palavra = input('Diga uma palavra: ').upper()
verificador = palindromo(palavra)

if verificador:
    print(palavra + ' é um palíndromo!')
else:
    print(palavra + ' não é um palíndromo!') 