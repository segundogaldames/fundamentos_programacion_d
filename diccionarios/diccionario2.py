def cargar():
    productos = {}
    for x in range(5):
        nombre = input(f"Ingrese el nombre del producto {x+1}: ")
        precio = int(input(f"Ingrese el precio del producto {x+1}: "))
        productos[nombre] = precio

    return productos

def mayor(productos):
    print("Lista de productos mayores a 10000")
    for nombre in productos:
        if productos[nombre] > 10000:
            print(nombre)

def imprimir(productos):
    print("Lista de productos")
    for nombre in productos:
        print(nombre, productos[nombre])

estado = True
while estado:
    try:
        productos = cargar()
        imprimir(productos)
        mayor(productos)

        estado = False
    except ValueError:
        print("Error")
    finally:
        print("Diccionario de productos")

