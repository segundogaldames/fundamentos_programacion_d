def cuadrado(numero):
    return numero * numero

def producto(num1, num2):
    return num1 * num2

def mensaje():
    return 'App de números'

estado = True
while estado:
    try:
        #programa principal
        print("Ingrese un valor para calcular el cuadrado")
        numero = int(input("Ingrese un número: "))
        resultado = cuadrado(numero)
        print(f"El cuadrado del número es {resultado}")
        #otra forma de llamar y ejecutar la funcion
        print(f"El cuadrado del número es {cuadrado(numero)}")

        #calcular producto
        print("Ingrese dos valores para calcular el producto")
        valor1 = int(input("Ingrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))
        producto = producto(valor1, valor2)
        print(f"El producto de los valores ingresados es: {producto}")
    
        estado = False
    except ValueError:
        print("Error: dato incorrecto")
    finally:
        print(mensaje())
        