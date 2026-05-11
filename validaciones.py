import re

def validar_horario(horario):
    """Valida que el horario tenga formato H:MM o HH:MM (00:00 a 23:59). Acepta hora sin cero inicial."""
    if not isinstance(horario, str):
        return False

    patron = r"^([0-1]?[0-9]|2[0-3]):([0-5][0-9])$"
    return bool(re.match(patron, horario.strip()))

def validar_horario_estricto(horario):
    """Valida horario en formato estricto HH:MM (requiere cero inicial, ej: 07:30)."""
    if not isinstance(horario, str):
        return False

    patron = r"^([0-1][0-9]|2[0-3]):([0-5][0-9])$"
    return bool(re.match(patron, horario.strip()))

def validar_dni(dni):
    """Valida que el DNI contenga entre 7 y 8 dígitos sin puntos ni espacios."""
    if not isinstance(dni, str):
        return False

    patron = r"^\d{7,8}$"
    return bool(re.match(patron, dni.strip()))

def validar_dni_con_formato(dni):
    """Valida DNI con o sin puntos separadores (ej: 12.345.678 o 12345678)."""
    if not isinstance(dni, str):
        return False

    patron = r"^\d{1,2}\.?\d{3}\.?\d{3}$"
    return bool(re.match(patron, dni.strip()))

def limpiar_dni(dni):
    """Elimina puntos, espacios y guiones de un DNI para dejarlo solo con dígitos."""
    if not isinstance(dni, str):
        return ""

    return re.sub(r"[.\s-]", "", dni.strip())

def validar_butaca(butaca):
    """Valida que el código de butaca tenga formato Letra(A-I) + Número(1-99). Ej: A1, H8."""
    if not isinstance(butaca, str):
        return False

    patron = r"^[A-I]([1-9]|[1-9][0-9])$"
    return bool(re.match(patron, butaca.strip().upper()))

def extraer_fila_columna(butaca):
    """Extrae la fila (letra) y columna (número) de un código de butaca. Retorna (None, None) si es inválido."""
    if not validar_butaca(butaca):
        return None, None

    patron = r"^([A-I])(\d+)$"
    match = re.match(patron, butaca.strip().upper())

    if match:
        fila = match.group(1)
        columna = int(match.group(2))
        return fila, columna

    return None, None

def validar_titulo(titulo):
    """Valida que el título no esté vacío y solo contenga caracteres permitidos (letras, números y símbolos básicos)."""
    if not isinstance(titulo, str):
        return False

    titulo = titulo.strip()

    if len(titulo) == 0:
        return False

    patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ0-9\s\-:,.\'"()&]+$'
    return bool(re.match(patron, titulo))

def validar_nombre_persona(nombre):
    """Valida que el nombre tenga al menos 2 caracteres y solo contenga letras, espacios y guiones."""
    if not isinstance(nombre, str):
        return False

    nombre = nombre.strip()

    if len(nombre) < 2:
        return False

    patron = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s\-']+$"
    return bool(re.match(patron, nombre))

def validar_direccion(direccion):
    """Valida que la dirección tenga al menos 5 caracteres, una letra y un número (ej: Av. Corrientes 1234)."""
    if not isinstance(direccion, str):
        return False

    direccion = direccion.strip()

    if len(direccion) < 5:
        return False

    patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ0-9\s\-,.\'"#º°]+$'

    tiene_letra = bool(re.search(r"[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]", direccion))
    tiene_numero = bool(re.search(r"\d", direccion))

    return bool(re.match(patron, direccion)) and tiene_letra and tiene_numero

def validar_nombre_cine(nombre):
    """Valida que el nombre del cine tenga al menos 2 caracteres y solo use letras, números y símbolos básicos."""
    if not isinstance(nombre, str):
        return False

    nombre = nombre.strip()

    if len(nombre) < 2:
        return False

    patron = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ0-9\s\-&.]+$"
    return bool(re.match(patron, nombre))

