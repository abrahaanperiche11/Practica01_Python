#3 Jugetería
peso_payaso=112
peso_muñeca=75
numero_muñeca=int(input('ingresar el número de muñecas vendidas: '))
numero_payaso=int(input('ingresar el número de payasos vendidos: '))
peso_paquete=peso_payaso*numero_payaso+peso_muñeca*numero_muñeca
print(f'El peso total es de {peso_paquete} (g)')