import pytest
from player_scouting.domain.estadisticas import Estadisticas

def test_estadisticas_guarda_sus_datos_correctamente():
    resultado = Estadisticas(15,20)
    assert resultado.goles == 15
    assert resultado.asistencias == 20