import pytest
from player_scouting.domain.value_objects import PuntuacionSimilitud

def test_puntuacion_similitud_se_crea_con_valor_valido():
    resultado = PuntuacionSimilitud(75)
    assert resultado.porcentaje == 75

def test_puntuacion_similitud_rechaza_un_valor_no_entero():
    with pytest.raises(ValueError):
        PuntuacionSimilitud(75.5)

def test_puntuacion_similitud_supera_el_rango():
     with pytest.raises(ValueError):
        PuntuacionSimilitud(120)

def test_puntuacion_similitud_es_inferior_al_rango():
     with pytest.raises(ValueError):
        PuntuacionSimilitud(-5)
        