def validar_numero_positivo(numero_str):
    """Valida que el string represente un número entero positivo (mayor a 0, sin ceros iniciales)."""
    if not isinstance(numero_str, str):
        return False

    patron = r"^[1-9]\d*$"
    return bool(re.match(patron, numero_str.strip()))

def validar_id(id_str):
    """Valida que el string sea un ID válido (número entero positivo)."""
    return validar_numero_positivo(id_str)

def validar_rango_numerico(numero_str, minimo=None, maximo=None):
    if not isinstance(numero_str, str):
        return False

    patron = r"^-?\d+$"
    if not re.match(patron, numero_str.strip()):
        return False

    numero = int(numero_str.strip())

    if minimo is not None and numero < minimo:
        return False

    if maximo is not None and numero > maximo:
        return False

    return True

def validar_opcion_menu(opcion, opciones_validas):
    if not isinstance(opcion, str):
        return False

    return opcion.strip() in opciones_validas

def validar_confirmacion(respuesta):
    """Valida respuesta s/n. Retorna True para afirmativo, False para negativo, None si es inválida."""
    if not isinstance(respuesta, str):
        return None

    respuesta = respuesta.strip().lower()

    patron_si = r"^(s|si|sí|yes|y)$"
    if re.match(patron_si, respuesta):
        return True

    patron_no = r"^(n|no)$"
    if re.match(patron_no, respuesta):
        return False

    return None

def validar_formato(formato):
    """Valida que el formato sea 2D o 3D (case-insensitive)."""
    if not isinstance(formato, str):
        return False

    patron = r"^[23][dD]$"
    return bool(re.match(patron, formato.strip()))

def normalizar_formato(formato):
    """Normaliza el formato a minúsculas (ej: 3D -> 3d). Retorna string vacío si es inválido."""
    if not validar_formato(formato):
        return ""

    return formato.strip().lower()

def validar_idioma(idioma, idiomas_validos=("español", "subtitulado")):
    if not isinstance(idioma, str):
        return False

    return idioma.strip().lower() in idiomas_validos

def normalizar_idioma(idioma):
    """Normaliza el idioma a minúsculas sin espacios extra. Retorna string vacío si la entrada no es string."""
    if not isinstance(idioma, str):
        return ""

    return idioma.strip().lower()

def validar_dia_semana(
    dia,
    dias_validos=(
        "lunes",
        "martes",
        "miercoles",
        "jueves",
        "viernes",
        "sabado",
        "domingo",
    ),
):
    if not isinstance(dia, str):
        return False

    dia = dia.strip().lower()

    if dia in dias_validos:
        return True

    abreviaciones = {
        "lun": "lunes",
        "mar": "martes",
        "mie": "miercoles",
        "jue": "jueves",
        "vie": "viernes",
        "sab": "sabado",
        "dom": "domingo",
    }

    return dia in abreviaciones

def normalizar_dia_semana(dia):
    if not isinstance(dia, str):
        return ""

    dia = dia.strip().lower()

    dia = dia.replace("á", "a").replace("é", "e").replace("í", "i")
    dia = dia.replace("ó", "o").replace("ú", "u")

    abreviaciones = {
        "lun": "lunes",
        "mar": "martes",
        "mie": "miercoles",
        "jue": "jueves",
        "vie": "viernes",
        "sab": "sabado",
        "dom": "domingo",
    }

    if dia in abreviaciones:
        return abreviaciones[dia]

    dias_validos = (
        "lunes",
        "martes",
        "miercoles",
        "jueves",
        "viernes",
        "sabado",
        "domingo",
    )
    if dia in dias_validos:
        return dia

    return ""

def limpiar_entrada(texto):
    """Limpia una entrada de usuario: reemplaza saltos de línea y tabs por espacios, y colapsa espacios múltiples."""
    if not isinstance(texto, str):
        return ""

    texto = re.sub(r"[\t\n\r\f\v]", " ", texto)

    texto = re.sub(r"\s+", " ", texto)

    return texto.strip()

def limpiar_espacios_multiples(texto):
    if not isinstance(texto, str):
        return ""

    return re.sub(r"\s+", " ", texto).strip()

