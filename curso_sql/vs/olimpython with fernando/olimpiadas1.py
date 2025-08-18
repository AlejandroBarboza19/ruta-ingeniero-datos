
while True:
    try:
        edades = int(input("ingrese el numero de edad que quiere ingresar: "))
        if edades < 0:
            print("El numero es negativo, ingrese uno positivo")
        else:
            break
    except ValueError:
        print("entrada invalida")
        

edad_total =[]

for i in range(edades):
    while True:
        try:
            edad = int(input(f"Ingrese la {i+1} edad: "))
            if edad < 0:
                print("el numero es negativo, ingrese uno mayor a 0 ")
            else:
                break
        except ValueError:
            print("entrada invalida")
    edad_total.append(edad)

print(f"Todas las edades son: {edad_total}")

suma_edad = 0 
edad_superiores_promedio = []
edad_inferiores_promedio = []
ordenada=sorted(edad_total)

for edad in edad_total:
    suma_edad += edad
    promedio = suma_edad / len(edad_total)

for i in edad_total:
    if i > promedio:
        edad_superiores_promedio.append(i)
    else:
        edad_inferiores_promedio.append(i)

print(f"La suma total de las edades es: {suma_edad}")
print(f"El promedio de las edades es: {promedio}")
print(f"La edad mayor es: {max(edad_total)}")
print(f"La edad menor es: {min(edad_total)}")
print(f"edades superiores al promedio: {edad_superiores_promedio}")
print(f"La edad inferior al promedio es: {edad_inferiores_promedio}")
print(f"La lista ordenada es: {ordenada}")

