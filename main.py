from utils import *

MENU_PRINCIPAL = (
    "[1] Gestión de Películas y Entradas",
    "[2] Venta de Entradas", 
    "[3] Informes Generales",
    "[4] Gestión de Complejo de Cines",
    "[5] Análisis con Operaciones de Conjuntos",
    "[0] Salir"
)

MENU_PELICULAS = (
    "[1] Agregar Película",
    "[2] Modificar Película",
    "[3] Listar todas las películas",
    "[4] Listar todas las funciones",
    "[5] Películas por idioma Y formato",
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
    "[4] Emitir Informe de Butacas por Tipo",
    "[0] Volver al menú"
)

MENU_CINES = (
    "[1] Listar Cines",
    "[2] Agregar Nuevo Cine",
    "[3] Eliminar Cine",
    "[4] Modificar Cine",
    "[5] Películas en común entre dos cines",
    "[6] Cines sin películas asignadas",
    "[7] Películas disponibles en todos los cines seleccionados",
    "[8] Comparar butacas disponibles por tipo",
    "[9] Análisis de funciones por día",
    "[10] Cines con y sin funciones",
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
        "A1": {"ocupado": True, "tipo": "extreme"},
        "A2": {"ocupado": False, "tipo": "extreme"},
        "A3": {"ocupado": False, "tipo": "extreme"},
        "A4": {"ocupado": False, "tipo": "extreme"},
        "A5": {"ocupado": False, "tipo": "extreme"},
        "A6": {"ocupado": False, "tipo": "extreme"},
        "A7": {"ocupado": False, "tipo": "extreme"},
        "A8": {"ocupado": False, "tipo": "extreme"},
        "A9": {"ocupado": False, "tipo": "extreme"},
        "B1": {"ocupado": False, "tipo": "extreme"},
        "B2": {"ocupado": False, "tipo": "extreme"},
        "B3": {"ocupado": False, "tipo": "extreme"},
        "B4": {"ocupado": False, "tipo": "extreme"},
        "B5": {"ocupado": False, "tipo": "extreme"},
        "B6": {"ocupado": False, "tipo": "extreme"},
        "B7": {"ocupado": False, "tipo": "extreme"},
        "B8": {"ocupado": False, "tipo": "extreme"},
        "B9": {"ocupado": False, "tipo": "extreme"},
        "C1": {"ocupado": False, "tipo": "normal"},
        "C2": {"ocupado": False, "tipo": "normal"},
        "C3": {"ocupado": False, "tipo": "normal"},
        "C4": {"ocupado": False, "tipo": "normal"},
        "C5": {"ocupado": False, "tipo": "normal"},
        "C6": {"ocupado": False, "tipo": "normal"},
        "C7": {"ocupado": False, "tipo": "normal"},
        "C8": {"ocupado": False, "tipo": "normal"},
        "C9": {"ocupado": False, "tipo": "normal"},
        "D1": {"ocupado": False, "tipo": "normal"},
        "D2": {"ocupado": False, "tipo": "normal"},
        "D3": {"ocupado": False, "tipo": "normal"},
        "D4": {"ocupado": False, "tipo": "normal"},
        "D5": {"ocupado": False, "tipo": "normal"},
        "D6": {"ocupado": False, "tipo": "normal"},
        "D7": {"ocupado": False, "tipo": "normal"},
        "D8": {"ocupado": False, "tipo": "normal"},
        "D9": {"ocupado": False, "tipo": "normal"},
        "E1": {"ocupado": False, "tipo": "normal"},
        "E2": {"ocupado": False, "tipo": "normal"},
        "E3": {"ocupado": False, "tipo": "normal"},
        "E4": {"ocupado": False, "tipo": "normal"},
        "E5": {"ocupado": False, "tipo": "normal"},
        "E6": {"ocupado": False, "tipo": "normal"},
        "E7": {"ocupado": False, "tipo": "normal"},
        "E8": {"ocupado": False, "tipo": "normal"},
        "E9": {"ocupado": False, "tipo": "normal"},
        "F1": {"ocupado": False, "tipo": "normal"},
        "F2": {"ocupado": False, "tipo": "normal"},
        "F3": {"ocupado": False, "tipo": "normal"},
        "F4": {"ocupado": False, "tipo": "normal"},
        "F5": {"ocupado": False, "tipo": "normal"},
        "F6": {"ocupado": False, "tipo": "normal"},
        "F7": {"ocupado": False, "tipo": "normal"},
        "F8": {"ocupado": False, "tipo": "normal"},
        "F9": {"ocupado": False, "tipo": "normal"},
        "G1": {"ocupado": False, "tipo": "normal"},
        "G2": {"ocupado": False, "tipo": "normal"},
        "G3": {"ocupado": False, "tipo": "normal"},
        "G4": {"ocupado": False, "tipo": "normal"},
        "G5": {"ocupado": False, "tipo": "normal"},
        "G6": {"ocupado": False, "tipo": "normal"},
        "G7": {"ocupado": False, "tipo": "normal"},
        "G8": {"ocupado": False, "tipo": "normal"},
        "G9": {"ocupado": False, "tipo": "normal"},
        "H1": {"ocupado": False, "tipo": "normal"},
        "H2": {"ocupado": False, "tipo": "normal"},
        "H3": {"ocupado": False, "tipo": "normal"},
        "H4": {"ocupado": False, "tipo": "normal"},
        "H5": {"ocupado": False, "tipo": "normal"},
        "H6": {"ocupado": False, "tipo": "normal"},
        "H7": {"ocupado": False, "tipo": "normal"},
        "H8": {"ocupado": False, "tipo": "normal"},
        "H9": {"ocupado": False, "tipo": "normal"}
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
                cinesElegidos = {cineId: cines[cineId] for cineId in peliculaData['complejos']}
                print("Elija el cine de la función.")
                listado = [(cineId, data["nombre"].strip(), data["direccion"].strip()) for cineId, data in cinesElegidos.items()]
                print("\n--- LISTADO DE CINES ---")
                for cineId, nombre, direccion in listado:
                    print(f"ID: {cineId:<3} | Nombre: {nombre:<25} | Dirección: {direccion}")
                while True:
                    cineId = input("Ingresa el ID del cine en el que se proyectará:")
                    while not cines.get(cineId):
                        cineId = input("Error. Ingresa el cine: ")
                    print("Elija la sala del cine.")
                    if (not salas) or (not any(sala['cineId'] == cineId for sala in salas.values())):
                        print("No hay salas disponibles para este cine. Debe crear una sala primero.")
                        break
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
                imprimirPeliculas(peliculas)
            elif opcionPeliculas == "4": 
                imprimirFunciones(funciones, peliculas, cines, salas)
            elif opcionPeliculas == "5":  # Películas por idioma Y formato
                print("\n--- PELÍCULAS POR IDIOMA Y FORMATO ---")
                idiomas = obtenerIdiomasDisponibles(peliculas)
                formatos = obtenerFormatosDisponibles(peliculas)
                
                print(f"Idiomas disponibles: {', '.join(sorted(idiomas))}")
                print(f"Formatos disponibles: {', '.join(sorted(formatos))}")
                
                idioma = input("\nIngrese el idioma: ").strip()
                formato = input("Ingrese el formato: ").strip()
                
                pelisResultado = peliculasPorIdiomaYFormato(peliculas, idioma, formato)
                
                if pelisResultado:
                    print(f"\nPelículas en {idioma} Y {formato}:")
                    for peliculaId in pelisResultado:
                        print(f"  - {peliculas[peliculaId]['titulo']} (ID: {peliculaId})")
                else:
                    print(f"\nNo hay películas con idioma {idioma} y formato {formato}.")

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
                    continue
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
                        "Ingresa el ID de la película que desee ver: ")
                    while not peliculas.get(peliculaId) or peliculaId not in peliculasEnCine.keys():
                        peliculaId = input(
                            "Ingresa el ID de la película que desee ver: ")
                        print("El ID de la película no corresponde a ninguna película en este cine. Intente nuevamente.")

                    salaId = input("Ingresa el ID de la sala en la que se proyectará:")
                    while not salas.get(salaId) or salas[salaId]['cineId'] != idCine:
                        salaId = input("Error. Ingresa la sala: ")
                    
                    diaPelicula = input("Ingrese el día de la función (por ejemplo, 'martes'): ").strip().lower()
                    horaPelicula = input("Ingrese la hora de la función (por ejemplo, '14:00'): ").strip()
                    if not funciones.get(peliculaId, {}).get(idCine, {}).get(salaId, {}).get(diaPelicula, {}) or horaPelicula not in funciones.get(peliculaId, {}).get(idCine, {}).get(salaId, {}).get(diaPelicula, {}):
                        print(f"No existe función para la película {peliculaId} en el cine {idCine}, sala {salaId}, día {diaPelicula} a las {horaPelicula}")
                        continue

                    salaData = salas.get(salaId)
                    if not salaData or salaData["cineId"] != idCine:
                        print(f"No se encontró la sala {salaId} en el cine {idCine}")
                        continue

                    asientosDisponiblesSet = informeButacasDisponibles(salaData["asientos"])
                    if not asientosDisponiblesSet:
                        print("No hay butacas disponibles en esta sala.")
                        continue
                    
                    extremeDisponibles = butacasDisponiblesPorTipo(salaData["asientos"], "extreme")
                    normalDisponibles = butacasDisponiblesPorTipo(salaData["asientos"], "normal")
                    print(f"\nButacas EXTREME disponibles ({len(extremeDisponibles)})")
                    print(f"Butacas NORMAL disponibles ({len(normalDisponibles)})s")
                    imprimirSala(salaData["asientos"])
                    
                    butaca = input("\nSeleccione una butaca disponible: ").strip().upper()
                    while butaca not in asientosDisponiblesSet:
                        butaca = input("Butaca no válida o no disponible. Seleccione una butaca disponible: ").strip().upper()

                    salas[salaId]["asientos"][butaca]["ocupado"] = True

                    nuevaEntrada = {
                        'cliente': nombreCliente,
                        'dni': dniCliente,
                        'cineId': idCine,
                        'peliculaId': peliculaId,
                        'salaId': salaId,
                        'butaca': butaca
                    }

                    entradas = generarEntrada(nuevaEntrada, entradas)
                    tipoButaca = salas[salaId]["asientos"][butaca]["tipo"]
                    print(
                        f"Felicidades, el cliente {nombreCliente} - {dniCliente} tiene reservado el asiento {butaca} (Tipo: {tipoButaca.upper()}) para la función.")
            elif opcionEntradas == "2": 
                idCine = input("Ingrese el ID del cine de la reserva a eliminar:")
                if not cines.get(idCine):
                    print("Error: No se encontró un cine con el ID proporcionado.")
                    continue
                    
                peliculasEnCine = peliculasPorCine(peliculas, idCine)

                if not peliculasEnCine:
                    print("No hay películas disponibles en este cine.")
                    continue

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

                if butaca not in salas[salaId]['asientos'] or not salas[salaId]['asientos'][butaca]["ocupado"]:
                    print("La reserva de ese asiento no existe o ya está disponible.")
                    continue

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
                    continue
                
                salas[salaId]['asientos'][butaca]["ocupado"] = False
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
                # Usando operaciones de conjuntos para obtener idiomas y formatos
                idiomas = obtenerIdiomasDisponibles(peliculas)
                formatos = obtenerFormatosDisponibles(peliculas)

                print("\n--- LISTADO DE PELÍCULAS DISPONIBLES ---")
                for peliculaId, titulo, idioma, formato, cines_str in disponibles:
                    print(f"ID: {peliculaId} | Título: {titulo} | Idioma: {idioma} | Formato: {formato} | Cines: {cines_str}")

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
                        print(", ".join(sorted(butacasDisponibles)))
                    else:
                        print("No hay butacas disponibles.")

            if opcionInformes == "4": #INFORME DE BUTACAS POR TIPO
                print("\n--- INFORME DE BUTACAS POR TIPO ---")
                for salaId, sala in salas.items():
                    print(f"\nCine ID: {sala['cineId']} - Sala ID: {salaId} - Número: {sala['numeroSala']}")
                    
                    # Usando operaciones de conjuntos para análisis por tipo
                    extremeTotal = butacasPorTipo(sala['asientos'], "extreme")
                    normalTotal = butacasPorTipo(sala['asientos'], "normal")
                    
                    extremeDisponibles = butacasDisponiblesPorTipo(sala['asientos'], "extreme")
                    normalDisponibles = butacasDisponiblesPorTipo(sala['asientos'], "normal")
                    
                    extremeOcupadas = butacasOcupadasPorTipo(sala['asientos'], "extreme")
                    normalOcupadas = butacasOcupadasPorTipo(sala['asientos'], "normal")
                    print(f"  EXTREME: {len(extremeTotal)} totales | {len(extremeDisponibles)} disponibles | {len(extremeOcupadas)} ocupadas")
                    print(f"  NORMAL: {len(normalTotal)} totales | {len(normalDisponibles)} disponibles | {len(normalOcupadas)} ocupadas")
                    imprimirSala(sala['asientos'])

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
                    continue
                confirmacion = input("¿Está seguro que desea eliminar el cine? (s/n): ").lower()
                if confirmacion == "s":
                    cines = eliminarCine(cineId, cines)
                    print("¡Cine eliminado con éxito!")

            if opcionCines == "4": 
                cineId = input("Ingrese el ID del cine que desea modificar: ")
                cineExistente = cines.get(cineId)
                if not cineExistente:
                    print("Error: No se encontró un cine con el ID proporcionado.")
                    continue

                nuevoNombre = input(
                    "Ingrese el nuevo nombre del cine (deje en blanco para no modificar): ").strip()
                nuevaDireccion = input(
                    "Ingrese la nueva dirección del cine (deje en blanco para no modificar): ").strip()
                cineEditado = (nuevoNombre if nuevoNombre else cineExistente['nombre'],
                                nuevaDireccion if nuevaDireccion else cineExistente['direccion'])
                
                if (cineEditado != tuple(cineExistente.values())):
                    cines = modificarCine(cineId, cineEditado, cines)
                    print("¡Cine modificado con éxito!")
            elif opcionCines == "5":  # Películas en común entre dos cines
                print("\n--- PELÍCULAS EN COMÚN ENTRE DOS CINES ---")
                imprimirCines(cines)
                cine1 = input("Ingrese el ID del primer cine: ")
                cine2 = input("Ingrese el ID del segundo cine: ")
                
                if not cines.get(cine1) or not cines.get(cine2):
                    print("Error: Uno o ambos cines no existen.")
                    continue
                
                peliculas1 = peliculasPorCine(peliculas, cine1)
                peliculas2 = peliculasPorCine(peliculas, cine2)
                
                # Intersección de conjuntos de IDs de películas
                idsComunes = set(peliculas1.keys()) & set(peliculas2.keys())
                
                if idsComunes:
                    print(f"\nPelículas en común entre {cines[cine1]['nombre']} y {cines[cine2]['nombre']}:")
                    for pid in idsComunes:
                        print(f"  - {peliculas[pid]['titulo']} (ID: {pid})")
                else:
                    print(f"\nNo hay películas en común entre estos cines.")

            elif opcionCines == "6":  # Cines sin películas
                print("\n--- CINES SIN PELÍCULAS ASIGNADAS ---")
                todosCinesSet = set(cines.keys())
                cinesSinPelis = cinesSinPeliculas(todosCinesSet, peliculas)
                
                if cinesSinPelis:
                    print("Los siguientes cines NO tienen películas asignadas:")
                    for cineId in cinesSinPelis:
                        print(f"  - {cines[cineId]['nombre']} (ID: {cineId})")
                else:
                    print("Todos los cines tienen al menos una película asignada.")

            elif opcionCines == "7":  # Películas en todos los cines seleccionados
                print("\n--- PELÍCULAS EN TODOS LOS CINES SELECCIONADOS ---")
                imprimirCines(cines)
                cinesSeleccionados = set()
                while True:
                    cineId = input("Ingrese ID de cine (ENTER para terminar): ")
                    if not cineId:
                        break
                    if cines.get(cineId):
                        cinesSeleccionados.add(cineId)
                    else:
                        print("Cine no encontrado.")
                
                if not cinesSeleccionados:
                    print("No se seleccionaron cines.")
                    continue
                
                pelisEnTodos = peliculasEnTodosCines(peliculas, cinesSeleccionados)
                
                if pelisEnTodos:
                    print(f"\nPelículas disponibles en TODOS los cines seleccionados:")
                    for pid, peli in pelisEnTodos.items():
                        print(f"  - {peli['titulo']} (ID: {pid})")
                else:
                    print("\nNo hay películas disponibles en todos los cines seleccionados.")

            elif opcionCines == "8":  # Comparar butacas por tipo
                print("\n--- ANÁLISIS DE BUTACAS POR TIPO (TODAS LAS SALAS) ---")
                
                # Usando operaciones de conjuntos para agregar datos de todas las salas
                todasExtremeDisp = set()
                todasNormalDisp = set()
                todasExtremeOcup = set()
                todasNormalOcup = set()
                
                for salaId, sala in salas.items():
                    extremeDisp = butacasDisponiblesPorTipo(sala['asientos'], "extreme")
                    normalDisp = butacasDisponiblesPorTipo(sala['asientos'], "normal")
                    extremeOcup = butacasOcupadasPorTipo(sala['asientos'], "extreme")
                    normalOcup = butacasOcupadasPorTipo(sala['asientos'], "normal")
                    
                    # Unión de conjuntos
                    todasExtremeDisp = todasExtremeDisp | extremeDisp
                    todasNormalDisp = todasNormalDisp | normalDisp
                    todasExtremeOcup = todasExtremeOcup | extremeOcup
                    todasNormalOcup = todasNormalOcup | normalOcup
                
                print(f"RESUMEN GLOBAL:")
                print(f"  Butacas EXTREME disponibles: {len(todasExtremeDisp)}")
                print(f"  Butacas EXTREME ocupadas: {len(todasExtremeOcup)}")
                print(f"  Butacas NORMAL disponibles: {len(todasNormalDisp)}")
                print(f"  Butacas NORMAL ocupadas: {len(todasNormalOcup)}")
                
                # Porcentajes
                totalExtreme = len(todasExtremeDisp) + len(todasExtremeOcup)
                totalNormal = len(todasNormalDisp) + len(todasNormalOcup)
                if totalExtreme > 0:
                    porcExtremeOcup = (len(todasExtremeOcup) / totalExtreme) * 100
                    print(f"  Ocupación EXTREME: {porcExtremeOcup:.1f}%")
                if totalNormal > 0:
                    porcNormalOcup = (len(todasNormalOcup) / totalNormal) * 100
                    print(f"  Ocupación NORMAL: {porcNormalOcup:.1f}%")
            
            if opcionCines == "10":  # Análisis de funciones por día
                print("\n--- ANÁLISIS DE FUNCIONES POR DÍA ---")
                peliculaId = input("Ingrese ID de película: ")
                if not peliculas.get(peliculaId):
                    print("Película no encontrada.")
                    continue
                
                cineId = input("Ingrese ID de cine: ")
                if not cines.get(cineId):
                    print("Cine no encontrado.")
                    continue
                
                # Usando conjuntos para obtener todos los días con funciones
                diasDisponibles = diasConFunciones(funciones, peliculaId, cineId)
                
                if diasDisponibles:
                    print(f"\nDías con funciones: {', '.join(sorted(diasDisponibles))}")
                    
                    dia = input("\nIngrese un día para ver horarios: ").lower()
                    if dia in diasDisponibles:
                        # Usando unión de conjuntos para todos los horarios
                        horarios = horariosEnDia(funciones, peliculaId, cineId, dia)
                        print(f"Horarios disponibles el {dia}: {', '.join(sorted(horarios))}")
                    else:
                        print(f"No hay funciones el {dia}.")
                else:
                    print("No hay funciones programadas para esta combinación.")
            
            elif opcionCines == "10":  # Cines con y sin funciones
                print("\n--- ANÁLISIS DE CINES CON/SIN FUNCIONES ---")
                
                # Usando operaciones de conjuntos
                todosCinesSet = set(cines.keys())
                cinesConFunc = cinesConFunciones(funciones)
                cinesSinFunc = todosCinesSet - cinesConFunc
                
                print(f"\nCines CON funciones programadas ({len(cinesConFunc)}):")
                for cineId in sorted(cinesConFunc):
                    print(f"  - {cines[cineId]['nombre']} (ID: {cineId})")
                
                print(f"\nCines SIN funciones programadas ({len(cinesSinFunc)}):")
                for cineId in sorted(cinesSinFunc):
                    print(f"  - {cines[cineId]['nombre']} (ID: {cineId})")

            input("\nPresione ENTER para volver al menú.")
            print("\n\n")