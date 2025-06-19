from datetime import datetime
turistas = {
        "001": ["John Doe", "Estados Unidos", "12-01-2024"],
        "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
        "012": ["Julian Martinez", "Argentina", "19-09-2023"],
        "014": ["Agustin Morales", "Argentina", "28-03-2024"],
        "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
        "006": ["Maria Lopez", "Mexico", "08-12-2023"],
        "007": ["Joao Silva", "Brasil", "20-06-2024"],
        "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
        "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
        "008": ["Ana Santos", "Brasil", "03-10-2023"],
        "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
        "011": ["Sofia Gomez", "Argentina", "07-04-2024"]
    }

def menu():
    print("****Menú Principal****")
    print("1. Turistas Por País")
    print("2. Turistas Por Mes")
    print("3. Buscar Turista")
    print("4. Agregar Turista")
    print("5. Eliminar Turista")
    print("6. Salir")

    opcion = int(input("Seleccione una opción: "))
    while opcion < 1 or opcion > 6:
        opcion = int(input("Ingrese nuevamente la opción: "))

    return opcion

def menu_meses():
    meses = [
        "1. Enero", "2. Febrero", "3. Marzo", "4. Abril",
        "5. Mayo", "6. Junio", "7. Julio", "8. Agosto",
        "9. Septiembre", "10. Octubre", "11. Noviembre", "12. Diciembre"
    ]

    for mes in meses:
        print(mes)
    
    seleccion = int(input("Seleccione un mes de la lista: "))
    while seleccion < 1 or seleccion > 12:
        seleccion = int(input("Vuelva a seleccionar una opción: "))
    
    return seleccion

def turistas_pais(pais):
    lista = [datos[0] for datos in turistas.values() if datos[1].lower() == pais.lower()]
    if not lista:
        return "No hay turistas de " + pais.capitalize()
    
    return lista
    

def turistas_mes(mes):
    meses_nombre = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    total = len(turistas)
    contador = 0
    for datos in turistas.values():
        fecha = datos[2]
        mes_turista = int(fecha.split("-")[1])
        if mes_turista == mes:
            contador += 1
    porcentaje = round((contador / total) * 100, 1)
    nombre_mes = meses_nombre[mes - 1]
    return f"El porcentaje de turistas del mes {nombre_mes.capitalize()} es {porcentaje} % "

def buscar_turista(turista):
    encontrado = None
    for datos in turistas.values():
        if datos[0].lower() == turista:
            encontrado = datos

    if not encontrado:
        return "Turista no encontrado."
    
    return f"Nombre: {encontrado[0]} | País: {encontrado[1]} | Fecha ingreso: {encontrado[2]}"
    
def agregar_turista(id,datos):
    turistas[id] = datos

def validar_id(id):
    if id in turistas:
        return True
    return False

def fecha_valida(fecha):
    try:
        datetime.strptime(fecha, "%d-%m-%Y")
        return True
    except:
        return False

def eliminar_turista(turista):
    for id_turista, datos in list(turistas.items()):
        if datos[0].lower() == turista:
            del turistas[id_turista]
            return "Turista eliminado con exito."
    return "Turista no encontrado. No se pudo eliminar."

def mensaje():
    return "App de Turismo"

def error():
    return "Error: dato incorrecto"

def main():
    estado = True
    while estado:
        try:
            opcion = menu()

            if opcion == 1:
                pais = input("Ingrese país: ")
                print("Lista de Turistas:")
                print(turistas_pais(pais))
                print("***********************")

            elif opcion == 2:
                mes = menu_meses()

                print(turistas_mes(mes))
                print("****************")
            elif opcion == 3:
                nombre = input("Ingrese el nombre del turista que busca: ")
                print(buscar_turista(nombre))
                print("**********************")
            elif opcion == 4:
                id = input("Ingrese el id del turista").strip()

                if not validar_id(id):
                    nombre = input("Ingrese el nombre del turista: ").strip()
                    pais = input("Ingrese el nombre del pais: ").strip()
                    fecha = input("Ingrese la fecha de ingreso (dd-mm-aaaa): ").strip()

                    while not fecha_valida(fecha):
                        fecha = input("Ingrese nuevamente la fecha de ingreso (dd-mm-aaaa): ").strip()

                    agregar_turista(id,[nombre, pais, fecha])
                    if buscar_turista(nombre):
                        print("El turista se ha ingresado correctamente")
                    else:
                        print("No se ha podido completar el registro")
                else:
                    print("El id de turista ya existe... intente con otro")

            elif opcion == 5:
                nombre = input("Ingrese nombre del turista a eliminar: ").strip().lower()
                print(eliminar_turista(nombre))
            else:
                print("Gracias por usar nuestra App")
                estado = False
        except ValueError:
            print(error())
        finally:
            print(mensaje())

main()