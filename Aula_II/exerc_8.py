def conversor(c):
    f = c * (9 / 5) + 32
    return f

celsius = float(input('Diga a temperatura em Celsius: '))
farenheit = conversor(celsius)
print('A temperatura ' + str(celsius) + ' C equivale a: ' + str(farenheit) + ' F')
