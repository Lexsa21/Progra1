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
                            try:
                                # Asegurar que 'complejos' sea serializable a JSON (lista)
                                if "complejos" in peliculaEditada and isinstance(
                                    peliculaEditada["complejos"], set
                                ):
                                    peliculaEditada["complejos"] = list(
                                        peliculaEditada["complejos"]
                                    )
                                modificarPelicula(peliculaId, peliculaEditada)

                                # Verificar que se guardó correctamente
                                pelicula_guardada = obtenerPelicula(peliculaId)
                                guardado_ok = True
                                # comparar campos relevantes
                                for key in ("titulo", "idioma", "formato"):
                                    if peliculaEditada.get(key) and peliculaEditada.get(key) != pelicula_guardada.get(
                                        key
                                    ):
                                        guardado_ok = False
                                # comparar complejos (ambos normalizados a conjuntos)
                                orig_complejos = set(peliculaEditada.get("complejos", []))
                                guard_complejos = set(pelicula_guardada.get("complejos", []))
                                if orig_complejos != guard_complejos:
                                    guardado_ok = False

                                if guardado_ok:
                                    print("\n✓ Película modificada con éxito!")
                                else:
                                    print(
                                        "\n⚠️  La película se guardó, pero la verificación no coincide."
                                    )
                            except Exception as e:
                                print(f"\n⚠️  No se pudo guardar la película: {e}")
                        break

                    elif opcionMod == "5":
                        gestionarFuncionesPelicula(peliculaId)

                    elif opcionMod == "1":
                        # Modificar título
                        nuevoTitulo = input(
                            f"Nuevo título (actual: {peliculaExistente.get('titulo', '')}): "
                        ).strip()
                        if nuevoTitulo:
                            valido, titulo_limpio, err = validar_entrada_completa(
                                nuevoTitulo, "titulo"
                            )
                            if valido:
                                peliculaEditada["titulo"] = titulo_limpio
                                print("✓ Título actualizado")
                            else:
                                print(f"⚠️  {err}")

                    elif opcionMod == "2":
                        # Modificar idioma
                        print("\nIdiomas válidos: Español, Subtitulado")
                        nuevoIdioma = input(
                            f"Nuevo idioma (actual: {peliculaExistente.get('idioma', '')}): "
                        ).strip()
                        if nuevoIdioma:
                            valido, idioma_limpio, err = validar_entrada_completa(
                                nuevoIdioma, "idioma", idiomas_validos=IDIOMAS_VALIDOS
                            )
                            if valido:
                                peliculaEditada["idioma"] = idioma_limpio
                                print("✓ Idioma actualizado")
                            else:
                                print(f"⚠️  {err}")

                    elif opcionMod == "3":
                        # Modificar formato
                        print("\nFormatos válidos: 2D, 3D")
                        nuevoFormato = input(
                            f"Nuevo formato (actual: {peliculaExistente.get('formato', '')}): "
                        ).strip()
                        if nuevoFormato:
                            valido, formato_limpio, err = validar_entrada_completa(
                                nuevoFormato, "formato"
                            )
                            if valido:
                                peliculaEditada["formato"] = formato_limpio
                                print("✓ Formato actualizado")
                            else:
                                print(f"⚠️  {err}")

                    elif opcionMod == "4":
                        # Modificar complejos (cines asignados)
                        while True:
                            mostrarMenu("GESTIÓN DE CINES ASIGNADOS", MENU_PELICULAS_CINES)
                            opcionCines = input("\n> Seleccione una opción: ").strip()
                            if opcionCines == "0":
                                break
                            elif opcionCines == "1":
                                if not peliculaEditada.get("complejos"):
                                    print("\n⚠️  No hay cines asignados a esta película.")
                                else:
                                    print("\nCines asignados:")
                                    for cid in sorted(peliculaEditada.get("complejos", [])):
                                        cine = obtenerCine(cid)
                                        nombre = cine.get("nombre", "Desconocido") if cine else "Desconocido"
                                        print(f"  • {nombre} (ID: {cid})")
                            elif opcionCines == "2":
                                imprimirCines()
                                cineIdAgregar = input("\nID del cine a agregar: ").strip()
                                cine = obtenerCine(cineIdAgregar)
                                if not cine:
                                    print("⚠️  Cine no encontrado.")
                                elif cineIdAgregar in peliculaEditada.get("complejos", set()):
                                    print("⚠️  Este cine ya está asignado a la película.")
                                else:
                                    peliculaEditada.setdefault("complejos", set()).add(cineIdAgregar)
                                    print(f"✓ Cine '{cine['nombre']}' agregado")
                            elif opcionCines == "3":
                                if not peliculaEditada.get("complejos"):
                                    print("⚠️  No hay cines para eliminar.")
                                    continue
                                print("\nCines asignados:")
                                for cid in sorted(peliculaEditada.get("complejos", [])):
                                    cine = obtenerCine(cid)
                                    nombre = cine.get("nombre", "Desconocido") if cine else "Desconocido"
                                    print(f"  • {nombre} (ID: {cid})")
                                cineIdEliminar = input("\nID del cine a eliminar: ").strip()
                                if cineIdEliminar not in peliculaEditada.get("complejos", set()):
                                    print("⚠️  Cine no asignado a la película.")
                                else:
                                    peliculaEditada["complejos"].remove(cineIdEliminar)
                                    print("✓ Cine eliminado")
                            else:
                                print("⚠️  Opción inválida. Intente nuevamente.")

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

                cines = obtenerCines()
                print("\n--- CINES DISPONIBLES ---")
                for cid, cinfo in cines.items():
                    print(f"[{cid}] {cinfo['nombre']} – {cinfo['direccion']}")
                idCine = input("\nSeleccione el ID del cine: ").strip()
                cine = cines.get(idCine)
                if not cine:
                    print("⚠️  Cine no encontrado.")
                    continue

                peliculasEnCine = peliculasPorCine(idCine)
                funciones = obtenerFunciones()

                peliculasConFunciones = {
                    pid: peli for pid, peli in peliculasEnCine.items()
                    if pid in funciones and idCine in funciones[pid]
                }

                if not peliculasConFunciones:
                    print(f"\n⚠️  No hay películas disponibles en el cine '{cine['nombre']}'.")
                    continue

                print(f"\n--- CARTELERA EN {cine['nombre']} ---")
                for pid, peli in peliculasConFunciones.items():
                    print(f"[{pid}] 🎬 {peli['titulo']} ({peli['formato']} - {peli['idioma']})")

                peliculaId = input("\nSeleccione el ID de la película: ").strip()
                if peliculaId not in peliculasConFunciones:
                    print("⚠️  Película no válida.")
                    continue
                pelicula = peliculasConFunciones[peliculaId]

                print(f"\n--- FUNCIONES DISPONIBLES DE '{pelicula['titulo']}' ---")
                funcionesDisponibles = []
                for salaId, diasData in funciones[peliculaId][idCine].items():
                    sala = obtenerSala(salaId)
                    for dia, horariosData in diasData.items():
                        for horario in sorted(horariosData.keys()):
                            funcionesDisponibles.append((salaId, dia, horario))
                            print(f"[{len(funcionesDisponibles)}] Sala {sala['numeroSala']} – {dia.capitalize()} {horario}")

                if not funcionesDisponibles:
                    print("⚠️  No hay funciones disponibles para esta película.")
                    continue

                seleccion = input("\nSeleccione el número de función: ").strip()
                if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(funcionesDisponibles)):
                    print("⚠️  Selección inválida.")
                    continue

                salaId, diaPelicula, horaPelicula = funcionesDisponibles[int(seleccion) - 1]
                funcionSeleccionada = funciones[peliculaId][idCine][salaId][diaPelicula][horaPelicula]
                asientosFuncion = funcionSeleccionada["butacas"]

                asientosDisponibles = informeButacasDisponibles(asientosFuncion)
                if not asientosDisponibles:
                    print("\n⚠️  No hay butacas disponibles para esta función.")
                    continue

                print("\n--- SELECCIÓN DE BUTACAS ---")
                imprimirSala(asientosFuncion)
                print("✅ Disponible | ❌ Ocupada | 🛠️ Inhabilitada")


                butacasValidas = []
                while True:
                    butacas_input = input("\nIngrese las butacas a reservar (separadas por coma, ENTER para finalizar): ").strip()
                    if not butacas_input:
                        if butacasValidas:
                            break
                        else:
                            print("⚠️  Debe seleccionar al menos una butaca.")
                            continue
                    butacasAComprar = [b.strip().upper() for b in butacas_input.split(",") if b.strip()]
                    alguna_valida = False
                    for butaca in butacasAComprar:
                        valido, butacaValida, error = validar_entrada_completa(butaca, "butaca")
                        if not valido:
                            print(f"⚠️  {error}")
                            continue
                        if butacaValida not in asientosDisponibles:
                            print(f"⚠️  La butaca {butacaValida} no está disponible.")
                            continue
                        asientosFuncion[butacaValida]["ocupado"] = True
                        butacasValidas.append(butacaValida)
                        alguna_valida = True
                    if not alguna_valida:
                        respuesta = input("¿Desea intentar seleccionar otra butaca? (s/n): ").strip()
                        confirmacion = validar_confirmacion(respuesta)
                        if not confirmacion:
                            print("Operación cancelada.")
                            butacasValidas = []
                            break

                precio_unitario = 2500
                total = precio_unitario * len(butacasValidas)

                print("\n🎟️  RESUMEN DE COMPRA")
                print("-" * 50)
                print(f"Cliente: {nombreCliente} (DNI {dniCliente})")
                print(f"Cine: {cine['nombre']}")
                print(f"Película: {pelicula['titulo']}")
                print(f"Sala: {obtenerSala(salaId)['numeroSala']}")
                print(f"Horario: {diaPelicula.capitalize()} {horaPelicula}")
                print(f"Butacas: {', '.join(butacasValidas)}")
                print(f"Precio unitario: ${precio_unitario}")
                print(f"Total a pagar: ${total}")
                print("-" * 50)

                respuesta_compra = input("¿Confirmar compra? (s/n): ").strip()
                confirmacion_compra = validar_confirmacion(respuesta_compra)

                if confirmacion_compra:
                    nuevaEntrada = {
                        "cliente": nombreCliente,
                        "dni": dniCliente,
                        "cineId": idCine,
                        "peliculaId": peliculaId,
                        "salaId": salaId,
                        "butacas": butacasValidas,
                        "dia": diaPelicula,
                        "horario": horaPelicula,
                        "precio_unitario": precio_unitario,
                        "total": total,
                    }
                    generarEntrada(nuevaEntrada)
                    import json
                    from utils import ARCHIVO_FUNCIONES
                    with open(ARCHIVO_FUNCIONES, mode="r", encoding="utf-8") as f:
                        funciones = json.load(f)
                    for butaca in butacasValidas:
                        funciones[peliculaId][idCine][salaId][diaPelicula][horaPelicula]["butacas"][butaca]["ocupado"] = True
                    with open(ARCHIVO_FUNCIONES, mode="w", encoding="utf-8") as f:
                        json.dump(funciones, f, indent=4, ensure_ascii=False)
                    print(f"\n✅ ¡Entrada generada con éxito!\n")
                else:
                    print("\n⚠️  Compra cancelada.")

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
                            f"  • Película: {ent['titulopeli']}, Cine: {ent['nombrecine']}, Sala: {ent['numerosala']}, Butacas: {', '.join(ent.get('butacas', []))}, Día: {ent['dia'].capitalize()}, Horario: {ent['horario']}"
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

                total_entradas = 0

                for cineId, cineData in informe.items():
                    print(f"\n{cineData['nombre']}")
                    print("-" * 50)

                    for peliculaId, peliculaData in cineData["entradas"].items():
                        cantidad = peliculaData["cantidad"]
                        total = peliculaData["total"]

                        print(f" • {peliculaData['titulo']}: {cantidad} entradas — ${total}")

                        total_entradas += cantidad

                print(f"\n{'=' * 50}")
                print(f"TOTAL DE ENTRADAS VENDIDAS: {total_entradas}")
                print(f"TOTAL RECAUDADO: ${ventasGenerales}")
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
                        salas = obtenerSalas()

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

                # Usar las funciones (instancias) para reflejar butacas ocupadas por ventas
                funciones = obtenerFunciones()

                todasExtremeDisp = set()
                todasNormalDisp = set()
                todasExtremeOcup = set()
                todasNormalOcup = set()

                for peliId, cineIDs in funciones.items():
                    for cineId, salasData in cineIDs.items():
                        for salaId, diasData in salasData.items():
                            for dia, horariosData in diasData.items():
                                for horario, funcData in horariosData.items():
                                    butacas = funcData.get("butacas", {})
                                    extremeDisp = butacasDisponiblesPorTipo(butacas, "extreme")
                                    normalDisp = butacasDisponiblesPorTipo(butacas, "normal")
                                    extremeOcup = butacasOcupadasPorTipo(butacas, "extreme")
                                    normalOcup = butacasOcupadasPorTipo(butacas, "normal")

                                    todasExtremeDisp |= extremeDisp
                                    todasNormalDisp |= normalDisp
                                    todasExtremeOcup |= extremeOcup
                                    todasNormalOcup |= normalOcup

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
                cines = obtenerCines()
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