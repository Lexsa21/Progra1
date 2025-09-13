FORMATOS_VALIDOS = {"2d", "3d"}
IDIOMAS_VALIDOS = {"español", "subtitulado"}
DIAS_SEMANA = {"lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"}

NUMERACION_FILAS = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
CONFIGURACION_SALA = (9, 8)  # (filas, columnas)

def imprimirPeliculas(peliculas):
    print("\n--- LISTADO DE PELÍCULAS ---")
    for peliculaId, pelicula in peliculas.items():
        print(f"ID: {peliculaId} | Título: {pelicula['titulo']} | Idioma: {pelicula['idioma']} | Formato: {pelicula['formato']} | ID Cine: {pelicula['complejo']}")
        if pelicula['schedule']:
            print("  Funciones:")
            for dia, horarios in pelicula['schedule'].items():
                for horario in horarios:
                    print(f"    - {dia.capitalize()} a las {horario}")
        else:
            print("  No hay horarios asignados.")
    print("\n")

def agregarPelicula(peliculaData, peliculas):
    peliculaId = generarId(peliculas)

    sala = crearSala()

    peliculaData["activo"] = True
    peliculaData["sala"] = sala

    peliculas[peliculaId] = peliculaData.copy()

    return peliculas

def modificarPelicula(peliculaId, peliculaData, peliculas):
    peliculas[peliculaId] = peliculaData.copy()

    return peliculas

    print(f"¡Película '{peliculaId}' modificada con éxito!")

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

def generarId(peliculas):
    nuevoId = len(peliculas.keys()) + 1
    peliculaId = f"{nuevoId}"

    return peliculaId

def crearSala():
    sala = {}
    filas, columnas = CONFIGURACION_SALA
    
    for i in range(1, filas + 1):
        for j in range(columnas):
            asiento = f"{NUMERACION_FILAS[j]}{i}"
            sala[asiento] = True
    return sala

def agregarSchedule():
    dia = input(
        "Ingresa el día de la semana para la proyección (o 'ENTER' para terminar): ")
    if not dia:
        return {}
    if dia.lower() not in DIAS_SEMANA:
        print("Error. Día no válido. Ingresar un día correcto.")
        return agregarSchedule()

    horario = input("Ingresa la hora (ej. 14:00): ")
    while not esHorario(horario):
        horario = input("Error. Ingresa la hora (ej. 14:00): ")

    # Retornar un diccionario con el día como clave y un set con el horario
    return {dia.lower(): {horario}}

def esHorario(horario):
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

def nuevoCine(cineData, cines):
    nuevo_id = str(int(max(cines.keys(), default="0")) + 1)

    cines[nuevo_id] = {"nombre": cineData[0], "direccion": cineData[1]}

    print(f"\nCine agregado con éxito: {cineData[0]} (ID: {nuevo_id})")
    return cines

def imprimirCines(cines):
    listado = [(cineId, data["nombre"].strip(), data["direccion"].strip()) for cineId, data in cines.items()]
    print("\n--- LISTADO DE CINES ---")
    for cineId, nombre, direccion in listado:
        print(f"ID: {cineId:<3} | Nombre: {nombre:<25} | Dirección: {direccion}")

def generarEntrada():
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
                    f"ID: {peliculaId}, Título: {info['titulo']}, Formato: {info['formato']}, Idioma: {info['idioma']}")
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
                f"ID: {movie_id}, Título: {info['titulo']}, Formato: {info['formato']}, Idioma: {info['idioma']}")

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
                "titulo": peliculas[peliculaId]["titulo"],
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
                    (peliculaId, data["titulo"].strip(), data["idioma"], data["formato"], cines.get(str(data.get("complejo")), {}).get("nombre", "Desconocido"))
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

def modificarCine(cineId, cineData, cines):
    cineModificado = {
        "nombre": cineData[0],
        "direccion": cineData[1]
    }
    cines[cineId].update(cineModificado)
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
        formatos_usados = {pelicula['formato'] for pelicula in peliculas.values()}
        idiomas_usados = {pelicula['idioma'] for pelicula in peliculas.values()}
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