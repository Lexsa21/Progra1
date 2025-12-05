import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

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
    formatearPreciosEntradas,
    obtenerTitulosPeliculasMayusculas,
    aplicarDescuentoPrecios,
    contarButacasDisponiblesRecursivo,
    obtenerPrimerasPeliculas,
    obtenerPeliculasPorFormato,
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

def test_peliculas_por_cine():
    resultado = peliculasPorCine("1")
    assert "1" in resultado and "6" in resultado

def test_contar_butacas_recursivo():
    butacas = {
        "A1": {"ocupado": False, "habilitado": True, "tipo": "normal"},
        "A2": {"ocupado": True, "habilitado": True, "tipo": "normal"},
        "A3": {"ocupado": False, "habilitado": False, "tipo": "normal"},
        "A4": {"ocupado": False, "habilitado": True, "tipo": "extreme"}
    }
    resultado = contarButacasDisponiblesRecursivo(butacas)
    assert resultado == 2 
    assert len(butacas) == 4

def test_obtener_primeras_peliculas():
    peliculas = {
        "1": {"titulo": "A", "activo": True},
        "2": {"titulo": "B", "activo": True},
        "3": {"titulo": "C", "activo": True},
        "4": {"titulo": "D", "activo": True}
    }
    primeras = obtenerPrimerasPeliculas(peliculas, 2)
    assert len(primeras) == 2