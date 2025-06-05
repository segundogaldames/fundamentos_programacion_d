estado = True
numeros = []
while estado:
    try:
        print("Ingrese 5 numeros enteros")
        for x in range(5):
            numero = int(input(f"Ingrese el valor {x+1}: "))
            numeros.append(numero)

        mayor = numeros[0]
        for x in range(1,5):
            if numeros[x] > mayor:
                mayor = numeros[x]

        print(f"Los datos ingresados son {numeros}")
        print(f"El valor mayor es: {mayor}")

        estado = False
    except ValueError:
        print("Error: dato incorrecto")
    finally:
        print("App de números")