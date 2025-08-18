"""nombre = input("Ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
año_actual = 2025
edad_cien =   100 - edad

calculo_edad= año_actual + edad_cien 

print("Hola", nombre, "cumpliras 100 años en:", calculo_edad)

#ejercicio 1 
num = int(input("ingrese su numero: "))
resto = num % 2 

if resto == 0:
    print("Numero par")
else: 
    print("Numero impar")

#ejercicio 2 
numeros= int(input("elija su numero: "))

for  numero in range(numeros): 
    print(numero+1)

#ejercicio 3
edad = int(input("Ingrese su edad: "))

if edad >= 18: 
    print("puedes votar")
else: 
    print("no puedes votar")"""

#ejercicio 4 Aprobado o no
nota = int(input("ingrese su nota del 1 al 10: "))

if nota >= 5 and nota <= 10:
    print("Aprobado")
elif nota < 5:
    print("Reprobado")
else: 
    print("Nota invalida")

#ejercicio 5
lista = ([])
for i in range(0,5):
    numeros = int(input("ingrese cinco numeros:"))
    agregando = lista.append(numeros)

print(lista)

#ejercicio 6
 

respuesta = int(input("intenta advinar el numero:"))

while respuesta != 7:
        print("es incorrecto sigue intentado")
        respuesta = int(input("di otro numero tu puedes:"))
        if respuesta == 7:
            print("es correcto")
