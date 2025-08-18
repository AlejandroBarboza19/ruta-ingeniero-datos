#ejercicio 6, Dada una lista de números, crea una nueva lista con solo los números pares e imprime esa lista.
numeros = [1, 4, 7, 10, 13, 16, 19, 22]
numeros_pares = []
numeros_impares = []
# Tu código aquí
for numero in numeros:
    if numero % 2== 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print(f"los numeros pares son: {numeros_pares} y los numeros impares son: {numeros_impares}")

#ejercicio 7, Dado un diccionario con productos y sus precios, imprime solo los productos cuyo precio sea mayor a 20.

productos = {
    "camisa": 15,
    "pantalón": 35,
    "zapatos": 50,
    "sombrero": 18
}

# Tu código aquí
for producto, precio in productos.items():
    if precio > 20:
        print(producto)
    else:
        continue


#ejercicio 8, Dado un conjunto de números, suma todos los valores y muestra el total.
numeros_set = {2, 5, 8, 3, 10}
sum_set = 0
# Tu código aquí
for numero in numeros_set:
    sum_set += numero
print(f"el total de la suma del conjunto fue: {sum_set}")


#ejercicio 9, Dado un diccionario con las edades de personas, aumenta la edad de cada persona en 1 año y muestra el diccionario actualizado.
edades = {
    "Ana": 25,
    "Luis": 30,
    "Sofía": 22
}

# Tu código aquí
for nombre, edad in edades.items():
    sum_edad = edad + 1
    print(f"{nombre} su edad actualizada es: {sum_edad}")

#solucion verdadera 
for nombre in edades:
    edades[nombre] += 1
print(edades)


#ejercicio 10, Dada una lista de nombres, pregunta al usuario un nombre y verifica si está en la lista. Imprime un mensaje acorde.


nombres = ["Ana", "Luis", "Sofía", "Carlos"]

# Tu código aquí
nombre_buscar = input("ingrese el nombre que quiere buscar en la lista: ")


for nombre in nombres:
    if nombre_buscar == nombre:
        print("Nombre encontrado, felicidades")
        break
else: 
    print("AQUI NO ES MAESTRO, no se encontre el nombre")


#que me falto para que esto funcione?  
"""for nombre in nombres:
            if nombre_buscar == nombre:
                print("Nombre encontrado, felicidades")
                break
            while nombre_buscar != nombre:
                respuesta=input("desea seguir buscando? si (s), no (n)")
                if respuesta == 's':
                    continue
                elif respuesta == 'n':
                 print("ok adios")
                break"""

#esto me falto 
nombres = ["Ana", "Luis", "Sofía", "Carlos"]

while True:
    nombre_buscar = input("Ingrese el nombre que quiere buscar en la lista: ")

    if nombre_buscar in nombres:
        print("Nombre encontrado, felicidades")
        break
    else:
        respuesta = input("No encontrado. ¿Desea seguir buscando? si (s), no (n): ")
        if respuesta.lower() == 'n':
            print("Ok, adiós")
            break
