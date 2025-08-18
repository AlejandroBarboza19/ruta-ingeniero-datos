frase = input("decime algo maestro y te calculo cuanto tardarias: ")

palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

print(f'dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en pedirlo')
print(f'Dalto lo diria en {cantidad_de_palabras*100//2*1.3/100} segundos ')
if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedi un testamento")

