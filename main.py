from utils import *

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

#----------------------------------------------------------------------------------------------
# DATOS INICIALES
#----------------------------------------------------------------------------------------------
cines = {
    "1": {"nombre": "Nuestra Señora del Lujan", "direccion": "Calle 24 e/ 125 y 127"},
    "2": {"nombre": "Los Sauces", "direccion": "Calle 79 e/ 10 y 12"},
    "3": {"nombre": "York", "direccion": "Calle 60 e/ 125 y 127"},
    "4": {"nombre": "Abasto", "direccion": "Rivadavia 888"}
}

salas = { 
    "1": {"cineId": "1", "numeroSala": "1", "asientos": generarAsientosSala()},
    "2": {"cineId": "1", "numeroSala": "2", "asientos": generarAsientosSala()},
    "3": {"cineId": "2", "numeroSala": "1", "asientos": generarAsientosSala()},
    "4": {"cineId": "4", "numeroSala": "1", "asientos": generarAsientosSala()}
}

# Marcar algunas butacas como inhabilitadas en la plantilla de la sala 1
salas["1"]["asientos"]["A2"]["habilitado"] = False

funciones = {
    "1": { # peliculaId
        "1": { # cineId
            "1": { # salaId
                "martes": {
                    "14:00": {"butacas": generarAsientosSala()},
                    "18:00": {"butacas": generarAsientosSala()},
                    "21:00": {"butacas": generarAsientosSala()}
                },
                "miercoles": {
                    "15:00": {"butacas": generarAsientosSala()},
                    "19:00": {"butacas": generarAsientosSala()}
                }
            },
            "2": { # salaId
                "martes": {
                    "16:00": {"butacas": generarAsientosSala()},
                    "20:00": {"butacas": generarAsientosSala()}
                }
            }
        }
    },
    "2": { # peliculaId
        "2": { # cineId
            "3": { # salaId
                "jueves": {
                    "17:00": {"butacas": generarAsientosSala()},
                    "20:30": {"butacas": generarAsientosSala()}
                }
            }
        }
    }
}
# Ocupar una butaca en una función específica para el ejemplo inicial
funciones["1"]["1"]["1"]["martes"]["14:00"]["butacas"]["A1"]["ocupado"] = True
funciones["1"]["1"]["1"]["martes"]["14:00"]["butacas"]["A2"]["habilitado"] = False
funciones["1"]["1"]["1"]["martes"]["18:00"]["butacas"]["A2"]["habilitado"] = False
funciones["1"]["1"]["1"]["martes"]["21:00"]["butacas"]["A2"]["habilitado"] = False
funciones["1"]["1"]["1"]["miercoles"]["15:00"]["butacas"]["A2"]["habilitado"] = False
funciones["1"]["1"]["1"]["miercoles"]["19:00"]["butacas"]["A2"]["habilitado"] = False

peliculas = {
    "1": {"titulo": "Spiderman", "formato": "2D", "idioma": "Español", "activo": True, "complejos": {"1"}},
    "2": {"titulo": "Avengers: Endgame", "formato": "3D", "idioma": "Subtitulado", "activo": True, "complejos": {"2"}},
    "3": {"titulo": "Coco", "formato": "2D", "idioma": "Español", "activo": True, "complejos": {"4"}}
}

entradas = {
    "1": {
        'cliente': "Juan Perez", 'dni': "12345678", 'cineId': "1",
        'peliculaId': "1", 'salaId': "1", 'butaca': "A1",
        'dia': "martes", 'horario': "14:00"
    }
}

