print(dir(__builtins__))  # para saber funciones builtin que hay en python
# funcion zip nos permite unir iterables
help(zip)
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
identificadores = 321, 322, 323, 324, 325
mezcla = zip(numeros, letras, identificadores)  # unimos los iterables y creamos un objeto zip
print(mezcla)
# para poder iterarlo debemos convertirlo a una lista por ejemplo
print(list(mezcla))  # creamos una lista, donde cada elemento es una tupla de un numero, una letra y un identificador
print(tuple(zip(numeros, letras)))  # tambien es valido, pero debemos hacer el zip de nuevo en este caso porque ya lo
                                    # consumimos de la variable mezcla, y solo se puede consumir una vez
# hay que tener cuidado con los set, ya que en ese caso el orden en que se agregaran al zip es aleatorio

# iteracion en paralelo con zip, esto es muy util para realizar tareas en paralelo
for numero, letra, identificador in zip(numeros, letras, identificadores):
    print(f'Numero: {numero}, Letra: {letra}, Id: {identificador}')

nueva_lista = []
for numero, letra, identificador in zip(numeros, letras, identificadores):
    nueva_lista.append(f'{identificador}--{numero}--{letra}')

print(nueva_lista)

# unzip
mezcla = [(1, 'a'), (2, 'b'), (3, 'c')]
numeros, letras = zip(*mezcla)  # asi se hace unzip
print(numeros, letras)

# ordenamiento usando zip
letras = ['c', 'd', 'a', 'e', 'b']
numeros = [3, 2, 4, 1, 0]
mezcla = zip(letras, numeros)
# sin ordenar
print(tuple(mezcla))
# ordenar por letra , primer iterable
print(sorted(zip(letras, numeros)))  # se ordenaran las letras
print(sorted(zip(numeros, letras)))  # se ordenaran por numeros

# crear diccionario a partir de 2 iterables usando zip
# un iterable correspondera a las keys y otro a los values
keys = ['Nombre', 'Apellido', 'Edad']
values = ['Juan', 'Perez', 18]
diccionario = dict(zip(keys, values))  # dict es el constructor de la clase dictionary
print(diccionario)

# actualizar elemento de un diccionario con zip
key = ['Edad']  # tenemos que usar un iterable para poder trabajar con zip, la llave debe tener el mism nombre obviamente
nueva_edad = [34]
diccionario.update(zip(key, nueva_edad))
print(diccionario)

