import json

FORMATOS_VALIDOS = ("2d", "3d")
IDIOMAS_VALIDOS = ("español", "subtitulado")
DIAS_SEMANA = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
TIPOS_BUTACA = ("normal", "extreme")

NUMERACION_FILAS = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
CONFIGURACION_SALA = (8, 8)  # (filas, columnas)
ARCHIVO_PELICULAS = "peliculas.json"
ARCHIVO_CINES = "cines.json"
ARCHIVO_SALAS = "salas.json"
ARCHIVO_FUNCIONES = "funciones.json"
ARCHIVO_ENTRADAS = "entradas.json"

def generarAsientosSala():
    """
    Genera la estructura de asientos para una sala nueva.
    
    Return:
        dict: Diccionario de butacas con configuración por defecto
    """
    butacas = {}
    filas, columnas = CONFIGURACION_SALA
    
    for i in range(filas):
        for j in range(columnas):
            asiento = f"{NUMERACION_FILAS[i]}{j + 1}"
            tipoButaca = "extreme" if i < 2 else "normal"
            butacas[asiento] = {
                "ocupado": False,
                "tipo": tipoButaca,
                "habilitado": True
            }
    
    return butacas

def obtenerPeliculas():
    try:
        with open(ARCHIVO_PELICULAS, mode="r", encoding="UTF-8") as archivoPeliculas:
            peliculas = json.load(archivoPeliculas)
            for pelicula in peliculas.values():
                pelicula["complejos"] = set(pelicula.get("complejos", []))
        return peliculas
    except Exception:
        print("\n⚠️  No se pudieron cargar las películas.")
        return {}
    
def obtenerPelicula(peliculaId):
    try:
        with open(ARCHIVO_PELICULAS, mode="r", encoding="UTF-8") as archivoPeliculas:
            peliculas = json.load(archivoPeliculas)
            pelicula = peliculas.get(peliculaId, {})
            pelicula["complejos"] = set(pelicula.get("complejos", []))
        return pelicula
    except Exception:
        print("\n⚠️  No se pudo cargar la película.")
        return {}

def obtenerCines():
    try:
        with open(ARCHIVO_CINES, mode="r", encoding="UTF-8") as archivoCines:
            cines = json.load(archivoCines)
        return cines
    except Exception:
        print("\n⚠️  No se pudieron cargar los cines.")
        return {}
    
def obtenerCine(cineId):
    try:
        with open(ARCHIVO_CINES, mode="r", encoding="UTF-8") as archivoCines:
            cines = json.load(archivoCines)
            cine = cines.get(cineId, {})
        return cine
    except Exception:
        print("\n⚠️  No se pudo cargar el cine.")
        return {}

def obtenerSalas():
    try:
        with open(ARCHIVO_SALAS, mode="r", encoding="UTF-8") as archivoSalas:
            salas = json.load(archivoSalas)
        return salas
    except Exception:
        print("\n⚠️  No se pudieron cargar las salas.")
        return {}
    
def obtenerSalasPorCine(cineId):
    try:
        with open(ARCHIVO_SALAS, mode="r", encoding="UTF-8") as archivoSalas:
            salas = json.load(archivoSalas)
            salasCine = {salaId: sala for salaId, sala in salas.items() if sala['cineId'] == cineId}
        return salasCine
    except Exception:
        print("\n⚠️  No se pudieron cargar las salas.")
        return {}

def obtenerSala(salaId):
    try:
        with open(ARCHIVO_SALAS, mode="r", encoding="UTF-8") as archivoSalas:
            salas = json.load(archivoSalas)
            sala = salas.get(salaId, {})
        return sala
    except Exception:
        print("\n⚠️  No se pudo cargar la sala.")
        return {}

def obtenerFunciones():
    try:
        with open(ARCHIVO_FUNCIONES, mode="r", encoding="UTF-8") as archivoFunciones:
            funciones = json.load(archivoFunciones)
        return funciones
    except Exception:
        print("\n⚠️  No se pudieron cargar las funciones.")
        return {}

