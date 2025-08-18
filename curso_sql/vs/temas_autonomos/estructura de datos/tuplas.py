colores = ("rojo", "verde", "azul")

for color in colores:
    print(color)
    
colores = ("rojo", "verde")
colores_lista = list(colores)
colores_lista.append("azul")
colores = tuple(colores_lista)
