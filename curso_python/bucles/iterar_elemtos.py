animales = ["gato","perro","loro","cocodrilo"]
numeros = [52,16,14,72]

#recorriendo la lista animales
for animal in animales: 
    print(f'Ahora la variable animal es igual a: {animal}')

#rrecoriendo la lista de numros y multiplicando cada valor por 10 
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#iterando dos listas del mismo tamaño al mismo tiempo 
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")

#forma corecta de recorrer una lista por su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

#usando el for/else in numeros:
    print(f'ejecutando el ultimo bucle, valor actual {numero}')
else: 
    print("el bucle termino")
#todo lo anteriror funciona para tuplas, conjuntos, listas