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


