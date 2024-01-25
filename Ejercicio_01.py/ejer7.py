 #7 opciones
primer_numero=float(input('ingresa el primer número: '))
segundo_numero=float(input('ingresa el segundo número: '))   
opcion=input('''¿Que deseas hacer? 
             A) Sumar ambos números
             B) Diferencia del primer numero con el segundo número
             C) Multiplicar los números
Ingrese la opción deseada: ''')
opcion=opcion.upper()
if opcion=='A':
    ratio=primer_numero+segundo_numero
elif opcion=='B':
    ratio=primer_numero-segundo_numero
elif opcion=='C':
    ratio=primer_numero*segundo_numero
else:
    print('Error, no se marcó ninguna opción')
print(f'el resultado es {ratio}')