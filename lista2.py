estado = True
productos = []
precios = []
while estado:
    try:
        print("1. Comprar")
        print("2. Pagar")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            producto = input("Ingrese un producto: ")
            precio = int(input("Ingrese un precio: "))
            while precio <= 0:
               precio = int(input("El precio ingresado no es válido... intente nuevamente: "))

            productos.append(producto)
            precios.append(precio)
        elif opcion == 2:
            if len(productos) > 0:
                print(f"Se han ingresado {len(productos)} productos. Los productos ingresados hasta aquí son: {productos}") 
                print(f"Suma a pagar es: {sum(precios)}") 
            else:
                print("No hay productos ingresados")
        elif opcion == 3:
            print("Muchas gracias por preferirnos")
            estado = False
        else:
            print("Opción no válida")
    except ValueError:
        print("Error: dato inválido")
    finally:
        print("App de Compras")      
        