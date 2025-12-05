import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
import re
import validaciones as v


@pytest.mark.parametrize("horario,esperado", [
    ("00:00", True),
    ("23:59", True),
    ("7:30", True),
    ("24:00", False),
    ("abc", False),
    (123, False),
])
def test_validar_horario(horario, esperado):
    assert v.validar_horario(horario) == esperado


@pytest.mark.parametrize("horario,esperado", [
    ("07:30", True),
    ("7:30", False),
    ("23:59", True),
])
def test_validar_horario_estricto(horario, esperado):
    assert v.validar_horario_estricto(horario) == esperado


@pytest.mark.parametrize("dni,esperado", [
    ("1234567", True),
    ("12345678", True),
    ("1234", False),
    ("abc", False),
])
def test_validar_dni(dni, esperado):
    assert v.validar_dni(dni) == esperado


@pytest.mark.parametrize("dni,esperado", [
    ("12.345.678", True),
    ("12345678", True),
    ("1.234.56", False),
])
def test_validar_dni_con_formato(dni, esperado):
    assert v.validar_dni_con_formato(dni) == esperado


def test_limpiar_dni():
    assert v.limpiar_dni("12.345.678") == "12345678"
    assert v.limpiar_dni(" 123-45678 ") == "12345678"
    assert v.limpiar_dni(12345678) == ""


@pytest.mark.parametrize("butaca,esperado", [
    ("A1", True),
    ("H8", True),
    ("Z1", False),
    ("A-1", False),
])
def test_validar_butaca(butaca, esperado):
    assert v.validar_butaca(butaca) == esperado


def test_extraer_fila_columna():
    assert v.extraer_fila_columna("A10") == ("A", 10)
    assert v.extraer_fila_columna("B5") == ("B", 5)
    assert v.extraer_fila_columna("Z1") == (None, None)


def test_validar_titulo_y_nombre():
    assert v.validar_titulo("Avatar 2: El Camino del Agua")
    assert not v.validar_titulo("")
    assert v.validar_nombre_persona("Juan Pérez")
    assert not v.validar_nombre_persona("J")
    assert not v.validar_nombre_persona(123)


def test_validar_direccion_y_nombre_cine():
    assert v.validar_direccion("Av. Corrientes 1234")
    assert not v.validar_direccion("12345")  # solo números
    assert v.validar_nombre_cine("Cine Atlas")
    assert v.validar_nombre_cine("Hoyts 3D")
    assert not v.validar_nombre_cine("")



def test_validar_numero_positivo_y_id():
    assert v.validar_numero_positivo("5")
    assert not v.validar_numero_positivo("0")
    assert not v.validar_numero_positivo("-3")
    assert v.validar_id("10")
    assert not v.validar_id("0")


@pytest.mark.parametrize("num,minimo,maximo,esperado", [
    ("5", 1, 10, True),
    ("-1", None, None, True),
    ("0", 1, 5, False),
    ("100", None, 99, False),
])
def test_validar_rango_numerico(num, minimo, maximo, esperado):
    assert v.validar_rango_numerico(num, minimo, maximo) == esperado



def test_validar_opcion_y_confirmacion():
    opciones = ["1", "2", "3"]
    assert v.validar_opcion_menu("1", opciones)
    assert not v.validar_opcion_menu("5", opciones)
    assert v.validar_confirmacion("sí") is True
    assert v.validar_confirmacion("no") is False
    assert v.validar_confirmacion("quizás") is None



def test_validar_formato_y_idioma():
    assert v.validar_formato("2D")
    assert v.normalizar_formato("3D") == "3d"
    assert not v.validar_formato("4D")

    assert v.validar_idioma("Español")
    assert not v.validar_idioma("Inglés")
    assert v.normalizar_idioma("SUBTITULADO") == "subtitulado"


def test_validar_y_normalizar_dia_semana():
    assert v.validar_dia_semana("lunes")
    assert v.validar_dia_semana("lun")
    assert not v.validar_dia_semana("xyz")

    assert v.normalizar_dia_semana("Lun") == "lunes"
    assert v.normalizar_dia_semana("Miércoles") == "miercoles"
    assert v.normalizar_dia_semana("abc") == ""


def test_limpieza_de_texto():
    assert v.limpiar_entrada(" Hola \n Mundo ") == "Hola Mundo"
    assert v.limpiar_espacios_multiples("Hola   Mundo") == "Hola Mundo"
    assert v.remover_caracteres_especiales("Hola@Mundo!") == "HolaMundo"
    assert v.remover_caracteres_especiales("Hola-Mundo", "-") == "Hola-Mundo"


def test_busqueda_y_extraccion():
    assert v.buscar_flexible("mundo", "Hola Mundo")
    assert not v.buscar_flexible("python", "Hola Mundo")
    assert v.buscar_palabra_completa("Hola", "Hola Mundo")
    assert not v.buscar_palabra_completa("Hol", "Hola Mundo")
    assert v.extraer_numeros("Calle 123 y 456") == ["123", "456"]


def test_validar_entrada_completa():
    ok, limpio, msg = v.validar_entrada_completa("14:30", "horario")
    assert ok and limpio == "14:30" and msg == ""

    ok, limpio, msg = v.validar_entrada_completa("A10", "butaca")
    assert ok and limpio == "A10"

    ok, limpio, msg = v.validar_entrada_completa("Pino 123", "direccion")
    assert ok

    ok, limpio, msg = v.validar_entrada_completa("subtitulado", "idioma")
    assert ok and limpio == "subtitulado"

    ok, limpio, msg = v.validar_entrada_completa("99999999", "dni")
    assert ok and limpio == "99999999"

    ok, limpio, msg = v.validar_entrada_completa("Invalido", "tipo_que_no_existe")
    assert not ok and msg == "Tipo de validación no reconocido"
