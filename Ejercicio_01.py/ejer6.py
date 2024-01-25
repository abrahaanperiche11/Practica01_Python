#6 cobrar entrada
edad=int(input('ingresa tu edad: '))
if edad<4:
    ratio=0
elif edad>=4 and edad<=18:
    ratio=5
elif edad>18:
    ratio=10
print(f'Debe pagar {ratio} dolares para su entrada')