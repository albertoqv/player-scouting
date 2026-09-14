from datetime import date

from player_scouting.domain.comparison import Comparison
from player_scouting.domain.entities import Player
from player_scouting.domain.value_objects import SimilarityScore


def test_comparacion_guarda_sus_datos_correctamente():
    jugador1 = Player(75, "Leo", "Delantero", date(2003, 6, 5))
    jugador2 = Player(80, "Kylian", "Delantero", date(1998, 12, 20))
    puntuacion_similitud = SimilarityScore(75)
    resultado = Comparison(jugador1, jugador2, puntuacion_similitud)
    assert resultado.player1 == Player(75, "Leo", "Delantero", date(2003, 6, 5))
    assert resultado.player2 == Player(80, "Kylian", "Delantero", date(1998, 12, 20))
    assert resultado.similarity_score == SimilarityScore(75)


def test_dos_comparaciones_con_los_mismos_jugadores_son_iguales():
    jugador1 = Player(75, "Pepe", "delantero", date(2003, 6, 5))
    jugador2 = Player(80, "Kylian", "Delantero", date(1998, 12, 20))
    puntuacion_similitud = SimilarityScore(75)
    a = Comparison(jugador1, jugador2, puntuacion_similitud)
    b = Comparison(jugador2, jugador1, puntuacion_similitud)

    assert a == b
