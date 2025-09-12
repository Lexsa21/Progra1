"""
-----------------------------------------------------------------------------------------------
Título: TP Cuatrimestral - Sistema de Gestión de Cine 
Fecha: 14/10/24
Autor: Equipo 10

Descripción: El sistema de gestión del cine permite administrar las funciones y 
ventas de un complejo de cines. Permite controlar las películas que se van a proyectar, 
en qué fecha y horario. Además, se van a poder gestionar ventas, y así ir modificando 
la disponibilidad de las butacas.  También emite informes generales. Por último, el programa 
permite gestionar el complejo de cines, modificando los cines existentes. 

Pendientes: 
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from utils import *

#----------------------------------------------------------------------------------------------
# CONFIGURACIÓN DE MENÚS CON TUPLAS (inmutables, apropiadas para datos constantes)
#----------------------------------------------------------------------------------------------
MENU_PRINCIPAL = (
    "[1] Gestión de Películas y Entradas",
    "[2] Venta de Entradas", 
    "[3] Informes Generales",
    "[4] Gestión de Complejo de Cines",
    "[0] Salir"
)

MENU_PELICULAS = (
    "[1] Agregar Película",
    "[2] Modificar Película",
    "[3] Eliminar Película", 
    "[4] Modificar valor de la entrada",
    "[5] Listar todas las películas",
    "[0] Volver al menú"
)

MENU_ENTRADAS = (
    "[1] Generar Entrada",
    "[2] Eliminar Venta",
    "[0] Volver al menú"
)

MENU_INFORMES = (
    "[1] Emitir Informe de Ventas",
    "[2] Emitir Listado de Películas Disponibles",
    "[3] Emitir Informe de Butacas Disponibles",
    "[0] Volver al menú"
)

MENU_CINES = (
    "[1] Listar Cines",
    "[2] Agregar Nuevo Cine",
    "[3] Eliminar Cine",
    "[4] Modificar Cine",
    "[0] Volver al menú"
)

def mostrarMenu(titulo, opciones):
    """Función auxiliar para mostrar menús de manera consistente"""
    print("\n---------------------------")
    print(titulo)
    print("\n---------------------------")
    for opcion in opciones:
        print(opcion)
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
while True:
    cines = {
            "1": {
                "nombre": "Nuestra Señora del Lujan",
                "direccion": "Calle 24 e/ 125 y 127"
            },
            "2": {
                "nombre": "Los Sauces",
                "direccion": "Calle 79 e/ 10 y 12"
            },
            "3": {
                "nombre": "York",
                "direccion": "Calle 60 e/ 125 y 127"
            },
            "4": {
                "nombre": "Abasto",
                "direccion": "Rivadavia888"
            },
            "5": {
                "nombre": "Rey",
                "direccion": "corrientes 1145 olivos"
            },
            "6": {
                "nombre": "Cinemark Caballito",
                "direccion": "Av la plata 600"
            },
            "7": {
                "nombre": "cinemaxi",
                "direccion": "cine123"
            }
        }
    
    peliculas = {
        "1": {
            "title": "Spiderman",
            "format": "2D",
            "language": "Español",
            "schedule": [
                "Martes a las 14:00"
            ],
            "activo": True,
            "sala": {
                "A1": True,
                "B1": True,
                "C1": True,
                "D1": True,
                "E1": True,
                "F1": True,
                "G1": True,
                "H1": True,
                "A2": True,
                "B2": True,
                "C2": True,
                "D2": True,
                "E2": True,
                "F2": True,
                "G2": True,
                "H2": True,
                "A3": True,
                "B3": True,
                "C3": True,
                "D3": True,
                "E3": True,
                "F3": True,
                "G3": True,
                "H3": True,
                "A4": True,
                "B4": True,
                "C4": True,
                "D4": True,
                "E4": True,
                "F4": True,
                "G4": True,
                "H4": True,
                "A5": True,
                "B5": True,
                "C5": True,
                "D5": True,
                "E5": True,
                "F5": True,
                "G5": True,
                "H5": True,
                "A6": True,
                "B6": True,
                "C6": True,
                "D6": True,
                "E6": True,
                "F6": True,
                "G6": True,
                "H6": True,
                "A7": True,
                "B7": True,
                "C7": True,
                "D7": True,
                "E7": True,
                "F7": True,
                "G7": True,
                "H7": True,
                "A8": True,
                "B8": True,
                "C8": True,
                "D8": True,
                "E8": True,
                "F8": True,
                "G8": True,
                "H8": True,
                "A9": True,
                "B9": True,
                "C9": True,
                "D9": True,
                "E9": True,
                "F9": True,
                "G9": True,
                "H9": True
            },
            "complejo": "1"
        },
        "2": {
            "title": "Avengers: Endgame",
            "format": "3D",
            "language": "Subtitulado",
            "schedule": [
                "Miércoles a las 18:00"
            ],
            "activo": True,
            "sala": {
                "A1": True,
                "B1": True,
                "C1": True,
                "D1": True,
                "E1": True,
                "F1": True,
                "G1": True,
                "H1": True,
                "A2": True,
                "B2": True,
                "C2": True,
                "D2": True,
                "E2": True,
                "F2": True,
                "G2": True,
                "H2": True,
                "A3": True,
                "B3": True,
                "C3": True,
                "D3": True,
                "E3": True,
                "F3": True,
                "G3": True,
                "H3": True,
                "A4": True,
                "B4": True,
                "C4": True,
                "D4": True,
                "E4": True,
                "F4": True,
                "G4": True,
                "H4": True,
                "A5": True,
                "B5": True,
                "C5": True,
                "D5": True,
                "E5": True,
                "F5": True,
                "G5": True,
                "H5": True,
                "A6": True,
                "B6": True,
                "C6": True,
                "D6": True,
                "E6": True,
                "F6": True,
                "G6": True,
                "H6": True,
                "A7": True,
                "B7": True,
                "C7": True,
                "D7": True,
                "E7": True,
                "F7": True,
                "G7": True,
                "H7": True,
                "A8": True,
                "B8": True,
                "C8": True,
                "D8": True,
                "E8": True,
                "F8": True,
                "G8": True,
                "H8": True,
                "A9": True,
                "B9": True,
                "C9": True,
                "D9": True,
                "E9": True,
                "F9": True,
                "G9": True,
                "H9": True
            },
            "complejo": "2"
        },
        "3": {
            "title": "Coco",
            "format": "2D",
            "language": "Español",
            "schedule": [
                "Jueves a las 16:00"
            ],
            "activo": True,
            "sala": {
                "A1": True,
                "B1": True,
                "C1": True,
                "D1": True,
                "E1": True,
                "F1": True,
                "G1": True,
                "H1": True,
                "A2": True,
                "B2": True,
                "C2": True,
                "D2": True,
                "E2": True,
                "F2": True,
                "G2": True,
                "H2": True,
                "A3": True,
                "B3": True,
                "C3": True,
                "D3": True,
                "E3": True,
                "F3": True,
                "G3": True,
                "H3": True,
                "A4": True,
                "B4": True,
                "C4": True,
                "D4": True,
                "E4": True,
                "F4": True,
                "G4": True,
                "H4": True,
                "A5": True,
                "B5": True,
                "C5": True,
                "D5": True,
                "E5": True,
                "F5": True,
                "G5": True,
                "H5": True,
                "A6": True,
                "B6": True,
                "C6": True,
                "D6": True,
                "E6": True,
                "F6": True,
                "G6": True,
                "H6": True,
                "A7": True,
                "B7": True,
                "C7": True,
                "D7": True,
                "E7": True,
                "F7": True,
                "G7": True,
                "H7": True,
                "A8": True,
                "B8": True,
                "C8": True,
                "D8": True,
                "E8": True,
                "F8": True,
                "G8": True,
                "H8": True,
                "A9": True,
                "B9": True,
                "C9": True,
                "D9": True,
                "E9": True,
                "F9": True,
                "G9": True,
                "H9": True
            },
            "complejo": "4"
        },
    }
    entradas = {}
    mostrarMenu("SISTEMA DE GESTIÓN DE CINE", MENU_PRINCIPAL)
    opcion = input("Seleccione una opción: ")

    if opcion == "0":
        print("Saliendo del sistema.")
        break
        
    # Opción 1: GESTIÓN DE PELÍCULAS Y ENTRADAS
    elif opcion == "1":   
        # Menú de Películas y Entradas
        while True:
            mostrarMenu("GESTIÓN DE PELÍCULAS Y ENTRADAS", MENU_PELICULAS)
            opcionPeliculas = input("Seleccione una opción: ")

            if opcionPeliculas == "0": break
            if opcionPeliculas == "1": agregarPelicula()
            elif opcionPeliculas == "2": 
                peliculaId = input("Ingresa el número de la película a modificar: ")

                modificarPelicula(peliculaId)
            elif opcionPeliculas == "3": 
                peliculaId = input("Ingresa el número de la película a eliminar: ")
                inactivarPelicula(peliculaId)
            elif opcionPeliculas == "4": modificarPrecioEntrada()
            elif opcionPeliculas == "5": 
                peliculas = listarPeliculas()
                if peliculas:
                    print("\nLista de todas las películas:")
                    for indice, (peliculaId, info) in enumerate(peliculas.items(), start=1):
                        if peliculas[peliculaId]['activo']:
                            print(
                                f"Número: {indice}, ID: {peliculaId}, Título: {info['title']}, Formato: {info['format']}, Idioma: {info['language']}")
                            if info['schedule']:
                                print("  Horarios:")
                                for entry in info['schedule']:
                                    print(f"    - {entry}")
                            else:
                                print("  No hay horarios asignados.")
                else:
                    print("No hay películas disponibles.")
            
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

    # Opción 2: VENTA DE ENTRADAS
    elif opcion == "2":   
        # Menú de Venta de Entradas
        while True:
            mostrarMenu("VENTA DE ENTRADAS", MENU_ENTRADAS)
            opcionEntradas = input("Seleccione una opción: ")

            if opcionEntradas == "0": break
            if opcionEntradas == "1": generarEntrada()
            elif opcionEntradas == "2": eliminarEntrada()
            # Implementación de Generar Entrada y Eliminar Venta aquí...

            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

    # Opción 3: INFORMES GENERALES
    elif opcion == "3":   
        # Menú de Informes Generales
        while True:
            mostrarMenu("INFORMES GENERALES", MENU_INFORMES)
            opcionInformes = input("Seleccione una opción: ")

            if opcionInformes == "0": break
            # Implementación de los informes aquí...
            if opcionInformes == "1": informeVentas()
            if opcionInformes == "2": 
                disponibles = informeListadoPeliculasDisponibles(peliculas, cines)
                idiomas = set(pelicula[2] for pelicula in disponibles)
                formatos = set(pelicula[3] for pelicula in disponibles)

                print("\n--- LISTADO DE PELÍCULAS DISPONIBLES ---")
                for peliculaId, titulo, idioma, formato, cineId in disponibles:
                    print(f"ID: {peliculaId} | Título: {titulo} | Idioma: {idioma} | Formato: {formato} | Cine: {cineId}")

                print("\nIdiomas disponibles:", ", ".join(sorted(idiomas)))
                print("Formatos disponibles:", ", ".join(sorted(formatos)))

            if opcionInformes == "3": 
                for peliculaId, dataPelicula in peliculas.items():
                    if dataPelicula['activo']:  # Solo películas activas
                        sala = dataPelicula.get('sala')

                        if not sala:  # Si no tiene sala asignada, asignamos una sala vacía por defecto
                            sala = {}

                        print(f"ID de la película: {peliculaId}")
                        print(
                            f"\nPelícula: {dataPelicula['title']} ({dataPelicula['format']} - {dataPelicula['language']})")
                        print("Butacas disponibles:")
                        # Mostrar butacas disponibles
                        butacasDisponibles = informeButacasDisponibles(sala)
                        if butacasDisponibles:
                            # esto agrupa las butacas disponibles en una cadena separada por coma.
                            print(", ".join(butacasDisponibles))
                        else:
                            print("No hay butacas disponibles.")
                    else:
                        print(
                            f"\nPelícula inactiva: {dataPelicula['title']} no se muestra en el informe.")

            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

    # Opción 4: GESTIÓN DE COMPLEJO DE CINES
    elif opcion == "4":   
        # Menú de Gestión de Complejo de Cines
        while True:
            mostrarMenu("GESTIÓN DE COMPLEJO DE CINES", MENU_CINES)
            opcionCines = input("Seleccione una opción: ")

            if opcionCines == "0": break
            if opcionCines == "1": 
                print("Lista de todos los cines:")
                imprimirCines(cines)

            if opcionCines == "2": 
                nombre = input("Ingrese el nombre del cine: ").strip()
                direccion = input("Ingrese la dirección del cine: ").strip()
                cineData = (nombre, direccion)
                cines = nuevoCine(cineData, cines)
                print("¡Cine agregado con éxito!")

            if opcionCines == "3": 
                cineId = input("Ingrese el ID del cine que desea eliminar: ")
                if not cines.get(cineId):
                    print("Error: No se encontró un cine con el ID proporcionado.")
                    break
                confirmacion = input("¿Está seguro que desea eliminar el cine? (s/n): ").lower()
                if confirmacion == "s":
                    cines = eliminarCine(cineId, cines)
                    print("¡Cine eliminado con éxito!")

            if opcionCines == "4": 
                cineId = input("Ingrese el ID del cine que desea modificar: ")
                cineExistente = cines.get(cineId)
                if not cineExistente:
                    print("Error: No se encontró un cine con el ID proporcionado.")
                    break

                nuevoNombre = input(
                    "Ingrese el nuevo nombre del cine (deje en blanco para no modificar): ").strip()
                nuevaDireccion = input(
                    "Ingrese la nueva dirección del cine (deje en blanco para no modificar): ").strip()
                cineEditado = (nuevoNombre if nuevoNombre else cineExistente['nombre'],
                                nuevaDireccion if nuevaDireccion else cineExistente['direccion'])
                
                if (cineEditado != tuple(cineExistente.values())):
                    cines = modificarCine(cineId, cineEditado, cines)
                    print("¡Cine modificado con éxito!")

            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


"""Se optimizo lineas de codigo del menu principal"""
"""se cambio la cantidad de 0 al generar un id"""
"""se cambio editar pelicula para saber que pelicula estamos cambiando"""
""" se cambio la funcion generar id, En vez de convertir y formatear el ID cada vez, consideramos usar solo el número como clave en el diccionario movies y formatearlo solo para mostrarlo. Así reduces el largo de la clave y simplificas la generación de ID."""
""" se cambio validacion de horarios, El valor esHorario = True es redundante ya que la función retorna True al final si el horario es válido, así que se elimino y se retorna False directamente en los casos de error."""


"""
La línea de código id_mapping = {i: k for i, k in enumerate(movies.keys(), 1)} crea un diccionario llamado id_mapping que relaciona números secuenciales con los IDs de las películas almacenadas en el diccionario movies. cómo funciona:

