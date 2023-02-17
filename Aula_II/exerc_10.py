import datetime 

def conversor_segundos(hr, min, seg):
    total_seg = seg + min*60 + hr*3600
    return total_seg

def conversor(seg):
    total = str(datetime.timedelta(seconds = seg)) 
    return total

print('Horario de entrada')
horas_ent = int(input('Diga as horas: '))
minutos_ent = int(input('Diga os minutos: '))
segundos_ent = int(input('Diga os segundos: '))

print('Horario de saída')
horas_sai = int(input('Diga as horas: '))
minutos_sai = int(input('Diga os minutos: '))
segundos_sai = int(input('Diga os segundos: '))

segundo_total = conversor_segundos(horas_sai, minutos_sai, segundos_sai) - conversor_segundos(horas_ent, minutos_ent, segundos_ent) 

horas_total = conversor(segundo_total)

print('O tempo total em segundos é: ' + str(segundo_total))
print('O tempo total em horas é: ' + str(horas_total))
