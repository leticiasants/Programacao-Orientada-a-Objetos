renda = float(input('Diga o valor de sua renda: '))
if renda > 4664.68:
    aliquota = 27.5
elif renda > 3751.06:
    aliquota = 22.5
elif renda > 2826.66:
    aliquota = 15
elif renda > 1903.99:
    aliquota = 7.5
else:
    aliquota = 0

if aliquota > 0:
    imposto = renda*(aliquota/100)
else: 
    imposto = 0


print('Alíquota: ' + str(aliquota) + ' Imposto: ' + str(imposto))