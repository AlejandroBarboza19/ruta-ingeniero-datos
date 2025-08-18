#creando diccionarios con dict()

diccionario = dict(nombre="lucas", apellido="dalto")

#las listas no pueden ser claves y usamos fonzenset para meter conjuntos
diccionario = {frozenset(["dalto","rancio"]):"jajaja"}

#creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido"])

print(diccionario)