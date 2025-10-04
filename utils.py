FORMATOS_VALIDOS = ("2d", "3d")
IDIOMAS_VALIDOS = ("español", "subtitulado")
DIAS_SEMANA = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
TIPOS_BUTACA = ("normal", "extreme")

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

    peliculaData["activo"] = True

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
    salasPorCine = {salaId: sala for salaId, sala in salas.items() if sala['cineId'] == cineId}
    if not salasPorCine:
        print("No hay salas registradas para este cine.")
        return
    for salaId, sala in salasPorCine.items():
        print(f"ID: {salaId} | Número de Sala: {sala['numeroSala']}")
    print("\n")

def crearSala(cineId, numeroSala, salas):
    """
    Crea una nueva sala con configuración de butacas predeterminada y la agrega al diccionario de salas.
    
    Parámetros:
        cineId (string): ID del cine al que pertenece la sala
        numeroSala (string): Número o nombre identificador de la sala
        salas (diccionario): Diccionario de salas existente donde:
            - key: ID de la sala (string)
            - value: Diccionario con datos de la sala
    
    Return:
        diccionario: Diccionario de salas actualizado con la nueva sala agregada
    """
    salaId = str(int(max(salas.keys(), default="0")) + 1)
    
    butacas = {}
    filas, columnas = CONFIGURACION_SALA
    
    for i in range(0, filas):
        for j in range(0, columnas):
            asiento = f"{NUMERACION_FILAS[i]}{j + 1}"
            tipoButaca = "extreme" if i < 2 else "normal"
            butacas[asiento] = {
                "ocupado": False,
                "tipo": tipoButaca,
                "habilitado": True
            }
    
    salas[salaId] = {
        "cineId": cineId,
        "numeroSala": numeroSala,
        "asientos": butacas
    }
    
    return salas

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
    """
    Retorna las películas que se proyectan en un cine específico.
    Usa operaciones de conjuntos para verificar pertenencia.
    """
    return {
        peliculaId: pelicula 
        for peliculaId, pelicula in peliculas.items() 
        if cineId in pelicula.get('complejos', set())
    }

def cinesEnComun(cinesIdPeli1, cinesIdPeli2):
    """
    Retorna conjunto de cines donde se proyectan ambas películas.
    Usa intersección de conjuntos.
    
    Parámetros:
        cinesIdPeli1 (set): Conjunto de IDs de cines de película 1
        cinesIdPeli2 (set): Conjunto de IDs de cines de película 2

    Return:
        set: Conjunto de IDs de cines en común
    """
    return cinesIdPeli1.intersection(cinesIdPeli2)

def todosCinesDisponibles(peliculas):
    """
    Retorna conjunto de todos los cines que tienen películas.
    
    Parámetros:
        peliculas (diccionario): Diccionario de películas
    
    Return:
        set: Conjunto con todos los IDs de cines disponibles
    """
    if not peliculas:
        return set()
    result = set()
    for pelicula in peliculas.values():
        result.update(pelicula.get('complejos', set()))
    return result

def cinesSinPeliculas(todosCines, peliculas):
    """
    Retorna conjunto de cines que NO tienen películas asignadas.
    
    Parámetros:
        todosCines (set): Conjunto con todos los IDs de cines existentes
        peliculas (diccionario): Diccionario de películas
    
    Return:
        set: Conjunto de IDs de cines sin películas
    """
    cinesConPeliculas = todosCinesDisponibles(peliculas)
    return todosCines.difference(cinesConPeliculas)

def peliculasEnTodosCines(peliculas, cinesRequeridos):
    """
    Retorna películas que se proyectan en TODOS los cines especificados.
    
    Parámetros:
        peliculas (diccionario): Diccionario de películas
        cinesRequeridos (set): Conjunto de IDs de cines requeridos
    
    Return:
        dict: Diccionario con películas que están en todos los cines requeridos
    """
    return {
        peliculaId: pelicula
        for peliculaId, pelicula in peliculas.items()
        if cinesRequeridos.issubset(pelicula.get('complejos', set()))
    }

def peliculasEnAlgunCine(peliculas, cinesBuscados):
    """
    Retorna películas que se proyectan en AL MENOS uno de los cines especificados.
    
    Parámetros:
        peliculas (diccionario): Diccionario de películas
        cinesBuscados (set): Conjunto de IDs de cines a buscar
    
    Return:
        dict: Diccionario con películas que están en alguno de los cines
    """
    return {
        peliculaId: pelicula
        for peliculaId, pelicula in peliculas.items()
        if pelicula.get('complejos', set()).intersection(cinesBuscados)
    }

