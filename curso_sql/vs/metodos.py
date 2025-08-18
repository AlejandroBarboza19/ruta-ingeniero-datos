# ========================================
# 📌 RESUMEN DE MÉTODOS ÚTILES EN PYTHON
# Listas, Conjuntos y Diccionarios
# ========================================

# ----------------------
# 1️⃣ LISTAS (list)
# ----------------------

# Crear lista
frutas = ["manzana", "pera", "uva"]

# Agregar al final
frutas.append("mango")

# Insertar en posición específica
frutas.insert(1, "kiwi")  # índice 1

# Agregar varios elementos
frutas.extend(["fresa", "sandía"])

# Cambiar valor
frutas[0] = "cereza"

# Eliminar por valor
frutas.remove("pera")  # Error si no existe

# Eliminar por índice
frutas.pop(2)  # Elimina "uva"
frutas.pop()   # Elimina el último

# Ordenar (modifica la lista)
frutas.sort()

# Ordenar sin modificar
lista_ordenada = sorted(frutas)

# Contar ocurrencias
cantidad = frutas.count("mango")

# ----------------------
# 2️⃣ CONJUNTOS (set)
# ----------------------

# Crear conjunto
numeros = {1, 2, 3}

# Agregar elemento
numeros.add(4)

# Agregar varios elementos
numeros.update([5, 6, 7])

# Eliminar elemento (error si no existe)
numeros.remove(2)

# Eliminar elemento (sin error)
numeros.discard(10)  # No pasa nada si no existe

# Eliminar y devolver un elemento aleatorio
valor_eliminado = numeros.pop()

# Vaciar conjunto
numeros.clear()

# Operaciones de conjuntos
a = {1, 2, 3}
b = {3, 4, 5}
union = a.union(b)            # {1, 2, 3, 4, 5}
interseccion = a.intersection(b)  # {3}
diferencia = a.difference(b)      # {1, 2}

# ----------------------
# 3️⃣ DICCIONARIOS (dict)
# ----------------------

# Crear diccionario
persona = {"nombre": "Juan", "edad": 25}

# Acceder a valor
nombre = persona["nombre"]

# Acceder sin error si no existe
ciudad = persona.get("ciudad", "No especificada")

# Agregar / Actualizar valor
persona["ciudad"] = "Bogotá"

# Eliminar clave (error si no existe)
del persona["edad"]

# Eliminar clave y obtener valor
valor = persona.pop("nombre", "No existe")

# Recorrer claves
for clave in persona:
    print(clave)

# Recorrer valores
for valor in persona.values():
    print(valor)

# Recorrer clave y valor
for clave, valor in persona.items():
    print(clave, valor)

# Vaciar diccionario
persona.clear()

# ----------------------
# 🔹 TIPS RÁPIDOS
# ----------------------
# - .append() → listas
# - .add() / .update() → conjuntos
# - .keys(), .values(), .items() → diccionarios
# - sorted() → devuelve una nueva lista ordenada
# - len(estructura) → devuelve el tamaño
# - "separador".join(lista) → une lista de strings en texto
