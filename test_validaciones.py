
from validaciones import *

def separador(titulo):
    print("\n" + "=" * 70)
    print(f" {titulo}")
    print("=" * 70)

def test_resultado(nombre_test, resultado_esperado, resultado_obtenido):
    estado = "✅ PASS" if resultado_esperado == resultado_obtenido else "❌ FAIL"
    print(f"{estado} | {nombre_test}")
    if resultado_esperado != resultado_obtenido:
        print(f"    Esperado: {resultado_esperado}, Obtenido: {resultado_obtenido}")

def test_validaciones_horario():
    separador("PRUEBAS DE VALIDACIÓN DE HORARIO")

    test_resultado("Horario válido 14:30", True, validar_horario("14:30"))
    test_resultado("Horario válido 9:45", True, validar_horario("9:45"))
    test_resultado("Horario válido 00:00", True, validar_horario("00:00"))
    test_resultado("Horario válido 23:59", True, validar_horario("23:59"))

    test_resultado("Horario inválido 25:00", False, validar_horario("25:00"))
    test_resultado("Horario inválido 14:60", False, validar_horario("14:60"))
    test_resultado("Horario inválido 14.30", False, validar_horario("14.30"))
    test_resultado("Horario inválido abc", False, validar_horario("abc"))

    print("\nHorario estricto (HH:MM):")
    test_resultado("Horario estricto 14:30", True, validar_horario_estricto("14:30"))
    test_resultado(
        "Horario estricto 9:45 (inválido)", False, validar_horario_estricto("9:45")
    )

def test_validaciones_dni():
    separador("PRUEBAS DE VALIDACIÓN DE DNI")

    test_resultado("DNI válido 12345678", True, validar_dni("12345678"))
    test_resultado("DNI válido 1234567", True, validar_dni("1234567"))

    test_resultado("DNI inválido 123456 (corto)", False, validar_dni("123456"))
    test_resultado("DNI inválido 123456789 (largo)", False, validar_dni("123456789"))
    test_resultado("DNI inválido abc12345", False, validar_dni("abc12345"))

    print("\nDNI con formato (puntos):")
    test_resultado(
        "DNI formato 12.345.678", True, validar_dni_con_formato("12.345.678")
    )
    test_resultado("DNI formato 12345678", True, validar_dni_con_formato("12345678"))

    print("\nLimpieza de DNI:")
    print(f"  12.345.678 → {limpiar_dni('12.345.678')}")
    print(f"  12 345 678 → {limpiar_dni('12 345 678')}")

def test_validaciones_butaca():
    separador("PRUEBAS DE VALIDACIÓN DE BUTACA")

    test_resultado("Butaca válida A1", True, validar_butaca("A1"))
    test_resultado("Butaca válida B12", True, validar_butaca("B12"))
    test_resultado("Butaca válida I8", True, validar_butaca("I8"))
    test_resultado("Butaca válida (minúscula) a5", True, validar_butaca("a5"))

    test_resultado("Butaca inválida Z1", False, validar_butaca("Z1"))
    test_resultado("Butaca inválida A0", False, validar_butaca("A0"))
    test_resultado("Butaca inválida 1A", False, validar_butaca("1A"))
    test_resultado("Butaca inválida AA1", False, validar_butaca("AA1"))

    print("\nExtracción de fila y columna:")
    fila, columna = extraer_fila_columna("A5")
    print(f"  A5 → Fila: {fila}, Columna: {columna}")
    fila, columna = extraer_fila_columna("B12")
    print(f"  B12 → Fila: {fila}, Columna: {columna}")

