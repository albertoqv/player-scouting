class CalculadorDeSimilitud:
    def similitud_metrica(self,valor_a,valor_b):
        if valor_a == valor_b:
            return 1
        else:
            resultado = 1 - abs(valor_a - valor_b)/max(valor_a,valor_b)
            return resultado