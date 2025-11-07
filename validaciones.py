import re

def validar_horario(horario):
    if not isinstance(horario, str):
        return False

    patron = r"^([0-1]?[0-9]|2[0-3]):([0-5][0-9])$"
    return bool(re.match(patron, horario.strip()))

def validar_horario_estricto(horario):
    if not isinstance(horario, str):
        return False

    patron = r"^([0-1][0-9]|2[0-3]):([0-5][0-9])$"
    return bool(re.match(patron, horario.strip()))

def validar_dni(dni):
    if not isinstance(dni, str):
        return False

    patron = r"^\d{7,8}$"
    return bool(re.match(patron, dni.strip()))

def validar_dni_con_formato(dni):
    if not isinstance(dni, str):
        return False

    patron = r"^\d{1,2}\.?\d{3}\.?\d{3}$"
    return bool(re.match(patron, dni.strip()))

def limpiar_dni(dni):
    if not isinstance(dni, str):
        return ""

    return re.sub(r"[.\s-]", "", dni.strip())

def validar_butaca(butaca):
    if not isinstance(butaca, str):
        return False

    patron = r"^[A-I]([1-9]|[1-9][0-9])$"
    return bool(re.match(patron, butaca.strip().upper()))

def extraer_fila_columna(butaca):
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
    if not isinstance(titulo, str):
        return False

    titulo = titulo.strip()

    if len(titulo) == 0:
        return False

    patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ0-9\s\-:,.\'"()&]+$'
    return bool(re.match(patron, titulo))

def validar_nombre_persona(nombre):
    if not isinstance(nombre, str):
        return False

    nombre = nombre.strip()

    if len(nombre) < 2:
        return False

    patron = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s\-']+$"
    return bool(re.match(patron, nombre))

def validar_direccion(direccion):
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
    if not isinstance(nombre, str):
        return False

    nombre = nombre.strip()

    if len(nombre) < 2:
        return False

    patron = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ0-9\s\-&.]+$"
    return bool(re.match(patron, nombre))

def validar_numero_positivo(numero_str):
    if not isinstance(numero_str, str):
        return False

    patron = r"^[1-9]\d*$"
    return bool(re.match(patron, numero_str.strip()))

def validar_id(id_str):
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
    if not isinstance(formato, str):
        return False

    patron = r"^[23][dD]$"
    return bool(re.match(patron, formato.strip()))

def normalizar_formato(formato):
    if not validar_formato(formato):
        return ""

    return formato.strip().lower()

def validar_idioma(idioma, idiomas_validos=("español", "subtitulado")):
    if not isinstance(idioma, str):
        return False

    return idioma.strip().lower() in idiomas_validos

def normalizar_idioma(idioma):
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