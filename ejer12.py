#12 nombre de archivo
nombre_archivo=input('ingresa el nombre de archo: ')
diccionario={
'.gif':'image/gif',
'.jpg':'image/jpeg',
'.jpeg':'image/jpeg',
'.png':'image/png',
'.pdf':'aplication/pdf',
'.txt':'text/plain',
'.zip':'aplication/zip',
}
archivo_minusculas=nombre_archivo.lower()
if archivo_minusculas.endswith('.gif')==True:
    nombre=diccionario['.gif']
elif archivo_minusculas.endswith('.jpg')==True:
    nombre=diccionario['.jpg']
elif archivo_minusculas.endswith('.jpeg')==True:
    nombre=diccionario['.jpeg']
elif archivo_minusculas.endswith('.png')==True:
    nombre=diccionario['.png']
elif archivo_minusculas.endswith('.pdf')==True:
    nombre=diccionario['.pdf']
elif archivo_minusculas.endswith('.txt')==True:
    nombre=diccionario['.txt']
elif archivo_minusculas.endswith('.zip')==True:
    nombre=diccionario['.zip']
salida_esperada=nombre
print(f'Tipo de archivo MIME: {salida_esperada}')
