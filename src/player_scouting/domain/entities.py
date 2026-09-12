class Jugador:
    def __init__(self,player_id,nombre,posicion,fecha_nacimiento):
        
        self.player_id = player_id
        self.nombre = nombre
        self.posicion = posicion
        self.fecha_nacimiento = fecha_nacimiento
    
    def __eq__(self,other):
        
       return self.player_id == other.player_id