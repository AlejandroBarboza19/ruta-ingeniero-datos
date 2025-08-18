class A:
    def hablar(self):
        print("Hola desde A")
class B:
    def  hablar(self):
        print("Hola desde B")
class C:
    def hablar(self):
        print("Hola desde C")
class D(A,C,B):
    pass

d = D()
d.hablar()
print(D.mro()) # .mro para ver el orden

#orden de ejecucion, osea estamos aprendiendo el orden y jerarquia que python 
#tiene con estos tipos de clases y herencias 
# mro = metodo de resolucion de orden

    