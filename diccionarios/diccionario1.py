def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])

estado = True
while estado:
    try:
        paises = {"Argentina": 40000000, "España": 46000000, "Brasil": 190000000, "Uruguay": 34000000}

        print(imprimir(paises))
    
        estado = False
    except ValueError:
        print("Error")
    finally:
        print("Diccionarios")