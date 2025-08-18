class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre 
        self.edad = edad 
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} esta estudiando")

Estudiante1 = Estudiante(
    input("Ingrese el nombre del estudiante: "), 
    input("Ingrese la edad del estudiante: "), 
    input("Ingrese el grado del estudiante: "))

def accion(): 
     respuesta = input("Que esta haciendo el estudiante? ")
     respuesta = respuesta.lower()
     if respuesta == 'estudiar':
        print(f"{Estudiante1.nombre} de {Estudiante1.edad} años y grado {Estudiante1.grado} esta estudiando")
     else:
        print(f"{Estudiante1.nombre} esta vagando")
        


accion()
