import pytest
from player_scouting.domain.entities import Jugador
from datetime import date

def test_jugador_guarda_sus_datos_correctamente():
    resultado = Jugador(75,"Leo","Delantero",date(2003, 6, 5))
    assert resultado.player_id == 75
    assert resultado.nombre == "Leo"
    assert resultado.posicion == "Delantero"
    assert resultado.fecha_nacimiento == date(2003, 6, 5)

def test_dos_jugadores_con_el_mismo_player_id_son_iguales():
    a = Jugador(75,"Pepe","delantero",date(2003, 6, 5))
    b = Jugador(75,"Pep","delantero",date(2003, 6, 5))

    assert a == b

def test_jugador_rechaza_un_player_id_menor_o_igual_a_0():
    with pytest.raises(ValueError):
       Jugador(0,"Pep","delantero",date(2003, 6, 5))
