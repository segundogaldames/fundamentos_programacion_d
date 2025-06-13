def cargar():
    palabras = {}
    continua = 's'
    while continua == 's':
        castellano = input("Ingrese una palabra en español: ")
        ingles = input("Ingrese el término en inglés: ")
        palabras[ingles] = castellano
        continua = input("Desea continuar? s/n")

    return palabras

def imprimir(palabras):
    for ingles in palabras:
        print(ingles, palabras[ingles])

def buscador(palabras):
    palabra = input("Ingrese la palabra que desea consultar: ")
    if palabra in palabras:
        print(f"En español significa: {palabras[palabra]}")
    else:
        print("Término no encontrado")
estado = True
while estado:
    try:
        palabras = cargar()
        imprimir(palabras)
        buscador(palabras)

        estado = False
    except ValueError:
        print("Error")
    finally:
        print("Diccionario ingles/español")