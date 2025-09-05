# ----------------------------------------------------------------------------------------------
# FUNCIONES
# ----------------------------------------------------------------------------------------------
import json


def listarPeliculas(pathArchivoPeliculas):
    """- Función que lista las películas activas del archivo movies.txt
       - Parámetros: 
            pathArchivoPeliculas (str): ruta de archivo JSON movies.txt con las películas
       - Retorno:
            None """
    try:
        archivoPeliculas = open(pathArchivoPeliculas,
                                mode="r", encoding="utf-8")
        peliculas = json.load(archivoPeliculas)
        archivoPeliculas.close()

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

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    return


def agregarPelicula(pathArchivoPeliculas, pathId, pathCine):
    """- Función que agrega una película al archivo movies.txt
       - Parámetros: 
            pathArchivoPeliculas (str): ruta de archivo JSON movies.txt con las películas
            pathId (str): ruta de archivo JSON id_mapping.txt con los ID y sus respectivos números
            pathCine (str): ruta de archivo JSON cines.txt con los cines
       - Retorno:
            None """

    try:
        # Se carga el contenido existente de los archivos JSON
        archivoPeliculas = open(pathArchivoPeliculas,
                                mode="r", encoding="utf-8")
        peliculas = json.load(archivoPeliculas)
        archivoPeliculas.close()

        archivoConIDs = open(pathId, mode="r", encoding="utf-8")
        id_mapping = json.load(archivoConIDs)
        archivoConIDs.close()

        archivoCines = open(pathCine, mode="r", encoding="utf-8")
        cines = json.load(archivoCines)

        peliculaId, number_id = generarId(pathArchivoPeliculas)

        titulo = input("Ingresa el título de la película: ")
        while not titulo:
            titulo = input(
                "Error. El título no puede estar vacío. Ingresa el título de la película: ")

        format_type = input("Ingresa el formato (2D/3D): ")
        while format_type.lower() not in ["2d", "3d"]:
            format_type = input("Error. Ingresa el formato (2D/3D): ")

        language = input("Ingresa el idioma (Español/Subtitulado): ")
        while language.lower() not in ["español", "subtitulado"]:
            language = input(
                "Error. Ingresa el idioma (Español/Subtitulado): ")

        sala = crearSala()

        print("Elija el cine en el que se proyectará.")
        limitec = 0
        for i in cines:
            print(f"{i} : {cines[i]['nombre']}")
            limitec += 1
        cine = int(input("Ingresa el numero del cine en el que se proyectará:"))
        while not cine or cine > limitec:
            cine = input("Error. Ingresa el cine: ")

        # Se agrega la película
        peliculas[peliculaId] = {
            'title': titulo,
            'format': format_type,
            'language': language,
            'schedule': [],
            'activo': True,
            # Permite una sala simbolica que guarde el estado (reservado o disponible) de los asientos de la sala.
            'sala': sala,
            # Hace falta que en las peliculas figure en que cine se proyectan.
            'complejo': cine
        }

        # Se agrega el id a id_mapping
        id_mapping[number_id] = peliculaId

        agregarSchedule(peliculas, peliculaId)

        # Se sobreescriben los archivos con los datos actualizados
        archivoPeliculas = open(pathArchivoPeliculas,
                                mode="w", encoding="utf-8")
        json.dump(peliculas, archivoPeliculas, ensure_ascii=False, indent=4)
        archivoPeliculas.close()

        archivoConIDs = open(pathId, mode="w", encoding="utf-8")
        json.dump(id_mapping, archivoConIDs, ensure_ascii=False, indent=4)
        archivoConIDs.close()

        print(f"¡Película '{titulo}' agregada con éxito con ID: {peliculaId}!")

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    return


