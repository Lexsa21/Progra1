# ----------------------------------------------------------------------------------------------
# FUNCIONES
# ----------------------------------------------------------------------------------------------
import json

# Constantes de archivos
ARCHIVO_PELICULAS = "movies.json"
ARCHIVO_ID_MAPPING = "id_mapping.txt"
ARCHIVO_CINES = "cines.json"
ARCHIVO_ENTRADAS = "entradas.json"

# Conjuntos para validaciones (más eficientes que listas para verificar membresía)
FORMATOS_VALIDOS = {"2d", "3d"}
IDIOMAS_VALIDOS = {"español", "subtitulado"}
DIAS_SEMANA = {"lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"}

# Tuplas para configuración de salas (inmutables, apropiadas para datos constantes)
NUMERACION_FILAS = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
CONFIGURACION_SALA = (9, 8)  # (filas, columnas)

def listarPeliculas():
    """- Función que lista las películas activas del archivo movies.txt
       - Parámetros: 
            pathArchivoPeliculas (str): ruta de archivo JSON movies.txt con las películas
       - Retorno:
            None """
    try:
        archivoPeliculas = open(ARCHIVO_PELICULAS,
                                mode="r", encoding="utf-8")
        peliculas = json.load(archivoPeliculas)
        archivoPeliculas.close()
        return peliculas
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)


def agregarPelicula():
    """- Función que agrega una película al archivo movies.txt
       - Parámetros: 
            pathArchivoPeliculas (str): ruta de archivo JSON movies.txt con las películas
            pathId (str): ruta de archivo JSON id_mapping.txt con los ID y sus respectivos números
            pathCine (str): ruta de archivo JSON cines.txt con los cines
       - Retorno:
            None """

    try:
        # Se carga el contenido existente de los archivos JSON
        peliculas = listarPeliculas()
        # archivoConIDs = open(pathId, mode="r", encoding="utf-8")
        # # id_mapping = json.load(archivoConIDs)
        # archivoConIDs.close()

        archivoCines = open(ARCHIVO_CINES, mode="r", encoding="utf-8")
        cines = json.load(archivoCines)

        peliculaId = generarId()

        titulo = input("Ingresa el título de la película: ")
        while not titulo:
            titulo = input(
                "Error. El título no puede estar vacío. Ingresa el título de la película: ")

        formatoPelicula = input("Ingresa el formato (2D/3D): ")
        while formatoPelicula.lower() not in FORMATOS_VALIDOS:
            formatoPelicula = input("Error. Ingresa el formato (2D/3D): ")

        idioma = input("Ingresa el idioma (Español/Subtitulado): ")
        while idioma.lower() not in IDIOMAS_VALIDOS:
            idioma = input(
                "Error. Ingresa el idioma (Español/Subtitulado): ")

        sala = crearSala()

        print("Elija el cine en el que se proyectará.")
        limitec = 0
        for i, cine in cines.items():
            print(f"{i} : {cine['nombre']}")
            limitec += 1
        cine = int(input("Ingresa el numero del cine en el que se proyectará:"))
        while not cine or cine > limitec:
            cine = input("Error. Ingresa el cine: ")

        # Se agrega la película
        peliculas[peliculaId] = {
            'title': titulo,
            'format': formatoPelicula,
            'language': idioma,
            'schedule': [],
            'activo': True,
            # Permite una sala simbolica que guarde el estado (reservado o disponible) de los asientos de la sala.
            'sala': sala,
            # Hace falta que en las peliculas figure en que cine se proyectan.
            'complejo': cine
        }

        # Se agrega el id a id_mapping
        # id_mapping[number_id] = peliculaId

        agregarSchedule(peliculas, peliculaId)

        # Se sobreescriben los archivos con los datos actualizados
        archivoPeliculas = open(ARCHIVO_PELICULAS,
                                mode="w", encoding="utf-8")
        json.dump(peliculas, archivoPeliculas, ensure_ascii=False, indent=4)
        archivoPeliculas.close()

        # archivoConIDs = open(pathId, mode="w", encoding="utf-8")
        # json.dump(id_mapping, archivoConIDs, ensure_ascii=False, indent=4)
        # archivoConIDs.close()

        print(f"¡Película '{titulo}' agregada con éxito con ID: {peliculaId}!")

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    return

