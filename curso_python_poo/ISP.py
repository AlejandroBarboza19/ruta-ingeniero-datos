from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comedor:
    @abstractmethod
    def comer(self):
        pass
class Durmiente():
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador):
    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("el humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando")

        