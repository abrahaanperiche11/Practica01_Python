#2 Consumo 
costo=float(input('¿Cuanto fue tu consumo en el restaurante?: '))
porcentaje_propina=float(input('ingresa el porcentaje (%) que desea dejar de propina: '))
porcentaje_propina=porcentaje_propina/100
costo_propina=costo*porcentaje_propina
print(f'debería dejar de propina {costo_propina}')