def modificarPelicula(peliculaId):
    """- Función que modifica una película del archivo movies.txt
       - Parámetros: 
            pathArchivoPeliculas (str): ruta de archivo JSON movies.txt con las películas
            pathId (str): ruta de archivo JSON id_mapping.txt con los ID y sus respectivos números
       - Retorno:
            None """

    try:
        peliculas = listarPeliculas()

        if peliculaId in peliculas.keys():
            pelicula = peliculas[peliculaId]

            titulo = input(
                f"Ingresa el nuevo título de la película ({pelicula['title']}): ")
            if titulo:  # Si el usuario no ingresa nada, conserva el valor original
                pelicula['title'] = titulo

            formato = input(
                f"Ingresa el nuevo formato (2D/3D) ({pelicula['format']}): ")
            while formato and formato.lower() not in ["2d", "3d"]:
                formato = input("Error. Ingresa el formato (2D/3D): ")
            if formato:
                pelicula['format'] = formato

            idioma = input(
                f"Ingresa el nuevo idioma (Español/Subtitulado) ({pelicula['language']}): ")
            while idioma and idioma.lower() not in ["español", "subtitulado"]:
                idioma = input(
                    "Error. Ingresa el idioma (Español/Subtitulado): ")
            if idioma:
                pelicula['language'] = idioma

            archivoPeliculas = open(ARCHIVO_PELICULAS, mode="w", encoding="utf-8")
            json.dump(peliculas, archivoPeliculas, ensure_ascii=False, indent=4)
            archivoPeliculas.close()

            print(f"¡Película '{peliculaId}' modificada con éxito!")
        else:
            print("Número de película no encontrado.")

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

def inactivarPelicula(peliculaId):
    """- Función que inactiva una película del archivo movies.txt
       - Parámetros: 
            pathArchivoPeliculas (str): ruta de archivo JSON movies.txt con las películas
            pathId (str): ruta de archivo JSON id_mapping.txt con los ID y sus respectivos números
       - Retorno:
            None """

    try:
        peliculas = listarPeliculas()

        if peliculaId in peliculas.keys():
            peliculas[peliculaId]['activo'] = False

            archivoPeliculas = open(
                ARCHIVO_PELICULAS, mode="w", encoding="utf-8")
            json.dump(peliculas, archivoPeliculas, ensure_ascii=False, indent=4)
            archivoPeliculas.close()

            print(f"¡Película '{peliculaId}' inactivada con éxito!")
        else:
            print("Número de película no encontrado.")

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

def modificarPrecioEntrada():
    print("Esta opción no está implementada en este ejemplo.")

def generarId():
    """- Función que genera un ID único para una película.
       - Parámetro:
           pathArchivoPeliculas (str): ruta de archivo JSON movies.txt con las películas
       - Retorno:
           movie_id (str): ID generado 
           number_id (str): número asociado al ID"""
    try:
        archivoPeliculas = open(ARCHIVO_PELICULAS,
                                mode="r", encoding="utf-8")
        movies = json.load(archivoPeliculas)
        archivoPeliculas.close()

        nuevoId = max(map(int, movies.keys()), default=0) + 1
        peliculaId = f"{nuevoId}"

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    return peliculaId

# Funcion que crea una sala nueva con butacas vacias para las funciones
# Es una sala "simbolica", no tomarselo como que existe una sala diferente por pelicula.
def crearSala():
    """- Función que genera una sala para cada pelicula, de iguales dimenciones y cantidad de asientos.
       - Parámetro:
           NONE
       - Retorno:
           sala (dict): diccionario con disponibilidad de cada asiento"""
    sala = {}
    filas, columnas = CONFIGURACION_SALA
    
    for i in range(1, filas + 1):
        for j in range(columnas):
            asiento = f"{NUMERACION_FILAS[j]}{i}"
            sala[asiento] = True
    return sala

