import json
from validaciones import *

FORMATOS_VALIDOS = ("2d", "3d")
IDIOMAS_VALIDOS = ("español", "subtitulado")
DIAS_SEMANA = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
TIPOS_BUTACA = ("normal", "extreme")

NUMERACION_FILAS = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
CONFIGURACION_SALA = (8, 8)
ARCHIVO_PELICULAS = "peliculas.json"
ARCHIVO_CINES = "cines.json"
ARCHIVO_SALAS = "salas.json"
ARCHIVO_FUNCIONES = "funciones.json"
ARCHIVO_ENTRADAS = "entradas.json"
ARCHIVO_PRECIOS = "precios.json"
ARCHIVO_LOG = "errores.log"

def registrarExcepcion(e):
    with open(ARCHIVO_LOG, mode="a", encoding="UTF-8") as archivoLog:
        archivoLog.write(f"Error: {str(e)}\n")

def generarAsientosSala():
    try:
        butacas = {}
        filas, columnas = CONFIGURACION_SALA

        for i in range(filas):
            for j in range(columnas):
                asiento = f"{NUMERACION_FILAS[i]}{j + 1}"
                tipoButaca = "extreme" if i < 2 else "normal"
                butacas[asiento] = {
                    "ocupado": False,
                    "tipo": tipoButaca,
                    "habilitado": True,
                }

        return butacas
    except Exception as e:
        print("\n⚠️  No se pudieron generar los asientos de la sala.")
        registrarExcepcion(e)
        return {}

def obtenerPeliculas():
    try:
        with open(ARCHIVO_PELICULAS, mode="r", encoding="UTF-8") as archivoPeliculas:
            peliculas = json.load(archivoPeliculas)
            for pelicula in peliculas.values():
                pelicula["complejos"] = set(pelicula.get("complejos", []))
        return peliculas
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las películas.")
        registrarExcepcion(e)
        return {}

def obtenerPelicula(peliculaId):
    try:
        with open(ARCHIVO_PELICULAS, mode="r", encoding="UTF-8") as archivoPeliculas:
            peliculas = json.load(archivoPeliculas)
            pelicula = peliculas.get(peliculaId, {})
            pelicula["complejos"] = set(pelicula.get("complejos", []))
        return pelicula
    except Exception as e:
        print("\n⚠️  No se pudo cargar la película.")
        registrarExcepcion(e)
        return {}

def obtenerCines():
    try:
        with open(ARCHIVO_CINES, mode="r", encoding="UTF-8") as archivoCines:
            cines = json.load(archivoCines)
        return cines
    except Exception as e:
        print("\n⚠️  No se pudieron cargar los cines.")
        registrarExcepcion(e)
        return {}

def obtenerCine(cineId):
    try:
        with open(ARCHIVO_CINES, mode="r", encoding="UTF-8") as archivoCines:
            cines = json.load(archivoCines)
            cine = cines.get(cineId, {})
        return cine
    except Exception as e:
        print("\n⚠️  No se pudo cargar el cine.")
        registrarExcepcion(e)
        return {}

def obtenerSalas():
    try:
        with open(ARCHIVO_SALAS, mode="r", encoding="UTF-8") as archivoSalas:
            salas = json.load(archivoSalas)
        return salas
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las salas.")
        registrarExcepcion(e)
        return {}

def obtenerSalasPorCine(cineId):
    try:
        with open(ARCHIVO_SALAS, mode="r", encoding="UTF-8") as archivoSalas:
            salas = json.load(archivoSalas)
            salasCine = {
                salaId: sala
                for salaId, sala in salas.items()
                if sala["cineId"] == cineId
            }
        return salasCine
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las salas.")
        registrarExcepcion(e)
        return {}

def obtenerSala(salaId):
    try:
        with open(ARCHIVO_SALAS, mode="r", encoding="UTF-8") as archivoSalas:
            salas = json.load(archivoSalas)
            sala = salas.get(salaId, {})
        return sala
    except Exception as e:
        print("\n⚠️  No se pudo cargar la sala.")
        registrarExcepcion(e)
        return {}

