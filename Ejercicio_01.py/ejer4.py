#4 Suma de números
N=int(input('ingresa un número entero positivo: '))
if N>0:
    suma_primeros_numeros=N*(N+1)*0.5
    print(f'la suma de los primeros números positivos desde 1 hasta {N} es {suma_primeros_numeros}')
else:
    print('No es un número positivo')