def obtenerFuncion(peliculaId, cineId, salaId, dia, horario):
    try:
        with open(ARCHIVO_FUNCIONES, mode="r", encoding="UTF-8") as archivoFunciones:
            funciones = json.load(archivoFunciones)
            funcion = funciones.get(peliculaId, {}).get(cineId, {}).get(salaId, {}).get(dia, {}).get(horario, {})
        return funcion
    except Exception:
        print("\n⚠️  No se pudo cargar la función.")
        return {}
    
def obtenerFuncionesPorPelicula(peliculaId):
    try:
        with open(ARCHIVO_FUNCIONES, mode="r", encoding="UTF-8") as archivoFunciones:
            funciones = json.load(archivoFunciones)
            return {peliId: cineId for peliId, cineId in funciones.items() if peliId == peliculaId}
    except Exception:
        print("\n⚠️  No se pudieron cargar las funciones.")
        return {}

def obtenerEntradas():
    try:
        with open(ARCHIVO_ENTRADAS, mode="r", encoding="UTF-8") as archivoEntradas:
            entradas = json.load(archivoEntradas)
        return entradas
    except Exception:
        print("\n⚠️  No se pudieron cargar las entradas.")
        return {}

def obtenerEntrada(entradaId):
    try:
        with open(ARCHIVO_ENTRADAS, mode="r", encoding="UTF-8") as archivoEntradas:
            entradas = json.load(archivoEntradas)
            entrada = entradas.get(entradaId, {})
        return entrada
    except Exception:
        print("\n⚠️  No se pudo cargar la entrada.")
        return {}

def imprimirPeliculas():
    """
    Imprime un listado formateado de todas las películas.
    
    Parámetros:
        peliculas (diccionario): Diccionario con las películas
    
    Return:
        None: Solo imprime en consola 
    """
    print("\n--- LISTADO DE PELÍCULAS ---")
    print("-" * 80)
    peliculas = obtenerPeliculas()
    for peliculaId, pelicula in peliculas.items():
        estado = "✓" if pelicula.get('activo', True) else "✗"
        cines_list = ', '.join(pelicula['complejos']) if pelicula['complejos'] else "Sin cines"
        print(f"[{peliculaId}] {pelicula['titulo']} ({estado})")
        print(f"    {pelicula['idioma']} | {pelicula['formato']} | Cines: {cines_list}")

def agregarPelicula(peliculaData):
    """
    Agrega una nueva película al diccionario de películas.
    
    Parámetros:
        peliculaData (diccionario): Datos de la película
        peliculas (diccionario): Diccionario existente de películas
    
    Return:
        string: peliculaId_generado
    """
    peliculas = obtenerPeliculas()
    peliculaId = generarId(peliculas)
    peliculaData["activo"] = True
    peliculas[peliculaId] = peliculaData.copy()
    for pelicula in peliculas.values():
        pelicula["complejos"] = list(pelicula.get("complejos", []))
    with open(ARCHIVO_PELICULAS, mode="w", encoding="UTF-8") as archivoPeliculas:
        json.dump(peliculas, archivoPeliculas, indent=4, ensure_ascii=False)
    return peliculaId

def eliminarSala(salaId):
    salas = obtenerSalas()
    del salas[salaId]
    with open(ARCHIVO_SALAS, mode="w", encoding="UTF-8") as archivoSalas:
        json.dump(salas, archivoSalas, indent=4, ensure_ascii=False)