def agregarCinesAPelicula(peliculaId, nuevosCines, peliculas):
    """
    Agrega cines a una película usando unión de conjuntos.
    
    Parámetros:
        peliculaId (string): ID de la película
        nuevosCines (set): Conjunto de IDs de cines a agregar
        peliculas (diccionario): Diccionario de películas
    
    Return:
        diccionario: Diccionario de películas actualizado
    """
    if peliculaId in peliculas:
        peliculas[peliculaId]['complejos'] = peliculas[peliculaId].get('complejos', set()).union(nuevosCines)
    return peliculas

def eliminarCinesDePelicula(peliculaId, cinesAEliminar, peliculas):
    """
    Elimina cines de una película usando diferencia de conjuntos.
    
    Parámetros:
        peliculaId (string): ID de la película
        cinesAEliminar (set): Conjunto de IDs de cines a eliminar
        peliculas (diccionario): Diccionario de películas
    
    Return:
        diccionario: Diccionario de películas actualizado
    """
    if peliculaId in peliculas:
        peliculas[peliculaId]['complejos'] = peliculas[peliculaId].get('complejos', set()).difference(cinesAEliminar)
    return peliculas

def butacasPorTipo(sala, tipo):
    """
    Retorna conjunto de butacas de un tipo específico.
    
    Parámetros:
        sala (diccionario): Diccionario de butacas
        tipo (string): Tipo de butaca ("normal" o "extreme")
    
    Return:
        set: Conjunto de IDs de butacas del tipo especificado
    """
    return {butaca for butaca, info in sala.items() if info["tipo"] == tipo}

def butacasDisponiblesPorTipo(sala, tipo):
    """
    Retorna conjunto de butacas disponibles de un tipo específico.
    
    Parámetros:
        sala (diccionario): Diccionario de butacas
        tipo (string): Tipo de butaca ("normal" o "extreme")
    
    Return:
        set: Conjunto de IDs de butacas disponibles del tipo especificado
    """
    butacasTipo = butacasPorTipo(sala, tipo)
    butacasDisponibles = informeButacasDisponibles(sala)
    return butacasTipo.intersection(butacasDisponibles)

def butacasOcupadasPorTipo(sala, tipo):
    """
    Retorna conjunto de butacas ocupadas de un tipo específico.
    
    Parámetros:
        sala (diccionario): Diccionario de butacas
        tipo (string): Tipo de butaca ("normal" o "extreme")
    
    Return:
        set: Conjunto de IDs de butacas ocupadas del tipo especificado
    """
    butacasTipo = butacasPorTipo(sala, tipo)
    butacasDisponibles = informeButacasDisponibles(sala)
    return butacasTipo.difference(butacasDisponibles)

def obtenerIdiomasDisponibles(peliculas):
    """
    Retorna conjunto de todos los idiomas disponibles en las películas.
    
    Parámetros:
        peliculas (diccionario): Diccionario de películas
    
    Return:
        set: Conjunto de idiomas disponibles
    """
    return {pelicula['idioma'] for pelicula in peliculas.values() if pelicula.get('activo', True)}

def obtenerFormatosDisponibles(peliculas):
    """
    Retorna conjunto de todos los formatos disponibles en las películas.
    
    Parámetros:
        peliculas (diccionario): Diccionario de películas
    
    Return:
        set: Conjunto de formatos disponibles
    """
    return {pelicula['formato'] for pelicula in peliculas.values() if pelicula.get('activo', True)}

def peliculasPorIdiomaYFormato(peliculas, idioma, formato):
    """
    Filtra películas por idioma Y formato usando operaciones de conjuntos.
    
    Parámetros:
        peliculas (diccionario): Diccionario de películas
        idioma (string): Idioma a filtrar
        formato (string): Formato a filtrar
    
    Return:
        set: Conjunto de IDs de películas que coinciden
    """
    peliculasPorIdioma = {peliculaId for peliculaId, pelicula in peliculas.items() if pelicula.get('idioma').upper() == idioma.upper()}
    peliculasPorFormato = {peliculaId for peliculaId, pelicula in peliculas.items() if pelicula.get('formato').upper() == formato.upper()}
    return peliculasPorIdioma.intersection(peliculasPorFormato)

def peliculasActivasIds(peliculas):
    """
    Retorna conjunto de IDs de películas activas.
    
    Parámetros:
        peliculas (diccionario): Diccionario de películas
    
    Return:
        set: Conjunto de IDs de películas activas
    """
    return {peliculaId for peliculaId, pelicula in peliculas.items() if pelicula.get('activo', True)}

def peliculasInactivasIds(peliculas):
    """
    Retorna conjunto de IDs de películas inactivas usando diferencia.
    
    Parámetros:
        peliculas (diccionario): Diccionario de películas
    
    Return:
        set: Conjunto de IDs de películas inactivas
    """
    todasPeliculas = set(peliculas.keys())
    activas = peliculasActivasIds(peliculas)
    return todasPeliculas.difference(activas)

