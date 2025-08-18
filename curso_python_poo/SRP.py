class TanquedeCombustible:
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self,cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad
        



class Auto():
    def __init__(self,tanque):
        self.posicion = 0
        self.combustible = 100
        self.tanque = tanque
    
    def mover(sefl,distancia):
        if sefl.combustible >= distancia / 2:
            sefl.posicion += distancia
            sefl.combustible -= distancia /2
        else:
            print("no hay combustible")
    
    def obtener_posicion(self):
        return self.posicion
    
tanque = TanquedeCombustible()

autito = Auto(tanque)

print(autito.obtener_posicion())
autito.mover(10)
print(autito.obtener_posicion())