def modificarPelicula(pathArchivoPeliculas, pathId):
    """- Función que modifica una película del archivo movies.txt
       - Parámetros: 
            pathArchivoPeliculas (str): ruta de archivo JSON movies.txt con las películas
            pathId (str): ruta de archivo JSON id_mapping.txt con los ID y sus respectivos números
       - Retorno:
            None """

    try:
        archivoPeliculas = open(pathArchivoPeliculas,
                                mode="r", encoding="utf-8")
        movies = json.load(archivoPeliculas)
        archivoPeliculas.close()

        f2 = open(pathId, mode="r", encoding="utf-8")
        id_mapping = json.load(f2)
        f2.close()

        movie_number = input("Ingresa el número de la película a modificar: ")
        if movie_number in id_mapping:
            movie_id = id_mapping[movie_number]
            movie = movies[movie_id]

            title = input(
                f"Ingresa el nuevo título de la película ({movie['title']}): ")
            if title:  # Si el usuario no ingresa nada, conserva el valor original
                movie['title'] = title

            format_type = input(
                f"Ingresa el nuevo formato (2D/3D) ({movie['format']}): ")
            while format_type and format_type.lower() not in ["2d", "3d"]:
                format_type = input("Error. Ingresa el formato (2D/3D): ")
            if format_type:
                movie['format'] = format_type

            language = input(
                f"Ingresa el nuevo idioma (Español/Subtitulado) ({movie['language']}): ")
            while language and language.lower() not in ["español", "subtitulado"]:
                language = input(
                    "Error. Ingresa el idioma (Español/Subtitulado): ")
            if language:
                movie['language'] = language

            archivoPeliculas = open(
                pathArchivoPeliculas, mode="w", encoding="utf-8")
            json.dump(movies, archivoPeliculas, ensure_ascii=False, indent=4)
            archivoPeliculas.close()

            f2 = open(pathId, mode="w", encoding="utf-8")
            json.dump(id_mapping, f2, ensure_ascii=False, indent=4)
            f2.close()

            print(f"¡Película '{movie_id}' modificada con éxito!")
        else:
            print("Número de película no encontrado.")

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    return


def inactivarPelicula(pathArchivoPeliculas, pathId):
    """- Función que inactiva una película del archivo movies.txt
       - Parámetros: 
            pathArchivoPeliculas (str): ruta de archivo JSON movies.txt con las películas
            pathId (str): ruta de archivo JSON id_mapping.txt con los ID y sus respectivos números
       - Retorno:
            None """

    try:
        archivoPeliculas = open(pathArchivoPeliculas,
                                mode="r", encoding="utf-8")
        movies = json.load(archivoPeliculas)
        archivoPeliculas.close()

        f2 = open(pathId, mode="r", encoding="utf-8")
        id_mapping = json.load(f2)
        f2.close()

        movie_number = input("Ingresa el número de la película a eliminar: ")
        if movie_number in id_mapping:
            movie_id = id_mapping[movie_number]
            movies[movie_id]['activo'] = False

            archivoPeliculas = open(
                pathArchivoPeliculas, mode="w", encoding="utf-8")
            json.dump(movies, archivoPeliculas, ensure_ascii=False, indent=4)
            archivoPeliculas.close()

            f2 = open(pathId, mode="w", encoding="utf-8")
            json.dump(id_mapping, f2, ensure_ascii=False, indent=4)
            f2.close()

            print(f"¡Película '{movie_id}' inactivada con éxito!")
        else:
            print("Número de película no encontrado.")

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    return


def modificarPrecioEntrada():
    print("Esta opción no está implementada en este ejemplo.")


def generarId(pathArchivoPeliculas):
    """- Función que genera un ID único para una película.
       - Parámetro:
           pathArchivoPeliculas (str): ruta de archivo JSON movies.txt con las películas
       - Retorno:
           movie_id (str): ID generado 
           number_id (str): número asociado al ID"""
    try:
        archivoPeliculas = open(pathArchivoPeliculas,
                                mode="r", encoding="utf-8")
        movies = json.load(archivoPeliculas)
        archivoPeliculas.close()

        nuevoId = max(map(int, movies.keys()), default=0) + 1
        peliculaId = f"{nuevoId:04d}"

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    return peliculaId, nuevoId

# Funcion que crea una sala nueva con butacas vacias para las funciones
# Es una sala "simbolica", no tomarselo como que existe una sala diferente por pelicula.


def crearSala():
    """- Función que genera una sala para cada pelicula, de iguales dimenciones y cantidad de asientos.
       - Parámetro:
           NONE
       - Retorno:
           sala (dicc): diccionario con disponibilidad de cada asiento"""
    sala = {}
    Abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    for i in range(1, 10):
        for j in range(0, 8):
            asiento = str(Abc[j])+str(i)
            sala[asiento] = True
    return sala