def modificarPelicula(peliculaId, peliculaData):
    """
    Modifica los datos de una película existente.
    
    Parámetros:
        peliculaId (string): ID de la película a modificar
        peliculaData (diccionario): Nuevos datos de la película
        peliculas (diccionario): Diccionario de películas a modificar

    Returns:
        diccionario: Diccionario de películas actualizado
    """
    try:
        peliculas = obtenerPeliculas()
        peliculas[peliculaId] = peliculaData.copy()
        for pelicula in peliculas.values():
            pelicula["complejos"] = list(pelicula.get("complejos", []))
        with open(ARCHIVO_PELICULAS, mode="w", encoding="UTF-8") as archivoPeliculas:
            json.dump(peliculas, archivoPeliculas, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️  Error al modificar la película: {e}")

def generarId(diccionario):
    """
    Genera un ID único para un nuevo elemento.
    
    Parámetros:
        diccionario (diccionario): Diccionario de elementos existentes
    
    Return:
        string: ID único como string
    """
    if not diccionario:
        return "1"
    nuevoId = max([int(k) for k in diccionario.keys()]) + 1
    return str(nuevoId)

def imprimirSalasPorCine(cineId):
    """
    Imprime las salas pertenecientes a un cine específico.
    
    Parámetros:
        cineId (string): ID del cine
        salas (diccionario): Diccionario de salas
    
    Return:
        None: Solo imprime en consola
    """
    print(f"\n--- SALAS DEL CINE (ID: {cineId}) ---")
    print("-" * 60)
    salas = obtenerSalas()
    salasPorCine = {salaId: sala for salaId, sala in salas.items() if sala['cineId'] == cineId}
    if not salasPorCine:
        print("⚠️  No hay salas registradas para este cine.")
        return
    for salaId, sala in salasPorCine.items():
        totalAsientos = len(sala['asientos'])
        disponibles = len(informeButacasDisponibles(sala['asientos']))
        print(f"[{salaId}] Sala {sala['numeroSala']} | {totalAsientos} asientos | {disponibles} disponibles (plantilla)")

def crearSala(cineId):
    """
    Crea una nueva sala con configuración de butacas predeterminada.
    
    Parámetros:
        cineId (string): ID del cine al que pertenece la sala
        salas (diccionario): Diccionario de salas existente
    
    Return:
        diccionario: Diccionario de salas actualizado
    """
    salas = obtenerSalas()
    salaId = generarId(salas)
    butacas = generarAsientosSala()
    
    salasCine = [sala for sala in salas.values() if sala['cineId'] == cineId]
    if salasCine:
        numeroSala = max([int(sala['numeroSala']) for sala in salasCine]) + 1
    else:
        numeroSala = 1

    salas[salaId] = {
        "cineId": cineId,
        "numeroSala": str(numeroSala),
        "asientos": butacas
    }
    with open(ARCHIVO_SALAS, mode="w", encoding="UTF-8") as archivoSalas:
        json.dump(salas, archivoSalas, indent=4, ensure_ascii=False)

def agregarFunciones(peliculaId, cineId, salaId, dia, horario, butacas):
    """
    Agrega o actualiza una función con su propia copia de butacas.
    """
    funciones = obtenerFunciones()
    if peliculaId not in funciones:
        funciones[peliculaId] = {}
    
    if cineId not in funciones[peliculaId]:
        funciones[peliculaId][cineId] = {}
        
    if salaId not in funciones[peliculaId][cineId]:
        funciones[peliculaId][cineId][salaId] = {}
            
    if dia not in funciones[peliculaId][cineId][salaId]:
        funciones[peliculaId][cineId][salaId][dia] = {}
    
    funciones[peliculaId][cineId][salaId][dia][horario] = {"butacas": butacas}

    with open(ARCHIVO_FUNCIONES, mode="w", encoding="UTF-8") as archivoFunciones:
        json.dump(funciones, archivoFunciones, indent=4, ensure_ascii=False)

def imprimirFunciones():
    """
    Imprime todas las funciones de manera organizada.
    """
    print("\n--- FUNCIONES PROGRAMADAS ---")
    print("=" * 80)
    funciones = obtenerFunciones()
    if not funciones:
        print("⚠️  No hay funciones programadas.")
        return
    peliculas = obtenerPeliculas()
    cines = obtenerCines()
    salas = obtenerSalas()
    for peliculaId, cineIDs in funciones.items():
        peliInfo = peliculas.get(peliculaId, {})
        print(f"\n📽️  {peliInfo.get('titulo', 'Desconocido')} (ID: {peliculaId})")
        print(f"   {peliInfo.get('idioma', '?')} | {peliInfo.get('formato', '?')}")
        print("-" * 80)
        
        for cineId, salaIDs in cineIDs.items():
            cineInfo = cines.get(cineId, {})
            print(f"\n  🏢 {cineInfo.get('nombre', 'Desconocido')} (ID: {cineId})")
            
            for salaId, dias in salaIDs.items():
                salaInfo = salas.get(salaId, {})
                print(f"    🎬 Sala {salaInfo.get('numeroSala', '?')}")
                
                for dia, horariosData in dias.items():
                    horarios_str = ', '.join(sorted(horariosData.keys())) # Extraemos las llaves que son los horarios
                    print(f"       • {dia.capitalize()}: {horarios_str}")

def imprimirFuncionesPorPelicula(peliculaId):
    """
    Imprime todas las funciones de una película específica de manera organizada.
    """
    print(f"\n--- FUNCIONES DE LA PELÍCULA (ID: {peliculaId}) ---")
    print("=" * 80)
    funciones = obtenerFuncionesPorPelicula(peliculaId)
    if not funciones:
        print("⚠️  No hay funciones programadas.")
        return
    peliculas = obtenerPeliculas()
    cines = obtenerCines()
    salas = obtenerSalas()
    for peliculaId, cineIDs in funciones.items():
        peliInfo = peliculas.get(peliculaId, {})
        print(f"\n📽️  {peliInfo.get('titulo', 'Desconocido')} (ID: {peliculaId})")
        print(f"   {peliInfo.get('idioma', '?')} | {peliInfo.get('formato', '?')}")
        print("-" * 80)
        
        for cineId, salaIDs in cineIDs.items():
            cineInfo = cines.get(cineId, {})
            print(f"\n  🏢 {cineInfo.get('nombre', 'Desconocido')} (ID: {cineId})")
            
            for salaId, dias in salaIDs.items():
                salaInfo = salas.get(salaId, {})
                print(f"    🎬 Sala {salaInfo.get('numeroSala', '?')}")
                
                for dia, horariosData in dias.items():
                    horarios_str = ', '.join(sorted(horariosData.keys())) # Extraemos las llaves que son los horarios
                    print(f"       • {dia.capitalize()}: {horarios_str}")


def eliminarFuncionesPorPeliculaCine(peliculaId, cineId, funciones):
    """
    Elimina todas las funciones de una película en un cine específico.
    """
    if peliculaId in funciones and cineId in funciones[peliculaId]:
        del funciones[peliculaId][cineId]
        if not funciones[peliculaId]:
            del funciones[peliculaId]
    return funciones

def eliminarFuncion(peliculaId, cineId, salaId = None, dia = None, horario = None):
    """
    Elimina una función específica o todas las funciones de un cine.
    Si se proporciona solo cineId, elimina todas las funciones de esa película en ese cine.
    Si se proporcionan parámetros adicionales, elimina de forma más específica.
    """
    try:
        funciones = obtenerFunciones()
        
        if peliculaId not in funciones or cineId not in funciones[peliculaId]:
            return funciones, False
        
        if not salaId:
            del funciones[peliculaId][cineId]
        else:
            if not dia:
                if salaId in funciones[peliculaId][cineId]:
                    del funciones[peliculaId][cineId][salaId]
            else:
                if not horario:
                    if salaId in funciones[peliculaId][cineId] and dia in funciones[peliculaId][cineId][salaId]:
                        del funciones[peliculaId][cineId][salaId][dia]
                else:
                    if (salaId in funciones[peliculaId][cineId] and 
                        dia in funciones[peliculaId][cineId][salaId] and
                        horario in funciones[peliculaId][cineId][salaId][dia]):
                        del funciones[peliculaId][cineId][salaId][dia][horario]
                    
                    if not funciones[peliculaId][cineId][salaId][dia]:
                        del funciones[peliculaId][cineId][salaId][dia]
                
                if salaId in funciones[peliculaId][cineId] and not funciones[peliculaId][cineId][salaId]:
                    del funciones[peliculaId][cineId][salaId]
        
        if not funciones[peliculaId][cineId]:
            del funciones[peliculaId][cineId]
        
        if not funciones[peliculaId]:
            del funciones[peliculaId]
        
        with open(ARCHIVO_FUNCIONES, mode="w", encoding="UTF-8") as archivoFunciones:
            json.dump(funciones, archivoFunciones, indent=4, ensure_ascii=False)
        
    except KeyError:
        print("\n⚠️  Error al eliminar la función.")
    except Exception:
        print("\n⚠️  Error al eliminar la función.")

def esHorario(horario):
    """
    Valida si un string tiene formato de horario válido (HH:MM).
    """
    if len(horario) != 5 or horario[2] != ":":
        return False

    try:
        horas, minutos = map(int, horario.split(":"))
        return 0 <= horas < 24 and 0 <= minutos < 60
    except ValueError:
        return False

def peliculasPorCine(cineId):
    """
    Retorna las películas que se proyectan en un cine específico.
    """
    peliculas = obtenerPeliculas()
    return {
        peliculaId: pelicula 
        for peliculaId, pelicula in peliculas.items() 
        if cineId in pelicula.get('complejos', set())
    }

def cinesSinPeliculas(todosCines):
    """
    Retorna conjunto de cines que NO tienen películas asignadas.
    """
    cinesConPeliculas = set()
    peliculas = obtenerPeliculas()
    for pelicula in peliculas.values():
        cinesConPeliculas.update(pelicula.get('complejos', set()))
    return todosCines.difference(cinesConPeliculas)

def peliculasEnTodosCines(cinesRequeridos):
    """
    Retorna películas que se proyectan en TODOS los cines especificados.
    """
    peliculas = obtenerPeliculas()
    return {
        peliculaId: pelicula
        for peliculaId, pelicula in peliculas.items()
        if cinesRequeridos.issubset(pelicula.get('complejos', set()))
    }

def butacasPorTipo(butacas, tipo):
    """
    Retorna conjunto de butacas de un tipo específico.
    """

    return {butaca for butaca, info in butacas.items() if info["tipo"] == tipo}

def butacasDisponiblesPorTipo(asientos, tipo):
    """
    Retorna conjunto de butacas disponibles de un tipo específico.
    """
    butacasTipo = butacasPorTipo(asientos, tipo)
    butacasDisponibles = informeButacasDisponibles(asientos)
    return butacasTipo.intersection(butacasDisponibles)

def butacasOcupadasPorTipo(asientos, tipo):
    """
    Retorna conjunto de butacas ocupadas de un tipo específico.
    """
    butacasTipo = butacasPorTipo(asientos, tipo)
    butacasOcupadas = {butaca for butaca, info in asientos.items() if info["ocupado"]}
    return butacasTipo.intersection(butacasOcupadas)


def obtenerIdiomasDisponibles():
    """
    Retorna conjunto de todos los idiomas disponibles.
    """
    peliculas = obtenerPeliculas()
    return {pelicula['idioma'] for pelicula in peliculas.values() if pelicula.get('activo', True)}

def obtenerFormatosDisponibles():
    """
    Retorna conjunto de todos los formatos disponibles.
    """
    peliculas = obtenerPeliculas()
    return {pelicula['formato'] for pelicula in peliculas.values() if pelicula.get('activo', True)}

def peliculasPorIdiomaYFormato(idioma, formato):
    """
    Filtra películas por idioma Y formato.
    """
    peliculas = obtenerPeliculas()
    resultado = set()
    for pelicula in peliculas.values():
        if (pelicula.get('idioma', '').lower() == idioma.lower() and
            pelicula.get('formato', '').lower() == formato.lower()):
            resultado.add(pelicula)
    return resultado

def cinesConFunciones():
    """
    Retorna conjunto de todos los cines que tienen funciones programadas.
    """
    cinesSet = set()
    funciones = obtenerFunciones()
    for cines in funciones.values():
        cinesSet.update(cines.keys())
    return cinesSet

def diasConFunciones(peliculaId, cineId):
    """
    Retorna conjunto de días con funciones para una película en un cine.
    """
    dias = set()
    funciones = obtenerFunciones()
    try:
        for diasData in funciones[peliculaId][cineId].values():
            dias.update(diasData.keys())
    except KeyError:
        pass
    return dias

def horariosEnDia(peliculaId, cineId, dia):
    """
    Retorna conjunto de todos los horarios en un día específico.
    """
    horarios = set()
    funciones = obtenerFunciones()
    try:
        for salaData in funciones[peliculaId][cineId].values():
            if dia in salaData:
                horarios.update(salaData[dia].keys())
    except KeyError:
        pass
    return horarios

def nuevoCine(cineData):
    """
    Agrega un nuevo cine.
    """
    cines = obtenerCines()
    id = generarId(cines)
    cines[id] = {"nombre": cineData[0], "direccion": cineData[1]}
    with open(ARCHIVO_CINES, mode="w", encoding="UTF-8") as archivoCines:
        json.dump(cines, archivoCines, indent=4, ensure_ascii=False)
    return id

def imprimirCines():
    """
    Imprime un listado formateado de todos los cines.
    """
    cines = obtenerCines()
    print("\n--- LISTADO DE CINES ---")
    print("-" * 80)
    for cineId, data in cines.items():
        nombre = data["nombre"].strip()
        direccion = data["direccion"].strip()
        print(f"[{cineId}] {nombre}")
        print(f"    📍 {direccion}")

def generarEntrada(datosEntrada):
    """
    Genera una nueva entrada.
    """
    entradas = obtenerEntradas()
    entradaId = generarId(entradas)
    entradas[entradaId] = datosEntrada
    with open(ARCHIVO_ENTRADAS, mode="w", encoding="UTF-8") as archivoEntradas:
        json.dump(entradas, archivoEntradas, indent=4, ensure_ascii=False)
    return entradaId

def eliminarEntrada(entradaId):
    """
    Elimina una entrada específica.
    """
    entradas = obtenerEntradas()
    with open(ARCHIVO_ENTRADAS, mode="w", encoding="UTF-8") as archivoEntradas:
        if entradaId in entradas:
            del entradas[entradaId]
        json.dump(entradas, archivoEntradas, indent=4, ensure_ascii=False)


def buscarEntradasPorDNI(dni):
    """
    Busca todas las entradas de un cliente por DNI.
    """
    resultado = []
    entradas = obtenerEntradas()
    peliculas = obtenerPeliculas()
    cines = obtenerCines()
    salas = obtenerSalas()
    for entradaId, entrada in entradas.items():
        if entrada.get('dni') == dni:
            infoEntrada = entrada.copy()
            infoEntrada['entradaId'] = entradaId
            infoEntrada['titulopeli'] = peliculas.get(entrada['peliculaId'], {}).get('titulo', 'Desconocido')
            infoEntrada['nombrecine'] = cines.get(entrada['cineId'], {}).get('nombre', 'Desconocido')
            infoEntrada['numerosala'] = salas.get(entrada['salaId'], {}).get('numeroSala', '?')
            resultado.append(infoEntrada)
    return resultado

def informeVentas():
    """
    Genera un informe detallado de ventas por cine y película.
    """
    informe = {}
    ventasGenerales = 0
    entradas = obtenerEntradas()
    peliculas = obtenerPeliculas()
    cines = obtenerCines()
    
    for entrada in entradas.values():
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

def informeListadoPeliculasDisponibles():
    """
    Genera listado de películas disponibles con sus cines.
    """
    disponibles = []
    peliculas = obtenerPeliculas()
    cines = obtenerCines()
    
    for peliculaId, data in peliculas.items():
        if not data.get("activo", True):
            continue
            
        cinesNombres = [cines[cineId]["nombre"] for cineId in data.get("complejos", []) if cineId in cines]
        cinesString = ", ".join(cinesNombres) if cinesNombres else "Sin cines"
        
        disponibles.append((
            peliculaId,
            data["titulo"].strip(),
            data["idioma"],
            data["formato"],
            cinesString
        ))

    return disponibles

def informeButacasDisponibles(butacas):
    """
    Retorna conjunto de butacas disponibles (no ocupadas y habilitadas).
    """
    return {butaca for butaca, info in butacas.items() 
            if not info["ocupado"] and info["habilitado"]}

def imprimirSala(butacas):
    """
    Imprime la configuración de una sala con el estado de cada butaca.
    """
    filas, columnas = CONFIGURACION_SALA
    print("\n--- MAPA DE LA SALA ---")
    print("  ", end="")
    for j in range(1, columnas + 1):
        print(f"  {j}  ", end="")
    print("\n")
    
    for i in range(filas):
        print(f"{NUMERACION_FILAS[i]} ", end="")
        for j in range(columnas):
            asiento = f"{NUMERACION_FILAS[i]}{j + 1}"
            if asiento in butacas:
                if not butacas[asiento]["habilitado"]:
                    simbolo = "🛠️" # Inhabilitada
                elif butacas[asiento]["ocupado"]:
                    simbolo = "❌" # Ocupada
                else:
                    simbolo = "✅" # Disponible
                tipo = butacas[asiento]["tipo"][0].upper()
                print(f"[{tipo}{simbolo}]", end="")
            else:
                print("[---]", end="")
        print()
    print("\n✅: Disponible | ❌: Ocupada | 🛠️: Inhabilitada")
    print("E: EXTREME | N: NORMAL\n")

def modificarCine(cineId, cineData, cines):
    """
    Modifica los datos de un cine existente.
    """
    try:
        cines = obtenerCines()
        cines[cineId] = cineData.copy()
        with open(ARCHIVO_CINES, mode="w", encoding="UTF-8") as archivoCines:
            json.dump(cines, archivoCines, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️  Error al modificar la película: {e}")

def eliminarCine(cineId):
    """
    Elimina un cine.
    """
    try:
        cines = obtenerCines()
        if cineId in cines:
            del cines[cineId]
        with open(ARCHIVO_CINES, mode="w", encoding="UTF-8") as archivoCines:
            json.dump(cines, archivoCines, indent=4, ensure_ascii=False)
    except Exception:
        print("\n⚠️  Error al eliminar el cine.")

def gestionarFuncionesPelicula(peliculaId):
    """
    Gestiona las funciones de una película (ver, agregar, eliminar).
    """
    while True:
        peliculas = obtenerPeliculas()
        cines = obtenerCines()
        salas = obtenerSalas()
        funciones = obtenerFunciones()
        complejosPelicula = peliculas[peliculaId].get('complejos', set())
        print(f"\nGestionando funciones de: {peliculas[peliculaId]['titulo']}")
        mostrarMenuFunciones()
        opcion = input("\n> Seleccione una opción: ").strip()
        
        if opcion == "0":
            break
            
        elif opcion == "1":  # Ver funciones actuales
            imprimirFuncionesPorPelicula(peliculaId)

        elif opcion == "2":  # Agregar función
            print("\n--- AGREGAR NUEVA FUNCIÓN ---")
            
            if not complejosPelicula:
                print("⚠️  La película no tiene cines asignados.")
                continue
            
            print("\nCines donde se proyecta esta película:")
            for cineId in complejosPelicula:
                if cines.get(cineId):
                    print(f"  [{cineId}] {cines[cineId]['nombre']}")
            
            cineId = input("\nID del cine: ").strip()
            if cineId not in complejosPelicula:
                print("⚠️  Cine no válido.")
                continue
            
            salasCine = {sId: s for sId, s in salas.items() if s['cineId'] == cineId}
            if not salasCine:
                print(f"\n⚠️  No hay salas en el cine '{cines[cineId]['nombre']}'.")
                continue
            
            print(f"\nSalas en {cines[cineId]['nombre']}:")
            imprimirSalasPorCine(cineId)
            
            salaId = input("\nID de la sala: ").strip()
            if salaId not in salasCine:
                print("⚠️  Sala no válida.")
                continue
            
            print(f"\nDías válidos: {', '.join([d.capitalize() for d in DIAS_SEMANA])}")
            dia = input("Día de la función: ").strip().lower()
            if dia not in DIAS_SEMANA:
                print("⚠️  Día no válido.")
                continue
            
            horario = input("Horario (ej. 14:00): ").strip()
            if not esHorario(horario):
                print("⚠️  Horario inválido. Use formato HH:MM")
                continue
            
            try:
                if horario in funciones[peliculaId][cineId][salaId][dia]:
                    print("⚠️  Esta función ya existe.")
                    continue
            except KeyError:
                pass
            
            butacasFuncion = generarAsientosSala()
            agregarFunciones(peliculaId, cineId, salaId, dia, horario, butacasFuncion)
            print(f"\n✓ Función agregada: {dia.capitalize()} {horario} en Sala {salas[salaId]['numeroSala']}")
            
        elif opcion == "3":  # Eliminar función
            if peliculaId not in funciones or not funciones[peliculaId]:
                print("\n⚠️  No hay funciones para eliminar.")
                continue
            
            print("\n--- ELIMINAR FUNCIÓN ---")
            listaFunciones = []
            index = 1
            
            for cineId, salasData in funciones[peliculaId].items():
                for salaId, diasData in salasData.items():
                    for dia, horariosData in diasData.items():
                        for horario in sorted(horariosData.keys()):
                            listaFunciones.append({
                                'cineId': cineId, 'salaId': salaId,
                                'dia': dia, 'horario': horario
                            })
                            print(f"[{index}] {cines.get(cineId,{}).get('nombre','?')} - Sala {salas.get(salaId,{}).get('numeroSala','?')} - {dia.capitalize()} {horario}")
                            index += 1
            
            if not listaFunciones:
                print("⚠️  No hay funciones para eliminar.")
                continue
            
            seleccion = input("\nNúmero de función a eliminar (ENTER para cancelar): ").strip()
            
            if not seleccion.isdigit():
                print("Operación cancelada.")
                continue
            
            indexSeleccionado = int(seleccion) - 1
            
            if not (0 <= indexSeleccionado < len(listaFunciones)):
                print("⚠️  Selección inválida.")
                continue

            funcion = listaFunciones[indexSeleccionado]
            confirmar = input(f"¿Confirma eliminar la función del {funcion['dia']} a las {funcion['horario']}? (s/n): ").strip().lower()

            if confirmar == 's':
                funciones, exito = eliminarFuncion(
                    peliculaId, funcion['cineId'], funcion['salaId'], funcion['dia'], funcion['horario'], funciones
                )
                if exito:
                    print("✓ Función eliminada con éxito.")
                else:
                    print("⚠️  Error al eliminar la función.")

def mostrarMenuFunciones():
    """ Muestra el menú de gestión de funciones. """
    print("\n" + "="*50)
    print("GESTIÓN DE FUNCIONES".center(50))
    print("="*50)
    print("[1] Ver funciones actuales")
    print("[2] Agregar función")
    print("[3] Eliminar función")
    print("[0] Volver")
    print("="*50)