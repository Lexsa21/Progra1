FORMATOS_VALIDOS = {"2d", "3d"}
IDIOMAS_VALIDOS = {"español", "subtitulado"}
DIAS_SEMANA = {"lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"}

NUMERACION_FILAS = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
CONFIGURACION_SALA = (9, 8)  # (filas, columnas)

def imprimirPeliculas(peliculas):
    """
    Imprime un listado formateado de todas las películas.
    
    Parámetros:
        peliculas (diccionario): Diccionario con las películas donde:
            - key: ID de la película (string)
            - value: Diccionario con datos de la película que debe contener:
                - titulo (string): Título de la película
                - idioma (string): Idioma de la película
                - formato (string): Formato de proyección (2D/3D)
                - complejos (conjunto): Conjunto de IDs de cines donde se proyecta
    
    Return:
        None: Solo imprime en consola 
    """
    print("\n--- LISTADO DE PELÍCULAS ---")
    for peliculaId, pelicula in peliculas.items():
        print(f"ID: {peliculaId} | Título: {pelicula['titulo']} | Idioma: {pelicula['idioma']} | Formato: {pelicula['formato']} | ID Cines: {', '.join(pelicula['complejos'])}")
    print("\n")

def agregarPelicula(peliculaData, peliculas):
    """
    Agrega una nueva película al diccionario de películas.
    
    Parámetros:
        peliculaData (diccionario): Diccionario con los datos de la película que debe contener:
            - titulo (string): Título de la película
            - formato (string): Formato de proyección (debe estar en FORMATOS_VALIDOS)
            - idioma (string): Idioma (debe estar en IDIOMAS_VALIDOS)
            - complejos (conjunto): Conjunto de IDs de cines
        peliculas (diccionario): Diccionario existente de películas donde agregar la nueva
    
    Return:
        tupla: (peliculas_actualizado, peliculaId_generado)
            - peliculas_actualizado (diccionario): Diccionario de películas con la nueva película
            - peliculaId_generado (string): ID asignado a la nueva película   
    """
    peliculaId = generarId(peliculas)

    sala = crearSala()

    peliculaData["activo"] = True
    peliculaData["sala"] = sala

    peliculas[peliculaId] = peliculaData.copy()

    return peliculas, peliculaId

def modificarPelicula(peliculaId, peliculaData, peliculas):
    """
    Modifica los datos de una película existente.
    
    Parámetros:
        peliculaId (string): ID de la película a modificar
        peliculaData (diccionario): Nuevos datos de la película que debe contener:
            - titulo (string): Título actualizado
            - formato (string): Formato actualizado
            - idioma (string): Idioma actualizado
            - complejos (conjunto): Conjunto actualizado de IDs de cines
            - activo (booleano): Estado de activación
            - sala (diccionario): Configuración de sala
        peliculas (diccionario): Diccionario de películas a modificar

    Returns:
        diccionario: Diccionario de películas actualizado con los nuevos datos 
    """
    peliculas[peliculaId] = peliculaData.copy()

    return peliculas

def generarId(peliculas):
    """
    Genera un ID único para una nueva película.
    
    Parámetros:
        peliculas (diccionario): Diccionario de películas existentes
    
    Return:
        string: ID único como string (ej: "1", "2", "3")
    """
    nuevoId = len(peliculas.keys()) + 1
    peliculaId = f"{nuevoId}"

    return peliculaId

def imprimirSalasPorCine(cineId, salas):
    """
    Imprime las salas pertenecientes a un cine específico.
    
    Parámetros:
        cineId (string): ID del cine del cual mostrar las salas
        salas (diccionario): Diccionario de salas donde:
            - key: ID de la sala (string)
            - value: Diccionario con datos de la sala que debe contener:
                - cineId (string): ID del cine al que pertenece
                - numeroSala (string/integer): Número identificador de la sala
    
    Return:
        None: Solo imprime en consola
    """
    print(f"\n--- SALAS DEL CINE ID: {cineId} ---")
    for salaId, sala in salas.items():
        if sala['cineId'] == cineId:
            print(f"ID: {salaId} | Número de Sala: {sala['numeroSala']}")
    print("\n")

def crearSala():
    """
    Crea una nueva sala con configuración de butacas predeterminada.
    
    Return:
        diccionario: Diccionario donde:
            - key: Identificador de butaca (ej: "A1", "B3") (str)
            - value: Disponibilidad de la butaca (booleano)
                - True: Butaca disponible
                - False: Butaca ocupada
    """
    sala = {}
    filas, columnas = CONFIGURACION_SALA
    
    for i in range(1, filas + 1):
        for j in range(columnas):
            asiento = f"{NUMERACION_FILAS[j]}{i}"
            sala[asiento] = True
    return sala

