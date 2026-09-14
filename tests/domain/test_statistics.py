import pytest

from player_scouting.domain.statistics import Statistics


def test_estadisticas_guarda_sus_datos_correctamente():
    resultado = Statistics(15, 20)
    assert resultado.goals == 15
    assert resultado.assists == 20


def test_estadisticas_rechaza_un_valor_de_goles_no_entero():
    with pytest.raises(ValueError):
        Statistics(15.5, 20)


def test_estadisticas_rechaza_un_valor_de_asistencias_no_entero():
    with pytest.raises(ValueError):
        Statistics(15, 20.5)


def test_estadisticas_goles_es_inferior_al_rango():
    with pytest.raises(ValueError):
        Statistics(-1, 20)


def test_estadisticas_asistencias_es_inferior_al_rango():
    with pytest.raises(ValueError):
        Statistics(20, -1)


def test_estadisticas_rechaza_un_valor_de_goles_booleano():
    with pytest.raises(ValueError):
        Statistics(True, 20)


def test_estadisticas_rechaza_un_valor_de_asistencias_booleano():
    with pytest.raises(ValueError):
        Statistics(15, True)
