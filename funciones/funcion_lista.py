def suma(numeros):
    return sum(numeros)

def promedio(numeros):
    return sum(numeros)/len(numeros)

def mayor(numeros):
    may = numeros[0]
    for x in range(1,len(numeros)):
        if numeros[x] > may:
            may = numeros[x]
    
    return may

def menor(numeros):
    men = numeros[0]
    for x in range(1,len(numeros)):
        if numeros[x] < men:
            men = numeros[x]

    return men

def error():
    return "Error: valores incorrectos"

def mensaje():
    return "App Listas"

estado = True
while estado:
    try:
        numeros = []
        print("Ingrese 5 valores enteros")
        for x in range(5):
            numero = int(input(f"Ingrese el valor {x+1}: "))
            numeros.append(numero)

        print(f"Los datos ingresados son: {numeros}")
        print(f"La suma de los valores ingresados es {suma(numeros)}")
        print(f"El promedio de los valores ingresados es {promedio(numeros)}")
        print(f"El valor mayor es {mayor(numeros)}")
        print(f"El valor menor es {menor(numeros)}")
    except ValueError:
        print(error())
    finally:
        print(mensaje())