def obtenerFunciones():
    try:
        with open(ARCHIVO_FUNCIONES, mode="r", encoding="UTF-8") as archivoFunciones:
            funciones = json.load(archivoFunciones)
        return funciones
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las funciones.")
        registrarExcepcion(e)
        return {}

def obtenerFuncion(peliculaId, cineId, salaId, dia, horario):
    try:
        with open(ARCHIVO_FUNCIONES, mode="r", encoding="UTF-8") as archivoFunciones:
            funciones = json.load(archivoFunciones)
            funcion = (
                funciones.get(peliculaId, {})
                .get(cineId, {})
                .get(salaId, {})
                .get(dia, {})
                .get(horario, {})
            )
        return funcion
    except Exception as e:
        print("\n⚠️  No se pudo cargar la función.")
        registrarExcepcion(e)
        return {}

def obtenerFuncionesPorPelicula(peliculaId):
    try:
        with open(ARCHIVO_FUNCIONES, mode="r", encoding="UTF-8") as archivoFunciones:
            funciones = json.load(archivoFunciones)
            return {
                peliId: cineId
                for peliId, cineId in funciones.items()
                if peliId == peliculaId
            }
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las funciones.")
        registrarExcepcion(e)
        return {}

def obtenerEntradas():
    try:
        with open(ARCHIVO_ENTRADAS, mode="r", encoding="UTF-8") as archivoEntradas:
            entradas = json.load(archivoEntradas)
        return entradas
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las entradas.")
        registrarExcepcion(e)
        return {}

def obtenerEntrada(entradaId):
    try:
        with open(ARCHIVO_ENTRADAS, mode="r", encoding="UTF-8") as archivoEntradas:
            entradas = json.load(archivoEntradas)
            entrada = entradas.get(entradaId, {})
        return entrada
    except Exception as e:
        print("\n⚠️  No se pudo cargar la entrada.")
        registrarExcepcion(e)
        return {}

def imprimirPeliculas():
    print("\n--- LISTADO DE PELÍCULAS ---")
    print("-" * 80)
    try:
        peliculas = obtenerPeliculas()
        for peliculaId, pelicula in peliculas.items():
            estado = "✓" if pelicula.get("activo", True) else "✗"
            cines = (
                ", ".join(pelicula["complejos"])
                if pelicula["complejos"]
                else "Sin cines"
            )
            print(f"[{peliculaId}] {pelicula['titulo']} ({estado})")
            print(f"    {pelicula['idioma']} | {pelicula['formato']} | Cines: {cines}")
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las películas.")
        registrarExcepcion(e)

def agregarPelicula(peliculaData):
    try:

        if not validar_titulo(peliculaData.get("titulo", "")):
            print("⚠️  Título inválido")
            return None

        if not validar_formato(peliculaData.get("formato", "")):
            print("⚠️  Formato inválido")
            return None

        if not validar_idioma(peliculaData.get("idioma", ""), IDIOMAS_VALIDOS):
            print("⚠️  Idioma inválido")
            return None

        peliculaData["formato"] = normalizar_formato(peliculaData["formato"])
        peliculaData["idioma"] = normalizar_idioma(peliculaData["idioma"])
        peliculaData["titulo"] = limpiar_entrada(peliculaData["titulo"])

        peliculas = obtenerPeliculas()
        peliculaId = generarId(peliculas)
        peliculaData["activo"] = True
        peliculas[peliculaId] = peliculaData.copy()
        for pelicula in peliculas.values():
            pelicula["complejos"] = list(pelicula.get("complejos", []))
        with open(ARCHIVO_PELICULAS, mode="w", encoding="UTF-8") as archivoPeliculas:
            json.dump(peliculas, archivoPeliculas, indent=4, ensure_ascii=False)
        return peliculaId
    except Exception as e:
        print(f"⚠️  Error al agregar la película: {e}")
        registrarExcepcion(e)
        return None