def agregarSchedule(movies, movie_id):
    """- Función que agrega el día y horario de la función a una película a agregar al archivo movies.txt
       - Parámetros:
           movies (dicc): contenido cargado del archivo JSON movies.txt
           movie_id (str): ID generado para la película a agregar
       - Retorno:
           movies (dicc): contenido actualizado del diccionario movies"""

    # Agregar a la función la verificación de que dos peliculas en el mismo complejo no tengan mismo día y horario (ya que solo existe una sala)

    while True:
        day = input(
            "Ingresa el día de la semana para la proyección (o 'fin' para terminar): ")
        if day.lower() == 'fin':
            break
        if day.lower() not in ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]:
            print("Error. Día no válido. Ingresar un día correcto.")
            continue

        time = input("Ingresa la hora (ej. 14:00): ")
        while not esHorario(time):
            time = input("Error. Ingresa la hora (ej. 14:00): ")

        schedule_entry = f"{day} a las {time}"
        movies[movie_id]['schedule'].append(schedule_entry)

    return movies


def esHorario(time):
    """- Función que valida que el horario tenga el formato HH:MM y sea un horario válido.
       - Parámetro:
           time (str): horario ingresado
       - Retorno:
           (bool): True si es un horario válido, False en caso contrario."""

    if len(time) != 5 or time[2] != ":":
        return False

    horas, minutos = time.split(":")
    if not (horas.isdigit() and minutos.isdigit()):
        return False

    return 0 <= int(horas) < 24 and 0 <= int(minutos) < 60

# Esta función debuelve la butaca disponible (si la hay) o 0 si no existe para esa función. idp = id de la pelicula, pathMovies = ruta al archivo que contiene las peliculas.


def butacaDisponible(idp, pathMovies):
    """- Función que busca la primera butaca disponible en una pelicula determinada.
       - Parámetro:
           idp (str): id de la pelicula 
           pathMovies (str): ruta de archivo JSON movies.txt con las películas
       - Retorno:
           butaca (str): butaca asignada para la pelicula
           """
    try:
        # Cargar las películas
        with open(pathMovies, mode="r", encoding="utf-8") as f:
            movies = json.load(f)

        peli = movies.get(idp)

        if peli is None or 'sala' not in peli:
            return None  # La película no existe o no tiene sala asignada

        for butaca, disponible in peli['sala'].items():
            if disponible:  # Si la butaca está disponible
                # Marcar la butaca como ocupada
                peli['sala'][butaca] = False
                # Guardar los cambios en el archivo
                with open(pathMovies, mode="w", encoding="utf-8") as f:
                    json.dump(movies, f, ensure_ascii=False, indent=4)
                return butaca

        return None  # No hay butacas disponibles
    except (FileNotFoundError, OSError) as e:
        print("Error al intentar abrir o guardar archivo:", e)
    except json.JSONDecodeError as e:
        print("Error al decodificar JSON:", e)

    return


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


def nuevoCine(path):
    """- Función que genera un nuevo cine.
       - Parámetro:
           path (str): ruta de archivo JSON cines.txt con los cines
       - Retorno:
           None
           """
    try:
        with open(path, mode="r", encoding="utf-8") as f1:
            cines = json.load(f1)

        # Generar nuevo ID
        nuevoid = max(int(i) for i in cines.keys()) + 1 if cines else 1

        # Solicitar nombre del cine
        title = input("Ingresa el nombre del nuevo cine: ")
        while not title:
            title = input(
                "Error. El nombre no puede estar vacío. Ingresa el nombre del nuevo cine: ")

        # Solicitar dirección del cine
        direcc = input("Ingresa la dirección del nuevo cine: ")
        while not direcc:
            direcc = input(
                "Error. La dirección no puede estar vacía. Ingresa la dirección del nuevo cine: ")

        # Agregar el nuevo cine al diccionario
        cines[str(nuevoid)] = {
            'nombre': title,
            'direccion': direcc
        }

        # Guardar los datos actualizados en el archivo JSON
        with open(path, mode="w", encoding="utf-8") as f1:
            json.dump(cines, f1, ensure_ascii=False, indent=4)

        print("¡Cine creado con éxito!")
    except (FileNotFoundError, OSError) as e:
        print("Error al intentar abrir o guardar archivo:", e)
    except json.JSONDecodeError as e:
        print("Error al decodificar JSON:", e)

    return


