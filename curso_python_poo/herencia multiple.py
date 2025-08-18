class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando")

class Artista():
    def __init__(self,habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f'mi habilidad es {self.habilidad}'
        
class EmpleadoArtiste(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f'hola soy {self.nombre} y mi habilidad es {self.mostrar_habilidad()} y trabajo en {self.empresa}') 
    
roberto = EmpleadoArtiste("Roberto",12,"colombiano","Cantar",4000000,"Google")

roberto.presentarse()


#como saber si es subclase

herencia = issubclass(EmpleadoArtiste,Artista)

#como saber instancias
instancia = isinstance(roberto,EmpleadoArtiste)
print(herencia)
print(instancia)