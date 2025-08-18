"""persona = {"nombre": "Juan", "edad": 25, "ciudad": "Bogotá"}

# Claves
for clave in persona:
    print(clave)

# Valores
for valor in persona.values():
    print(valor)

# Clave y valor
for clave, valor in persona.items():
    print(clave, ":", valor)

persona = {"nombre": "Juan", "edad": 25}

# Agregar o actualizar
persona["ciudad"] = "Bogotá"
persona["edad"] = 26  

# Eliminar
del persona["nombre"]"""

#ejercicio manejo de diccionarios
datos_personas = {
    "nombre" : "Alejo",
    "edad" : 20,
    "ciudad" : "bello"
}
print(datos_personas)
for keys in datos_personas:
    print(keys)

values = datos_personas.values()
print(values)

datos_personas["ciudad"] = "tutunendo"
datos_personas["profesion"] = "Ingeniero de Datos"

#primer itento del ultimo topico 
"""
for i in datos_personas.items():
    print(datos_personas)"""

#segundo intento del ultimo topico del ejercicio 

for key,value in datos_personas.items():
    print(f"key: {key} | value:{value}")