def agregarSchedule(peliculas, peliculaId):
    """- Función que agrega el día y horario de la función a una película a agregar al archivo movies.txt
       - Parámetros:
           movies (dicc): contenido cargado del archivo JSON movies.txt
           movie_id (str): ID generado para la película a agregar
       - Retorno:
           movies (dicc): contenido actualizado del diccionario movies"""

    # Agregar a la función la verificación de que dos peliculas en el mismo complejo no tengan mismo día y horario (ya que solo existe una sala)
    while True:
        dia = input(
            "Ingresa el día de la semana para la proyección (o 'fin' para terminar): ")
        if dia.lower() == 'fin':
            break
        if dia.lower() not in DIAS_SEMANA:
            print("Error. Día no válido. Ingresar un día correcto.")
            continue

        horario = input("Ingresa la hora (ej. 14:00): ")
        while not esHorario(horario):
            horario = input("Error. Ingresa la hora (ej. 14:00): ")

        schedule_entry = f"{dia} a las {horario}"
        peliculas[peliculaId]['schedule'].append(schedule_entry)

    return peliculas

def esHorario(horario):
    """- Función que valida que el horario tenga el formato HH:MM y sea un horario válido.
       - Parámetro:
           horario (str): horario ingresado
       - Retorno:
           (bool): True si es un horario válido, False en caso contrario."""

    if len(horario) != 5 or horario[2] != ":":
        return False

    horas, minutos = horario.split(":")
    if not (horas.isdigit() and minutos.isdigit()):
        return False

    return 0 <= int(horas) < 24 and 0 <= int(minutos) < 60

# # Esta función debuelve la butaca disponible (si la hay) o 0 si no existe para esa función. idp = id de la pelicula, pathMovies = ruta al archivo que contiene las peliculas.

def butacaDisponible(peliculaId):
    """- Función que busca la primera butaca disponible en una pelicula determinada.
       - Parámetro:
           peliculaId (str): id de la pelicula 
           pathMovies (str): ruta de archivo JSON movies.txt con las películas
       - Retorno:
           butaca (str): butaca asignada para la pelicula
           """
    try:
        # Cargar las películas
        with open(ARCHIVO_PELICULAS, mode="r", encoding="utf-8") as f:
            movies = json.load(f)

        peli = movies.get(peliculaId)

        if peli is None or 'sala' not in peli:
            return None  # La película no existe o no tiene sala asignada

        for butaca, disponible in peli['sala'].items():
            if disponible:  # Si la butaca está disponible
                # Marcar la butaca como ocupada
                peli['sala'][butaca] = False
                # Guardar los cambios en el archivo
                with open(ARCHIVO_PELICULAS, mode="w", encoding="utf-8") as f:
                    json.dump(movies, f, ensure_ascii=False, indent=4)
                return butaca

        return None  # No hay butacas disponibles
    except (FileNotFoundError, OSError) as e:
        print("Error al intentar abrir o guardar archivo:", e)
    except json.JSONDecodeError as e:
        print("Error al decodificar JSON:", e)

    return

def filtrar_peliculas_por_cine(peliculas, cine_id):
    """- Función auxiliar que filtra películas por cine usando dictionary comprehension
       - Parámetros:
           peliculas (dict): diccionario con todas las películas
           cine_id (int): ID del cine a filtrar
       - Retorno:
           dict: diccionario con películas filtradas por cine"""
    return {
        int(pelicula_id): info 
        for pelicula_id, info in peliculas.items() 
        if info.get('complejo') == cine_id and info.get('activo', False)
    }