def listarCines(path):
    """- Función que lista los cines creados.
       - Parámetro:
           path (str): ruta de archivo JSON cines.txt con los cines
       - Retorno:
           None
           """
    try:
        with open(path, mode="r", encoding="utf-8") as f1:
            cines = json.load(f1)

        print("Lista de todos los cines:")
        for i in cines:
            print(
                f"ID: {i}, Nombre: {cines[i]['nombre']}, Dirección: {cines[i]['direccion']}")
    except (FileNotFoundError, OSError) as e:
        print(f"Error al intentar abrir archivo: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")

    return

# Reserva un asiento para una pelicula. listapelis = archivo / estructura de datos con las peliculas, listaentradas = archivo/estructura de datos que gusrde las entradas a las peliculas.


def generarEntrada(pathMovies, pathEntradas, pathCines):
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
        listarCines(pathCines)
        idCine = input("Ingrese el ID del cine donde desea reservar:")

        # Cargar las películas
        with open(pathMovies, mode="r", encoding="utf-8") as f1:
            movies = json.load(f1)

        # Filtrar las películas por cine
        peliculas_en_cine = {int(movie_id): info for movie_id, info in movies.items(
        ) if info.get('complejo') == int(idCine)}

        if peliculas_en_cine:
            print("\nLista de todas las películas en este cine:")
            for movie_id, info in peliculas_en_cine.items():
                print(
                    f"ID: {movie_id}, Título: {info['title']}, Formato: {info['format']}, Idioma: {info['language']}")
                if info['schedule']:
                    print("  Horarios:")
                    for entry in info['schedule']:
                        print(f"    - {entry}")
                else:
                    print("No hay horarios asignados.")

            # Bucle para pedir el ID de película hasta que sea correcto
            while True:
                idPelicula = ingresarIdPelicula(
                    "Seleccionar el ID de la película que desee ver")

                if idPelicula in peliculas_en_cine:
                    break  # Salir del bucle si el ID es correcto
                else:
                    print(
                        "El ID de la película no corresponde a ninguna película en este cine. Intente nuevamente.")

            # Verificar la disponibilidad de butacas
            butaca = butacaDisponible(str(idPelicula).zfill(4), pathMovies)

            if butaca is None:
                print("No hay butacas disponibles para esta película en este cine.")
                return

            # Cargar las entradas para actualizar
            with open(pathEntradas, mode="r", encoding="utf-8") as f2:
                entradas = json.load(f2)

            # Generar un nuevo ID para la entrada
            nueva_entrada = {
                'cliente': nombreCliente,
                'cine': idCine,
                'pelicula': idPelicula,
                'butaca': butaca
            }
            nuevo_id = str(len(entradas) + 1)
            entradas[nuevo_id] = nueva_entrada

            # Guardar las entradas actualizadas
            with open(pathEntradas, mode="w", encoding="utf-8") as f2:
                json.dump(entradas, f2, ensure_ascii=False, indent=4)

            print(
                f"Felicidades, el cliente {nombreCliente} tiene reservado el asiento {butaca} para la función.")

    except (FileNotFoundError, OSError) as e:
        print("Error al intentar abrir o guardar archivo:", e)
    except json.JSONDecodeError as e:
        print("Error al decodificar JSON:", e)


