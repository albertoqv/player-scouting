class Estadisticas:
    def __init__(self, goles: int, asistencias: int) -> None:
        if not isinstance(goles, int) or isinstance(goles, bool):
            raise ValueError("Los goles deben ser un entero")
        if not isinstance(asistencias, int) or isinstance(asistencias, bool):
            raise ValueError("Las asistencias deben ser un entero")
        if goles < 0:
            raise ValueError("Los goles deben ser igual o mayor que 0")
        if asistencias < 0:
            raise ValueError("Las asistencias deben ser igual o mayor que 0")
        self.goles = goles
        self.asistencias = asistencias
