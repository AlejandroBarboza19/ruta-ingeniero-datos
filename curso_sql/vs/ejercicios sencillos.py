#ejercicio 1
colores = ["rojo", "azul", "verde", "amarillo", "negro"]

# Tu código aquí: recorrer colores e imprimirlos
for color in colores:
    print(color)

#Ejercicio 2: Sumar números en lista
numeros = [3, 7, 2, 9, 4]
# Tu código aquí para sumar e imprimir resultado

suma = 0
for numero in numeros:
    suma += numero
print(suma)
    

#Ejercicio 3: Diccionario y recorrido
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Medellín"
}

# Tu código aquí para recorrer e imprimir clave y valor
for clave,valor in persona.items():
    print(f"{clave}: {valor}")

#Ejercicio 4: Agregar a lista dentro de diccionario

programador = {
    "nombre": "Laura",
    "lenguajes": ["Python", "JavaScript"]
}

# Agrega "Java" a la lista de lenguajes y luego imprime la lista completa
programador["lenguajes"].append("Java")
print(programador["lenguajes"])


