from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")

# Objetos
pedrito = Estudiante("Pedrito", 25, "Masculino", "programación")
dalto = Trabajador("Lucas", 21, "Masculino", "programación")

# Ejecución
dalto.presentarse()
dalto.hacer_actividad()

pedrito.presentarse()
pedrito.hacer_actividad()