#----------------------------------------------------------------------------------------------
# BUCLE PRINCIPAL
#----------------------------------------------------------------------------------------------
while True:
    mostrarMenu("SISTEMA DE GESTIÓN DE CINE", MENU_PRINCIPAL)
    opcion = input("\n> Seleccione una opción: ").strip()

    if opcion == "0":
        print("\n¡Gracias por usar el sistema! Hasta pronto.")
        break
        
    # Opción 1: GESTIÓN DE PELÍCULAS
    elif opcion == "1":   
        while True:
            mostrarMenu("GESTIÓN DE PELÍCULAS", MENU_PELICULAS)
            opcionPeliculas = input("\n> Seleccione una opción: ").strip()

            if opcionPeliculas == "0": 
                break
                
            elif opcionPeliculas == "1":  # Agregar Película
                print("\n--- AGREGAR NUEVA PELÍCULA ---")
                peliculaData = {}
                peliculaData['titulo'] = input("Título de la película: ").strip()
                while not peliculaData['titulo']:
                    print("⚠️  El título no puede estar vacío.")
                    peliculaData['titulo'] = input("Título de la película: ").strip()

                print(f"\nFormatos válidos: {', '.join([f.upper() for f in FORMATOS_VALIDOS])}")
                peliculaData['formato'] = input("Formato (2D/3D): ").strip()
                while peliculaData['formato'].lower() not in FORMATOS_VALIDOS:
                    print(f"⚠️  Formato inválido. Opciones: {', '.join(FORMATOS_VALIDOS)}")
                    peliculaData['formato'] = input("Formato (2D/3D): ").strip()

                print(f"\nIdiomas válidos: {', '.join([i.capitalize() for i in IDIOMAS_VALIDOS])}")
                peliculaData['idioma'] = input("Idioma (Español/Subtitulado): ").strip()
                while peliculaData['idioma'].lower() not in IDIOMAS_VALIDOS:
                    print(f"⚠️  Idioma inválido. Opciones: {', '.join(IDIOMAS_VALIDOS)}")
                    peliculaData['idioma'] = input("Idioma (Español/Subtitulado): ").strip()

                print("\n--- SELECCIÓN DE CINES ---")
                imprimirCines(cines)
                peliculaData['complejos'] = set()
                
                while True:
                    cineId = input("\nID del cine (ENTER para finalizar selección): ").strip()
                    if not cineId:
                        if not peliculaData['complejos']:
                            print("⚠️  Debe seleccionar al menos un cine.")
                            continue
                        break
                    
                    if cineId not in cines:
                        print("⚠️  Cine no encontrado.")
                        continue
                    
                    if cineId in peliculaData['complejos']:
                        print("⚠️  Este cine ya fue agregado.")
                        continue
                        
                    peliculaData['complejos'].add(cineId)
                    print(f"✓ Cine '{cines[cineId]['nombre']}' agregado")

                peliculas, peliculaId = agregarPelicula(peliculaData, peliculas)
                print(f"\n✓ ¡Película '{peliculaData['titulo']}' agregada con éxito! (ID: {peliculaId})")
                
                if input("\n¿Desea agregar funciones ahora? (s/n): ").strip().lower() == 's':
                    funciones = gestionarFuncionesPelicula(peliculaId, peliculaData['complejos'], peliculas, cines, salas, funciones)

            elif opcionPeliculas == "2":  # Modificar Película
                if not peliculas:
                    print("\n⚠️  No hay películas registradas.")
                    continue
                    
                print("\n--- MODIFICAR PELÍCULA ---")
                imprimirPeliculas(peliculas)
                
                peliculaId = input("\nID de la película a modificar: ").strip()
                if peliculaId not in peliculas:
                    print("⚠️  Película no encontrada.")
                    continue
                
                peliculaExistente = peliculas[peliculaId]
                peliculaEditada = peliculaExistente.copy()
                peliculaEditada['complejos'] = peliculaExistente['complejos'].copy()
                
                while True:
                    print(f"\nEditando: {peliculaExistente['titulo']}")
                    mostrarMenu("MODIFICAR DATOS DE LA PELÍCULA", MENU_MODIFICACION_PELICULA)
                    opcionMod = input("\n> Seleccione una opción: ").strip()

                    if opcionMod == "0":
                        if peliculaEditada != peliculaExistente:
                            peliculas = modificarPelicula(peliculaId, peliculaEditada, peliculas)
                            print("\n✓ Película modificada con éxito!")
                        break
                        
                    elif opcionMod == "5":
                        funciones = gestionarFuncionesPelicula(peliculaId, peliculaEditada['complejos'], peliculas, cines, salas, funciones)

            elif opcionPeliculas == "3":
                imprimirPeliculas(peliculas) if peliculas else print("\n⚠️  No hay películas registradas.")
                    
            elif opcionPeliculas == "4":
                imprimirFunciones(funciones, peliculas, cines, salas) if funciones else print("\n⚠️  No hay funciones programadas.")
                    
            elif opcionPeliculas == "5": # Películas por idioma Y formato
                if not peliculas:
                    print("\n⚠️  No hay películas registradas.")
                    continue
                
                print("\n--- PELÍCULAS POR IDIOMA Y FORMATO ---")
                print(f"Idiomas disponibles: {', '.join(sorted(obtenerIdiomasDisponibles(peliculas)))}")
                print(f"Formatos disponibles: {', '.join(sorted(obtenerFormatosDisponibles(peliculas)))}")
                
                idioma = input("\nIdioma: ").strip()
                formato = input("Formato: ").strip()
                
                pelisResultado = peliculasPorIdiomaYFormato(peliculas, idioma, formato)
                
                if pelisResultado:
                    print(f"\nPelículas en '{idioma.capitalize()}' Y formato '{formato.upper()}':")
                    for pId in pelisResultado:
                        print(f"  • {peliculas[pId]['titulo']} (ID: {pId})")
                else:
                    print(f"\n⚠️  No se encontraron películas con esos criterios.")

            input("\nPresione ENTER para continuar...")

    # Opción 2: VENTA DE ENTRADAS
    elif opcion == "2":   
        while True:
            mostrarMenu("VENTA DE ENTRADAS", MENU_ENTRADAS)
            opcionEntradas = input("\n> Seleccione una opción: ").strip()

            if opcionEntradas == "0": 
                break
                
            elif opcionEntradas == "1":  # Generar Entrada
                print("\n--- GENERAR NUEVA ENTRADA ---")
                
                nombreCliente = input("Nombre del cliente: ").strip()
                dniCliente = input("DNI del cliente: ").strip()
                if not nombreCliente or not dniCliente.isdigit():
                    print("⚠️  Datos de cliente inválidos.")
                    continue
                
                imprimirCines(cines)
                idCine = input("\nID del cine: ").strip()
                if idCine not in cines:
                    print("⚠️  Cine no encontrado.")
                    continue
                
                peliculasEnCine = peliculasPorCine(peliculas, idCine)
                if not peliculasEnCine:
                    print(f"\n⚠️  No hay películas disponibles en '{cines[idCine]['nombre']}'.")
                    continue
                
                print(f"\n--- PELÍCULAS EN {cines[idCine]['nombre'].upper()} ---")
                peliculasConFunciones = {}
                for pId, pInfo in peliculasEnCine.items():
                    if pId in funciones and idCine in funciones[pId]:
                        peliculasConFunciones[pId] = pInfo
                        print(f"\n[{pId}] {pInfo['titulo']} ({pInfo['formato']} - {pInfo['idioma']})")
                        print("  Funciones disponibles:")
                        for salaId, diasData in funciones[pId][idCine].items():
                            salaInfo = salas.get(salaId, {})
                            print(f"    Sala {salaInfo.get('numeroSala', '?')}:")
                            for dia, horariosData in diasData.items():
                                print(f"      • {dia.capitalize()}: {', '.join(sorted(horariosData.keys()))}")
                
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
                    funcion_seleccionada = funciones[peliculaId][idCine][salaId][diaPelicula][horaPelicula]
                    asientos_funcion = funcion_seleccionada["butacas"]
                except KeyError:
                    print("⚠️  Función (sala, día u horario) no válida.")
                    continue
                
                asientosDisponiblesSet = informeButacasDisponibles(asientos_funcion)
                if not asientosDisponiblesSet:
                    print("\n⚠️  No hay butacas disponibles para esta función.")
                    continue

                imprimirSala(asientos_funcion)
                
                butaca = input("Seleccione una butaca: ").strip().upper()
                if butaca not in asientosDisponiblesSet:
                    print("⚠️  Butaca no válida o no disponible.")
                    continue
                
                print("\n--- RESUMEN DE LA COMPRA ---")
                print(f"Película: {peliculas[peliculaId]['titulo']}, Butaca: {butaca}")
                
                if input("\n¿Confirmar compra? (s/n): ").strip().lower() == 's':
                    asientos_funcion[butaca]["ocupado"] = True
                    
                    nuevaEntrada = {
                        'cliente': nombreCliente, 'dni': dniCliente, 'cineId': idCine,
                        'peliculaId': peliculaId, 'salaId': salaId, 'butaca': butaca,
                        'dia': diaPelicula, 'horario': horaPelicula
                    }
                    entradas = generarEntrada(nuevaEntrada, entradas)
                    print(f"\n✓ ¡Entrada generada con éxito!")
                else:
                    print("\nCompra cancelada.")
                    
            elif opcionEntradas == "2":  # Eliminar Venta
                print("\n--- ELIMINAR VENTA ---")
                dniCliente = input("DNI del cliente: ").strip()
                entradasCliente = buscarEntradasPorDNI(dniCliente, entradas, peliculas, cines, salas)
                
                if not entradasCliente:
                    print(f"\n⚠️  No se encontraron entradas para el DNI {dniCliente}.")
                    continue
                
                print(f"\n--- ENTRADAS DE {entradasCliente[0]['cliente'].upper()} ---")
                for idx, entrada in enumerate(entradasCliente, 1):
                    print(f"[{idx}] ID: {entrada['entradaId']} - {entrada['titulopeli']} - Butaca: {entrada['butaca']}")
                
                try:
                    seleccion = int(input("\nNúmero de entrada a eliminar: ").strip()) - 1
                    if not (0 <= seleccion < len(entradasCliente)):
                        raise ValueError
                    
                    entradaEliminar = entradasCliente[seleccion]
                    
                    if input(f"\n¿Confirma eliminar esta entrada? (s/n): ").strip().lower() == 's':
                        # --- CAMBIO CLAVE: Liberar la butaca en la sala de la función específica ---
                        try:
                            funcion = funciones[entradaEliminar['peliculaId']][entradaEliminar['cineId']][entradaEliminar['salaId']][entradaEliminar['dia']][entradaEliminar['horario']]
                            funcion["butacas"][entradaEliminar['butaca']]["ocupado"] = False
                            entradas = eliminarEntrada(entradaEliminar['entradaId'], entradas)
                            print("\n✓ Entrada eliminada y butaca liberada.")
                        except KeyError:
                            print("⚠️ Error: La función asociada a esta entrada ya no existe, solo se eliminará la entrada.")
                            entradas = eliminarEntrada(entradaEliminar['entradaId'], entradas)
                    else:
                        print("\nOperación cancelada.")
                except (ValueError, IndexError):
                    print("⚠️ Selección inválida.")

            elif opcionEntradas == "3":  # Ver mis entradas
                dniCliente = input("\nDNI del cliente: ").strip()
                entradasCliente = buscarEntradasPorDNI(dniCliente, entradas, peliculas, cines, salas)
                if not entradasCliente:
                    print(f"⚠️ No se encontraron entradas para el DNI {dniCliente}.")
                else:
                    print(f"\n--- ENTRADAS DE {entradasCliente[0]['cliente'].upper()} ---")
                    for ent in entradasCliente:
                        print(f"  • Película: {ent['titulopeli']}, Cine: {ent['nombrecine']}, Sala: {ent['numerosala']}, Butaca: {ent['butaca']}")

            input("\nPresione ENTER para continuar...")
    
    # Opción 3: INFORMES GENERALES
    elif opcion == "3":   
        while True:
            mostrarMenu("INFORMES GENERALES", MENU_INFORMES)
            opcionInformes = input("\n> Seleccione una opción: ").strip()

            if opcionInformes == "0": 
                break
                
            elif opcionInformes == "1":  # Informe de Ventas
                if not entradas:
                    print("\n⚠️  No hay ventas registradas.")
                else:
                    informe, ventasGenerales = informeVentas(entradas, peliculas, cines)
                    print("\n--- INFORME DE VENTAS ---")
                    for cineId, cineData in informe.items():
                        print(f"\n{cineData['nombre']}")
                        print("-" * 50)
                        for peliculaId, peliculaData in cineData["entradas"].items():
                            print(f"  • {peliculaData['titulo']}: {peliculaData['cantidad']} entradas")
                    print(f"\n{'='*50}")
                    print(f"TOTAL DE VENTAS: {ventasGenerales} entradas")
                    print("="*50)

            elif opcionInformes == "2":  # Listado de Películas Disponibles
                if not peliculas:
                    print("\n⚠️  No hay películas registradas.")
                else:
                    disponibles = informeListadoPeliculasDisponibles(peliculas, cines)
                    
                    if not disponibles:
                        print("\n⚠️  No hay películas disponibles actualmente.")
                    else:
                        idiomas = obtenerIdiomasDisponibles(peliculas)
                        formatos = obtenerFormatosDisponibles(peliculas)
                        
                        print("\n--- LISTADO DE PELÍCULAS DISPONIBLES ---")
                        print("-" * 80)
                        for peliculaId, titulo, idioma, formato, cines_str in disponibles:
                            print(f"[{peliculaId}] {titulo}")
                            print(f"    Idioma: {idioma} | Formato: {formato}")
                            print(f"    Cines: {cines_str}")
                            print()
                        
                        print(f"Idiomas disponibles: {', '.join(sorted(idiomas))}")
                        print(f"Formatos disponibles: {', '.join(sorted(formatos))}")

            elif opcionInformes == "3":  # Informe de Butacas Disponibles
                if not salas:
                    print("\n⚠️  No hay salas registradas.")
                else:
                    print("\n--- INFORME DE BUTACAS DISPONIBLES POR SALA ---")
                    for salaId, sala in salas.items():
                        cineInfo = cines.get(sala['cineId'], {})
                        print(f"\n{cineInfo.get('nombre', 'Desconocido')} - Sala {sala['numeroSala']}")
                        print("-" * 60)
                        
                        butacasDisponibles = informeButacasDisponibles(sala['asientos'])
                        totalButacas = len(sala['asientos'])
                        ocupadas = totalButacas - len(butacasDisponibles)
                        
                        print(f"Total: {totalButacas} | Disponibles: {len(butacasDisponibles)} | Ocupadas: {ocupadas}")
                        print()
                        imprimirSala(sala['asientos'])

            elif opcionInformes == "4":  # Informe de Butacas por Tipo
                if not salas:
                    print("\n⚠️  No hay salas registradas.")
                else:
                    print("\n--- INFORME DE BUTACAS POR TIPO ---")
                    for salaId, sala in salas.items():
                        cineInfo = cines.get(sala['cineId'], {})
                        print(f"\n{cineInfo.get('nombre', 'Desconocido')} - Sala {sala['numeroSala']}")
                        print("-" * 60)
                        
                        extremeTotal = butacasPorTipo(sala['asientos'], "extreme")
                        normalTotal = butacasPorTipo(sala['asientos'], "normal")
                        
                        extremeDisponibles = butacasDisponiblesPorTipo(sala['asientos'], "extreme")
                        normalDisponibles = butacasDisponiblesPorTipo(sala['asientos'], "normal")
                        
                        extremeOcupadas = butacasOcupadasPorTipo(sala['asientos'], "extreme")
                        normalOcupadas = butacasOcupadasPorTipo(sala['asientos'], "normal")
                        
                        print(f"EXTREME: {len(extremeTotal)} totales | {len(extremeDisponibles)} disponibles | {len(extremeOcupadas)} ocupadas")
                        print(f"NORMAL:  {len(normalTotal)} totales | {len(normalDisponibles)} disponibles | {len(normalOcupadas)} ocupadas")
                        print()
                        imprimirSala(sala['asientos'])

            input("\nPresione ENTER para continuar...")

    # Opción 4: GESTIÓN DE COMPLEJO DE CINES
    elif opcion == "4":   
        while True:
            mostrarMenu("GESTIÓN DE COMPLEJO DE CINES", MENU_CINES)
            opcionCines = input("\n> Seleccione una opción: ").strip()

            if opcionCines == "0": 
                break
                
            elif opcionCines == "1":  # Listar Cines
                if not cines:
                    print("\n⚠️  No hay cines registrados.")
                else:
                    imprimirCines(cines)

            elif opcionCines == "2":  # Agregar Nuevo Cine
                print("\n--- AGREGAR NUEVO CINE ---")
                nombre = input("Nombre del cine: ").strip()
                while not nombre:
                    print("⚠️  El nombre no puede estar vacío.")
                    nombre = input("Nombre del cine: ").strip()
                
                direccion = input("Dirección del cine: ").strip()
                while not direccion:
                    print("⚠️  La dirección no puede estar vacía.")
                    direccion = input("Dirección del cine: ").strip()
                
                cineData = (nombre, direccion)
                cines, nuevoCineId = nuevoCine(cineData, cines)
                
                crear_salas = input("\n¿Desea crear salas ahora? (s/n): ").strip().lower()
                if crear_salas == 's':
                    cantidadSalas = input("Cantidad de salas a crear: ").strip()
                    while not cantidadSalas or not cantidadSalas.isdigit() or int(cantidadSalas) <= 0:
                        print("⚠️  Ingrese un número válido.")
                        cantidadSalas = input("Cantidad de salas a crear: ").strip()
                    
                    cantidadSalas = int(cantidadSalas)
                    for i in range(cantidadSalas):
                        salas = crearSala(nuevoCineId, salas)
                    
                    print(f"\n✓ {cantidadSalas} sala(s) creada(s) con éxito!")

            elif opcionCines == "3":  # Eliminar Cine
                if not cines:
                    print("\n⚠️  No hay cines registrados.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                print("\n--- ELIMINAR CINE ---")
                imprimirCines(cines)
                
                cineId = input("\nID del cine a eliminar: ").strip()
                if not cines.get(cineId):
                    print("⚠️  Cine no encontrado.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                print(f"\n⚠️  ADVERTENCIA: Se eliminarán también:")
                print("  • Todas las salas del cine")
                print("  • Todas las funciones del cine")
                print("  • Todas las entradas vendidas para este cine")
                
                confirmar = input(f"\n¿Confirma eliminar '{cines[cineId]['nombre']}'? (s/n): ").strip().lower()
                
                if confirmar == 's':
                    salasAEliminar = [salaId for salaId, sala in salas.items() if sala['cineId'] == cineId]
                    for salaId in salasAEliminar:
                        del salas[salaId]
                    
                    for peliculaId in list(funciones.keys()):
                        if cineId in funciones[peliculaId]:
                            del funciones[peliculaId][cineId]
                    
                    entradasAEliminar = [entId for entId, ent in entradas.items() if ent['cineId'] == cineId]
                    for entId in entradasAEliminar:
                        del entradas[entId]
                    
                    for pelicula in peliculas.values():
                        if cineId in pelicula['complejos']:
                            pelicula['complejos'].remove(cineId)
                    
                    cines = eliminarCine(cineId, cines)
                    print("\n✓ Cine eliminado con éxito!")
                else:
                    print("\nOperación cancelada.")

            elif opcionCines == "4":  # Modificar Cine
                if not cines:
                    print("\n⚠️  No hay cines registrados.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                print("\n--- MODIFICAR CINE ---")
                imprimirCines(cines)
                
                cineId = input("\nID del cine a modificar: ").strip()
                cineExistente = cines.get(cineId)
                
                if not cineExistente:
                    print("⚠️  Cine no encontrado.")
                    input("\nPresione ENTER para continuar...")
                    continue

                cineEditado = cineExistente.copy()
                
                while True:
                    print(f"\nEditando: {cineExistente['nombre']}")
                    mostrarMenu("MODIFICACIÓN DE CINE", MENU_MODIFICACION_CINE)
                    opcionMod = input("\n> Seleccione una opción: ").strip()
                    
                    if opcionMod == "0":  # Guardar
                        if cineEditado != cineExistente:
                            cines = modificarCine(cineId, cineEditado, cines)
                            print("\n✓ Cine modificado con éxito!")
                        break
                        
                    elif opcionMod == "1":  # Modificar Nombre
                        nuevoNombre = input(f"Nuevo nombre (actual: {cineExistente['nombre']}): ").strip()
                        if nuevoNombre:
                            cineEditado['nombre'] = nuevoNombre
                            print("✓ Nombre actualizado")
                            
                    elif opcionMod == "2":  # Modificar Dirección
                        nuevaDireccion = input(f"Nueva dirección (actual: {cineExistente['direccion']}): ").strip()
                        if nuevaDireccion:
                            cineEditado['direccion'] = nuevaDireccion
                            print("✓ Dirección actualizada")

            elif opcionCines == "5":  # Modificar Salas de Cine
                if not cines:
                    print("\n⚠️  No hay cines registrados.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                print("\n--- MODIFICAR SALAS DE CINE ---")
                imprimirCines(cines)
                
                cineId = input("\nID del cine: ").strip()
                if not cines.get(cineId):
                    print("⚠️  Cine no encontrado.")
                    input("\nPresione ENTER para continuar...")
                    continue

                while True:
                    print(f"\nGestionando salas de: {cines[cineId]['nombre']}")
                    mostrarMenu("MODIFICACIÓN DE SALAS", MENU_MODIFICACION_SALAS)
                    opcionMod = input("\n> Seleccione una opción: ").strip()
                    
                    if opcionMod == "0":
                        break
                        
                    elif opcionMod == "1":  # Listar Salas
                        salasCine = {salaId: sala for salaId, sala in salas.items() if sala['cineId'] == cineId}
                        if not salasCine:
                            print("\n⚠️  No hay salas en este cine.")
                        else:
                            imprimirSalasPorCine(cineId, salas)
                            
                    elif opcionMod == "2":  # Generar nueva Sala
                        salas = crearSala(cineId, salas)
                        print("✓ Sala creada con éxito!")
                        
                    elif opcionMod == "3":  # Modificar Sala
                        salasCine = {salaId: sala for salaId, sala in salas.items() if sala['cineId'] == cineId}
                        if not salasCine:
                            print("\n⚠️  No hay salas en este cine.")
                            continue
                        
                        imprimirSalasPorCine(cineId, salas)
                        salaId = input("\nID de la sala a modificar: ").strip()
                        
                        if salaId not in salasCine:
                            print("⚠️  Sala no encontrada.")
                            continue
                        
                        while True:
                            mostrarMenu("MODIFICACIÓN DE SALA", MENU_MODIFICACION_SALA)
                            opcionSala = input("\n> Seleccione una opción: ").strip()
                            
                            if opcionSala == "0":
                                break
                                
                            elif opcionSala == "1":  # Mostrar Sala
                                imprimirSala(salas[salaId]['asientos'])
                                
                            elif opcionSala == "2":  # Inhabilitar/Habilitar Butaca
                                imprimirSala(salas[salaId]['asientos'])
                                codigoButaca = input("\nCódigo de la butaca: ").strip().upper()
                                
                                if codigoButaca not in salas[salaId]['asientos']:
                                    print("⚠️  Butaca no encontrada.")
                                    continue
                                
                                butaca = salas[salaId]['asientos'][codigoButaca]
                                if butaca['ocupado']:
                                    print("⚠️  No se puede modificar una butaca ocupada.")
                                    continue
                                
                                nuevoEstado = not butaca['habilitado']
                                butaca['habilitado'] = nuevoEstado
                                estado_texto = "habilitada" if nuevoEstado else "inhabilitada"
                                print(f"✓ Butaca {codigoButaca} {estado_texto}")
                                
                    elif opcionMod == "4":  # Eliminar Sala
                        salasCine = {salaId: sala for salaId, sala in salas.items() if sala['cineId'] == cineId}
                        if not salasCine:
                            print("\n⚠️  No hay salas en este cine.")
                            continue
                        
                        imprimirSalasPorCine(cineId, salas)
                        salaId = input("\nID de la sala a eliminar: ").strip()
                        
                        if salaId not in salasCine:
                            print("⚠️  Sala no encontrada.")
                            continue
                        
                        tieneFunciones = False
                        for peliFuncs in funciones.values():
                            if cineId in peliFuncs and salaId in peliFuncs[cineId]:
                                tieneFunciones = True
                                break
                        
                        if tieneFunciones:
                            print("\n⚠️  ADVERTENCIA: Esta sala tiene funciones programadas que serán eliminadas.")
                        
                        confirmar = input(f"\n¿Confirma eliminar la sala {salas[salaId]['numeroSala']}? (s/n): ").strip().lower()
                        
                        if confirmar == 's':
                            for peliculaId in list(funciones.keys()):
                                if cineId in funciones[peliculaId] and salaId in funciones[peliculaId][cineId]:
                                    del funciones[peliculaId][cineId][salaId]
                            
                            entradasElim = [entId for entId, ent in entradas.items() if ent['salaId'] == salaId]
                            for entId in entradasElim:
                                del entradas[entId]
                            
                            del salas[salaId]
                            print("✓ Sala eliminada con éxito!")

            elif opcionCines == "6":  # Películas en común entre dos cines
                if len(cines) < 2:
                    print("\n⚠️  Se necesitan al menos 2 cines registrados.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                print("\n--- PELÍCULAS EN COMÚN ENTRE DOS CINES ---")
                imprimirCines(cines)
                
                cine1 = input("\nID del primer cine: ").strip()
                cine2 = input("ID del segundo cine: ").strip()
                
                if not cines.get(cine1) or not cines.get(cine2):
                    print("⚠️  Uno o ambos cines no existen.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                if cine1 == cine2:
                    print("⚠️  Debe seleccionar dos cines diferentes.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                peliculas1 = peliculasPorCine(peliculas, cine1)
                peliculas2 = peliculasPorCine(peliculas, cine2)
                
                idsComunes = set(peliculas1.keys()) & set(peliculas2.keys())
                
                if idsComunes:
                    print(f"\nPelículas en común entre '{cines[cine1]['nombre']}' y '{cines[cine2]['nombre']}':")
                    print("-" * 60)
                    for pid in sorted(idsComunes):
                        print(f"  • {peliculas[pid]['titulo']} (ID: {pid})")
                else:
                    print(f"\n⚠️  No hay películas en común entre estos cines.")

            elif opcionCines == "7":  # Cines sin películas asignadas
                print("\n--- CINES SIN PELÍCULAS ASIGNADAS ---")
                todosCinesSet = set(cines.keys())
                cinesSinPelis = cinesSinPeliculas(todosCinesSet, peliculas)
                
                if cinesSinPelis:
                    print("Los siguientes cines NO tienen películas asignadas:")
                    print("-" * 60)
                    for cineId in sorted(cinesSinPelis):
                        print(f"  • {cines[cineId]['nombre']} (ID: {cineId})")
                else:
                    print("✓ Todos los cines tienen al menos una película asignada.")

            elif opcionCines == "8":  # Películas en todos los cines seleccionados
                if not cines:
                    print("\n⚠️  No hay cines registrados.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                print("\n--- PELÍCULAS EN TODOS LOS CINES SELECCIONADOS ---")
                imprimirCines(cines)
                
                cinesSeleccionados = set()
                print("\nSeleccione los cines (ENTER sin texto para finalizar)")
                
                while True:
                    cineId = input(f"ID de cine ({len(cinesSeleccionados)} seleccionados): ").strip()
                    if not cineId:
                        break
                    if not cines.get(cineId):
                        print("⚠️  Cine no encontrado.")
                    elif cineId in cinesSeleccionados:
                        print("⚠️  Este cine ya fue seleccionado.")
                    else:
                        cinesSeleccionados.add(cineId)
                        print(f"✓ '{cines[cineId]['nombre']}' agregado")
                
                if not cinesSeleccionados:
                    print("⚠️  No se seleccionaron cines.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                pelisEnTodos = peliculasEnTodosCines(peliculas, cinesSeleccionados)
                
                if pelisEnTodos:
                    print(f"\nPelículas disponibles en TODOS los {len(cinesSeleccionados)} cines seleccionados:")
                    print("-" * 60)
                    for pid, peli in pelisEnTodos.items():
                        print(f"  • {peli['titulo']} (ID: {pid})")
                else:
                    print("\n⚠️  No hay películas disponibles en todos los cines seleccionados.")

            elif opcionCines == "9":  # Comparar butacas por tipo
                if not salas:
                    print("\n⚠️  No hay salas registradas.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                print("\n--- ANÁLISIS GLOBAL DE BUTACAS POR TIPO ---")
                
                todasExtremeDisp = set()
                todasNormalDisp = set()
                todasExtremeOcup = set()
                todasNormalOcup = set()
                
                for salaId, sala in salas.items():
                    extremeDisp = butacasDisponiblesPorTipo(sala['asientos'], "extreme")
                    normalDisp = butacasDisponiblesPorTipo(sala['asientos'], "normal")
                    extremeOcup = butacasOcupadasPorTipo(sala['asientos'], "extreme")
                    normalOcup = butacasOcupadasPorTipo(sala['asientos'], "normal")
                    
                    todasExtremeDisp = todasExtremeDisp | extremeDisp
                    todasNormalDisp = todasNormalDisp | normalDisp
                    todasExtremeOcup = todasExtremeOcup | extremeOcup
                    todasNormalOcup = todasNormalOcup | normalOcup
                
                print("\nRESUMEN GLOBAL:")
                print("="*60)
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

            elif opcionCines == "10":  # Análisis de funciones por día
                if not funciones:
                    print("\n⚠️  No hay funciones programadas.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                print("\n--- ANÁLISIS DE FUNCIONES POR DÍA ---")
                imprimirPeliculas(peliculas)
                
                peliculaId = input("\nID de película: ").strip()
                if not peliculas.get(peliculaId):
                    print("⚠️  Película no encontrada.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                imprimirCines(cines)
                cineId = input("\nID de cine: ").strip()
                if not cines.get(cineId):
                    print("⚠️  Cine no encontrado.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                diasDisponibles = diasConFunciones(funciones, peliculaId, cineId)
                
                if diasDisponibles:
                    print(f"\nDías con funciones: {', '.join([d.capitalize() for d in sorted(diasDisponibles)])}")
                    
                    dia = input("\nDía para ver horarios: ").strip().lower()
                    if dia in diasDisponibles:
                        horarios = horariosEnDia(funciones, peliculaId, cineId, dia)
                        print(f"\nHorarios el {dia.capitalize()}: {', '.join(sorted(horarios))}")
                    else:
                        print(f"⚠️  No hay funciones el {dia}.")
                else:
                    print("⚠️  No hay funciones programadas para esta combinación.")

            elif opcionCines == "11":  # Cines con/sin funciones
                if not cines:
                    print("\n⚠️  No hay cines registrados.")
                    input("\nPresione ENTER para continuar...")
                    continue
                
                print("\n--- ANÁLISIS DE CINES CON/SIN FUNCIONES ---")
                
                todosCinesSet = set(cines.keys())
                cinesConFunc = cinesConFunciones(funciones)
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