estado = True
notas = []
while estado:
    try:
        print("1. Ingresar Notas")
        print("2. Ver Resultados")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            nota = float(input("Ingrese la nota: "))

            while nota < 1 or nota > 7:
                nota = float(input("La nota no es válida... intente de nuevo: "))

            notas.append(nota)
        elif opcion == 2:
            if len(notas) > 0:
                print(f"Las notas ingresadas hasta aquí son: {notas}")
                promedio  = sum(notas) / len(notas)
                print(f"El promedio de las notas ingresadas es: {round(promedio,2)}")
            else:
                print("No se han ingresado notas al sistema")
        elif opcion == 3:
            print("Gracias por usar nuestra App")
            estado = False
        else: 
            print("Opción no válida")
    except ValueError:
        print("Error: datos no válidos")
    finally:
        print("App de notas")