def test_validaciones_texto():
    separador("PRUEBAS DE VALIDACIÓN DE TEXTO")

    print("Títulos de películas:")
    test_resultado(
        "Título válido 'Avengers: Endgame'", True, validar_titulo("Avengers: Endgame")
    )
    test_resultado("Título válido 'Spider-Man 2'", True, validar_titulo("Spider-Man 2"))
    test_resultado("Título válido con acentos", True, validar_titulo("La misión"))
    test_resultado("Título inválido vacío", False, validar_titulo(""))
    test_resultado("Título inválido caracteres", False, validar_titulo("Film@#$%"))

    print("\nNombres de personas:")
    test_resultado(
        "Nombre válido 'Juan Pérez'", True, validar_nombre_persona("Juan Pérez")
    )
    test_resultado(
        "Nombre válido 'María O'Connor'", True, validar_nombre_persona("María O'Connor")
    )
    test_resultado(
        "Nombre inválido con números", False, validar_nombre_persona("Juan123")
    )
    test_resultado("Nombre inválido corto", False, validar_nombre_persona("J"))

    print("\nDirecciones:")
    test_resultado(
        "Dirección válida 'Av. Corrientes 1234'",
        True,
        validar_direccion("Av. Corrientes 1234"),
    )
    test_resultado("Dirección válida 'Calle 123'", True, validar_direccion("Calle 123"))
    test_resultado("Dirección inválida sin número", False, validar_direccion("Avenida"))
    test_resultado("Dirección inválida corta", False, validar_direccion("Av"))

    print("\nNombres de cines:")
    test_resultado("Cine válido 'Cinemark'", True, validar_nombre_cine("Cinemark"))
    test_resultado(
        "Cine válido 'Cine & Arte'", True, validar_nombre_cine("Cine & Arte")
    )

def test_validaciones_numericas():
    separador("PRUEBAS DE VALIDACIÓN NUMÉRICA")

    print("Números positivos:")
    test_resultado("Número válido '123'", True, validar_numero_positivo("123"))
    test_resultado("Número válido '1'", True, validar_numero_positivo("1"))
    test_resultado("Número inválido '0'", False, validar_numero_positivo("0"))
    test_resultado("Número inválido '-5'", False, validar_numero_positivo("-5"))
    test_resultado("Número inválido '12.5'", False, validar_numero_positivo("12.5"))

    print("\nIDs:")
    test_resultado("ID válido '42'", True, validar_id("42"))
    test_resultado("ID inválido '0'", False, validar_id("0"))

    print("\nRangos numéricos:")
    test_resultado("Rango 5 entre 1-10", True, validar_rango_numerico("5", 1, 10))
    test_resultado("Rango 15 entre 1-10", False, validar_rango_numerico("15", 1, 10))
    test_resultado("Rango sin mínimo", True, validar_rango_numerico("5", None, 10))
    test_resultado("Rango sin máximo", True, validar_rango_numerico("15", 5, None))

def test_validaciones_menu():
    separador("PRUEBAS DE VALIDACIÓN DE MENÚ")

    opciones = ["0", "1", "2", "3"]
    print(f"Opciones válidas: {opciones}")
    test_resultado("Opción válida '1'", True, validar_opcion_menu("1", opciones))
    test_resultado("Opción válida '0'", True, validar_opcion_menu("0", opciones))
    test_resultado("Opción inválida '5'", False, validar_opcion_menu("5", opciones))

    print("\nConfirmaciones (s/n):")
    test_resultado("Confirmación 's'", True, validar_confirmacion("s"))
    test_resultado("Confirmación 'si'", True, validar_confirmacion("si"))
    test_resultado("Confirmación 'yes'", True, validar_confirmacion("yes"))
    test_resultado("Confirmación 'n'", False, validar_confirmacion("n"))
    test_resultado("Confirmación 'no'", False, validar_confirmacion("no"))
    test_resultado("Confirmación inválida", None, validar_confirmacion("xyz"))

