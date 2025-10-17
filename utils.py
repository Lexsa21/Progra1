FORMATOS_VALIDOS = ("2d", "3d")
IDIOMAS_VALIDOS = ("español", "subtitulado")
DIAS_SEMANA = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
TIPOS_BUTACA = ("normal", "extreme")

NUMERACION_FILAS = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
CONFIGURACION_SALA = (8, 8)  # (filas, columnas)

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

def imprimirPeliculas(peliculas):
    """
    Imprime un listado formateado de todas las películas.
    
    Parámetros:
        peliculas (diccionario): Diccionario con las películas
    
    Return:
        None: Solo imprime en consola 
    """
    print("\n--- LISTADO DE PELÍCULAS ---")
    print("-" * 80)
    for peliculaId, pelicula in peliculas.items():
        estado = "✓" if pelicula.get('activo', True) else "✗"
        cines_list = ', '.join(pelicula['complejos']) if pelicula['complejos'] else "Sin cines"
        print(f"[{peliculaId}] {pelicula['titulo']} ({estado})")
        print(f"    {pelicula['idioma']} | {pelicula['formato']} | Cines: {cines_list}")

def agregarPelicula(peliculaData, peliculas):
    """
    Agrega una nueva película al diccionario de películas.
    
    Parámetros:
        peliculaData (diccionario): Datos de la película
        peliculas (diccionario): Diccionario existente de películas
    
    Return:
        tupla: (peliculas_actualizado, peliculaId_generado)
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
        peliculaData (diccionario): Nuevos datos de la película
        peliculas (diccionario): Diccionario de películas a modificar

    Returns:
        diccionario: Diccionario de películas actualizado
    """
    peliculas[peliculaId] = peliculaData.copy()
    return peliculas

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

def imprimirSalasPorCine(cineId, salas):
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
    salasPorCine = {salaId: sala for salaId, sala in salas.items() if sala['cineId'] == cineId}
    if not salasPorCine:
        print("⚠️  No hay salas registradas para este cine.")
        return
    for salaId, sala in salasPorCine.items():
        totalAsientos = len(sala['asientos'])
        disponibles = len(informeButacasDisponibles(sala['asientos']))
        print(f"[{salaId}] Sala {sala['numeroSala']} | {totalAsientos} asientos | {disponibles} disponibles (plantilla)")

def crearSala(cineId, salas):
    """
    Crea una nueva sala con configuración de butacas predeterminada.
    
    Parámetros:
        cineId (string): ID del cine al que pertenece la sala
        salas (diccionario): Diccionario de salas existente
    
    Return:
        diccionario: Diccionario de salas actualizado
    """
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
    
    return salas

# MODIFICADO: La función agregarFunciones ahora maneja la nueva estructura anidada.
def agregarFunciones(peliculaId, cineId, salaId, dia, horario, butacas, funciones):
    """
    Agrega o actualiza una función con su propia copia de butacas.
    """
    if peliculaId not in funciones:
        funciones[peliculaId] = {}
    
    if cineId not in funciones[peliculaId]:
        funciones[peliculaId][cineId] = {}
        
    if salaId not in funciones[peliculaId][cineId]:
        funciones[peliculaId][cineId][salaId] = {}
            
    if dia not in funciones[peliculaId][cineId][salaId]:
        funciones[peliculaId][cineId][salaId][dia] = {}
    
    # Cada horario ahora es un diccionario que contiene las butacas
    funciones[peliculaId][cineId][salaId][dia][horario] = {"butacas": butacas}
    
    return funciones

# MODIFICADO: imprimirFunciones adaptado a la nueva estructura.
def imprimirFunciones(funciones, peliculas, cines, salas):
    """
    Imprime todas las funciones de manera organizada.
    """
    print("\n--- FUNCIONES PROGRAMADAS ---")
    print("=" * 80)
    
    if not funciones:
        print("⚠️  No hay funciones programadas.")
        return
    
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

def eliminarFuncion(peliculaId, cineId, salaId, dia, horario, funciones):
    """
    Elimina una función específica.
    """
    try:
        if horario in funciones[peliculaId][cineId][salaId][dia]:
            del funciones[peliculaId][cineId][salaId][dia][horario]
            
            if not funciones[peliculaId][cineId][salaId][dia]:
                del funciones[peliculaId][cineId][salaId][dia]
            if not funciones[peliculaId][cineId][salaId]:
                del funciones[peliculaId][cineId][salaId]
            if not funciones[peliculaId][cineId]:
                del funciones[peliculaId][cineId]
            if not funciones[peliculaId]:
                del funciones[peliculaId]
            
            return funciones, True
    except KeyError:
        pass
    
    return funciones, False

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

