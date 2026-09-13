from player_scouting.domain.value_objects import PuntuacionSimilitud
class CalculadorDeSimilitud:
    def similitud_metrica(self,valor_a,valor_b):
        if valor_a == valor_b:
            return 1
        else:
            resultado = 1 - abs(valor_a - valor_b)/max(valor_a,valor_b)
            return resultado
    
    def similitud_total(self,estadistica_j1,estadistica_j2):
        similitud_goles = self.similitud_metrica(estadistica_j1.goles,estadistica_j2.goles)
        similitud_asistencias =self.similitud_metrica(estadistica_j1.asistencias,estadistica_j2.asistencias)
        media = (similitud_goles + similitud_asistencias) / 2
        porcentaje = round(media *100)
        return PuntuacionSimilitud(porcentaje)
