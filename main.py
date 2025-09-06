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
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Menú principal
    #------------------------------------------------------------------------------------------
    while True:
        print("\n---------------------------")
        print("SISTEMA DE GESTIÓN DE CINE")
        print("---------------------------")
        print("[1] Gestión de Películas y Entradas")
        print("[2] Venta de Entradas")
        print("[3] Informes Generales")
        print("[4] Gestión de Complejo de Cines")
        print("[0] Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo del sistema.")
            break
            
        # Opción 1: GESTIÓN DE PELÍCULAS Y ENTRADAS
        elif opcion == "1":   
            # Menú de Películas y Entradas
            while True:
                print("\n---------------------------")
                print("GESTIÓN DE PELÍCULAS Y ENTRADAS")
                print("---------------------------\n")
                print("[1] Agregar Película")
                print("[2] Modificar Película")
                print("[3] Eliminar Película")
                print("[4] Modificar valor de la entrada")
                print("[5] Listar todas las películas")
                print("[0] Volver al menú")
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
                print("\n---------------------------")
                print("VENTA DE ENTRADAS")
                print("---------------------------")
                print("[1] Generar Entrada")
                print("[2] Eliminar Venta")
                print("[0] Volver al menú")
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
                print("\n---------------------------")
                print("INFORMES GENERALES")
                print("---------------------------")
                print("[1] Emitir Informe de Ventas")
                print("[2] Emitir Listado de Películas Disponibles")
                print("[3] Emitir Informe de Butacas Disponibles")
                print("[0] Volver al menú")
                opcionInformes = input("Seleccione una opción: ")

                if opcionInformes == "0": break
                # Implementación de los informes aquí...
                if opcionInformes == "1": informeVentas()
                if opcionInformes == "2": informeListadoPeliculasDisponibles()
                if opcionInformes == "3": informeButacasDisponibles()

                input("\nPresione ENTER para volver al menú.")
                print("\n\n")

        # Opción 4: GESTIÓN DE COMPLEJO DE CINES
        elif opcion == "4":   
            # Menú de Gestión de Complejo de Cines
            while True:
                print("\n---------------------------")
                print("GESTIÓN DE COMPLEJO DE CINES")
                print("---------------------------")
                print("[1] Listar Cines")
                print("[2] Agregar Nuevo Cine")
                print("[3] Eliminar Cine")
                print("[4] Modificar Cine")
                print("[0] Volver al menú")
                opcionCines = input("Seleccione una opción: ")

                if opcionCines == "0": break
                if opcionCines == "1": 
                    cines = listarCines()
                    print("Lista de todos los cines:")
                    for i in cines:
                        print(
                            f"ID: {i}, Nombre: {cines[i]['nombre']}, Dirección: {cines[i]['direccion']}")
                if opcionCines == "2": nuevoCine()
                if opcionCines == "3": eliminarCine()
                if opcionCines == "4": modificarCine()
                # Implementación de gestión de cines aquí...

                input("\nPresione ENTER para volver al menú.")
                print("\n\n")

if __name__ == "__main__":
    main()


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