"""def eliminarEntrada(pathMovies, pathEntradas, pathCines):
    - Función que elimina la entrada a una pelicula de un cliente, dejando su asiento disponible
       - Parámetro:
           pathMovies (str): ruta de archivo JSON movies.txt con las películas
           pathCines (str): ruta de archivo JSON cines.txt con los cines
           pathEntradas (str): ruta de archivo JSON entradas.txt con las entradas
       - Retorno:
           None
           
    try:
        listarCines(pathCines)  # Asumimos que esta función imprime los cines y sus IDs
        idCine = input("Ingrese el ID del cine de la reserva a eliminar:")

        # Cargar las películas
        with open(pathMovies, mode="r", encoding="utf-8") as f1:
            movies = json.load(f1)

        # Filtrar las películas por cine
        peliculas_en_cine = {int(movie_id): info for movie_id, info in movies.items() if info.get('complejo') == int(idCine)}

        if not peliculas_en_cine:
            print("No hay películas disponibles en este cine.")
            return

        print("\nLista de todas las películas en este cine:")
        for movie_id, info in peliculas_en_cine.items():
            print(f"ID: {movie_id}, Título: {info['title']}, Formato: {info['format']}, Idioma: {info['language']}")

        idPelicula = ingresarIdPelicula("Seleccione el ID de la película de la reserva a eliminar:")

        pelicula_id_str = str(idPelicula).zfill(4)
        if pelicula_id_str not in movies:
            print("El ID de la película no es válido.")
            return

        nombreCliente = input("Ingrese el nombre del cliente de la reserva:").lower()
        butaca = input("Ingrese el asiento reservado a eliminar:")

        if butaca not in movies[pelicula_id_str]['sala'] or movies[pelicula_id_str]['sala'][butaca] == True:
            print("La reserva de ese asiento no existe o ya está disponible.")
            return

        with open(pathEntradas, mode="r", encoding="utf-8") as f2:
            entradas = json.load(f2)

        entrada_a_eliminar = None
        for entrada_id, entrada in entradas.items():
            if (entrada['cliente'].lower() == nombreCliente and entrada['cine'] == idCine and 
                entrada['pelicula'] == idPelicula and entrada['butaca'] == butaca):
                entrada_a_eliminar = entrada_id
                break

        if not entrada_a_eliminar:
            print("No se encontró una reserva que coincida con los datos proporcionados.")
            return

        del entradas[entrada_a_eliminar]
        movies[pelicula_id_str]['sala'][butaca] = True

        with open(pathEntradas, mode="w", encoding="utf-8") as f2:
            json.dump(entradas, f2, ensure_ascii=False, indent=4)

        with open(pathMovies, mode="w", encoding="utf-8") as f1:
            json.dump(movies, f1, ensure_ascii=False, indent=4)

        print(f"La reserva para el cliente {nombreCliente} en el asiento {butaca} ha sido eliminada exitosamente.")

    except (FileNotFoundError, OSError) as e:
        print("Error al intentar abrir o guardar archivo:", e)
    except json.JSONDecodeError as e:
        print("Error al decodificar JSON:", e)
    
    return
"""


def eliminarEntrada(pathMovies, pathEntradas, pathCines):
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
        listarCines(pathCines)
        idCine = input("Ingrese el ID del cine de la reserva a eliminar:")

        # Cargar las películas
        with open(pathMovies, mode="r", encoding="utf-8") as f1:
            movies = json.load(f1)

        # Filtrar las películas por cine
        peliculas_en_cine = {int(movie_id): info for movie_id, info in movies.items(
        ) if info.get('complejo') == int(idCine)}

        if not peliculas_en_cine:
            print("No hay películas disponibles en este cine.")
            return

        print("\nLista de todas las películas en este cine:")
        for movie_id, info in peliculas_en_cine.items():
            print(
                f"ID: {movie_id}, Título: {info['title']}, Formato: {info['format']}, Idioma: {info['language']}")

        # Bucle para validar el ID de película en el cine seleccionado
        while True:
            idPelicula = ingresarIdPelicula(
                "Seleccione el ID de la película de la reserva a eliminar:")

            if idPelicula in peliculas_en_cine:
                break  # Salir del bucle si el ID es válido para el cine
            else:
                print(
                    "El ID de la película no corresponde a ninguna película en este cine. Intente nuevamente.")

        pelicula_id_str = str(idPelicula).zfill(4)

        nombreCliente = input(
            "Ingrese el nombre del cliente de la reserva:").lower()
        butaca = input("Ingrese el asiento reservado a eliminar:")

        # Verificar que la butaca esté reservada en la película seleccionada
        if butaca not in movies[pelicula_id_str]['sala'] or movies[pelicula_id_str]['sala'][butaca] == True:
            print("La reserva de ese asiento no existe o ya está disponible.")
            return

        with open(pathEntradas, mode="r", encoding="utf-8") as f2:
            entradas = json.load(f2)

        # Encontrar la entrada correspondiente para eliminar
        entrada_a_eliminar = None
        for entrada_id, entrada in entradas.items():
            if (entrada['cliente'].lower() == nombreCliente and entrada['cine'] == idCine and
                    entrada['pelicula'] == idPelicula and entrada['butaca'] == butaca):
                entrada_a_eliminar = entrada_id
                break

        if not entrada_a_eliminar:
            print("No se encontró una reserva que coincida con los datos proporcionados.")
            return

        # Eliminar la entrada y liberar la butaca
        del entradas[entrada_a_eliminar]
        movies[pelicula_id_str]['sala'][butaca] = True

        with open(pathEntradas, mode="w", encoding="utf-8") as f2:
            json.dump(entradas, f2, ensure_ascii=False, indent=4)

        with open(pathMovies, mode="w", encoding="utf-8") as f1:
            json.dump(movies, f1, ensure_ascii=False, indent=4)

        print(
            f"La reserva para el cliente {nombreCliente} en el asiento {butaca} ha sido eliminada exitosamente.")

    except (FileNotFoundError, OSError) as e:
        print("Error al intentar abrir o guardar archivo:", e)
    except json.JSONDecodeError as e:
        print("Error al decodificar JSON:", e)


