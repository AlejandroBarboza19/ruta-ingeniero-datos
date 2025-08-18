
"""class Celular():
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP"

Celular = Celular()
print(Celular.marca)"""

class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f"estas haciendo un llamado: {self.modelo}")

    def cortar(self):
        print(f"Cortaste la llamada desde un: {self.modelo}")

celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 15 pro","96MP")

celular1.llamar()
celular2.cortar()
 