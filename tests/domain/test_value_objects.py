import pytest

from player_scouting.domain.exceptions import InvalidSimilarityScoreError
from player_scouting.domain.value_objects import SimilarityScore


def test_puntuacion_similitud_se_crea_con_valor_valido():
    resultado = SimilarityScore(75)
    assert resultado.percentage == 75


def test_puntuacion_similitud_rechaza_un_valor_no_entero():
    with pytest.raises(InvalidSimilarityScoreError):
        SimilarityScore(75.5)


def test_puntuacion_similitud_supera_el_rango():
    with pytest.raises(InvalidSimilarityScoreError):
        SimilarityScore(120)


def test_puntuacion_similitud_es_inferior_al_rango():
    with pytest.raises(InvalidSimilarityScoreError):
        SimilarityScore(-5)


def test_dos_puntuaciones_con_el_mismo_valor_son_iguales():
    a = SimilarityScore(75)
    b = SimilarityScore(75)

    assert a == b


def test_puntuacion_similitud_rechaza_un_valor_booleano():
    with pytest.raises(InvalidSimilarityScoreError):
        SimilarityScore(True)
