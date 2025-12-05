import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
import re
import validaciones as v


def test_validar_horario_00_00():
    assert v.validar_horario("00:00") == True

def test_validar_horario_23_59():
    assert v.validar_horario("23:59") == True

def test_validar_horario_7_30():
    assert v.validar_horario("7:30") == True

def test_validar_horario_24_00():
    assert v.validar_horario("24:00") == False

def test_validar_horario_abc():
    assert v.validar_horario("abc") == False

def test_validar_horario_123():
    assert v.validar_horario(123) == False


def test_validar_horario_estricto_07_30():
    assert v.validar_horario_estricto("07:30") == True

def test_validar_horario_estricto_7_30():
    assert v.validar_horario_estricto("7:30") == False

def test_validar_horario_estricto_23_59():
    assert v.validar_horario_estricto("23:59") == True


def test_validar_dni_1234567():
    assert v.validar_dni("1234567") == True

def test_validar_dni_12345678():
    assert v.validar_dni("12345678") == True

def test_validar_dni_1234():
    assert v.validar_dni("1234") == False

def test_validar_dni_abc():
    assert v.validar_dni("abc") == False


def test_validar_dni_con_formato_12_345_678():
    assert v.validar_dni_con_formato("12.345.678") == True

def test_validar_dni_con_formato_12345678():
    assert v.validar_dni_con_formato("12345678") == True

def test_validar_dni_con_formato_1_234_56():
    assert v.validar_dni_con_formato("1.234.56") == False


def test_limpiar_dni():
    assert v.limpiar_dni("12.345.678") == "12345678"
    assert v.limpiar_dni(" 123-45678 ") == "12345678"
    assert v.limpiar_dni(12345678) == ""


def test_validar_butaca_A1():
    assert v.validar_butaca("A1") == True

def test_validar_butaca_H8():
    assert v.validar_butaca("H8") == True

def test_validar_butaca_Z1():
    assert v.validar_butaca("Z1") == False

def test_validar_butaca_A_1():
    assert v.validar_butaca("A-1") == False


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


def test_validar_rango_numerico_5_1_10():
    assert v.validar_rango_numerico("5", 1, 10) == True

def test_validar_rango_numerico_neg1_none_none():
    assert v.validar_rango_numerico("-1", None, None) == True

def test_validar_rango_numerico_0_1_5():
    assert v.validar_rango_numerico("0", 1, 5) == False

def test_validar_rango_numerico_100_none_99():
    assert v.validar_rango_numerico("100", None, 99) == False



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
