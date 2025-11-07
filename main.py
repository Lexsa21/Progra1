from utils import *
from validaciones import *

MENU_PRINCIPAL = (
    "[1] Gestión de Películas",
    "[2] Venta de Entradas", 
    "[3] Informes Generales",
    "[4] Gestión de Complejo de Cines",
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

MENU_MODIFICACION_PELICULA = (
    "[1] Modificar Título",
    "[2] Modificar Idioma",
    "[3] Modificar Formato",
    "[4] Modificar Complejos",
    "[5] Gestionar Funciones",
    "[0] Guardar"
)

MENU_ENTRADAS = (
    "[1] Generar Entrada",
    "[2] Eliminar Venta",
    "[3] Ver mis entradas (por DNI)",
    "[0] Volver al menú"
)

MENU_INFORMES = (
    "[1] Emitir Informe de Ventas",
    "[2] Emitir Listado de Películas Disponibles",
    "[3] Emitir Informe de Butacas (Plantillas de Salas)",
    "[4] Emitir Informe de Butacas por Tipo (Plantillas de Salas)",
    "[0] Volver al menú"
)

MENU_CINES = (
    "[1] Listar Cines",
    "[2] Agregar Nuevo Cine",
    "[3] Eliminar Cine",
    "[4] Modificar Cine",
    "[5] Modificar Salas de Cine",
    "[6] Películas en común entre dos cines",
    "[7] Cines sin películas asignadas",
    "[8] Películas disponibles en todos los cines seleccionados",
    "[9] Comparar butacas disponibles por tipo (Global)",
    "[10] Análisis de funciones por día",
    "[11] Cines con y sin funciones",
    "[0] Volver al menú"
)

MENU_MODIFICACION_CINE = (
    "[1] Modificar Nombre",
    "[2] Modificar Dirección",
    "[0] Guardar"
)

MENU_MODIFICACION_SALAS = (
    "[1] Listar Salas",
    "[2] Generar nueva Sala",
    "[3] Modificar Sala",
    "[4] Eliminar Sala",
    "[0] Volver"
)

MENU_MODIFICACION_SALA = (
    "[1] Mostrar Sala (Plantilla)",
    "[2] Inhabilitar/Habilitar Butaca (Plantilla)",
    "[0] Volver"
)

MENU_PELICULAS_CINES = (
    "[1] Listar Cines Asignados",
    "[2] Agregar Cine",
    "[3] Eliminar Cine",
    "[0] Continuar"
)

def mostrarMenu(titulo, opciones):
    print("\n" + "="*50)
    print(titulo.center(50))
    print("="*50)
    for opcion in opciones:
        print(opcion)
    print("="*50)

while True:
    mostrarMenu("SISTEMA DE GESTIÓN DE CINE", MENU_PRINCIPAL)
    opcion = input("\n> Seleccione una opción: ").strip()

    if opcion == "0":
        print("\n¡Gracias por usar el sistema! Hasta pronto.")
        break

    elif opcion == "1":
        while True:
            mostrarMenu("GESTIÓN DE PELÍCULAS", MENU_PELICULAS)
            opcionPeliculas = input("\n> Seleccione una opción: ").strip()

            if opcionPeliculas == "0": 
                break

            elif opcionPeliculas == "1":
                print("\n--- AGREGAR NUEVA PELÍCULA ---")
                peliculaData = {}
                peliculaData["titulo"] = input("Título de la película: ").strip()
                while not peliculaData["titulo"]:
                    print("⚠️  El título no puede estar vacío.")
                    peliculaData["titulo"] = input("Título de la película: ").strip()

                print("\nFormatos válidos: 2D, 3D")
                while True:
                    formato_input = input("Formato (2D/3D): ").strip()
                    valido, formato_limpio, error = validar_entrada_completa(
                        formato_input, "formato"
                    )

                    if valido:
                        peliculaData["formato"] = formato_limpio
                        break
                    else:
                        print(f"⚠️  {error}")

                print("\nIdiomas válidos: Español, Subtitulado")
                while True:
                    idioma_input = input("Idioma: ").strip()
                    valido, idioma_limpio, error = validar_entrada_completa(
                        idioma_input, "idioma", idiomas_validos=IDIOMAS_VALIDOS
                    )

                    if valido:
                        peliculaData["idioma"] = idioma_limpio
                        break
                    else:
                        print(f"⚠️  {error}")

                print("\n--- SELECCIÓN DE CINES ---")
                imprimirCines()
                peliculaData["complejos"] = set()

                while True:
                    cineId = input(
                        "\nID del cine (ENTER para finalizar selección): "
                    ).strip()
                    if not cineId:
                        if not peliculaData["complejos"]:
                            print("⚠️  Debe seleccionar al menos un cine.")
                            continue
                        break
                    cine = obtenerCine(cineId)
                    if not cine:
                        print("⚠️  Cine no encontrado.")
                        continue

                    if cineId in peliculaData["complejos"]:
                        print("⚠️  Este cine ya fue agregado.")
                        continue

                    peliculaData["complejos"].add(cineId)
                    print(f"✓ Cine '{cine['nombre']}' agregado")

                peliculaId = agregarPelicula(peliculaData)
                print(
                    f"\n✓ ¡Película '{peliculaData['titulo']}' agregada con éxito! (ID: {peliculaId})"
                )

                respuesta = input("\n¿Desea agregar funciones ahora? (s/n): ").strip()
                confirmacion = validar_confirmacion(respuesta)

                if confirmacion is None:
                    print("⚠️  Respuesta inválida. Se asume 'no'.")
                    confirmacion = False

                if confirmacion:
                    gestionarFuncionesPelicula(peliculaId)

            elif opcionPeliculas == "2":
                print("\n--- MODIFICAR PELÍCULA ---")
                imprimirPeliculas()

                peliculaId = input("\nID de la película a modificar: ").strip()
                try:
                    peliculaExistente = obtenerPelicula(peliculaId)
                except Exception:
                    print("⚠️  Película no encontrada.")
                    continue

                peliculaEditada = peliculaExistente.copy()

                while True:
                    print(f"\nEditando: {peliculaExistente['titulo']}")
                    mostrarMenu(
                        "MODIFICAR DATOS DE LA PELÍCULA", MENU_MODIFICACION_PELICULA
                    )
                    opcionMod = input("\n> Seleccione una opción: ").strip()

                    if opcionMod == "0":
                        if peliculaEditada != peliculaExistente:
                            modificarPelicula(peliculaId, peliculaEditada)
                            print("\n✓ Película modificada con éxito!")
                        break

                    elif opcionMod == "5":
                        gestionarFuncionesPelicula(peliculaId)

            elif opcionPeliculas == "3":
                imprimirPeliculas()

            elif opcionPeliculas == "4":
                imprimirFunciones()

            elif opcionPeliculas == "5":
                print("\n--- PELÍCULAS POR IDIOMA Y FORMATO ---")
                print(
                    f"Idiomas disponibles: {', '.join(sorted(obtenerIdiomasDisponibles()))}"
                )
                print(
                    f"Formatos disponibles: {', '.join(sorted(obtenerFormatosDisponibles()))}"
                )

                idioma = input("\nIdioma: ").strip()
                formato = input("Formato: ").strip()

                pelisResultado = peliculasPorIdiomaYFormato(idioma, formato)

                if pelisResultado:
                    print(
                        f"\nPelículas en '{idioma.capitalize()}' Y formato '{formato.upper()}':"
                    )
                    for pelicula in pelisResultado:
                        print(f"  • {pelicula['titulo']} (ID: {pelicula['id']})")
                else:
                    print(f"\n⚠️  No se encontraron películas con esos criterios.")

            input("\nPresione ENTER para continuar...")

    elif opcion == "2":
        while True:
            mostrarMenu("VENTA DE ENTRADAS", MENU_ENTRADAS)
            opcionEntradas = input("\n> Seleccione una opción: ").strip()

            if opcionEntradas == "0":
                break

            elif opcionEntradas == "1":
                print("\n--- GENERAR NUEVA ENTRADA ---")

                nombreCliente = input("Nombre del cliente: ").strip()
                valido_nombre, nombre_limpio, error_nombre = validar_entrada_completa(
                    nombreCliente, "nombre"
                )

                if not valido_nombre:
                    print(f"⚠️  {error_nombre}")
                    continue

                nombreCliente = nombre_limpio

                dni_input = input("DNI del cliente: ").strip()
                valido_dni, dni_limpio, error_dni = validar_entrada_completa(
                    dni_input, "dni"
                )

                if not valido_dni:
                    print(f"⚠️  {error_dni}")
                    continue

                dniCliente = dni_limpio

                imprimirFunciones()
                idCine = input("\nID del cine: ").strip()
                cine = obtenerCine(idCine)
                if not cine:
                    print("⚠️  Cine no encontrado.")
                    continue

                peliculasEnCine = peliculasPorCine(idCine)
                if not peliculasEnCine:
                    print(f"\n⚠️  No hay películas disponibles en '{cine['nombre']}'.")
                    continue

                print(f"\n--- PELÍCULAS EN {cine['nombre'].upper()} ---")
                peliculasConFunciones = {}
                funciones = obtenerFunciones()
                for peliculaId, pelicula in peliculasEnCine.items():
                    if peliculaId in funciones and idCine in funciones[peliculaId]:
                        peliculasConFunciones[peliculaId] = pelicula
                        print(
                            f"\n[{peliculaId}] {pelicula['titulo']} ({pelicula['formato']} - {pelicula['idioma']})"
                        )
                        print("  Funciones disponibles:")
                        for salaId, diasData in funciones[peliculaId][idCine].items():
                            salaInfo = obtenerSala(salaId)
                            print(
                                f"   [{salaId}] Sala {salaInfo.get('numeroSala', '?')}:"
                            )
                            for dia, horariosData in diasData.items():
                                print(
                                    f"      • {dia.capitalize()}: {', '.join(sorted(horariosData.keys()))}"
                                )

                if not peliculasConFunciones:
                    print(f"\n⚠️  No hay funciones programadas en este cine.")
                    continue

                peliculaId = input("\nID de la película: ").strip()
                if peliculaId not in peliculasConFunciones:
                    print("⚠️  Película no válida.")
                    continue

                salaId = input("\nID de la sala: ").strip()
                diaPelicula = input("Día: ").strip().lower()
                horaPelicula = input("Horario: ").strip()

                try:
                    funcionSeleccionada = funciones[peliculaId][idCine][salaId][
                        diaPelicula
                    ][horaPelicula]
                    asientosFuncion = funcionSeleccionada["butacas"]
                except KeyError:
                    print("⚠️  Función (sala, día u horario) no válida.")
                    continue

                asientosDisponiblesSet = informeButacasDisponibles(asientosFuncion)
                if not asientosDisponiblesSet:
                    print("\n⚠️  No hay butacas disponibles para esta función.")
                    continue

                butacasAComprar = []
                seguirReservandoButacas = "s"
                while seguirReservandoButacas == "s":
                    imprimirSala(asientosFuncion)
                    butaca_input = input("Seleccione una butaca: ").strip()
                    valido, butaca, error = validar_entrada_completa(
                        butaca_input, "butaca"
                    )

                    if not valido:
                        print(f"⚠️  {error}")
                        continue

                    if butaca not in asientosDisponiblesSet:
                        print("⚠️  Butaca no disponible. Por favor seleccione otra.")
                        continue

                    butacasAComprar.append(butaca)
                    asientosDisponiblesSet.remove(butaca)
                    asientosFuncion[butaca]["ocupado"] = True
                    respuesta_butaca = input(
                        "¿Desea reservar otra butaca? (s/n): "
                    ).strip()
                    confirmacion_butaca = validar_confirmacion(respuesta_butaca)

                    if confirmacion_butaca is None:
                        seguirReservandoButacas = "n"
                    else:
                        seguirReservandoButacas = "s" if confirmacion_butaca else "n"

                print("\n--- RESUMEN DE LA COMPRA ---")
                print(
                    f"Película: {pelicula['titulo']}, Butacas: {', '.join(butacasAComprar)}"
                )

                respuesta_compra = input("\n¿Confirmar compra? (s/n): ").strip()
                confirmacion_compra = validar_confirmacion(respuesta_compra)

                if confirmacion_compra is None:
                    print("⚠️  Respuesta inválida. Operación cancelada.")
                    confirmacion_compra = False

                if confirmacion_compra:
                    nuevaEntrada = {
                        "cliente": nombreCliente,
                        "dni": dniCliente,
                        "cineId": idCine,
                        "peliculaId": peliculaId,
                        "salaId": salaId,
                        "butacas": butacasAComprar,
                        "dia": diaPelicula,
                        "horario": horaPelicula,
                    }
                    generarEntrada(nuevaEntrada)
                    print(f"\n✓ ¡Entrada generada con éxito!")
                else:
                    print("\nCompra cancelada.")

            elif opcionEntradas == "2":
                print("\n--- ELIMINAR VENTA ---")
                dniCliente = input("DNI del cliente: ").strip()
                entradasCliente = buscarEntradasPorDNI(dniCliente)

                if not entradasCliente:
                    print(f"\n⚠️  No se encontraron entradas para el DNI {dniCliente}.")
                    continue

                print(f"\n--- ENTRADAS DE {entradasCliente[0]['cliente'].upper()} ---")
                for index, entrada in enumerate(entradasCliente, 1):
                    print(
                        f"[{index}] ID: {entrada['entradaId']} - {entrada['titulopeli']} - Butaca: {entrada['butaca']}"
                    )

                try:
                    seleccion = (
                        int(input("\nNúmero de entrada a eliminar: ").strip()) - 1
                    )
                    if not (0 <= seleccion < len(entradasCliente)):
                        raise ValueError

                    entradaEliminar = entradasCliente[seleccion]

                    respuesta_eliminar = input(
                        f"\n¿Confirma eliminar esta entrada? (s/n): "
                    ).strip()
                    confirmacion_eliminar = validar_confirmacion(respuesta_eliminar)

                    if confirmacion_eliminar is None:
                        print("⚠️  Respuesta inválida. Operación cancelada.")
                        confirmacion_eliminar = False

                    if confirmacion_eliminar:
                        try:
                            funcion = funciones[entradaEliminar["peliculaId"]][
                                entradaEliminar["cineId"]
                            ][entradaEliminar["salaId"]][entradaEliminar["dia"]][
                                entradaEliminar["horario"]
                            ]
                            funcion["butacas"][entradaEliminar["butaca"]]["ocupado"] = (
                                False
                            )
                            eliminarEntrada(entradaEliminar["entradaId"])
                            print("\n✓ Entrada eliminada y butaca liberada.")
                        except KeyError:
                            print(
                                "⚠️ Error: La función asociada a esta entrada ya no existe, solo se eliminará la entrada."
                            )
                            eliminarEntrada(entradaEliminar["entradaId"])
                    else:
                        print("\nOperación cancelada.")
                except (ValueError, IndexError):
                    print("⚠️ Selección inválida.")

            elif opcionEntradas == "3":
                dniCliente = input("\nDNI del cliente: ").strip()
                entradasCliente = buscarEntradasPorDNI(dniCliente)
                if not entradasCliente:
                    print(f"⚠️ No se encontraron entradas para el DNI {dniCliente}.")
                else:
                    print(
                        f"\n--- ENTRADAS DE {entradasCliente[0]['cliente'].upper()} ---"
                    )
                    for ent in entradasCliente:
                        print(
                            f"  • Película: {ent['titulopeli']}, Cine: {ent['nombrecine']}, Sala: {ent['numerosala']}, Butacas: {', '.join(ent['butacas'])}, Día: {ent['dia'].capitalize()}, Horario: {ent['horario']}"
                        )

            input("\nPresione ENTER para continuar...")

    elif opcion == "3":
        while True:
            mostrarMenu("INFORMES GENERALES", MENU_INFORMES)
            opcionInformes = input("\n> Seleccione una opción: ").strip()

            if opcionInformes == "0":
                break

            elif opcionInformes == "1":
                informe, ventasGenerales = informeVentas()
                print("\n--- INFORME DE VENTAS ---")
                for cineId, cineData in informe.items():
                    print(f"\n{cineData['nombre']}")
                    print("-" * 50)
                    for peliculaId, peliculaData in cineData["entradas"].items():
                        print(
                            f"  • {peliculaData['titulo']}: {peliculaData['cantidad']} entradas"
                        )
                print(f"\n{'=' * 50}")
                print(f"TOTAL DE VENTAS: {ventasGenerales} entradas")
                print("=" * 50)

            elif opcionInformes == "2":
                disponibles = informeListadoPeliculasDisponibles()

                if not disponibles:
                    print("\n⚠️  No hay películas disponibles actualmente.")
                else:
                    idiomas = obtenerIdiomasDisponibles()
                    formatos = obtenerFormatosDisponibles()

                    print("\n--- LISTADO DE PELÍCULAS DISPONIBLES ---")
                    print("-" * 80)
                    for peliculaId, titulo, idioma, formato, cines_str in disponibles:
                        print(f"[{peliculaId}] {titulo}")
                        print(f"    Idioma: {idioma} | Formato: {formato}")
                        print(f"    Cines: {cines_str}")
                        print()

                    print(f"Idiomas disponibles: {', '.join(sorted(idiomas))}")
                    print(f"Formatos disponibles: {', '.join(sorted(formatos))}")

            elif opcionInformes == "3":
                salas = obtenerSalas()
                cines = obtenerCines()
                print("\n--- INFORME DE BUTACAS DISPONIBLES POR SALA ---")
                for salaId, sala in salas.items():
                    cineInfo = cines.get(sala["cineId"], {})
                    print(
                        f"\n{cineInfo.get('nombre', 'Desconocido')} - Sala {sala['numeroSala']}"
                    )
                    print("-" * 60)

                    butacasDisponibles = informeButacasDisponibles(sala["asientos"])
                    totalButacas = len(sala["asientos"])
                    ocupadas = totalButacas - len(butacasDisponibles)

                    print(
                        f"Total: {totalButacas} | Disponibles: {len(butacasDisponibles)} | Ocupadas: {ocupadas}"
                    )
                    print()
                    imprimirSala(sala["asientos"])

            elif opcionInformes == "4":
                salas = obtenerSalas()
                cines = obtenerCines()
                print("\n--- INFORME DE BUTACAS POR TIPO ---")
                for salaId, sala in salas.items():
                    cineInfo = cines.get(sala["cineId"], {})
                    print(
                        f"\n{cineInfo.get('nombre', 'Desconocido')} - Sala {sala['numeroSala']}"
                    )
                    print("-" * 60)

                    extremeTotal = butacasPorTipo(sala["asientos"], "extreme")
                    normalTotal = butacasPorTipo(sala["asientos"], "normal")

                    extremeDisponibles = butacasDisponiblesPorTipo(
                        sala["asientos"], "extreme"
                    )
                    normalDisponibles = butacasDisponiblesPorTipo(
                        sala["asientos"], "normal"
                    )

                    extremeOcupadas = butacasOcupadasPorTipo(
                        sala["asientos"], "extreme"
                    )
                    normalOcupadas = butacasOcupadasPorTipo(sala["asientos"], "normal")

                    print(
                        f"EXTREME: {len(extremeTotal)} totales | {len(extremeDisponibles)} disponibles | {len(extremeOcupadas)} ocupadas"
                    )
                    print(
                        f"NORMAL:  {len(normalTotal)} totales | {len(normalDisponibles)} disponibles | {len(normalOcupadas)} ocupadas"
                    )
                    print()
                    imprimirSala(sala["asientos"])

            input("\nPresione ENTER para continuar...")

    elif opcion == "4":
        while True:
            mostrarMenu("GESTIÓN DE COMPLEJO DE CINES", MENU_CINES)
            opcionCines = input("\n> Seleccione una opción: ").strip()

            if opcionCines == "0":
                break

            elif opcionCines == "1":
                imprimirCines()

            elif opcionCines == "2":
                print("\n--- AGREGAR NUEVO CINE ---")
                while True:
                    nombre = input("Nombre del cine: ").strip()
                    nombre = limpiar_entrada(nombre)

                    if not validar_nombre_cine(nombre):
                        print(
                            "⚠️  Nombre inválido. Use solo letras, números y símbolos básicos."
                        )
                        continue

                    break

                while True:
                    direccion = input("Dirección del cine: ").strip()
                    direccion = limpiar_entrada(direccion)

                    if not validar_direccion(direccion):
                        print(
                            "⚠️  Dirección inválida. Debe contener calle y número (ej: Av. Corrientes 1234)."
                        )
                        continue

                    break

                cineData = (nombre, direccion)
                nuevoCineId = nuevoCine(cineData)

                respuesta_salas = input("\n¿Desea crear salas ahora? (s/n): ").strip()
                confirmacion_salas = validar_confirmacion(respuesta_salas)

                if confirmacion_salas is None:
                    confirmacion_salas = False

                if confirmacion_salas:
                    while True:
                        cantidad_input = input("Cantidad de salas a crear: ").strip()

                        if not validar_numero_positivo(cantidad_input):
                            print("⚠️  Ingrese un número entero mayor a 0.")
                            continue

                        cantidadSalas = int(cantidad_input)
                        break

                    cantidadSalas = int(cantidadSalas)
                    for i in range(cantidadSalas):
                        crearSala(nuevoCineId)

                    print(f"\n✓ {cantidadSalas} sala(s) creada(s) con éxito!")

            elif opcionCines == "3":
                print("\n--- ELIMINAR CINE ---")
                imprimirCines()

                cineId = input("\nID del cine a eliminar: ").strip()
                cine = obtenerCine(cineId)
                if not cine:
                    print("⚠️  Cine no encontrado.")
                    input("\nPresione ENTER para continuar...")
                    continue

                print(f"\n⚠️  ADVERTENCIA: Se eliminarán también:")
                print("  • Todas las salas del cine")
                print("  • Todas las funciones del cine")
                print("  • Todas las entradas vendidas para este cine")

                respuesta_confirmar = input(
                    f"\n¿Confirma eliminar '{cine['nombre']}'? (s/n): "
                ).strip()
                confirmacion_eliminar_cine = validar_confirmacion(respuesta_confirmar)

                if confirmacion_eliminar_cine is None:
                    print("⚠️  Respuesta inválida. Operación cancelada.")
                    confirmacion_eliminar_cine = False

                confirmar = "s" if confirmacion_eliminar_cine else "n"
                salas = obtenerSalas()
                funciones = obtenerFunciones()
                entradas = obtenerEntradas()
                peliculas = obtenerPeliculas()
                if confirmar == "s":
                    salasAEliminar = [
                        salaId
                        for salaId, sala in salas.items()
                        if sala["cineId"] == cineId
                    ]
                    for salaId in salasAEliminar:
                        eliminarSala(salaId)
                    for peliculaId in list(funciones.keys()):
                        if cineId in funciones[peliculaId]:
                            eliminarFuncion(peliculaId, cineId)

                    entradasAEliminar = [
                        entId
                        for entId, ent in entradas.items()
                        if ent["cineId"] == cineId
                    ]
                    for entId in entradasAEliminar:
                        eliminarEntrada(entId)

                    for pelicula in peliculas.values():
                        if cineId in pelicula["complejos"]:
                            pelicula["complejos"].remove(cineId)
                            modificarPelicula(pelicula["id"], pelicula)

                    eliminarCine(cineId)
                    print("\n✓ Cine eliminado con éxito!")
                else:
                    print("\nOperación cancelada.")

            elif opcionCines == "4":
                print("\n--- MODIFICAR CINE ---")
                imprimirCines()

                cineId = input("\nID del cine a modificar: ").strip()
                cineExistente = obtenerCine(cineId)

                if not cineExistente:
                    print("⚠️  Cine no encontrado.")
                    input("\nPresione ENTER para continuar...")
                    continue

                cineEditado = cineExistente.copy()

                while True:
                    print(f"\nEditando: {cineExistente['nombre']}")
                    mostrarMenu("MODIFICACIÓN DE CINE", MENU_MODIFICACION_CINE)
                    opcionMod = input("\n> Seleccione una opción: ").strip()

                    if opcionMod == "0":
                        if cineEditado != cineExistente:
                            cines = modificarCine(cineId, cineEditado)
                            print("\n✓ Cine modificado con éxito!")
                        break

                    elif opcionMod == "1":
                        nuevoNombre = input(
                            f"Nuevo nombre (actual: {cineExistente['nombre']}): "
                        ).strip()
                        if nuevoNombre:
                            cineEditado["nombre"] = nuevoNombre
                            print("✓ Nombre actualizado")

                    elif opcionMod == "2":
                        nuevaDireccion = input(
                            f"Nueva dirección (actual: {cineExistente['direccion']}): "
                        ).strip()
                        if nuevaDireccion:
                            cineEditado["direccion"] = nuevaDireccion
                            print("✓ Dirección actualizada")

            elif opcionCines == "5":
                print("\n--- MODIFICAR SALAS DE CINE ---")
                imprimirCines()

                cineId = input("\nID del cine: ").strip()
                cine = obtenerCine(cineId)

                if not cine:
                    print("⚠️  Cine no encontrado.")
                    input("\nPresione ENTER para continuar...")
                    continue

                while True:
                    print(f"\nGestionando salas de: {cine['nombre']}")
                    mostrarMenu("MODIFICACIÓN DE SALAS", MENU_MODIFICACION_SALAS)
                    opcionMod = input("\n> Seleccione una opción: ").strip()

                    if opcionMod == "0":
                        break

                    elif opcionMod == "1":
                        salasCine = obtenerSalasPorCine(cineId)
                        if not salasCine:
                            print("\n⚠️  No hay salas en este cine.")
                        else:
                            imprimirSalasPorCine(cineId)

                    elif opcionMod == "2":
                        salas = crearSala(cineId, salas)
                        print("✓ Sala creada con éxito!")

                    elif opcionMod == "3":
                        salasCine = obtenerSalasPorCine(cineId)
                        if not salasCine:
                            print("\n⚠️  No hay salas en este cine.")
                            continue

                        imprimirSalasPorCine(cineId)
                        salaId = input("\nID de la sala a modificar: ").strip()

                        if salaId not in salasCine:
                            print("⚠️  Sala no encontrada.")
                            continue

                        while True:
                            mostrarMenu("MODIFICACIÓN DE SALA", MENU_MODIFICACION_SALA)
                            opcionSala = input("\n> Seleccione una opción: ").strip()

                            if opcionSala == "0":
                                break

                            elif opcionSala == "1":
                                imprimirSala(salas[salaId]["asientos"])

                            elif opcionSala == "2":
                                imprimirSala(salas[salaId]["asientos"])
                                codigoButaca = (
                                    input("\nCódigo de la butaca: ").strip().upper()
                                )

                                if codigoButaca not in salas[salaId]["asientos"]:
                                    print("⚠️  Butaca no encontrada.")
                                    continue

                                butaca = salas[salaId]["asientos"][codigoButaca]
                                if butaca["ocupado"]:
                                    print(
                                        "⚠️  No se puede modificar una butaca ocupada."
                                    )
                                    continue

                                nuevoEstado = not butaca["habilitado"]
                                butaca["habilitado"] = nuevoEstado
                                estado_texto = (
                                    "habilitada" if nuevoEstado else "inhabilitada"
                                )
                                print(f"✓ Butaca {codigoButaca} {estado_texto}")

                    elif opcionMod == "4":
                        salasCine = {
                            salaId: sala
                            for salaId, sala in salas.items()
                            if sala["cineId"] == cineId
                        }
                        if not salasCine:
                            print("\n⚠️  No hay salas en este cine.")
                            continue

                        imprimirSalasPorCine(cineId)
                        salaId = input("\nID de la sala a eliminar: ").strip()
                        sala = obtenerSala(salaId)
                        if not sala:
                            print("⚠️  Sala no encontrada.")
                            continue

                        tieneFunciones = False
                        for peliFuncs in funciones.values():
                            if cineId in peliFuncs and salaId in peliFuncs[cineId]:
                                tieneFunciones = True
                                break

                        if tieneFunciones:
                            print(
                                "\n⚠️  ADVERTENCIA: Esta sala tiene funciones programadas que serán eliminadas."
                            )

                        confirmar = (
                            input(
                                f"\n¿Confirma eliminar la sala {salas[salaId]['numeroSala']}? (s/n): "
                            )
                            .strip()
                            .lower()
                        )

                        if confirmar == "s":
                            for peliculaId in list(funciones.keys()):
                                if (
                                    cineId in funciones[peliculaId]
                                    and salaId in funciones[peliculaId][cineId]
                                ):
                                    eliminarFuncion(peliculaId, cineId, salaId)

                            entradasElim = [
                                entId
                                for entId, ent in entradas.items()
                                if ent["salaId"] == salaId
                            ]
                            for entId in entradasElim:
                                eliminarEntrada(entId)

                            eliminarSala(salaId)
                            print("✓ Sala eliminada con éxito!")

            elif opcionCines == "6":

                print("\n--- PELÍCULAS EN COMÚN ENTRE DOS CINES ---")
                imprimirCines()

                cine1 = input("\nID del primer cine: ").strip()
                cine2 = input("ID del segundo cine: ").strip()

                cine1 = obtenerCine(cine1)
                cine2 = obtenerCine(cine2)
                if not cine1 or not cine2:
                    print("⚠️  Uno o ambos cines no existen.")
                    input("\nPresione ENTER para continuar...")
                    continue

                if cine1 == cine2:
                    print("⚠️  Debe seleccionar dos cines diferentes.")
                    input("\nPresione ENTER para continuar...")
                    continue

                peliculas1 = peliculasPorCine(cine1)
                peliculas2 = peliculasPorCine(cine2)

                idsComunes = set(peliculas1.keys()) & set(peliculas2.keys())

                if idsComunes:
                    print(
                        f"\nPelículas en común entre '{cine1['nombre']}' y '{cine2['nombre']}':"
                    )
                    print("-" * 60)
                    for pid in sorted(idsComunes):
                        print(f"  • {peliculas[pid]['titulo']} (ID: {pid})")
                else:
                    print(f"\n⚠️  No hay películas en común entre estos cines.")

            elif opcionCines == "7":
                print("\n--- CINES SIN PELÍCULAS ASIGNADAS ---")
                cines = obtenerCines()
                todosCinesSet = set(cines.keys())
                cinesSinPelis = cinesSinPeliculas(todosCinesSet)

                if cinesSinPelis:
                    print("Los siguientes cines NO tienen películas asignadas:")
                    print("-" * 60)
                    for cineId in sorted(cinesSinPelis):
                        print(f"  • {cines[cineId]['nombre']} (ID: {cineId})")
                else:
                    print("✓ Todos los cines tienen al menos una película asignada.")

            elif opcionCines == "8":
                print("\n--- PELÍCULAS EN TODOS LOS CINES SELECCIONADOS ---")
                imprimirCines()

                cinesSeleccionados = set()
                print("\nSeleccione los cines (ENTER sin texto para finalizar)")

                while True:
                    cineId = input(
                        f"ID de cine ({len(cinesSeleccionados)} seleccionados): "
                    ).strip()
                    if not cineId:
                        break
                    cine = obtenerCine(cineId)
                    if not cine:
                        print("⚠️  Cine no encontrado.")
                    elif cineId in cinesSeleccionados:
                        print("⚠️  Este cine ya fue seleccionado.")
                    else:
                        cinesSeleccionados.add(cineId)
                        print(f"✓ '{cine['nombre']}' agregado")

                if not cinesSeleccionados:
                    print("⚠️  No se seleccionaron cines.")
                    input("\nPresione ENTER para continuar...")
                    continue

                pelisEnTodos = peliculasEnTodosCines(cinesSeleccionados)

                if pelisEnTodos:
                    print(
                        f"\nPelículas disponibles en TODOS los {len(cinesSeleccionados)} cines seleccionados:"
                    )
                    print("-" * 60)
                    for pid, peli in pelisEnTodos.items():
                        print(f"  • {peli['titulo']} (ID: {pid})")
                else:
                    print(
                        "\n⚠️  No hay películas disponibles en todos los cines seleccionados."
                    )

            elif opcionCines == "9":
                print("\n--- ANÁLISIS GLOBAL DE BUTACAS POR TIPO ---")

                todasExtremeDisp = set()
                todasNormalDisp = set()
                todasExtremeOcup = set()
                todasNormalOcup = set()

                for salaId, sala in salas.items():
                    extremeDisp = butacasDisponiblesPorTipo(sala["asientos"], "extreme")
                    normalDisp = butacasDisponiblesPorTipo(sala["asientos"], "normal")
                    extremeOcup = butacasOcupadasPorTipo(sala["asientos"], "extreme")
                    normalOcup = butacasOcupadasPorTipo(sala["asientos"], "normal")

                    todasExtremeDisp = todasExtremeDisp | extremeDisp
                    todasNormalDisp = todasNormalDisp | normalDisp
                    todasExtremeOcup = todasExtremeOcup | extremeOcup
                    todasNormalOcup = todasNormalOcup | normalOcup

                print("\nRESUMEN GLOBAL:")
                print("=" * 60)
                print(f"Butacas EXTREME disponibles: {len(todasExtremeDisp)}")
                print(f"Butacas EXTREME ocupadas:    {len(todasExtremeOcup)}")
                print(f"Butacas NORMAL disponibles:  {len(todasNormalDisp)}")
                print(f"Butacas NORMAL ocupadas:     {len(todasNormalOcup)}")

                totalExtreme = len(todasExtremeDisp) + len(todasExtremeOcup)
                totalNormal = len(todasNormalDisp) + len(todasNormalOcup)

                if totalExtreme > 0:
                    porcExtremeOcup = (len(todasExtremeOcup) / totalExtreme) * 100
                    print(f"\nOcupación EXTREME: {porcExtremeOcup:.1f}%")
                if totalNormal > 0:
                    porcNormalOcup = (len(todasNormalOcup) / totalNormal) * 100
                    print(f"Ocupación NORMAL:  {porcNormalOcup:.1f}%")

            elif opcionCines == "10":
                print("\n--- ANÁLISIS DE FUNCIONES POR DÍA ---")
                imprimirPeliculas()

                peliculaId = input("\nID de película: ").strip()

                pelicula = obtenerPelicula(peliculaId)
                if not pelicula:
                    print("⚠️  Película no encontrada.")
                    input("\nPresione ENTER para continuar...")
                    continue

                imprimirCines()
                cineId = input("\nID de cine: ").strip()
                cine = obtenerCine(cineId)
                if not cine:
                    print("⚠️  Cine no encontrado.")
                    input("\nPresione ENTER para continuar...")
                    continue

                diasDisponibles = diasConFunciones(peliculaId, cineId)

                if diasDisponibles:
                    print(
                        f"\nDías con funciones: {', '.join([d.capitalize() for d in sorted(diasDisponibles)])}"
                    )

                    dia = input("\nDía para ver horarios: ").strip().lower()
                    if dia in diasDisponibles:
                        horarios = horariosEnDia(peliculaId, cineId, dia)
                        print(
                            f"\nHorarios el {dia.capitalize()}: {', '.join(sorted(horarios))}"
                        )
                    else:
                        print(f"⚠️  No hay funciones el {dia}.")
                else:
                    print("⚠️  No hay funciones programadas para esta combinación.")

            elif opcionCines == "11":
                print("\n--- ANÁLISIS DE CINES CON/SIN FUNCIONES ---")

                todosCinesSet = set(cines.keys())
                cinesConFunc = cinesConFunciones()
                cinesSinFunc = todosCinesSet - cinesConFunc

                print(f"\nCines CON funciones programadas ({len(cinesConFunc)}):")
                print("-" * 60)
                if cinesConFunc:
                    for cineId in sorted(cinesConFunc):
                        print(f"  • {cines[cineId]['nombre']} (ID: {cineId})")
                else:
                    print("  Ninguno")

                print(f"\nCines SIN funciones programadas ({len(cinesSinFunc)}):")
                print("-" * 60)
                if cinesSinFunc:
                    for cineId in sorted(cinesSinFunc):
                        print(f"  • {cines[cineId]['nombre']} (ID: {cineId})")
                else:
                    print("  Ninguno")

            input("\nPresione ENTER para continuar...")

    else:
        print("\n⚠️  Opción inválida. Por favor intente nuevamente.")