def obtener_peliculas_activas(peliculas):
    """- Función auxiliar que filtra solo películas activas usando dictionary comprehension
       - Parámetros:
           peliculas (dict): diccionario con todas las películas
       - Retorno:
           dict: diccionario con solo películas activas"""
    return {
        pelicula_id: info 
        for pelicula_id, info in peliculas.items() 
        if info.get('activo', False)
    }

def ingresarIdPelicula(comentario):
    """- Función para ingresar ID de película
       - Parámetro:
           comentario (str): comentario que se le hace al cliente cuando ingresa el ID
       - Retorno:
           idPelicula (int): el ID"""

    while True:
        try:
            idPelicula = int(input(comentario))
            if idPelicula < 0:
                raise Exception("Ingrese un valor positivo")
            return idPelicula
        except ValueError:
            print("No se ha ingresado un valor válido")
        except Exception as ex:
            print(ex)

# Función que crea un nuevo cine
def nuevoCine(cineData, cines):
    """Agrega un nuevo cine usando tupla (nombre, direccion)."""
    # Creamos el próximo ID automáticamente
    nuevo_id = str(int(max(cines.keys(), default="0")) + 1)

    # Convertimos tupla en diccionario para guardar
    cines[nuevo_id] = {"nombre": cineData[0], "direccion": cineData[1]}

    print(f"\n✅ Cine agregado con éxito: {cineData[0]} (ID: {nuevo_id})")
    return cines
# def nuevoCine():
#     """- Función que genera un nuevo cine.
#        - Parámetro:
#            path (str): ruta de archivo JSON cines.txt con los cines
#        - Retorno:
#            None
#            """
#     try:
#         with open(ARCHIVO_CINES, mode="r", encoding="utf-8") as f1:
#             cines = json.load(f1)

#         # Generar nuevo ID
#         nuevoid = max(int(i) for i in cines.keys()) + 1 if cines else 1

#         # Solicitar nombre del cine
#         title = input("Ingresa el nombre del nuevo cine: ")
#         while not title:
#             title = input(
#                 "Error. El nombre no puede estar vacío. Ingresa el nombre del nuevo cine: ")

#         # Solicitar dirección del cine
#         direcc = input("Ingresa la dirección del nuevo cine: ")
#         while not direcc:
#             direcc = input(
#                 "Error. La dirección no puede estar vacía. Ingresa la dirección del nuevo cine: ")

#         # Agregar el nuevo cine al diccionario
#         cines[str(nuevoid)] = {
#             'nombre': title,
#             'direccion': direcc
#         }

#         # Guardar los datos actualizados en el archivo JSON
#         with open(ARCHIVO_CINES, mode="w", encoding="utf-8") as f1:
#             json.dump(cines, f1, ensure_ascii=False, indent=4)

#         print("¡Cine creado con éxito!")
#     except (FileNotFoundError, OSError) as e:
#         print("Error al intentar abrir o guardar archivo:", e)
#     except json.JSONDecodeError as e:
#         print("Error al decodificar JSON:", e)

#     return

def listarCines():
    """- Función que lista los cines creados.
       - Parámetro:
           path (str): ruta de archivo JSON cines.txt con los cines
       - Retorno:
           None
           """
    try:
        with open(ARCHIVO_CINES, mode="r", encoding="utf-8") as f1:
            cines = json.load(f1)
        return cines
    except (FileNotFoundError, OSError) as e:
        print(f"Error al intentar abrir archivo: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")

