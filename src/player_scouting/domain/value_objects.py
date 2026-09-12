class PuntuacionSimilitud:
    def __init__(self,porcentaje):
        if not isinstance(porcentaje, int):
             raise ValueError("El porcentaje debe ser un entero")
        self.porcentaje = porcentaje
