 #8 Hora
hora=input("ingresa la hora en formato 24:00 : ")
horas, minutos=hora.split(":")
horas=float(horas)
minutos=float(minutos)
if minutos<60:
    hora_desimal=horas+minutos*(1/60) #llevaremos a un solo número en sistema decimal para hacer una comparación más facil
    if hora_desimal>=7 and hora_desimal<=8:
        print('hora de desayunar')
    elif hora_desimal>=12 and hora_desimal<=13:
        print('hora de almorzar')
    elif hora_desimal>=18 and hora_desimal<=19:
        print('hora de cenar')
    else:
        print(' ')
else:
    print('No corresponde con el formato de 60 minutos por hora')