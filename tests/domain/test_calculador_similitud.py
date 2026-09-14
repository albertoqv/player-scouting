import pytest

from player_scouting.domain.similarity_calculator import SimilarityCalculator
from player_scouting.domain.statistics import Statistics
from player_scouting.domain.value_objects import SimilarityScore


def test_similitud_metrica_con_valores_iguales_es_uno():
    calculador = SimilarityCalculator()

    resultado = calculador.similarity_metric(10, 10)

    assert resultado == 1


def test_calcular_similitud_metrica_con_valores_distintos():
    calculador = SimilarityCalculator()
    resultado = calculador.similarity_metric(10, 12)
    assert resultado == pytest.approx(0.833, rel=0.01)


def test_calcular_similitud_total():
    estadistica_j1 = Statistics(10, 15)
    estadistica_j2 = Statistics(15, 10)
    calculador = SimilarityCalculator()
    resultado = calculador.total_similarity(estadistica_j1, estadistica_j2)
    assert resultado == SimilarityScore(67)
