#Herencias - Ejercicio 2.1

class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y mi edad es {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def migrado(self):
        print(f"mi grado es {self.grado}")

estudiante1 = Estudiante("Valentina",19,"noveno")

estudiante1.presentarse()
estudiante1.migrado()
print("_____________________________________________\n")


#MRO y Herencias # ejercicio 2.2

class Animal:
    def comer(self):
        print("comiendo...")

class Mamifero(Animal):
    def amamantar(self):
        print("amamantando...")

class Ave(Animal):
    def volar(self):
        print("Volando...")

class murcielago(Mamifero,Ave):
    pass

batman = murcielago()
batman.amamantar()
batman.volar()
batman.comer()
