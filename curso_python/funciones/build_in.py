numeros = [4,7,1,42,15]
#encontrando el numero mayor de una lista 
numero_mas_alto = max(numeros)


#encontrando el mas bajo 
numero_mas_bajo = min(numeros)


#redoneando a 6 decimales
numero = round(12.345678,3)

#retorna False -> 0, vacio, False, none / True -> distinto a 0, True, Cadena, Datos no vacios  
resultado_bool = bool("ladsa")


#retorna True, si todos los valores son verdaderos
resultado_all = all(["234", True, [344,23]])

#suma todos los valores de un iterable
suma_total = sum(numeros)

print(suma_total)