def test_validaciones_formato():
    separador("PRUEBAS DE VALIDACIÓN DE FORMATO")

    test_resultado("Formato válido '2D'", True, validar_formato("2D"))
    test_resultado("Formato válido '3d'", True, validar_formato("3d"))
    test_resultado("Formato válido '2d'", True, validar_formato("2d"))
    test_resultado("Formato válido '3D'", True, validar_formato("3D"))

    test_resultado("Formato inválido '4D'", False, validar_formato("4D"))
    test_resultado("Formato inválido 'IMAX'", False, validar_formato("IMAX"))

    print("\nNormalización de formato:")
    print(f"  '2D' → '{normalizar_formato('2D')}'")
    print(f"  '3D' → '{normalizar_formato('3D')}'")

def test_validaciones_idioma():
    separador("PRUEBAS DE VALIDACIÓN DE IDIOMA")

    test_resultado("Idioma 'español'", True, validar_idioma("español"))
    test_resultado("Idioma 'subtitulado'", True, validar_idioma("subtitulado"))
    test_resultado("Idioma 'ESPAÑOL' (mayúscula)", True, validar_idioma("ESPAÑOL"))

    test_resultado("Idioma 'inglés'", False, validar_idioma("inglés"))

    print("\nNormalización de idioma:")
    print(f"  'ESPAÑOL' → '{normalizar_idioma('ESPAÑOL')}'")
    print(f"  'Subtitulado' → '{normalizar_idioma('Subtitulado')}'")

def test_validaciones_dia():
    separador("PRUEBAS DE VALIDACIÓN DE DÍA")

    test_resultado("Día 'lunes'", True, validar_dia_semana("lunes"))
    test_resultado("Día 'domingo'", True, validar_dia_semana("domingo"))
    test_resultado("Día 'MARTES' (mayúscula)", True, validar_dia_semana("MARTES"))

    test_resultado("Abreviación 'lun'", True, validar_dia_semana("lun"))
    test_resultado("Abreviación 'dom'", True, validar_dia_semana("dom"))

    test_resultado("Día inválido 'lunez'", False, validar_dia_semana("lunez"))

    print("\nNormalización de día:")
    print(f"  'lun' → '{normalizar_dia_semana('lun')}'")
    print(f"  'DOMINGO' → '{normalizar_dia_semana('DOMINGO')}'")
    print(f"  'miércoles' → '{normalizar_dia_semana('miércoles')}'")

def test_funciones_limpieza():
    separador("PRUEBAS DE FUNCIONES DE LIMPIEZA")

    print("Limpieza de entrada:")
    print(f"  '  Hola    mundo  ' → '{limpiar_entrada('  Hola    mundo  ')}'")
    print(f"  'Texto\\n\\tcon espacios' → '{limpiar_entrada('Texto\n\tcon espacios')}'")

    print("\nLimpieza de espacios múltiples:")
    print(f"  'Hola     mundo' → '{limpiar_espacios_multiples('Hola     mundo')}'")

    print("\nRemoción de caracteres especiales:")
    print(f"  'Hola@#$Mundo!' → '{remover_caracteres_especiales('Hola@#$Mundo!')}'")
    print(
        f"  'Hola-Mundo' (permitir -) → '{remover_caracteres_especiales('Hola-Mundo', '-')}'"
    )

def test_funciones_busqueda():
    separador("PRUEBAS DE FUNCIONES DE BÚSQUEDA")

    print("Búsqueda flexible (case-insensitive):")
    test_resultado(
        "'avengers' en 'The Avengers'",
        True,
        buscar_flexible("avengers", "The Avengers Endgame"),
    )
    test_resultado(
        "'SPIDER' en 'spider-man'", True, buscar_flexible("SPIDER", "spider-man")
    )
    test_resultado(
        "'batman' en 'superman'", False, buscar_flexible("batman", "superman")
    )

    print("\nBúsqueda de palabra completa:")
    test_resultado(
        "'hola' en 'hola mundo'", True, buscar_palabra_completa("hola", "hola mundo")
    )
    test_resultado(
        "'hola' en 'holandes'", False, buscar_palabra_completa("hola", "holandes")
    )

    print("\nExtracción de números:")
    numeros = extraer_numeros("Tengo 25 años y vivo en la calle 123")
    print(f"  'Tengo 25 años y vivo en la calle 123' → {numeros}")

