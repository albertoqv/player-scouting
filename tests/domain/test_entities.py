import pytest
from player_scouting.domain.entities import Jugador
from datetime import date

def test_dos_jugadores_con_el_mismo_player_id_son_iguales():
    a = Jugador(75,"Pepe","delantero",date(2003, 6, 5))
    b = Jugador(75,"Pep","delantero",date(2003, 6, 5))

    assert a == b