# Reserva un asiento para una pelicula. listapelis = archivo / estructura de datos con las peliculas, listaentradas = archivo/estructura de datos que gusrde las entradas a las peliculas.
def generarEntrada():
    """- Función que genera una entrada para un cliente para asistir a una pelicula
       - Parámetro:
           pathMovies (str): ruta de archivo JSON movies.txt con las películas
           pathCines (str): ruta de archivo JSON cines.txt con los cines
           pathEntradas (str): ruta de archivo JSON entradas.txt con las entradas
       - Retorno:
           None
           """
    try:
        nombreCliente = input("Ingrese el nombre del cliente: ")
        # Asumimos que esta función imprime los cines y sus IDs
        listarCines()
        idCine = input("Ingrese el ID del cine donde desea reservar:")

        # Cargar las películas
        peliculas = listarPeliculas()

        # Filtrar las películas por cine usando la nueva función auxiliar
        peliculasEnCine = filtrar_peliculas_por_cine(peliculas, int(idCine))

        if peliculasEnCine:
            print("\nLista de todas las películas en este cine:")
            for peliculaId, info in peliculasEnCine.items():
                print(
                    f"ID: {peliculaId}, Título: {info['title']}, Formato: {info['format']}, Idioma: {info['language']}")
                if info['schedule']:
                    print("  Horarios:")
                    for entry in info['schedule']:
                        print(f"    - {entry}")
                else:
                    print("No hay horarios asignados.")

            # Bucle para pedir el ID de película hasta que sea correcto
            while True:
                peliculaId = ingresarIdPelicula(
                    "Seleccionar el ID de la película que desee ver")

                if peliculaId in peliculasEnCine:
                    break  # Salir del bucle si el ID es correcto
                else:
                    print(
                        "El ID de la película no corresponde a ninguna película en este cine. Intente nuevamente.")

            # Verificar la disponibilidad de butacas
            butaca = butacaDisponible(peliculaId)

            if butaca is None:
                print("No hay butacas disponibles para esta película en este cine.")
                return

            # Cargar las entradas para actualizar
            with open(ARCHIVO_ENTRADAS, mode="r", encoding="utf-8") as f2:
                entradas = json.load(f2)

            # Generar un nuevo ID para la entrada
            nuevaEntrada = {
                'cliente': nombreCliente,
                'cine': idCine,
                'pelicula': peliculaId,
                'butaca': butaca
            }
            nuevo_id = str(len(entradas) + 1)
            entradas[nuevo_id] = nuevaEntrada

            # Guardar las entradas actualizadas
            with open(ARCHIVO_ENTRADAS, mode="w", encoding="utf-8") as f2:
                json.dump(entradas, f2, ensure_ascii=False, indent=4)

            print(
                f"Felicidades, el cliente {nombreCliente} tiene reservado el asiento {butaca} para la función.")

    except (FileNotFoundError, OSError) as e:
        print("Error al intentar abrir o guardar archivo:", e)
    except json.JSONDecodeError as e:
        print("Error al decodificar JSON:", e)

