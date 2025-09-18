from utils import *

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
    "[4] Listar todas las películas",
    "[5] Listar todas las funciones",
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

MENU_PELICULAS_CINES = (
    "[1] Listar Cines",
    "[2] Agregar Cine",
    "[3] Eliminar Cine",
    "[0] Continuar"
)

def mostrarMenu(titulo, opciones):
    """
    Muestra un menú formateado en la consola.
    
    Esta función auxiliar proporciona una presentación consistente para todos los menús
    del sistema, incluyendo un título y una lista de opciones numeradas.
    
    Parámetros:
        titulo (string): El título del menú a mostrar
        opciones (tupla): Tupla de strings con las opciones del menú
    
    Returns:
        None: Solo imprime en consola
        
    """
    print("\n---------------------------")
    print(titulo)
    print("\n---------------------------")
    for opcion in opciones:
        print(opcion)
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
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
#ARMAR ENTIDAD SALAS COMO CONJUNTO
salas = { 
        "1": { #salaID
            "cineId": "1",
            "numeroSala": "1", #Nombre de la sala
            "asientos": {
                "A1": False,
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
        }
        }
    }
"""
    La estructura es:
    {
        "peliculaID": {
            "cineID": {
                "salaID": [
                    {
                        "dia": {
                            "horas"
                        }
                    }
                ]
            }
        }
    }
"""
funciones = {
    "1": {  # peliculaID
        "1": {  # cineID
            "1": {  # salaID
                "martes": {
                    "14:00", 
                    "18:00"
                }
            }
        }
    },
}

peliculas = {
    "1": {
        "titulo": "Spiderman",
        "formato": "2D",
        "idioma": "Español",
        "activo": True,
        "complejos": {"1"}
    },
    "2": {
        "titulo": "Avengers: Endgame",
        "formato": "3D",
        "idioma": "Subtitulado",
        "activo": True,
        "complejos": {"2"}
    },
    "3": {
        "titulo": "Coco",
        "formato": "2D",
        "idioma": "Español",
        "activo": True,
        "complejos": {"4"}
    },
}
entradas = {
    "1": {
        'cliente': "Juan Perez",
        'dni': "12345",
        'cineId': "1",
        'peliculaId': "1",
        'salaId': "1",
        'butaca': "A1"
    }
}