def peliculasPorCine(peliculas, cineId):
    """
    Retorna las películas que se proyectan en un cine específico.
    """
    return {
        peliculaId: pelicula 
        for peliculaId, pelicula in peliculas.items() 
        if cineId in pelicula.get('complejos', set())
    }

def cinesSinPeliculas(todosCines, peliculas):
    """
    Retorna conjunto de cines que NO tienen películas asignadas.
    """
    cinesConPeliculas = set()
    for pelicula in peliculas.values():
        cinesConPeliculas.update(pelicula.get('complejos', set()))
    return todosCines.difference(cinesConPeliculas)

def peliculasEnTodosCines(peliculas, cinesRequeridos):
    """
    Retorna películas que se proyectan en TODOS los cines especificados.
    """
    return {
        peliculaId: pelicula
        for peliculaId, pelicula in peliculas.items()
        if cinesRequeridos.issubset(pelicula.get('complejos', set()))
    }

def butacasPorTipo(asientos, tipo):
    """
    Retorna conjunto de butacas de un tipo específico.
    """
    return {butaca for butaca, info in asientos.items() if info["tipo"] == tipo}

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


def obtenerIdiomasDisponibles(peliculas):
    """
    Retorna conjunto de todos los idiomas disponibles.
    """
    return {pelicula['idioma'] for pelicula in peliculas.values() if pelicula.get('activo', True)}

def obtenerFormatosDisponibles(peliculas):
    """
    Retorna conjunto de todos los formatos disponibles.
    """
    return {pelicula['formato'] for pelicula in peliculas.values() if pelicula.get('activo', True)}

def peliculasPorIdiomaYFormato(peliculas, idioma, formato):
    """
    Filtra películas por idioma Y formato.
    """
    resultado = set()
    for peliculaId, pelicula in peliculas.items():
        if (pelicula.get('idioma', '').lower() == idioma.lower() and 
            pelicula.get('formato', '').lower() == formato.lower()):
            resultado.add(peliculaId)
    return resultado

def cinesConFunciones(funciones):
    """
    Retorna conjunto de todos los cines que tienen funciones programadas.
    """
    cinesSet = set()
    for cines in funciones.values():
        cinesSet.update(cines.keys())
    return cinesSet

def diasConFunciones(funciones, peliculaId, cineId):
    """
    Retorna conjunto de días con funciones para una película en un cine.
    """
    dias = set()
    try:
        for diasData in funciones[peliculaId][cineId].values():
            dias.update(diasData.keys())
    except KeyError:
        pass
    return dias

def horariosEnDia(funciones, peliculaId, cineId, dia):
    """
    Retorna conjunto de todos los horarios en un día específico.
    """
    horarios = set()
    try:
        for salaData in funciones[peliculaId][cineId].values():
            if dia in salaData:
                horarios.update(salaData[dia].keys())
    except KeyError:
        pass
    return horarios

def nuevoCine(cineData, cines):
    """
    Agrega un nuevo cine.
    """
    nuevo_id = generarId(cines)
    cines[nuevo_id] = {"nombre": cineData[0], "direccion": cineData[1]}
    return cines, nuevo_id

def imprimirCines(cines):
    """
    Imprime un listado formateado de todos los cines.
    """
    print("\n--- LISTADO DE CINES ---")
    print("-" * 80)
    for cineId, data in cines.items():
        nombre = data["nombre"].strip()
        direccion = data["direccion"].strip()
        print(f"[{cineId}] {nombre}")
        print(f"    📍 {direccion}")

def generarEntrada(datosEntrada, entradas):
    """
    Genera una nueva entrada.
    """
    entradaId = generarId(entradas)
    entradas[entradaId] = datosEntrada
    return entradas

def eliminarEntrada(entradaId, entradas):
    """
    Elimina una entrada específica.
    """
    if entradaId in entradas:
        del entradas[entradaId]
    return entradas