def informeVentas(pathEntradas, pathMovies, pathCines):
    """- Genera un informe de ventas de entradas, mostrando la cantidad de entradas vendidas por película y cine.
       - Parámetro:
           pathEntradas (str): ruta de archivo JSON entradas.txt con las entradas
           pathMovies (str): ruta de archivo JSON movies.txt con las películas
           pathCines (str): ruta de archivo JSON cines.txt con los cines
       - Retorno:
           None"""
    try:
        # Abrir y cargar los archivos JSON
        with open(pathEntradas, "r", encoding="utf-8") as f:
            entradas = json.load(f)

        with open(pathMovies, "r", encoding="utf-8") as f:
            movies = json.load(f)

        with open(pathCines, "r", encoding="utf-8") as f:
            cines = json.load(f)

        # Crear un informe acumulativo de entradas vendidas por cine y película, un total general de ventas
        informe = {}
        ventasGenerales = 0
        for entrada in entradas.values():
            cine_id = entrada.get("cine")
            # Aseguramos que el ID de película tenga 4 dígitos
            pelicula_id = str(entrada.get("pelicula")).zfill(4)

            # Verificar si el cine existe
            if cine_id not in cines:
                print(
                    f"Advertencia: El cine con ID {cine_id} no existe. Ignorando esta entrada.")
                continue  # Saltar si el cine no existe

            # Verificar si la película existe
            if pelicula_id not in movies:
                print(
                    f"Advertencia: La película con ID {pelicula_id} no existe. Ignorando esta entrada.")
                continue  # Saltar si la película no existe

            # Agregar cine al informe si no existe
            if cine_id not in informe:
                informe[cine_id] = {
                    "nombre": cines[cine_id]["nombre"], "entradas": {}}

            # Agregar película al informe de ese cine si no existe
            if pelicula_id not in informe[cine_id]["entradas"]:
                informe[cine_id]["entradas"][pelicula_id] = {
                    "titulo": movies[pelicula_id]["title"],
                    "cantidad": 0
                }

            # Incrementar la cantidad de entradas vendidas para esa película en ese cine
            informe[cine_id]["entradas"][pelicula_id]["cantidad"] += 1
            ventasGenerales += 1

        # Imprimir el informe de ventas
        for cine_id, cine_data in informe.items():
            print(f"\nCine: {cine_data['nombre']}")
            for pelicula_id, pelicula_data in cine_data["entradas"].items():
                print(
                    f"  - Película: {pelicula_data['titulo']}, Entradas Vendidas: {pelicula_data['cantidad']}")

        print(f"\nTotal de ventas Totales realizadas: {ventasGenerales}")

    except (FileNotFoundError, OSError) as e:
        print(f"-Error- al intentar abrir archivo: {e}")

    return