def eliminarEntrada():
    """- Función que elimina la entrada a una pelicula de un cliente, dejando su asiento disponible
       - Parámetro:
           pathMovies (str): ruta de archivo JSON movies.txt con las películas
           pathCines (str): ruta de archivo JSON cines.txt con los cines
           pathEntradas (str): ruta de archivo JSON entradas.txt con las entradas
       - Retorno:
           None
           """
    try:
        # Asumimos que esta función imprime los cines y sus IDs
        listarCines()
        idCine = input("Ingrese el ID del cine de la reserva a eliminar:")

        # Cargar las películas
        with open(ARCHIVO_PELICULAS, mode="r", encoding="utf-8") as f1:
            peliculas = json.load(f1)

        # Filtrar las películas por cine
        peliculasEnCine = {int(peliculaId): info for peliculaId, info in peliculas.items(
        ) if info.get('complejo') == int(idCine)}

        if not peliculasEnCine:
            print("No hay películas disponibles en este cine.")
            return

        print("\nLista de todas las películas en este cine:")
        for movie_id, info in peliculasEnCine.items():
            print(
                f"ID: {movie_id}, Título: {info['title']}, Formato: {info['format']}, Idioma: {info['language']}")

        # Bucle para validar el ID de película en el cine seleccionado
        while True:
            peliculaId = ingresarIdPelicula(
                "Seleccione el ID de la película de la reserva a eliminar:")

            if peliculaId in peliculasEnCine:
                break  # Salir del bucle si el ID es válido para el cine
            else:
                print(
                    "El ID de la película no corresponde a ninguna película en este cine. Intente nuevamente.")

        pelicula_id_str = str(peliculaId)

        nombreCliente = input(
            "Ingrese el nombre del cliente de la reserva:").lower()
        butaca = input("Ingrese el asiento reservado a eliminar:")

        # Verificar que la butaca esté reservada en la película seleccionada
        if butaca not in peliculas[pelicula_id_str]['sala'] or peliculas[pelicula_id_str]['sala'][butaca] == True:
            print("La reserva de ese asiento no existe o ya está disponible.")
            return

        with open(ARCHIVO_ENTRADAS, mode="r", encoding="utf-8") as f2:
            entradas = json.load(f2)

        # Encontrar la entrada correspondiente para eliminar
        entradaEliminarId = None
        for entradaId, entrada in entradas.items():
            if (entrada['cliente'].lower() == nombreCliente and entrada['cine'] == idCine and
                    entrada['pelicula'] == peliculaId and entrada['butaca'] == butaca):
                entradaEliminarId = entradaId
                break

        if not entradaEliminarId:
            print("No se encontró una reserva que coincida con los datos proporcionados.")
            return

        # Eliminar la entrada y liberar la butaca
        del entradas[entradaEliminarId]
        peliculas[pelicula_id_str]['sala'][butaca] = True

        with open(ARCHIVO_ENTRADAS, mode="w", encoding="utf-8") as f2:
            json.dump(entradas, f2, ensure_ascii=False, indent=4)

        with open(ARCHIVO_PELICULAS, mode="w", encoding="utf-8") as f1:
            json.dump(peliculas, f1, ensure_ascii=False, indent=4)

        print(
            f"La reserva para el cliente {nombreCliente} en el asiento {butaca} ha sido eliminada exitosamente.")

    except (FileNotFoundError, OSError) as e:
        print("Error al intentar abrir o guardar archivo:", e)
    except json.JSONDecodeError as e:
        print("Error al decodificar JSON:", e)

def crear_estadisticas_ventas(entradas, peliculas, cines):
    """- Función auxiliar que crea estadísticas de ventas
       - Parámetros:
           entradas (dict): diccionario con todas las entradas
           peliculas (dict): diccionario con todas las películas
           cines (dict): diccionario con todos los cines
       - Retorno:
           tuple: (informe, ventasGenerales)"""
    
    # Inicializar el diccionario de informe manualmente
    informe = {}
    ventasGenerales = 0
    
    for entrada in entradas.values():
        cineId = entrada.get("cine")
        peliculaId = str(entrada.get("pelicula"))
        
        # Verificaciones de existencia
        if cineId not in cines or peliculaId not in peliculas:
            continue
            
        # Inicializar la entrada del cine si no existe
        if cineId not in informe:
            informe[cineId] = {
                "nombre": cines[cineId]["nombre"],
                "entradas": {}
            }
        
        # Inicializar la entrada de la película si no existe
        if peliculaId not in informe[cineId]["entradas"]:
            informe[cineId]["entradas"][peliculaId] = {
                "titulo": peliculas[peliculaId]["title"],
                "cantidad": 0
            }
        
        # Incrementar contador de entradas para esta película
        informe[cineId]["entradas"][peliculaId]["cantidad"] += 1
        ventasGenerales += 1
    
    return informe, ventasGenerales