def generarFuncion(cineId, salaId):
    dia = input(
        "Ingresa el día de la semana para la proyección (o 'ENTER' para terminar): ")
    if not dia:
        return {}
    if dia.lower() not in DIAS_SEMANA:
        print("Error. Día no válido. Ingresar un día correcto.")
        return generarFuncion(cineId, salaId)

    horario = input("Ingresa la hora (ej. 14:00): ")
    while not esHorario(horario):
        horario = input("Error. Ingresa la hora (ej. 14:00): ")
    return {cineId: {salaId: {dia.lower(): {horario}}}}

def agregarFunciones(peliculaId, funcionesPelicula, funciones):
    if peliculaId not in funciones:
        funciones[peliculaId] = {}
    funciones[peliculaId].update(funcionesPelicula)
    return funciones

def imprimirFunciones(funciones, peliculas, cines, salas):
    print("\n--- FUNCIONES DE LA PELÍCULA ---")
    for peliculaId, cineIDs in funciones.items():
        print(f"Película ID: {peliculaId} - Título: {peliculas.get(peliculaId, {}).get('titulo', 'Desconocido')}")
        for cineId, salaIDs in cineIDs.items():
            print(f"  Cine ID: {cineId} - Nombre: {cines.get(cineId, {}).get('nombre', 'Desconocido')}")
            for salaId, dias in salaIDs.items():
                print(f"    Sala ID: {salaId} - Número de Sala: {salas.get(salaId, {}).get('numeroSala', 'Desconocido')}")
                for dia, horarios in dias.items():
                    horarios_str = ', '.join(sorted(horarios))
                print(f"    {dia.capitalize()}: {horarios_str}")

def eliminarFuncionesPorPeliculaCine(peliculaId, cineId, funciones):
    """Elimina todas las funciones de una película en un cine específico."""
    if peliculaId in funciones:
        if cineId in funciones[peliculaId]:
            del funciones[peliculaId][cineId]
            print(f"Se han eliminado todas las funciones de la película ID {peliculaId} en el cine ID {cineId}.")
        else:
            print(f"No se encontraron funciones para la película ID {peliculaId} en el cine ID {cineId}.")
    else:
        print(f"No se encontraron funciones para la película ID {peliculaId}.")
    return funciones

def esHorario(horario):
    if len(horario) != 5 or horario[2] != ":":
        return False

    horas, minutos = horario.split(":")
    if not (horas.isdigit() and minutos.isdigit()):
        return False

    return 0 <= int(horas) < 24 and 0 <= int(minutos) < 60

def peliculasPorCine(peliculas, cineId):
    return {
        peliculaId: pelicula for peliculaId, pelicula in peliculas.items() if cineId in pelicula.get('complejos', set())
    }

def nuevoCine(cineData, cines):
    """
    Agrega un nuevo cine al diccionario de cines.
    
    Parámetros:
        cineData (tupla/lista): Datos del cine en formato [nombre, dirección]
            - cineData[0] (string): Nombre del cine
            - cineData[1] (string): Dirección del cine
        cines (dccionario): Diccionario de cines existentes donde:
            - key: ID del cine (string)
            - value: Diccionario con 'nombre' y 'direccion'
    
    Return:
        dccionario: Diccionario de cines actualizado con el nuevo cine agregado
    """
    nuevo_id = str(int(max(cines.keys(), default="0")) + 1)

    cines[nuevo_id] = {"nombre": cineData[0], "direccion": cineData[1]}

    print(f"\nCine agregado con éxito: {cineData[0]} (ID: {nuevo_id})")
    return cines

def imprimirCines(cines):
    """
    Imprime un listado formateado de todos los cines.
    
    Parámetros:
        cines (diccionario): Diccionario de cines donde:
            - key: ID del cine (string)
            - value: Diccionario con:
                - nombre (string): Nombre del cine
                - direccion (string): Dirección del cine
    
    Return:
        None: Solo imprime en consola
    """
    listado = [(cineId, data["nombre"].strip(), data["direccion"].strip()) for cineId, data in cines.items()]
    print("\n--- LISTADO DE CINES ---")
    for cineId, nombre, direccion in listado:
        print(f"ID: {cineId:<3} | Nombre: {nombre:<25} | Dirección: {direccion}")

