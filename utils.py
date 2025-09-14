FORMATOS_VALIDOS = {"2d", "3d"}
IDIOMAS_VALIDOS = {"español", "subtitulado"}
DIAS_SEMANA = {"lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"}

NUMERACION_FILAS = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
CONFIGURACION_SALA = (9, 8)  # (filas, columnas)

def imprimirPeliculas(peliculas):
    print("\n--- LISTADO DE PELÍCULAS ---")
    for peliculaId, pelicula in peliculas.items():
        print(f"ID: {peliculaId} | Título: {pelicula['titulo']} | Idioma: {pelicula['idioma']} | Formato: {pelicula['formato']} | ID Cines: {', '.join(pelicula['complejos'])}")
    print("\n")

def agregarPelicula(peliculaData, peliculas):
    peliculaId = generarId(peliculas)

    sala = crearSala()

    peliculaData["activo"] = True
    peliculaData["sala"] = sala

    peliculas[peliculaId] = peliculaData.copy()

    return peliculas, peliculaId

def modificarPelicula(peliculaId, peliculaData, peliculas):
    peliculas[peliculaId] = peliculaData.copy()

    return peliculas

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

def imprimirSalasPorCine(cineId, salas):
    print(f"\n--- SALAS DEL CINE ID: {cineId} ---")
    for salaId, sala in salas.items():
        if sala['cineId'] == cineId:
            print(f"ID: {salaId} | Número de Sala: {sala['numeroSala']}")
    print("\n")

def crearSala():
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
    nuevo_id = str(int(max(cines.keys(), default="0")) + 1)

    cines[nuevo_id] = {"nombre": cineData[0], "direccion": cineData[1]}

    print(f"\nCine agregado con éxito: {cineData[0]} (ID: {nuevo_id})")
    return cines

def imprimirCines(cines):
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
    entradaId = str(len(entradas) + 1)
    entradas[entradaId] = datosEntrada
    return entradas

def eliminarEntrada(entradaId, entradas):
    del entradas[entradaId]
    return entradas

def informeVentas(entradas, peliculas, cines):
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
    cineModificado = {
        "nombre": cineData[0],
        "direccion": cineData[1]
    }
    cines[cineId].update(cineModificado)
    return cines

def eliminarCine(cineId, cines):
    del cines[cineId]
    return cines