def buscarEntradasPorDNI(dni, entradas, peliculas, cines, salas):
    """
    Busca todas las entradas de un cliente por DNI.
    """
    resultado = []
    for entradaId, entrada in entradas.items():
        if entrada.get('dni') == dni:
            info_entrada = entrada.copy()
            info_entrada['entradaId'] = entradaId
            info_entrada['titulopeli'] = peliculas.get(entrada['peliculaId'], {}).get('titulo', 'Desconocido')
            info_entrada['nombrecine'] = cines.get(entrada['cineId'], {}).get('nombre', 'Desconocido')
            info_entrada['numerosala'] = salas.get(entrada['salaId'], {}).get('numeroSala', '?')
            resultado.append(info_entrada)
    return resultado

def informeVentas(entradas, peliculas, cines):
    """
    Genera un informe detallado de ventas por cine y película.
    """
    informe = {}
    ventasGenerales = 0
    
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

def informeListadoPeliculasDisponibles(peliculas, cines):
    """
    Genera listado de películas disponibles con sus cines.
    """
    disponibles = []
    
    for peliculaId, data in peliculas.items():
        if not data.get("activo", True):
            continue
            
        cines_nombres = [cines[cineId]["nombre"] for cineId in data.get("complejos", []) if cineId in cines]
        cines_str = ", ".join(cines_nombres) if cines_nombres else "Sin cines"
        
        disponibles.append((
            peliculaId,
            data["titulo"].strip(),
            data["idioma"],
            data["formato"],
            cines_str
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
    cines[cineId].update(cineData)
    return cines

def eliminarCine(cineId, cines):
    """
    Elimina un cine.
    """
    if cineId in cines:
        del cines[cineId]
    return cines

def gestionarFuncionesPelicula(peliculaId, complejosPelicula, peliculas, cines, salas, funciones):
    """
    Gestiona las funciones de una película (ver, agregar, eliminar).
    """
    while True:
        print(f"\nGestionando funciones de: {peliculas[peliculaId]['titulo']}")
        mostrarMenuFunciones()
        opcion = input("\n> Seleccione una opción: ").strip()
        
        if opcion == "0":
            break
            
        elif opcion == "1":  # Ver funciones actuales
            imprimirFunciones({peliculaId: funciones.get(peliculaId, {})}, peliculas, cines, salas)
                            
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
            imprimirSalasPorCine(cineId, salas)
            
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
            
            butacas_funcion = generarAsientosSala()
            funciones = agregarFunciones(peliculaId, cineId, salaId, dia, horario, butacas_funcion, funciones)
            print(f"\n✓ Función agregada: {dia.capitalize()} {horario} en Sala {salas[salaId]['numeroSala']}")
            
        elif opcion == "3":  # Eliminar función
            if peliculaId not in funciones or not funciones[peliculaId]:
                print("\n⚠️  No hay funciones para eliminar.")
                continue
            
            print("\n--- ELIMINAR FUNCIÓN ---")
            listaFunciones = []
            idx = 1
            
            for cineId, salasData in funciones[peliculaId].items():
                for salaId, diasData in salasData.items():
                    for dia, horariosData in diasData.items():
                        for horario in sorted(horariosData.keys()):
                            listaFunciones.append({
                                'cineId': cineId, 'salaId': salaId,
                                'dia': dia, 'horario': horario
                            })
                            print(f"[{idx}] {cines.get(cineId,{}).get('nombre','?')} - Sala {salas.get(salaId,{}).get('numeroSala','?')} - {dia.capitalize()} {horario}")
                            idx += 1
            
            if not listaFunciones:
                print("⚠️  No hay funciones para eliminar.")
                continue
            
            seleccion = input("\nNúmero de función a eliminar (ENTER para cancelar): ").strip()
            
            if not seleccion.isdigit():
                print("Operación cancelada.")
                continue
            
            idx_sel = int(seleccion) - 1
            
            if not (0 <= idx_sel < len(listaFunciones)):
                print("⚠️  Selección inválida.")
                continue
            
            func = listaFunciones[idx_sel]
            confirmar = input(f"¿Confirma eliminar la función del {func['dia']} a las {func['horario']}? (s/n): ").strip().lower()
            
            if confirmar == 's':
                funciones, exito = eliminarFuncion(
                    peliculaId, func['cineId'], func['salaId'], func['dia'], func['horario'], funciones
                )
                if exito:
                    print("✓ Función eliminada con éxito.")
                else:
                    print("⚠️  Error al eliminar la función.")
    
    return funciones

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