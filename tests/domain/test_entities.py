from datetime import date, timedelta

import pytest

from player_scouting.domain.entities import Player

manana = date.today() + timedelta(days=1)


def test_jugador_guarda_sus_datos_correctamente():
    resultado = Player(75, "Leo", "Delantero", date(2003, 6, 5))
    assert resultado.player_id == 75
    assert resultado.name == "Leo"
    assert resultado.position == "Delantero"
    assert resultado.date_of_birth == date(2003, 6, 5)


def test_dos_jugadores_con_el_mismo_player_id_son_iguales():
    a = Player(75, "Pepe", "delantero", date(2003, 6, 5))
    b = Player(75, "Pep", "delantero", date(2003, 6, 5))

    assert a == b


def test_jugador_rechaza_un_player_id_menor_o_igual_a_0():
    with pytest.raises(ValueError):
        Player(0, "Pep", "delantero", date(2003, 6, 5))


def test_jugador_rechaza_un_player_id_no_entero():
    with pytest.raises(ValueError):
        Player(75.5, "Pep", "delantero", date(2003, 6, 5))


def test_jugador_rechaza_una_fecha_nacimiento_futura():
    with pytest.raises(ValueError):
        Player(75, "Pep", "delantero", manana)


def test_jugador_rechaza_un_player_id_booleano():
    with pytest.raises(ValueError):
        Player(True, "Pep", "delantero", date(2003, 6, 5))
