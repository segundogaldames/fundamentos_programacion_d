def cargar():
    personas = {}
    print("Ingrese cuatro personas con su rut: ")
    for x in range(4):
        rut = int(input(f"Ingrese el rut de la persona {x+1} sin digito verificador  sin puntos ni guion: "))

        while len(str(rut)) < 7 or len(str(rut)) > 8:
            rut = int(input("El rut ingresado no es válido... intente nuevamente: "))

        nombre = input("Ingrese el nombre de la persona con rut {rut}: ")
        personas[rut] = nombre
    return personas

def imprimir(personas):
    print("Lista de personas")
    for rut in personas:
        print(rut, personas[rut])

def buscador(personas):
    rut = int(input("Ingrese el rut de la persona que busca"))
    if rut in personas:
        print(f"El nombre asociado al rut {rut} es {personas[rut]}")
    else:
        print(f"No se encuentra una persona asociada al rut {rut}")

estado = True
while estado:
    try:
        personas = cargar()
        imprimir(personas)
        buscador(personas)

        estado = False
    except ValueError:
        print("Error: dato incorrecto")
    finally:
        print("App de Registro de Personas")