class Comparacion:
    def __init__(self,jugador1,jugador2,puntuacion_similitud):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.puntuacion_similitud = puntuacion_similitud
        
    
    def __eq__(self,other):
        mismo_orden = self.jugador1 == other.jugador1 and self.jugador2 == other.jugador2
        orden_invertido = self.jugador1 == other.jugador2 and self.jugador2 == other.jugador1
        return (mismo_orden or orden_invertido) and self.puntuacion_similitud == other.puntuacion_similitud