import pytest
from player_scouting.domain.estadisticas import Estadisticas

def test_estadisticas_guarda_sus_datos_correctamente():
    resultado = Estadisticas(15,20)
    assert resultado.goles == 15
    assert resultado.asistencias == 20

def test_estadisticas_rechaza_un_valor_de_goles_no_entero():
    with pytest.raises(ValueError):
        Estadisticas(15.5,20)
def test_estadisticas_rechaza_un_valor_de_asistencias_no_entero():
    with pytest.raises(ValueError):
        Estadisticas(15,20.5)

def test_estadisticas_goles_es_inferior_al_rango():
    with pytest.raises(ValueError):
        Estadisticas(-1,20)

def test_estadisticas_asistencias_es_inferior_al_rango():
    with pytest.raises(ValueError):
        Estadisticas(20,-1)