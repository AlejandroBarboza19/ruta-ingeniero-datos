#primer tipo de datos compuestos
lista = ["Lucas Dalto", "Soy dalto", True,1.85] #corchetes y se pueden modificar

tupla = ("Lucas Dalto", "Soy dalto", True,1.85) #con parentesis y no se pueden mdificar 

#print(lista[3])

#creando un conjunto (set)

conjunto = {"Lucas Dalto", "Soy dalto", True,1.85} #se puede modificar pero elementos no, se hace creando una nueva lista
#no puede haber datos duplicados
#no se pueden llamar a los elementos por sus indices 
#son desordenaods 

#creando un diccionario 
diccionario = {
    'nombre': 'Lucas dalto',
    'canal' : 'Soy dalto',
    'esta_emocionado': True,
    'altura' : 1.85,
    'dato_duplicado' : 'Soy dalto'
}

print(diccionario['altura'])