movies.keys(): Esto obtiene todas las claves del diccionario movies, que en este contexto son los IDs de las películas. Por ejemplo, si movies tiene IDs como '0000000000001', '0000000000002', etc., movies.keys() devolverá un iterable con esos IDs.

enumerate(movies.keys(), 1): La función enumerate toma un iterable y devuelve pares de índice y valor. En este caso, comienza a contar desde 1 (debido al segundo argumento 1), por lo que generará pares como (1, '0000000000001'), (2, '0000000000002'), etc. Cada número (el índice) se asociará con un ID de película.

{i: k for i, k in ...}: Este es un "diccionario por comprensión". Está construyendo un nuevo diccionario donde i es el número secuencial (el índice de enumerate) y k es el ID de la película. Por lo tanto, por cada par generado por enumerate, se añadirá una entrada en el nuevo diccionario id_mapping.

"""

"""En resumen, esta línea de código crea un diccionario que mapea números secuenciales (comenzando desde 1) a los IDs de las películas, lo que facilita referenciar películas mediante un número en lugar de usar directamente su ID, mejorando así la usabilidad del sistema."""

"""Se modificó el uso de diccionarios a archivos JSON
   No se utilizaron excepciones para las validaciones, es necesario?? 
   se modificó para que el título no pueda estar vacío
   se modularizo la función para agregar el schedule en la funcion de agregar peliculas"""
