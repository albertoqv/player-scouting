import pytest
from player_scouting.domain.calculador_similitud import CalculadorDeSimilitud


def test_similitud_metrica_con_valores_iguales_es_uno():
    calculador = CalculadorDeSimilitud()

    resultado = calculador.similitud_metrica(10, 10)

    assert resultado == 1

def test_calcular_similitud_metrica_con_valores_distintos():
    calculador = CalculadorDeSimilitud()
    resultado = calculador.similitud_metrica(10, 12)
    assert resultado == pytest.approx(0.833, rel=0.01)