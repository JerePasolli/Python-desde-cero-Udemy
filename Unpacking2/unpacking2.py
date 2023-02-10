# * desempaquetar, aplica a cualquier iterable excepto diccionarios
numeros = [1, 2, 3]
print(numeros)
print(*numeros, sep=' - ')  # para desempaquetar, podemos agregar un separador

# para hacer lo mismo en diccionario debemos usar **

# tambien podemos usar unpacking en funciones


def sumar(a, b, c):
    print(f'Resultado: {a+b+c}')


# sumar(numeros)  # no funcionara, ya que la lista cuenta como un solo argumento, y la funcion necesita 3
sumar(*numeros)  # haciendo uso de unpacking la funcion rebira los 3 parametros que tiene la lista

# extraer algunas partes de una lista
mi_lista = list(range(1, 7))
print(mi_lista)
a, *b, c, d = mi_lista  # a alguna variable le debemos colocar operador de unpacking, ya que son 4 variables y la lista
                        # tiene 6 elementos
print(a, b, c, d)  # b sera una lista con los valores 2, 3 y 4

# unir listas con unpacking
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [lista1, lista2]  # no va a concatenar listas, sino que creara una lista de listas (matriz)
print(lista3)
lista3 = [*lista1, *lista2]  # ahora si creamos una tercer lista que es la suma de las dos anteriores, usando unpacking
print(lista3)

# unir diccionarios con operador **
dicc1 = {'A':1, 'B':2, 'C':3}
dicc2 = {'D':4, 'E':5}
dicc3 = {**dicc1, **dicc2}  # creamos un diccionario que es concatenacion de los otros dos
print(dicc3)

# construir lista a partir de string
lista = [*'HolaMundo']  # crearemos una lista con los caracteres de la cadena
print(lista)
print(*lista, sep='-')
