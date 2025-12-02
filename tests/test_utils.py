import json
import pytest
from utils import (
    generarAsientosSala,
    generarId,
    butacasPorTipo,
    butacasDisponiblesPorTipo,
    informeButacasDisponibles,
    peliculasPorCine,
    cinesSinPeliculas,
    peliculasEnTodosCines,
)


def test_generar_asientos_sala():
    asientos = generarAsientosSala()
    assert isinstance(asientos, dict)
    assert len(asientos) == 64
    assert "A1" in asientos
    assert asientos["A1"]["tipo"] == "extreme"
    assert asientos["A3"]["tipo"] == "extreme"
    assert asientos["H8"]["tipo"] == "normal"

def test_generar_id():
    dic = {"1": {}, "2": {}, "3": {}}
    nuevo = generarId(dic)
    assert nuevo == "4"

def test_generar_id_diccionario_vacio():
    dic = {}
    nuevo = generarId(dic)
    assert nuevo == "1"

def test_butacas_por_tipo():
    asientos = generarAsientosSala()
    extreme = butacasPorTipo(asientos, "extreme")
    normal = butacasPorTipo(asientos, "normal")
    assert all(asientos[b]["tipo"] == "extreme" for b in extreme)
    assert all(asientos[b]["tipo"] == "normal" for b in normal)
    assert len(extreme) + len(normal) == len(asientos)

def test_informe_butacas_disponibles():
    asientos = generarAsientosSala()
    disponibles = informeButacasDisponibles(asientos)
    assert isinstance(disponibles, set)
    assert len(disponibles) == 64
    asientos["A1"]["ocupado"] = True
    disponibles = informeButacasDisponibles(asientos)
    assert "A1" not in disponibles

def test_butacas_disponibles_por_tipo():
    asientos = generarAsientosSala()
    disponibles_extreme = butacasDisponiblesPorTipo(asientos, "extreme")
    assert all(asientos[b]["tipo"] == "extreme" for b in disponibles_extreme)
    asiento = list(disponibles_extreme)[0]
    asientos[asiento]["ocupado"] = True
    disponibles_extreme_nuevo = butacasDisponiblesPorTipo(asientos, "extreme")
    assert asiento not in disponibles_extreme_nuevo

def test_peliculas_por_cine(monkeypatch):
    peliculas = {
        "1": {"titulo": "Avatar", "complejos": {"C1", "C2"}},
        "2": {"titulo": "Matrix", "complejos": {"C2"}},
    }

    monkeypatch.setattr("utils.obtenerPeliculas", lambda: peliculas)
    resultado = peliculasPorCine("C2")
    assert "1" in resultado and "2" in resultado

def test_cines_sin_peliculas(monkeypatch):
    peliculas = {
        "1": {"titulo": "Avatar", "complejos": {"C1"}},
    }
    monkeypatch.setattr("utils.obtenerPeliculas", lambda: peliculas)
    todosCines = {"C1", "C2", "C3"}
    resultado = cinesSinPeliculas(todosCines)
    assert resultado == {"C2", "C3"}

def test_peliculas_en_todos_cines(monkeypatch):
    peliculas = {
        "1": {"titulo": "Avatar", "complejos": {"C1", "C2"}},
        "2": {"titulo": "Matrix", "complejos": {"C1"}},
    }
    monkeypatch.setattr("utils.obtenerPeliculas", lambda: peliculas)
    resultado = peliculasEnTodosCines({"C1", "C2"})
    assert "1" in resultado
    assert "2" not in resultado

# Agregar tests para las funciones de Hito 2 y 3:

def test_formatear_precios_entradas(monkeypatch):
    precios = {"2d": 2500, "3d": 3500}
    monkeypatch.setattr("utils.obtenerPreciosEntradas", lambda: precios)
    formateados = formatearPreciosEntradas()
    assert "2D: $2,500" in formateados
    assert "3D: $3,500" in formateados

def test_obtener_titulos_mayusculas(monkeypatch):
    peliculas = {
        "1": {"titulo": "Avatar", "activo": True},
        "2": {"titulo": "Matrix", "activo": True}
    }
    monkeypatch.setattr("utils.obtenerPeliculas", lambda: peliculas)
    titulos = obtenerTitulosPeliculasMayusculas()
    assert "AVATAR" in titulos
    assert "MATRIX" in titulos

def test_aplicar_descuento_precios(monkeypatch):
    precios = {"2d": 1000, "3d": 2000}
    monkeypatch.setattr("utils.obtenerPreciosEntradas", lambda: precios)
    con_descuento = aplicarDescuentoPrecios(10)
    assert con_descuento["2d"] == 900
    assert con_descuento["3d"] == 1800

def test_contar_butacas_recursivo():
    butacas = {
        "A1": {"ocupado": False, "habilitado": True, "tipo": "normal"},
        "A2": {"ocupado": True, "habilitado": True, "tipo": "normal"},
        "A3": {"ocupado": False, "habilitado": False, "tipo": "normal"},
        "A4": {"ocupado": False, "habilitado": True, "tipo": "extreme"}
    }
    resultado = contarButacasDisponiblesRecursivo(butacas)
    assert resultado == 2  # Solo A1 y A4 están disponibles
    assert len(butacas) == 4  # Verificar que no se modificó el diccionario

def test_obtener_primeras_peliculas(monkeypatch):
    peliculas = {
        "1": {"titulo": "A", "activo": True},
        "2": {"titulo": "B", "activo": True},
        "3": {"titulo": "C", "activo": True},
        "4": {"titulo": "D", "activo": True}
    }
    monkeypatch.setattr("utils.obtenerPeliculas", lambda: peliculas)
    primeras = obtenerPrimerasPeliculas(peliculas, 2)
    assert len(primeras) == 2

def test_obtener_peliculas_por_formato(monkeypatch):
    peliculas = {
        "1": {"titulo": "Avatar", "formato": "3d"},
        "2": {"titulo": "Matrix", "formato": "2d"}
    }
    monkeypatch.setattr("utils.obtenerPeliculas", lambda: peliculas)
    pelis_3d = obtenerPeliculasPorFormato("3d")
    assert "1" in pelis_3d
    assert "2" not in pelis_3d