class Vehiculo():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
            print(f"el vehiculo de marca {self.marca} de modelo {self.modelo} se mueve ")

class Moto(Vehiculo):
    def mover(self):
        print(f"La moto {self.marca} {self.modelo} avanza sobre dos ruedas")

class Camion(Vehiculo):
    def mover(self):
        print(f"El camion {self.marca} {self.modelo} avanza lentamente")

vehiculos = [Moto("nMax","250"), Camion("Toyota","Fortune")]

for vehiculo in vehiculos:
     vehiculo.mover()

    




