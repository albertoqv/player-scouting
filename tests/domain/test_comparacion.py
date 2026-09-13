import pytest
from player_scouting.domain.entities import Jugador
from datetime import date, timedelta
from player_scouting.domain.value_objects import PuntuacionSimilitud
from player_scouting.domain.comparacion import Comparacion


def test_comparacion_guarda_sus_datos_correctamente():
    jugador1 = Jugador(75, "Leo", "Delantero", date(2003, 6, 5))
    jugador2 = Jugador(80, "Kylian", "Delantero", date(1998, 12, 20))
    puntuacion_similitud = PuntuacionSimilitud(75)
    resultado = Comparacion(jugador1,jugador2,puntuacion_similitud)
    assert resultado.jugador1 == Jugador(75, "Leo", "Delantero", date(2003, 6, 5))
    assert resultado.jugador2 == Jugador(80, "Kylian", "Delantero", date(1998, 12, 20))
    assert resultado.puntuacion_similitud == PuntuacionSimilitud(75)

def test_dos_comparaciones_con_los_mismos_jugadores_son_iguales():
    jugador1 = Jugador(75,"Pepe","delantero",date(2003, 6, 5))
    jugador2 = Jugador(80, "Kylian", "Delantero", date(1998, 12, 20))
    puntuacion_similitud = PuntuacionSimilitud(75)
    a = Comparacion(jugador1,jugador2,puntuacion_similitud)
    b = Comparacion(jugador2,jugador1,puntuacion_similitud)


    assert a == b