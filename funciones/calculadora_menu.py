def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def producto(a, b):
    return a * b

def division(a,b):
    if b == 0:
        return "No se puede dividir por cero"
    return a/b

def error():
    return "Error: valores incorrectos"

def mensaje():
    return "App Calculadora"

def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def ingresar_opcion():
    opcion = int(input("Seleccione una opción: "))

    while opcion < 1 or opcion > 5:
        opcion = int(input("La opción no es correcta... intente de nuevo: "))

    return opcion

estado = True
while estado:
    try:
        menu()
        op = ingresar_opcion()

        if op == 5:
            print("Gracias por usar nuestra App")
            estado= False
        else:
            valor1 = int(input("Ingrese el primer valor: "))
            valor2 = int(input("Ingrese el segundo valor: "))

            if op == 1:    
                print(f"La suma es {suma(valor1, valor2)}")
            elif op == 2:
                print(f"La resta es {resta(valor1, valor2)}")
            elif op == 3:
                print(f"El producto es {producto(valor1, valor2)}")
            elif op == 4:
                print(f"El cuociente es {division(valor1, valor2)}")
            else:
                print(error())

    except ValueError:
        print(error())
    finally:
        print(mensaje())