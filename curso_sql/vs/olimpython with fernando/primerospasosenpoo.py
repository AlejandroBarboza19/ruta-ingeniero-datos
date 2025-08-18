class coche(): 
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} ha arrancado")

carro_de_valentina = coche("Mazda","2","rosado")
carro_de_alejo = coche("Mercedes","Benz","Blanco")

carro_de_valentina.arrancar()
carro_de_alejo.arrancar()