def cinesConFunciones(funciones):
    """
    Retorna conjunto de todos los cines que tienen funciones programadas.
    
    Parámetros:
        funciones (diccionario): Diccionario de funciones
    
    Return:
        set: Conjunto de IDs de cines con funciones
    """
    cinesSet = set()
    for cines in funciones.values():
        cinesSet = cinesSet.union(set(cines.keys()))
    return cinesSet

def diasConFunciones(funciones, peliculaId, cineId):
    """
    Retorna conjunto de días con funciones para una película en un cine.
    
    Parámetros:
        funciones (diccionario): Diccionario de funciones
        peliculaId (string): ID de la película
        cineId (string): ID del cine
    
    Return:
        set: Conjunto de días con funciones
    """
    dias = set()
    if peliculaId in funciones and cineId in funciones[peliculaId]:
        for diasData in funciones[peliculaId][cineId].values():
            dias = dias.union(set(diasData.keys()))
    return dias

def horariosEnDia(funciones, peliculaId, cineId, dia):
    """
    Retorna conjunto de todos los horarios en un día específico (todas las salas).
    
    Parámetros:
        funciones (diccionario): Diccionario de funciones
        peliculaId (string): ID de la película
        cineId (string): ID del cine
        dia (string): Día de la semana
    
    Return:
        set: Conjunto de horarios disponibles ese día
    """
    horarios = set()
    if peliculaId in funciones and cineId in funciones[peliculaId]:
        for diasData in funciones[peliculaId][cineId].values():
            if dia in diasData:
                horarios = horarios.union(diasData[dia])
    return horarios

def nuevoCine(cineData, cines):
    """
    Agrega un nuevo cine al diccionario de cines.
    
    Parámetros:
        cineData (tupla/lista): Datos del cine en formato [nombre, dirección]
            - cineData[0] (string): Nombre del cine
            - cineData[1] (string): Dirección del cine
        cines (diccionario): Diccionario de cines existentes donde:
            - key: ID del cine (string)
            - value: Diccionario con 'nombre' y 'direccion'
    
    Return:
        tupla: (cines_actualizado, nuevo_id)
            - cines_actualizado (diccionario): Diccionario de cines actualizado
            - nuevo_id (string): ID del nuevo cine creado
    """
    nuevo_id = str(int(max(cines.keys(), default="0")) + 1)

    cines[nuevo_id] = {"nombre": cineData[0], "direccion": cineData[1]}

    print(f"\nCine agregado con éxito: {cineData[0]} (ID: {nuevo_id})")
    return cines, nuevo_id

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
    """
    Retorna conjunto de butacas disponibles.
    Usa conjuntos para optimizar la búsqueda.
    
    Parámetros:
        butacas (diccionario): Diccionario de butacas donde:
            - key: ID de butaca (string)
            - value: Diccionario con 'ocupado' y 'tipo'
    
    Return:
        set: Conjunto de IDs de butacas disponibles
    """
    return {butaca for butaca, info in butacas.items() if not info["ocupado"] and info["habilitado"]}

def imprimirSala(butacas):
    """
    Imprime la configuración de una sala con el estado de cada butaca.
    
    Parámetros:
        butacas (diccionario): Diccionario de butacas donde:
            - key: ID de butaca (string)
            - value: Diccionario con 'ocupado' y 'tipo'
    
    Return:
        None: Solo imprime en consola
    """
    filas, columnas = CONFIGURACION_SALA
    print("\n--- CONFIGURACIÓN DE SALA ---")
    for i in range(0, filas):
        fila_str = ""
        for j in range(0, columnas):
            asiento = f"{NUMERACION_FILAS[i]}{j + 1}"
            if asiento in butacas:
                estado = "✅"
                if not butacas[asiento]["habilitado"]:
                    estado = "🛠️"
                elif butacas[asiento]["ocupado"]:
                    estado = "❌"
                tipo = butacas[asiento]["tipo"][0].upper()
                fila_str += f"{asiento}({tipo}): {estado} "
            else:
                fila_str += "---- "
        print(fila_str.strip())
    print("✅: Disponible | ❌: Ocupada | 🛠️: Inhabilitada\n")

def modificarCine(cineId, cineData, cines):
    """
    Modifica los datos de un cine existente.
    
    Parámetros:
        cineId (string): ID del cine a modificar
        cineData (diccionario): Nuevos datos del cine
            - cineData["nombre"] (string): Nuevo nombre del cine
            - cineData["direccion"] (string): Nueva dirección del cine
        cines (diccionario): Diccionario de cines a modificar donde:
            - key: ID del cine (string)
            - value: Diccionario con 'nombre' y 'direccion'
    
    Return:
        diccionario: Diccionario de cines actualizado con los nuevos datos
    """
    cines[cineId].update(cineData)
    return cines

def eliminarCine(cineId, cines):
    del cines[cineId]
    return cines