"""frutas = ["manzana", "pera", "uva"]

# Recorrer y mostrar
for fruta in frutas:
    print(fruta)

Recorrer con índice
for i in range(len(frutas)):
    print(i, frutas[i])


frutas = ["manzana", "pera"]

# Agregar
frutas.append("uva")  
# Insertar en posición específica
frutas.insert(1, "mango")  
# Cambiar
frutas[0] = "sandía"  
# Eliminar
frutas.remove("pera")  
# Eliminar por índice
frutas.pop(0)  """

#ejercicio de listas
frutas = ["maracuya","banano","mora","lulo","granadilla"]

for fruta in frutas:
    print(fruta)

frutas.append("kiwi")
frutas.remove("lulo")

print(frutas)

for i in range(len(frutas)):
    print(i, frutas[i])