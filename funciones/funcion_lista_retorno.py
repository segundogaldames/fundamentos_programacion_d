def cargar():
    li = []
    for x in range(3):
        valor = int(input(f"Ingrese el valor {x+1}"))
        li.append(valor)
    return li

def mayor_menor(lista):
    mayor = lista[0]
    menor = lista[0]

    for x in range(1,len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]
        else:
            if lista[x] < menor:
                menor = lista[x]
    return [mayor, menor]

estado = True
while estado:
    try:
        lista = cargar()
        rango = mayor_menor(lista)
        print(f"Los datos ingresados son {lista}")
        print(f"El mayor valor es {rango[0]}")
        print(f"El menor valor es {rango[1]}")

        estado = False
    except ValueError:
        print("Error")
    finally:
        print("App")

    