manzanas = int(input("ingrese la cantidad inicial de manzanas: "))
naranjas =  int(input("ingrese la cantidad inicial de naranjas: "))
platanos =  int(input("ingrese la cantidad inicial de platanos: "))

ventas_manzanas = int(input("ingrese la cantidad de ventas de manzanas: "))
ventas_naranjas = int(input("ingrese la cantidad de ventas de naranjas: "))
ventas_platanos = int(input("ingrese la cantidad de ventas de platanos: "))

actualizacion_m = manzanas - ventas_manzanas
print("INVENTARIO ACTUALIZADO: ")
if actualizacion_m <= 0:
    print("No hay suficientes manzanas")
else: 
    print("Manzanas: ",actualizacion_m)
actualizacion_n = naranjas - ventas_naranjas
if actualizacion_n <= 0:
    print("No hay suficientes naranjas")
else: 
    print("Naranjas: ",actualizacion_n)
actualizacion_p = platanos - ventas_platanos
if actualizacion_p <= 0:
    print("No hay suficientes platanos")
else: 
    print("platanos: ",actualizacion_p)