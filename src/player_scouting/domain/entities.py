class Jugador:
    def __init__(self,player_id,nombre,posicion,fecha_nacimiento):
        if not isinstance(player_id, int):
            raise ValueError("El player_id debe ser un entero")
        if player_id <= 0:
            raise ValueError("El player_id debe ser un valor mayor que 0")
        self.player_id = player_id
        self.nombre = nombre
        self.posicion = posicion
        self.fecha_nacimiento = fecha_nacimiento
    
    def __eq__(self,other):
        
       return self.player_id == other.player_id