def informeVentas():
    """- Genera un informe de ventas de entradas, mostrando la cantidad de entradas vendidas por película y cine.
       - Parámetro:
           pathEntradas (str): ruta de archivo JSON entradas.txt con las entradas
           pathMovies (str): ruta de archivo JSON movies.txt con las películas
           pathCines (str): ruta de archivo JSON cines.txt con los cines
       - Retorno:
           None"""
    try:
        # Abrir y cargar los archivos JSON
        with open(ARCHIVO_ENTRADAS, "r", encoding="utf-8") as f:
            entradas = json.load(f)

        with open(ARCHIVO_PELICULAS, "r", encoding="utf-8") as f:
            peliculas = json.load(f)

        with open(ARCHIVO_CINES, "r", encoding="utf-8") as f:
            cines = json.load(f)

        # Usar la función auxiliar para crear estadísticas con defaultdict
        informe, ventasGenerales = crear_estadisticas_ventas(entradas, peliculas, cines)

        # Imprimir el informe de ventas
        for cineId, cineData in informe.items():
            print(f"\nCine: {cineData['nombre']}")
            for peliculaId, peliculaData in cineData["entradas"].items():
                print(
                    f"  - Película: {peliculaData['titulo']}, Entradas Vendidas: {peliculaData['cantidad']}")

        print(f"\nTotal de ventas Totales realizadas: {ventasGenerales}")

    except (FileNotFoundError, OSError) as e:
        print(f"-Error- al intentar abrir archivo: {e}")

def informeListadoPeliculasDisponibles(peliculas, cines):
    """Muestra todas las películas activas, con idiomas y formatos sin duplicados por cine."""
    disponibles = [
                    (peliculaId, data["title"].strip(), data["language"], data["format"], cines.get(str(data.get("complejo")), {}).get("nombre", "Desconocido"))
                    for peliculaId, data in peliculas.items()
                    if data.get("activo", True)  # filtramos con comprensión de listas
                ]

    if not disponibles:
        print("No hay películas disponibles actualmente.")
        return []

    # Conjuntos para eliminar duplicados de idiomas y formatos
    return disponibles

def informeButacasDisponibles(sala):
    """- Función que genera un informe de las butacas disponibles para cada película.
       - Parámetro:
           pathMovies (str): ruta de archivo JSON movies.txt con las películas
       - Retorno:
           None"""
            # Mostrar butacas disponibles
    butacasDisponibles = set([butaca for butaca, disponible in sala.items() if disponible])
    return butacasDisponibles

def modificarCine(cineId, cineModificado, cines):
    """- Modifica los datos de un cine existente.
       - Parámetro:
           cineId (str): ID del cine a modificar
           cineModificado (dict): diccionario con los datos modificados del cine
           cines (dict): diccionario con todos los cines
       - Retorno:
           None"""
    cines[cineId].update(cineModificado)
    print("¡Cine modificado con éxito!")
    print("Cines actuales:", cines)
    for i in cines:
        print(
            f"ID: {i}, Nombre: {cines[i]['nombre']}, Dirección: {cines[i]['direccion']}")
    return cines
    
def obtener_estadisticas_sistema():
    """- Función que obtiene estadísticas generales del sistema usando conjuntos
       - Retorno:
           dict: estadísticas del sistema"""
    try:
        with open(ARCHIVO_PELICULAS, "r", encoding="utf-8") as f:
            peliculas = json.load(f)
        
        with open(ARCHIVO_CINES, "r", encoding="utf-8") as f:
            cines = json.load(f)
            
        with open(ARCHIVO_ENTRADAS, "r", encoding="utf-8") as f:
            entradas = json.load(f)
        
        # Usar conjuntos para obtener elementos únicos eficientemente
        formatos_usados = {pelicula['format'] for pelicula in peliculas.values()}
        idiomas_usados = {pelicula['language'] for pelicula in peliculas.values()}
        clientes_unicos = {entrada['cliente'] for entrada in entradas.values()}
        
        estadisticas = {
            'total_peliculas': len(peliculas),
            'peliculas_activas': len(obtener_peliculas_activas(peliculas)),
            'total_cines': len(cines),
            'total_entradas_vendidas': len(entradas),
            'clientes_unicos': len(clientes_unicos),
            'formatos_disponibles': list(formatos_usados),
            'idiomas_disponibles': list(idiomas_usados)
        }
        
        return estadisticas
        
    except (FileNotFoundError, OSError) as e:
        print(f"Error al obtener estadísticas: {e}")
        return {}

def eliminarCine(cineId, cines):
    del cines[cineId]
    return cines