def informeListadoPeliculasDisponibles(pathMovies):
    """- Emite un listado de películas disponibles.
       - Parámetro:
           pathMovies (str): ruta de archivo JSON movies.txt con las películas
       - Retorno: 
           None"""
    try:
        # Abrir archivo de películas
        with open(pathMovies, mode="r", encoding="utf-8") as f:
            movies = json.load(f)

        # Contador de películas activas
        contador_peliculas = 0

        print("\nListado de películas disponibles:")
        for movie_id, info in movies.items():
            if info['activo']:  # Solo mostrar películas activas
                contador_peliculas += 1
                print(
                    f"ID: {movie_id}, Título: {info['title']}, Formato: {info['format']}, Idioma: {info['language']}")
                if info['schedule']:
                    print("  Horarios:")
                    for entry in info['schedule']:
                        print(f"    - {entry}")
                else:
                    print("  No hay horarios asignados.")

        # Mensaje de si no hay películas activas
        if contador_peliculas == 0:
            print("No hay películas activas disponibles.")
        else:
            print(f"\nTotal de películas activas: {contador_peliculas}")

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    return


def informeButacasDisponibles(pathMovies):
    """- Función que genera un informe de las butacas disponibles para cada película.
       - Parámetro:
           pathMovies (str): ruta de archivo JSON movies.txt con las películas
       - Retorno:
           None"""
    try:
        with open(pathMovies, mode="r", encoding="utf-8") as f:
            movies = json.load(f)

        # Recorrer todas las películas
        for movie_id, movie_info in movies.items():
            if movie_info['activo']:  # Solo películas activas
                sala = movie_info.get('sala')

                if sala is None:  # Si no tiene sala asignada, asignamos una sala vacía por defecto
                    sala = {}

                print(
                    f"\nPelícula: {movie_info['title']} ({movie_info['format']} - {movie_info['language']})")
                print(f"ID de la película: {movie_id}")
                print("Butacas disponibles:")

                # Mostrar butacas disponibles
                disponibles = [butaca for butaca,
                               disponible in sala.items() if disponible]
                if disponibles:
                    # esto agrupa las butacas disponibles en una cadena separada por coma.
                    print(", ".join(disponibles))
                else:
                    print("No hay butacas disponibles.")

            else:
                print(
                    f"\nPelícula inactiva: {movie_info['title']} no se muestra en el informe.")

    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir el archivo de películas:", detalle)

    return


def modificarCine(pathCines):
    """- Modifica los datos de un cine existente.
       - Parámetro:
           pathCines (str): ruta de archivo JSON cines.txt con los cines
       - Retorno:
           None"""
    try:
        with open(pathCines, mode="r", encoding="utf-8") as f1:
            cines = json.load(f1)

        cine_id = input("Ingrese el ID del cine que desea modificar: ")
        if cine_id not in cines:
            print("Error: No se encontró un cine con el ID proporcionado.")
            return

        # Pedir nuevos datos
        nuevo_nombre = input(
            "Ingrese el nuevo nombre del cine (deje en blanco para no modificar): ")
        nueva_direccion = input(
            "Ingrese la nueva dirección del cine (deje en blanco para no modificar): ")

        # Actualizar campos si se proporcionan nuevos valores
        if nuevo_nombre:
            cines[cine_id]['nombre'] = nuevo_nombre
        if nueva_direccion:
            cines[cine_id]['direccion'] = nueva_direccion

        # Guardar datos actualizados
        with open(pathCines, mode="w", encoding="utf-8") as f1:
            json.dump(cines, f1, ensure_ascii=False, indent=4)

        print("¡Cine modificado con éxito!")
    except (FileNotFoundError, OSError) as e:
        print(f"Error al intentar abrir o guardar archivo: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")

    return


def eliminarCine(pathCines):
    """- Elimina un cine del registro.
       - Parámetro:
           pathCines (str): ruta de archivo JSON cines.txt con los cines
       - Retorno:
           None"""
    try:
        with open(pathCines, mode="r", encoding="utf-8") as f1:
            cines = json.load(f1)

        cine_id = input("Ingrese el ID del cine que desea eliminar: ")
        if cine_id not in cines:
            print("Error: No se encontró un cine con el ID proporcionado.")
            return

        # Confirmar eliminación
        confirmacion = input(
            "¿Está seguro que desea eliminar el cine? (s/n): ").lower()
        if confirmacion == 's':
            del cines[cine_id]
            with open(pathCines, mode="w", encoding="utf-8") as f1:
                json.dump(cines, f1, ensure_ascii=False, indent=4)
            print("¡Cine eliminado con éxito!")
        else:
            print("Operación cancelada.")
    except (FileNotFoundError, OSError) as e:
        print(f"Error al intentar abrir o guardar archivo: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")

    return