def imprimirCines(cines):
    listado = [(cineId, data["nombre"].strip(), data["direccion"].strip()) for cineId, data in cines.items()]
    print("\n--- LISTADO DE CINES ---")
    for cineId, nombre, direccion in listado:
        print(f"ID: {cineId:<3} | Nombre: {nombre:<25} | Dirección: {direccion}")

def generarEntrada(datosEntrada, entradas):
    """
    Genera una nueva entrada y la agrega al diccionario de entradas.
    
    Parámetros:
        datosEntrada (diccionario): Datos de la entrada que debe contener:
            - cliente (string): Nombre del cliente
            - dni (string): DNI del cliente
            - cineId (string): ID del cine
            - peliculaId (string): ID de la película
            - salaId (string): ID de la sala
            - butaca (string): Identificación de la butaca (ej: "A1")
        entradas (diccionario): Diccionario de entradas existentes donde:
            - key: ID de la entrada (string)
            - value: Diccionario con datos de la entrada
    
    Return:
        diccionario: Diccionario de entradas actualizado con la nueva entrada
    """
    entradaId = str(len(entradas) + 1)
    entradas[entradaId] = datosEntrada
    return entradas

def eliminarEntrada(entradaId, entradas):
    """
    Elimina una entrada específica del diccionario de entradas.
    
    Parámetros:
        entradaId (string): ID de la entrada a eliminar
        entradas (diccionario): Diccionario de entradas donde:
            - key: ID de la entrada (string)
            - value: Diccionario con datos de la entrada
    
    Return:
        diccionario: Diccionario de entradas actualizado sin la entrada eliminada
    """
    del entradas[entradaId]
    return entradas

def informeVentas(entradas, peliculas, cines):
    """
    Genera un informe detallado de ventas por cine y película.
    
    Parámetros:
        entradas (diccionario): Diccionario de entradas vendidas donde:
            - key: ID de entrada (string)
            - value: Datos de entrada con cineId, peliculaId, etc.
        peliculas (diccionario): Diccionario de películas para obtener títulos
        cines (diccionario): Diccionario de cines para obtener nombres
    
    Return:
        tupla: (informe, ventasGenerales)
            - informe (diccionario): Estructura jerárquica:
                {cineId: {"nombre": string, "entradas": {peliculaId: {"titulo": string, "cantidad": integer}}}}
            - ventasGenerales (integer): Total de entradas vendidas
    """
    informe = {}
    ventasGenerales = 0
    print(entradas)
    for entrada in entradas.values():
        print(entrada)
        cineId = entrada.get("cineId")
        peliculaId = entrada.get("peliculaId")
        if not cines.get(cineId) or not peliculas.get(peliculaId):
            continue
        if cineId not in informe:
            informe[cineId] = {
                "nombre": cines[cineId]["nombre"],
                "entradas": {}
            }
        if peliculaId not in informe[cineId]["entradas"]:
            informe[cineId]["entradas"][peliculaId] = {
                "titulo": peliculas[peliculaId]["titulo"],
                "cantidad": 0
            }
        
        informe[cineId]["entradas"][peliculaId]["cantidad"] += 1
        ventasGenerales += 1

    return informe, ventasGenerales

def informeListadoPeliculasDisponibles(peliculas, cines):
    disponibles = [
                    (peliculaId, data["titulo"].strip(), data["idioma"], data["formato"], ", ".join(cine["nombre"] for cineId, cine in cines.items() if cineId in data.get("complejos", [])))
                    for peliculaId, data in peliculas.items()
                    if data.get("activo", True)
                ]

    if not disponibles:
        print("No hay películas disponibles actualmente.")
        return []

    return disponibles

def informeButacasDisponibles(butacas):
    butacasDisponibles = set([butaca for butaca, disponible in butacas.items() if disponible])
    return butacasDisponibles

def modificarCine(cineId, cineData, cines):
    """
    Modifica los datos de un cine existente.
    
    Parámetros:
        cineId (string): ID del cine a modificar
        cineData (tupla/lista): Nuevos datos del cine en formato [nombre, dirección]
            - cineData[0] (string): Nuevo nombre del cine
            - cineData[1] (string): Nueva dirección del cine
        cines (diccionario): Diccionario de cines a modificar donde:
            - key: ID del cine (string)
            - value: Diccionario con 'nombre' y 'direccion'
    
    Return:
        diccionario: Diccionario de cines actualizado con los nuevos datos
    """
    cineModificado = {
        "nombre": cineData[0],
        "direccion": cineData[1]
    }
    cines[cineId].update(cineModificado)
    return cines

def eliminarCine(cineId, cines):
    del cines[cineId]
    return cines