def eliminarSala(salaId):
    try:
        salas = obtenerSalas()
        del salas[salaId]
        with open(ARCHIVO_SALAS, mode="w", encoding="UTF-8") as archivoSalas:
            json.dump(salas, archivoSalas, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️  Error al eliminar la sala: {e}")
        registrarExcepcion(e)

def modificarPelicula(peliculaId, peliculaData):
    try:
        peliculas = obtenerPeliculas()
        peliculas[peliculaId] = peliculaData.copy()
        for pelicula in peliculas.values():
            pelicula["complejos"] = list(pelicula.get("complejos", []))
        with open(ARCHIVO_PELICULAS, mode="w", encoding="UTF-8") as archivoPeliculas:
            json.dump(peliculas, archivoPeliculas, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️  Error al modificar la película")
        registrarExcepcion(e)

def generarId(diccionario):
    try:
        if not diccionario:
            return "1"
        nuevoId = max([int(k) for k in diccionario.keys()]) + 1
        return str(nuevoId)
    except Exception as e:
        print("\n⚠️  No se pudo generar un ID único.")
        registrarExcepcion(e)
        return "1"

def imprimirSalasPorCine(cineId):
    print(f"\n--- SALAS DEL CINE (ID: {cineId}) ---")
    print("-" * 60)
    try:
        salas = obtenerSalas()
        salasPorCine = {
            salaId: sala for salaId, sala in salas.items() if sala["cineId"] == cineId
        }
        if not salasPorCine:
            print("⚠️  No hay salas registradas para este cine.")
            return
        for salaId, sala in salasPorCine.items():
            totalAsientos = len(sala["asientos"])
            disponibles = len(informeButacasDisponibles(sala["asientos"]))
            print(
                f"[{salaId}] Sala {sala['numeroSala']} | {totalAsientos} asientos | {disponibles} disponibles (plantilla)"
            )
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las salas.")
        registrarExcepcion(e)

def crearSala(cineId):
    try:
        salas = obtenerSalas()
        salaId = generarId(salas)
        butacas = generarAsientosSala()

        salasCine = [sala for sala in salas.values() if sala["cineId"] == cineId]
        if salasCine:
            numeroSala = max([int(sala["numeroSala"]) for sala in salasCine]) + 1
        else:
            numeroSala = 1

        salas[salaId] = {
            "cineId": cineId,
            "numeroSala": str(numeroSala),
            "asientos": butacas,
        }
        with open(ARCHIVO_SALAS, mode="w", encoding="UTF-8") as archivoSalas:
            json.dump(salas, archivoSalas, indent=4, ensure_ascii=False)
    except Exception as e:
        print("\n⚠️  No se pudo crear la sala.")
        registrarExcepcion(e)

def agregarFunciones(peliculaId, cineId, salaId, dia, horario, butacas):
    try:
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
    except Exception as e:
        print("\n⚠️  No se pudo agregar la función.")
        registrarExcepcion(e)

def imprimirFunciones():
    print("\n--- FUNCIONES PROGRAMADAS ---")
    print("=" * 80)
    try:
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
                        horarios_str = ", ".join(
                            sorted(horariosData.keys())
                        )
                        print(f"       • {dia.capitalize()}: {horarios_str}")
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las funciones.")
        registrarExcepcion(e)

def imprimirFuncionesPorPelicula(peliculaId):
    print(f"\n--- FUNCIONES DE LA PELÍCULA (ID: {peliculaId}) ---")
    print("=" * 80)
    try:
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
                        horarios_str = ", ".join(
                            sorted(horariosData.keys())
                        )
                        print(f"       • {dia.capitalize()}: {horarios_str}")
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las funciones.")
        registrarExcepcion(e)

def eliminarFuncion(peliculaId, cineId, salaId=None, dia=None, horario=None):
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
                    if (
                        salaId in funciones[peliculaId][cineId]
                        and dia in funciones[peliculaId][cineId][salaId]
                    ):
                        del funciones[peliculaId][cineId][salaId][dia]
                else:
                    if (
                        salaId in funciones[peliculaId][cineId]
                        and dia in funciones[peliculaId][cineId][salaId]
                        and horario in funciones[peliculaId][cineId][salaId][dia]
                    ):
                        del funciones[peliculaId][cineId][salaId][dia][horario]

                    if not funciones[peliculaId][cineId][salaId][dia]:
                        del funciones[peliculaId][cineId][salaId][dia]

                if (
                    salaId in funciones[peliculaId][cineId]
                    and not funciones[peliculaId][cineId][salaId]
                ):
                    del funciones[peliculaId][cineId][salaId]

        if not funciones[peliculaId][cineId]:
            del funciones[peliculaId][cineId]

        if not funciones[peliculaId]:
            del funciones[peliculaId]

        with open(ARCHIVO_FUNCIONES, mode="w", encoding="UTF-8") as archivoFunciones:
            json.dump(funciones, archivoFunciones, indent=4, ensure_ascii=False)

    except KeyError:
        print("\n⚠️  Error al eliminar la función.")
        registrarExcepcion(e)
    except Exception as e:
        print("\n⚠️  Error al eliminar la función.")
        registrarExcepcion(e)

def esHorario(horario):
    return validar_horario(horario)

def peliculasPorCine(cineId):
    try:
        peliculas = obtenerPeliculas()
        return {
            peliculaId: pelicula
            for peliculaId, pelicula in peliculas.items()
            if cineId in pelicula.get("complejos", set())
        }
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las películas.")
        registrarExcepcion(e)
        return {}

def cinesSinPeliculas(todosCines):
    try:
        cinesConPeliculas = set()
        peliculas = obtenerPeliculas()
        for pelicula in peliculas.values():
            cinesConPeliculas.update(pelicula.get("complejos", set()))
        return todosCines.difference(cinesConPeliculas)
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las películas.")
        registrarExcepcion(e)
        return set()

def peliculasEnTodosCines(cinesRequeridos):
    try:
        peliculas = obtenerPeliculas()
        return {
            peliculaId: pelicula
            for peliculaId, pelicula in peliculas.items()
            if cinesRequeridos.issubset(pelicula.get("complejos", set()))
        }
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las películas.")
        registrarExcepcion(e)
        return {}

def butacasPorTipo(butacas, tipo):

    return {butaca for butaca, info in butacas.items() if info["tipo"] == tipo}

def butacasDisponiblesPorTipo(asientos, tipo):
    butacasTipo = butacasPorTipo(asientos, tipo)
    butacasDisponibles = informeButacasDisponibles(asientos)
    return butacasTipo.intersection(butacasDisponibles)

def butacasOcupadasPorTipo(asientos, tipo):
    butacasTipo = butacasPorTipo(asientos, tipo)
    butacasOcupadas = {butaca for butaca, info in asientos.items() if info["ocupado"]}
    return butacasTipo.intersection(butacasOcupadas)

def obtenerIdiomasDisponibles():
    try:
        peliculas = obtenerPeliculas()
        return {
            pelicula["idioma"]
            for pelicula in peliculas.values()
            if pelicula.get("activo", True)
        }
    except Exception as e:
        print("\n⚠️  No se pudieron cargar los idiomas disponibles.")
        registrarExcepcion(e)
        return set()

def obtenerFormatosDisponibles():
    try:
        peliculas = obtenerPeliculas()
        return {
            pelicula["formato"]
            for pelicula in peliculas.values()
            if pelicula.get("activo", True)
        }
    except Exception as e:
        print("\n⚠️  No se pudieron cargar los formatos disponibles.")
        registrarExcepcion(e)
        return set()

def peliculasPorIdiomaYFormato(idioma, formato):
    try:
        peliculas = obtenerPeliculas()
        resultado = set()
        for pelicula in peliculas.values():
            if (
                pelicula.get("idioma", "").lower() == idioma.lower()
                and pelicula.get("formato", "").lower() == formato.lower()
            ):
                resultado.add(pelicula)
        return resultado
    except Exception as e:
        print("\n⚠️  No se pudieron cargar las películas.")
        registrarExcepcion(e)
        return set()

def cinesConFunciones():
    cinesSet = set()
    funciones = obtenerFunciones()
    for cines in funciones.values():
        cinesSet.update(cines.keys())
    return cinesSet

def diasConFunciones(peliculaId, cineId):
    dias = set()
    funciones = obtenerFunciones()
    try:
        for diasData in funciones[peliculaId][cineId].values():
            dias.update(diasData.keys())
    except KeyError:
        print(
            f"\n⚠️  No se encontraron funciones para la película {peliculaId} en el cine {cineId}."
        )
    return dias

def horariosEnDia(peliculaId, cineId, dia):
    horarios = set()
    funciones = obtenerFunciones()
    try:
        for salaData in funciones[peliculaId][cineId].values():
            if dia in salaData:
                horarios.update(salaData[dia].keys())
    except KeyError:
        print(
            f"\n⚠️  No se encontraron funciones para la película {peliculaId} en el cine {cineId}."
        )
    return horarios

def nuevoCine(cineData):
    try:
        nombre = cineData[0]
        direccion = cineData[1]

        if not validar_nombre_cine(nombre):
            print("⚠️  Nombre de cine inválido")
            return None

        if not validar_direccion(direccion):
            print("⚠️  Dirección inválida. Debe contener calle y número")
            return None

        nombre = limpiar_entrada(nombre)
        direccion = limpiar_entrada(direccion)

        cines = obtenerCines()
        id = generarId(cines)
        cines[id] = {"nombre": nombre, "direccion": direccion}
        with open(ARCHIVO_CINES, mode="w", encoding="UTF-8") as archivoCines:
            json.dump(cines, archivoCines, indent=4, ensure_ascii=False)
        return id
    except Exception as e:
        print("\n⚠️  No se pudo agregar el cine.")
        registrarExcepcion(e)
        return None

def imprimirCines():
    cines = obtenerCines()
    print("\n--- LISTADO DE CINES ---")
    print("-" * 80)
    for cineId, data in cines.items():
        nombre = data["nombre"].strip()
        direccion = data["direccion"].strip()
        print(f"[{cineId}] {nombre}")
        print(f"    📍 {direccion}")

def generarEntrada(datosEntrada):
    try:
        entradas = obtenerEntradas()
        entradaId = generarId(entradas)
        entradas[entradaId] = datosEntrada
        with open(ARCHIVO_ENTRADAS, mode="w", encoding="UTF-8") as archivoEntradas:
            json.dump(entradas, archivoEntradas, indent=4, ensure_ascii=False)
        return entradaId
    except Exception as e:
        print("\n⚠️  No se pudo generar la entrada.")
        registrarExcepcion(e)
        return None

def eliminarEntrada(entradaId):
    try:
        entradas = obtenerEntradas()
        with open(ARCHIVO_ENTRADAS, mode="w", encoding="UTF-8") as archivoEntradas:
            if entradaId in entradas:
                del entradas[entradaId]
            json.dump(entradas, archivoEntradas, indent=4, ensure_ascii=False)
    except Exception as e:
        print("\n⚠️  No se pudo eliminar la entrada.")
        registrarExcepcion(e)

def buscarEntradasPorDNI(dni):
    try:
        entradas = obtenerEntradas()
        resultado = [
            {
                **entrada,
                "entradaId": entradaId,
                "titulopeli": obtenerPelicula(entrada["peliculaId"]).get("titulo", "Desconocido"),
                "nombrecine": obtenerCine(entrada["cineId"]).get("nombre", "Desconocido"),
                "numerosala": obtenerSala(entrada["salaId"]).get("numeroSala", "?"),
            }
            for entradaId, entrada in entradas.items()
            if entrada.get("dni") == dni
        ]
        return resultado
    except Exception as e:
        print("\n⚠️  No se pudo buscar las entradas por DNI.")
        registrarExcepcion(e)
        return []

def informeVentas():
    informe = {}
    ventasGenerales = 0

    entradas = obtenerEntradas()
    peliculas = obtenerPeliculas()
    cines = obtenerCines()
    precios = obtenerPreciosEntradas()

    for entrada in entradas.values():
        cineId = entrada.get("cineId")
        peliculaId = entrada.get("peliculaId")

        if not cines.get(cineId) or not peliculas.get(peliculaId):
            continue

        formato = peliculas[peliculaId].get("formato", "").lower()

        precio = precios.get(formato, 0)

        ventasGenerales += precio

        if cineId not in informe:
            informe[cineId] = {
                "nombre": cines[cineId]["nombre"],
                "entradas": {}
            }

        if peliculaId not in informe[cineId]["entradas"]:
            informe[cineId]["entradas"][peliculaId] = {
                "titulo": peliculas[peliculaId]["titulo"],
                "cantidad": 0,
                "total": 0
            }

        informe[cineId]["entradas"][peliculaId]["cantidad"] += 1
        informe[cineId]["entradas"][peliculaId]["total"] += precio

    return informe, ventasGenerales



def informeListadoPeliculasDisponibles():
    peliculas = obtenerPeliculas()
    cines = obtenerCines()
    disponibles = [
        (
            peliculaId,
            data["titulo"].strip(),
            data["idioma"],
            data["formato"],
            ", ".join([
                cines[cineId]["nombre"]
                for cineId in data.get("complejos", [])
                if cineId in cines
            ]) or "Sin cines",
        )
        for peliculaId, data in peliculas.items()
        if data.get("activo", True)
    ]
    return disponibles

def informeButacasDisponibles(butacas):
    return {
        butaca
        for butaca, info in butacas.items()
        if not info["ocupado"] and info["habilitado"]
    }

def imprimirSala(butacas):
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
                    simbolo = "🛠️"
                elif butacas[asiento]["ocupado"]:
                    simbolo = "❌"
                else:
                    simbolo = "✅"
                tipo = butacas[asiento]["tipo"][0].upper()
                print(f"[{tipo}{simbolo}]", end="")
            else:
                print("[---]", end="")
        print()
    print("\n✅: Disponible | ❌: Ocupada | 🛠️: Inhabilitada")
    print("E: EXTREME | N: NORMAL\n")

def modificarCine(cineId, cineData, cines):
    try:
        cines = obtenerCines()
        cines[cineId] = cineData.copy()
        with open(ARCHIVO_CINES, mode="w", encoding="UTF-8") as archivoCines:
            json.dump(cines, archivoCines, indent=4, ensure_ascii=False)
    except Exception as e:
        registrarExcepcion(e)
        print(f"⚠️  Error al modificar la película")

def eliminarCine(cineId):
    try:
        cines = obtenerCines()
        if cineId in cines:
            del cines[cineId]
        with open(ARCHIVO_CINES, mode="w", encoding="UTF-8") as archivoCines:
            json.dump(cines, archivoCines, indent=4, ensure_ascii=False)
    except Exception as e:
        registrarExcepcion(e)
        print("\n⚠️  Error al eliminar el cine.")

def gestionarFuncionesPelicula(peliculaId):
    while True:
        peliculas = obtenerPeliculas()
        cines = obtenerCines()
        salas = obtenerSalas()
        funciones = obtenerFunciones()
        complejosPelicula = peliculas[peliculaId].get("complejos", set())
        print(f"\nGestionando funciones de: {peliculas[peliculaId]['titulo']}")
        mostrarMenuFunciones()
        opcion = input("\n> Seleccione una opción: ").strip()

        if opcion == "0":
            break

        elif opcion == "1":
            imprimirFuncionesPorPelicula(peliculaId)

        elif opcion == "2":
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

            salasCine = {sId: s for sId, s in salas.items() if s["cineId"] == cineId}
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
            print(
                f"\n✓ Función agregada: {dia.capitalize()} {horario} en Sala {salas[salaId]['numeroSala']}"
            )

        elif opcion == "3":
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
                            listaFunciones.append(
                                {
                                    "cineId": cineId,
                                    "salaId": salaId,
                                    "dia": dia,
                                    "horario": horario,
                                }
                            )
                            print(
                                f"[{index}] {cines.get(cineId, {}).get('nombre', '?')} - Sala {salas.get(salaId, {}).get('numeroSala', '?')} - {dia.capitalize()} {horario}"
                            )
                            index += 1

            if not listaFunciones:
                print("⚠️  No hay funciones para eliminar.")
                continue

            seleccion = input(
                "\nNúmero de función a eliminar (ENTER para cancelar): "
            ).strip()

            if not seleccion.isdigit():
                print("Operación cancelada.")
                continue

            indexSeleccionado = int(seleccion) - 1

            if not (0 <= indexSeleccionado < len(listaFunciones)):
                print("⚠️  Selección inválida.")
                continue

            funcion = listaFunciones[indexSeleccionado]
            confirmar = (
                input(
                    f"¿Confirma eliminar la función del {funcion['dia']} a las {funcion['horario']}? (s/n): "
                )
                .strip()
                .lower()
            )

            if confirmar == "s":
                funciones, exito = eliminarFuncion(
                    peliculaId,
                    funcion["cineId"],
                    funcion["salaId"],
                    funcion["dia"],
                    funcion["horario"],
                    funciones,
                )
                if exito:
                    print("✓ Función eliminada con éxito.")
                else:
                    print("⚠️  Error al eliminar la función.")

def mostrarMenuFunciones():
    print("\n" + "=" * 50)
    print("GESTIÓN DE FUNCIONES".center(50))
    print("=" * 50)
    print("[1] Ver funciones actuales")
    print("[2] Agregar función")
    print("[3] Eliminar función")
    print("[0] Volver")
    print("=" * 50)


def obtenerPrimerasPeliculas(peliculas, cantidad=3):
    """
    Devuelve una lista con los primeros 'cantidad' títulos de películas activas.
    Usa list comprehension y slicing.
    """
    try:
        titulos = [p["titulo"] for p in peliculas.values() if p.get("activo", True)]
        return titulos[:cantidad]
    except Exception as e:
        registrarExcepcion(e)
        return []


def obtenerPeliculasPorFormato(formato_buscado):
    """
    Devuelve las películas que coinciden con el formato indicado (2D o 3D)
    usando filter() y lambda.
    """
    try:
        peliculas = obtenerPeliculas()
        resultado = dict(filter(lambda item: item[1]["formato"].lower() == formato_buscado.lower(), peliculas.items()))
        return resultado
    except Exception as e:
        registrarExcepcion(e)
        return {}


def contarButacasDisponiblesRecursivo(butacas):
    """
    Cuenta recursivamente cuántas butacas están disponibles (no ocupadas y habilitadas).
    Se aplica recursividad.
    """
    if not butacas:
        return 0

    clave, datos = butacas.popitem()
    contador_actual = 1 if not datos["ocupado"] and datos["habilitado"] else 0
    return contador_actual + contarButacasDisponiblesRecursivo(butacas)


def obtenerPreciosEntradas():
    """
    Lee los precios de las entradas desde precios.json.
    Devuelve un diccionario con las claves en minúscula (ej: '2d', '3d').
    Si hay un error, devuelve un diccionario vacío y registra la excepción.
    """
    try:
        with open(ARCHIVO_PRECIOS, mode="r", encoding="UTF-8") as archivoPrecios:
            precios = json.load(archivoPrecios)

        precios_normalizados = {k.lower(): v for k, v in precios.items()}
        return precios_normalizados

    except Exception as e:
        print("\n⚠️  No se pudo cargar el archivo de precios. Se asumirá precio $0.")
        registrarExcepcion(e)
        return {}
