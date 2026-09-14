from datetime import date
class Jugador:
    def __init__(self, player_id: int, nombre: str, posicion: str, fecha_nacimiento: date) -> None:
        if not isinstance(player_id, int) or isinstance(player_id, bool):
            raise ValueError("El player_id debe ser un entero")
        if player_id <= 0:
            raise ValueError("El player_id debe ser un valor mayor que 0")
        if fecha_nacimiento > date.today():
            raise ValueError("La fecha no puede ser futura")
        self.player_id = player_id
        self.nombre = nombre
        self.posicion = posicion
        self.fecha_nacimiento = fecha_nacimiento

    def __eq__(self, other: "Jugador") -> bool:

       return self.player_id == other.player_id
