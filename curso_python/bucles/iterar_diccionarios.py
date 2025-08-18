diccionario = {
    "nombre" : "Lucas",
    "apellido":"dalto",
    "subs": 1000000
}
#rrecoriendo diccionario para obtener las claves
for key in diccionario:
    key 
    print(f'la clave es {key}')
    
#rrecoriendo diccionario con items para obtener clave y valor 
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es: {value}')
