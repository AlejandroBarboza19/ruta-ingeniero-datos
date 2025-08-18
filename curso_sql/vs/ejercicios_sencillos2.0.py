#ejercicio 1 Dada la lista de números, imprime cada número multiplicado por 2.
numeros = [1, 3, 5, 7, 9]

# Tu código aquí
for numero in numeros:
    mlp=numero*2
    print(mlp)
    if mlp == 18:
        print("ZUNDADA ZUNDADA ZUNDADA ZUNDADA ZUNZUN DADA")
    #le quise meter condicional normamente lo haria asi 
    """for numero in numeros:
        print(numero*2)"""
    
#ejercicio 2 Dada la tupla de frutas, imprime cada fruta en mayúsculas.
frutas = ("manzana", "banana", "cereza")

# Tu código aquí
for fruta in frutas:
    FRUTAS = fruta.upper()
    print(FRUTAS)
#asi si estoy entendiendo poco a poco

#ejercicio 3, Dado el conjunto de letras, imprime cada letra y su código ASCII (usa ord()).
letras = {'a', 'b', 'c'}
# Tu código aquí
for letra in letras:
    asqui = ord(letra)
    print(f"{letra}: {asqui}")

#ejercicio 4, Dado el diccionario con países y capitales, imprime el país y la capital en formato: La capital de Colombia es Bogotá.
capitales = {
    "Colombia": "Bogotá",
    "México": "Ciudad de México",
    "Argentina": "Buenos Aires"
}

# Tu código aquí
for clave,Valor in capitales.items():
    print(f"la capital de {clave} es {Valor}")


#ejercicio  5, Dado un diccionario donde cada clave es un estudiante y su valor es una lista de notas, imprime el promedio de notas por estudiante.

notas = {
    "Ana": [4, 5, 3, 4],
    "Luis": [3, 3, 4, 2],
    "Sofía": [5, 5, 5, 4]
}

# Tu código aquí
notas_ana = notas["Ana"]
notas_luis = notas["Luis"]
notas_sofia = notas["Sofía"]

suma_notas_luis = 0
suma_notas_ana = 0 
suma_notas_sofia = 0

for nota in notas_ana:
    suma_notas_ana += nota
    promedio_ana = suma_notas_ana / len(notas_ana) 
print(f"el promedio de notas de ana son: {promedio_ana}")  

for nota in notas_luis:
    suma_notas_luis += nota
    promedio_luis = suma_notas_luis / len(notas_luis)
print(f"el promedio de notas de luis son: {promedio_luis}")  

for nota in notas_sofia:
    suma_notas_sofia += nota
    promedio_sofia = suma_notas_sofia/ len(notas_sofia)
print(f"el promedio de notas de sofia son: {promedio_sofia}")  

#opcion optimizada 
for estudiante, lista_notas in notas.items():
    suma = 0
    for nota in lista_notas:
        suma += nota
    promedio = suma / len(lista_notas)
    print(f"El promedio de notas de {estudiante} es: {promedio:.2f}")