"""
Bucle principal del sistema.

IMPORTANTE: Las estructuras de datos (cines, peliculas, entradas) están definidas 
dentro del scope del bucle principal. Esto significa que se inicializan/resetean en cada 
iteración, lo que puede causa pérdida de datos por cada ejecución.
"""
while True:
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
            if opcionPeliculas == "1":
                peliculaData = {} 

                peliculaData['titulo'] = input("Ingresa el título de la película: ")
                while not peliculaData['titulo']:
                    peliculaData['titulo'] = input(
                        "Error. El título no puede estar vacío. Ingresa el título de la película: ")

                peliculaData['formato'] = input("Ingresa el formato (2D/3D): ")
                while peliculaData['formato'].lower() not in FORMATOS_VALIDOS:
                    peliculaData['formato'] = input("Error. Ingresa el formato (2D/3D): ")

                peliculaData['idioma'] = input("Ingresa el idioma (Español/Subtitulado): ")
                while peliculaData['idioma'].lower() not in IDIOMAS_VALIDOS:
                    peliculaData['idioma'] = input(
                        "Error. Ingresa el idioma (Español/Subtitulado): ")

                print("Elija el cine en el que se proyectará.")
                imprimirCines(cines)
                peliculaData['complejos'] = set()
                while True:
                    cineId = input("Ingresa el ID del cine en el que se proyectará:")
                    while not cines.get(cineId):
                        cineId = input("Error. Ingresa el cine: ")
                    peliculaData['complejos'].add(cineId)
                    continuar = input("¿Desea agregar otro cine? (s/n): ").lower()
                    if continuar != 's':
                        break

                funcionesPelicula = {}
                print("Elija el cine de la función.")
                listado = [(cineId, data["nombre"].strip(), data["direccion"].strip()) for cineId, data in cines.items()]
                print("\n--- LISTADO DE CINES ---")
                for cineId, nombre, direccion in listado:
                    print(f"ID: {cineId:<3} | Nombre: {nombre:<25} | Dirección: {direccion}")
                while True:
                    cineId = input("Ingresa el ID del cine en el que se proyectará:")
                    while not cines.get(cineId):
                        cineId = input("Error. Ingresa el cine: ")
                    print("Elija la sala del cine.")
                    imprimirSalasPorCine(cineId, salas)
                    salaId = input("Ingresa el ID de la sala en la que se proyectará:")
                    while not salas.get(salaId) or salas[salaId]['cineId'] != cineId:
                        salaId = input("Error. Ingresa la sala: ")
                    nuevaFuncion = generarFuncion(cineId, salaId)

                    for dia, horas in nuevaFuncion[cineId][salaId].items():
                        if not funcionesPelicula.get(cineId):
                            funcionesPelicula[cineId] = {}
                        if not funcionesPelicula[cineId].get(salaId):
                            funcionesPelicula[cineId][salaId] = {}
                        if dia in funcionesPelicula[cineId][salaId]:
                            funcionesPelicula[cineId][salaId][dia].update(horas)
                        else:
                            funcionesPelicula[cineId][salaId][dia] = set(horas)
                    continuar = input("¿Desea agregar otra función? (s/n): ").lower()
                    if continuar != 's':
                        break
                peliculas, peliculaId = agregarPelicula(peliculaData, peliculas)
                funciones = agregarFunciones(peliculaId, funcionesPelicula, funciones)
                print(f"¡Película '{peliculaData['titulo']}' agregada con éxito!")

            elif opcionPeliculas == "2": 
                peliculaId = input("Ingresa el número de la película a modificar: ")
                peliculaExistente = peliculas.get(peliculaId).copy()
                peliculaEditada = {}
                if not peliculaExistente:
                    print("Error: No se encontró una película con el ID proporcionado.")
                    break

                nuevoTitulo = input(
                    "Ingrese el nuevo título de la película (deje en blanco para no modificar): ").strip()

                nuevoFormato = input(
                    "Ingrese el nuevo formato de la película (deje en blanco para no modificar): ").strip()
                while (nuevoFormato and nuevoFormato.lower() not in FORMATOS_VALIDOS) or not nuevoFormato:
                    print("Error. Formato no válido.")
                    nuevoFormato = input("Ingrese el nuevo formato de la película (deje en blanco para no modificar): ")

                nuevoIdioma = input(
                    "Ingrese el nuevo idioma de la película (deje en blanco para no modificar): ").strip()
                while (nuevoIdioma and nuevoIdioma.lower() not in IDIOMAS_VALIDOS) or not nuevoIdioma:
                    print("Error. Ingresa el idioma (Español/Subtitulado): ")
                    nuevoIdioma = input("Ingrese el nuevo idioma de la película (deje en blanco para no modificar): ").strip()

                peliculaEditada["complejos"] = peliculaExistente['complejos'].copy()
                modificarComplejos = input(
                    "¿Desea modificar los complejos? (s/n): ").strip().lower()
                if modificarComplejos == 's':
                    while True:
                        mostrarMenu("GESTIÓN COMPLEJOS", MENU_PELICULAS_CINES)
                        opcionComplejo = input("Seleccione una opción: ")

                        if opcionComplejo == "1":
                            for cineId in peliculaEditada["complejos"]:
                                data = cines.get(cineId, {})
                                nombre = data.get("nombre", "").strip()
                                direccion = data.get("direccion", "").strip()
                                print(f"ID: {cineId:<3} | Nombre: {nombre:<25} | Dirección: {direccion}")
                        elif opcionComplejo == "2":
                            print("Elija el cine en el que se proyectará.")
                            imprimirCines(cines)
                            nuevoComplejo = input(
                                "Ingrese el ID del nuevo complejo: ").strip()
                            if nuevoComplejo and cines.get(nuevoComplejo):
                                peliculaEditada['complejos'].add(nuevoComplejo)
                            else:
                                print("Error: No se encontró un cine con el ID proporcionado.")
                        elif opcionComplejo == "3":
                            print("ADVERTENCIA: Esta acción no solo eliminará el cine de la lista de complejos de la película, " \
                            "\nsino que también eliminará todas las funciones asociadas a ese cine para esta película.")
                            complejoId = input(
                                "Ingrese el ID del complejo a eliminar (vacío para cancelar): ").strip()
                            if cines.get(complejoId):
                                peliculaEditada['complejos'].remove(complejoId)
                                funciones = eliminarFuncionesPorPeliculaCine(peliculaId, complejoId, funciones)
                            else:
                                print("Error: No se encontró un cine con el ID proporcionado.")
                        else:
                            break

                peliculaEditada = {
                    "titulo": nuevoTitulo if nuevoTitulo else peliculaExistente['titulo'],
                    "formato": nuevoFormato if nuevoFormato else peliculaExistente['formato'],
                    "idioma": nuevoIdioma if nuevoIdioma else peliculaExistente['idioma'],
                    "activo": peliculaExistente['activo'],
                    "complejos": peliculaEditada['complejos'].copy()
                }
                if (peliculaEditada != peliculaExistente):
                    peliculas = modificarPelicula(peliculaId, peliculaEditada, peliculas)

                print(f"¡Película '{peliculaId}' modificada con éxito!")

            elif opcionPeliculas == "3": 
                peliculaId = input("Ingresa el número de la película a eliminar: ")
                inactivarPelicula(peliculaId)
            elif opcionPeliculas == "4": 
                imprimirPeliculas(peliculas)
            elif opcionPeliculas == "5": 
                imprimirFunciones(funciones, peliculas, cines, salas)

            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

    # Opción 2: VENTA DE ENTRADAS
    elif opcion == "2":   
        while True:
            mostrarMenu("VENTA DE ENTRADAS", MENU_ENTRADAS)
            opcionEntradas = input("Seleccione una opción: ")

            if opcionEntradas == "0": break
            if opcionEntradas == "1": 
                nombreCliente = input("Ingrese el nombre del cliente: ")
                dniCliente = input("Ingrese el DNI del cliente: ")
                idCine = input("Ingrese el ID del cine donde desea reservar:")
                if not cines.get(idCine):
                    print("Error: No se encontró un cine con el ID proporcionado.")
                    break
                peliculasEnCine = peliculasPorCine(peliculas, idCine)

                if peliculasEnCine:
                    print("\nPELICULAS EN ESTE CINE:")
                    for peliculaId, info in peliculasEnCine.items():
                        print(
                            f"ID: {peliculaId}, Título: {info['titulo']}, Formato: {info['formato']}, Idioma: {info['idioma']}")
                        if funciones.get(peliculaId, {}).get(idCine, {}):
                            print("  Salas:")
                            for salaId, sala in funciones.get(peliculaId, {}).get(idCine, {}).items():
                                print(f"    - Sala {salaId}: ")
                                for dia, horas in sala.items():
                                    print(f"      - {dia.capitalize()}: {', '.join(sorted(horas))}")
                        else:
                            print("No hay horarios asignados.")
                    peliculaId = input(
                        "Ingresa el ID de la película que desee ver")
                    while not peliculas.get(peliculaId) and not peliculaId in peliculasEnCine.keys():
                        peliculaId = input(
                            "Ingresa el ID de la película que desee ver")
                        print("El ID de la película no corresponde a ninguna película en este cine. Intente nuevamente.")

                    salaId = input("Ingresa el ID de la sala en la que se proyectará:")
                    while not salas.get(salaId) or salas[salaId]['cineId'] != idCine:
                        salaId = input("Error. Ingresa la sala: ")
                    
                    diaPelicula = input("Ingrese el día de la función (por ejemplo, 'martes'): ").strip().lower()
                    horaPelicula = input("Ingrese la hora de la función (por ejemplo, '14:00'): ").strip()
                    if not funciones.get(peliculaId, {}).get(idCine, {}).get(salaId, {}).get(diaPelicula, {}) or horaPelicula not in funciones.get(peliculaId, {}).get(idCine, {}).get(salaId, {}).get(diaPelicula, {}):
                        print(f"No existe función para la película {peliculaId} en el cine {idCine}, sala {salaId}, día {diaPelicula} a las {horaPelicula}")
                        break

                    salaData = salas.get(salaId)
                    if not salaData or salaData["cineId"] != idCine:
                        print(f"No se encontró la sala {salaId} en el cine {idCine}")
                        break

                    asientosDisponibles = [asiento for asiento, disponible in salaData["asientos"].items() if disponible]
                    if not asientosDisponibles:
                        print("No hay butacas disponibles en esta sala.")
                        break

                    print("Butacas disponibles:", ", ".join(asientosDisponibles))
                    butaca = input("Seleccione una butaca disponible: ").strip().upper()
                    while butaca not in asientosDisponibles:
                        butaca = input("Butaca no válida o no disponible. Seleccione una butaca disponible: ").strip().upper()

                    salas[salaId]["asientos"][butaca] = False

                    nuevaEntrada = {
                        'cliente': nombreCliente,
                        'dni': dniCliente,
                        'cineId': idCine,
                        'peliculaId': peliculaId,
                        'butaca': butaca
                    }

                    entradas = generarEntrada(nuevaEntrada, entradas)
                    print(
                        f"Felicidades, el cliente {nombreCliente} - {dniCliente} tiene reservado el asiento {butaca} para la función.")
            elif opcionEntradas == "2": 
                idCine = input("Ingrese el ID del cine de la reserva a eliminar:")
                if not cines.get(idCine):
                    print("Error: No se encontró un cine con el ID proporcionado.")
                    break
                    
                peliculasEnCine = peliculasPorCine(peliculas, idCine)

                if not peliculasEnCine:
                    print("No hay películas disponibles en este cine.")
                    break

                print("\nLista de todas las películas en este cine:")
                for peliculaId, info in peliculasEnCine.items():
                    print(
                        f"ID: {peliculaId}, Título: {info['titulo']}, Formato: {info['formato']}, Idioma: {info['idioma']}")

                peliculaId = input("Ingresa el ID de la película: ")
                while not peliculas.get(peliculaId) or peliculaId not in peliculasEnCine.keys():
                    peliculaId = input("Error. El ID de la película no corresponde a ninguna película en este cine. Intente nuevamente: ")
                
                salaId = input("Ingresa el ID de la sala:")
                while not salas.get(salaId) or salas[salaId]['cineId'] != idCine:
                    salaId = input("Error. Sala no válida para este cine. Ingresa el ID de la sala: ")

                nombreCliente = input("Ingrese el nombre del cliente: ")
                dniCliente = input("Ingrese el DNI del cliente: ")
                butaca = input("Ingrese el asiento reservado a eliminar: ").upper()

                if butaca not in salas[salaId]['asientos'] or salas[salaId]['asientos'][butaca] == True:
                    print("La reserva de ese asiento no existe o ya está disponible.")
                    break

                entradaEliminarId = None
                for entradaId, entrada in entradas.items():
                    if (entrada['cliente'].lower() == nombreCliente.lower() and 
                        entrada['dni'] == dniCliente and
                        entrada['cineId'] == idCine and
                        entrada['peliculaId'] == peliculaId and 
                        entrada['butaca'] == butaca):
                        entradaEliminarId = entradaId
                        break

                if not entradaEliminarId:
                    print("No se encontró una reserva que coincida con los datos proporcionados.")
                    break
                
                salas[salaId]['asientos'][butaca] = True
                entradas = eliminarEntrada(entradaEliminarId, entradas)

                print(f"La reserva para el cliente {nombreCliente} - {dniCliente} en el asiento {butaca} ha sido eliminada exitosamente.")

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
            if opcionInformes == "1": 
                informe, ventasGenerales = informeVentas(entradas, peliculas, cines)
                # Imprimir el informe de ventas
                for cineId, cineData in informe.items():
                    print(f"\nCine: {cineData['nombre']}")
                    for peliculaId, peliculaData in cineData["entradas"].items():
                        print(
                            f"  - Película: {peliculaData['titulo']}, Entradas Vendidas: {peliculaData['cantidad']}")

                print(f"\nTotal de ventas Totales realizadas: {ventasGenerales}")

            if opcionInformes == "2":
                disponibles = informeListadoPeliculasDisponibles(peliculas, cines)
                idiomas = set(pelicula[2] for pelicula in disponibles)
                formatos = set(pelicula[3] for pelicula in disponibles)

                print("\n--- LISTADO DE PELÍCULAS DISPONIBLES ---")
                for peliculaId, titulo, idioma, formato, cines in disponibles:
                    print(f"ID: {peliculaId} | Título: {titulo} | Idioma: {idioma} | Formato: {formato} | Cines: {cines}")

                print("\nIdiomas disponibles:", ", ".join(sorted(idiomas)))
                print("Formatos disponibles:", ", ".join(sorted(formatos)))

            if opcionInformes == "3": #INFORME DE BUTACAS 
                print("\n--- INFORME DE BUTACAS DISPONIBLES POR CINE ---")
                for salaId, sala in salas.items():
                    print(f"ID del cine: {sala['cineId']}")
                    print(
                        f"\nID de la sala: {salaId} - {sala['numeroSala']} - Butacas totales: {len(sala['asientos'])}")
                    print("Butacas disponibles:")
                    butacasDisponibles = informeButacasDisponibles(sala['asientos'])
                    if butacasDisponibles:
                        print(", ".join(butacasDisponibles))
                    else:
                        print("No hay butacas disponibles.")

            input("\nPresione ENTER para volver al menú.")
            print("\n\n")

    # Opción 4: GESTIÓN DE COMPLEJO DE CINES
    elif opcion == "4":   
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