def test_validacion_completa():
    separador("PRUEBAS DE VALIDACIÓN COMPLETA")

    print("Validación de horario:")
    valido, limpio, error = validar_entrada_completa("14:30", "horario")
    print(f"  '14:30' → Válido: {valido}, Limpio: '{limpio}', Error: '{error}'")

    valido, limpio, error = validar_entrada_completa("25:00", "horario")
    print(f"  '25:00' → Válido: {valido}, Limpio: '{limpio}', Error: '{error}'")

    print("\nValidación de DNI:")
    valido, limpio, error = validar_entrada_completa("12.345.678", "dni")
    print(f"  '12.345.678' → Válido: {valido}, Limpio: '{limpio}', Error: '{error}'")

    print("\nValidación de butaca:")
    valido, limpio, error = validar_entrada_completa("a5", "butaca")
    print(f"  'a5' → Válido: {valido}, Limpio: '{limpio}', Error: '{error}'")

    print("\nValidación de formato:")
    valido, limpio, error = validar_entrada_completa("2D", "formato")
    print(f"  '2D' → Válido: {valido}, Limpio: '{limpio}', Error: '{error}'")

def ejemplos_uso_practico():
    separador("EJEMPLOS DE USO PRÁCTICO EN EL SISTEMA")

    print("\n📝 Ejemplo 1: Validar entrada de horario")
    print("-" * 50)
    horario = "  14:30  "
    if validar_horario(horario):
        horario_limpio = limpiar_entrada(horario)
        print(f"✅ Horario válido: {horario_limpio}")
    else:
        print("❌ Horario inválido")

    print("\n📝 Ejemplo 2: Validar y limpiar DNI")
    print("-" * 50)
    dni = "12.345.678"
    dni_limpio = limpiar_dni(dni)
    if validar_dni(dni_limpio):
        print(f"✅ DNI válido: {dni_limpio}")
    else:
        print("❌ DNI inválido")

    print("\n📝 Ejemplo 3: Validar butaca con normalización")
    print("-" * 50)
    butaca = "a5"
    if validar_butaca(butaca):
        butaca_normalizada = butaca.upper()
        fila, columna = extraer_fila_columna(butaca_normalizada)
        print(f"✅ Butaca válida: {butaca_normalizada}")
        print(f"   Fila: {fila}, Columna: {columna}")
    else:
        print("❌ Butaca inválida")

    print("\n📝 Ejemplo 4: Validar día con abreviación")
    print("-" * 50)
    dia = "lun"
    if validar_dia_semana(dia):
        dia_completo = normalizar_dia_semana(dia)
        print(f"✅ Día válido: '{dia}' → '{dia_completo}'")
    else:
        print("❌ Día inválido")

    print("\n📝 Ejemplo 5: Búsqueda flexible de películas")
    print("-" * 50)
    peliculas = ["Avengers: Endgame", "Spider-Man: No Way Home", "The Batman"]
    termino_busqueda = "AVENGERS"
    print(f"Buscando: '{termino_busqueda}'")
    for pelicula in peliculas:
        if buscar_flexible(termino_busqueda, pelicula):
            print(f"  ✅ Encontrada: {pelicula}")

def main():
    print("\n" + "=" * 70)
    print(" PRUEBAS DEL MÓDULO DE VALIDACIONES")
    print(" Sistema de Gestión de Cines")
    print("=" * 70)

    test_validaciones_horario()
    test_validaciones_dni()
    test_validaciones_butaca()
    test_validaciones_texto()
    test_validaciones_numericas()
    test_validaciones_menu()
    test_validaciones_formato()
    test_validaciones_idioma()
    test_validaciones_dia()
    test_funciones_limpieza()
    test_funciones_busqueda()
    test_validacion_completa()

    ejemplos_uso_practico()

    print("\n" + "=" * 70)
    print(" FIN DE LAS PRUEBAS")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()