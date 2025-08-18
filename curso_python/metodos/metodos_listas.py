#funcion para crear una lista con list
lista = list([34])

#devuelve la cantidad elementos de la lista 
cantidad_de_elementos = len(lista)

#agreagando un elemento  a la lista 
lista.append(65)

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"TOMA MAMA")

#agregando varios elementos a la lista 
lista.extend([12,2030])

#eliminando un elemento de la lista por su indice
lista.pop(0) # -1 para eliminar el ultimo -2 antepenultimo y asi sucesivamente 

#removiendo un elemento de la lista por su valor 
lista.remove("TOMA MAMA")

#eliminando todos los elementos de la lista 
#lista.clear()

#ordenando la lista si usamos el parametro reverse=True de mayor a menor 
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()



print(lista)