def remover_caracteres_especiales(texto, permitidos=""):
    if not isinstance(texto, str):
        return ""

    permitidos_escaped = re.escape(permitidos)

    patron = r"[^a-zA-ZáéíóúÁÉÍÓÚñÑüÜ0-9\s" + permitidos_escaped + r"]"

    return re.sub(patron, "", texto)

def buscar_flexible(termino, texto):
    if not isinstance(termino, str) or not isinstance(texto, str):
        return False

    patron = re.compile(re.escape(termino), re.IGNORECASE)
    return bool(patron.search(texto))

def buscar_palabra_completa(palabra, texto):
    if not isinstance(palabra, str) or not isinstance(texto, str):
        return False

    patron = r"\b" + re.escape(palabra) + r"\b"
    return bool(re.search(patron, texto, re.IGNORECASE))

def extraer_numeros(texto):
    if not isinstance(texto, str):
        return []

    return re.findall(r"\d+", texto)

def validar_entrada_completa(entrada, tipo_validacion, **kwargs):
    """
    Función unificada de validación que limpia y valida una entrada según su tipo.
    Tipos soportados: horario, dni, butaca, titulo, nombre, direccion, numero_positivo, id, formato, idioma, dia.
    Retorna una tupla (es_valido: bool, valor_limpio: str, mensaje_error: str).
    """
    if not isinstance(entrada, str):
        return False, "", "Entrada inválida"

    entrada_limpia = limpiar_entrada(entrada)

    if tipo_validacion == "horario":
        if validar_horario(entrada_limpia):
            return True, entrada_limpia, ""
        return False, "", "Horario inválido. Use formato HH:MM (00:00 - 23:59)"

    elif tipo_validacion == "dni":
        dni_limpio = limpiar_dni(entrada_limpia)
        if validar_dni(dni_limpio):
            return True, dni_limpio, ""
        return False, "", "DNI inválido. Debe contener 7 u 8 dígitos"

    elif tipo_validacion == "butaca":
        if validar_butaca(entrada_limpia):
            return True, entrada_limpia.upper(), ""
        return False, "", "Butaca inválida. Use formato: Letra (A-I) + Número (1-99)"

    elif tipo_validacion == "titulo":
        if validar_titulo(entrada_limpia):
            return True, entrada_limpia, ""
        return False, "", "Título inválido. Use solo letras, números y símbolos básicos"

    elif tipo_validacion == "nombre":
        if validar_nombre_persona(entrada_limpia):
            return True, entrada_limpia, ""
        return False, "", "Nombre inválido. Use solo letras, espacios y guiones"

    elif tipo_validacion == "direccion":
        if validar_direccion(entrada_limpia):
            return True, entrada_limpia, ""
        return False, "", "Dirección inválida. Debe contener calle y número"

    elif tipo_validacion == "numero_positivo":
        if validar_numero_positivo(entrada_limpia):
            return True, entrada_limpia, ""
        return False, "", "Debe ser un número entero positivo"

    elif tipo_validacion == "id":
        if validar_id(entrada_limpia):
            return True, entrada_limpia, ""
        return False, "", "ID inválido. Debe ser un número positivo"

    elif tipo_validacion == "formato":
        if validar_formato(entrada_limpia):
            formato_norm = normalizar_formato(entrada_limpia)
            return True, formato_norm, ""
        return False, "", "Formato inválido. Use: 2D o 3D"

    elif tipo_validacion == "idioma":
        idiomas = kwargs.get("idiomas_validos", ("español", "subtitulado"))
        if validar_idioma(entrada_limpia, idiomas):
            idioma_norm = normalizar_idioma(entrada_limpia)
            return True, idioma_norm, ""
        return False, "", f"Idioma inválido. Opciones: {', '.join(idiomas)}"

    elif tipo_validacion == "dia":
        if validar_dia_semana(entrada_limpia):
            dia_norm = normalizar_dia_semana(entrada_limpia)
            return True, dia_norm, ""
        return (
            False,
            "",
            "Día inválido. Use nombre completo o abreviación (lun, mar, etc.)",
        )

    else:
        return False, "", "Tipo de validación no reconocido"