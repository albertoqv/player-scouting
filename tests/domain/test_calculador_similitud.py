import pytest
from player_scouting.domain.calculador_similitud import CalculadorDeSimilitud


def test_similitud_metrica_con_valores_iguales_es_uno():
    calculador = CalculadorDeSimilitud()

    resultado = calculador.similitud_metrica(10, 10)

    assert resultado == 1