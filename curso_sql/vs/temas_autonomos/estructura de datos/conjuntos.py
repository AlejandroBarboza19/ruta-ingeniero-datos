numeros = {1, 2, 3}

for num in numeros:
    print(num)
numeros = {1, 2, 3}

# Agregar
numeros.add(4)  
# Eliminar
numeros.remove(2)  # Error si no existe
numeros.discard(5)# No da error si no existe
