diccionario = {
    "nombre" : "lucas",
    "apellido" : "dalto",
    "subs": 1000000
}

#nos devuelve un objeto diict_item
claves = diccionario.keys()

#obteniendo un elemento con get, si no lo encuentra no para el programa
claves1 = diccionario.get("subs")

#eliminando  todo el diccionario 
#diccionario.clear()

#eliminando un elemento del diccionario 
diccionario.pop("subs")

#obteniiendo un elemento dict_items iterable 
diccionario_iterable = diccionario.items()


print(diccionario)