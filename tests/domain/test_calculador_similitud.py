import pytest
from player_scouting.domain.calculador_similitud import CalculadorDeSimilitud
from player_scouting.domain.estadisticas import Estadisticas
from player_scouting.domain.value_objects import PuntuacionSimilitud

def test_similitud_metrica_con_valores_iguales_es_uno():
    calculador = CalculadorDeSimilitud()

    resultado = calculador.similitud_metrica(10, 10)

    assert resultado == 1

def test_calcular_similitud_metrica_con_valores_distintos():
    calculador = CalculadorDeSimilitud()
    resultado = calculador.similitud_metrica(10, 12)
    assert resultado == pytest.approx(0.833, rel=0.01)

def test_calcular_similitud_total():
    estadistica_j1 = Estadisticas(10,15)
    estadistica_j2 = Estadisticas(15,10)
    calculador = CalculadorDeSimilitud()
    resultado = calculador.similitud_total(estadistica_j1,estadistica_j2)
    assert resultado == PuntuacionSimilitud(67)