class PuntuacionSimilitud:
    def __init__(self, porcentaje: int) -> None:
        if not isinstance(porcentaje, int) or isinstance(porcentaje, bool):
            raise ValueError("El porcentaje debe ser un entero")
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe ser un valor entre 0 y 100")

        self.porcentaje = porcentaje

    def __eq__(self, other: PuntuacionSimilitud) -> bool:

        return self.porcentaje == other.porcentaje
