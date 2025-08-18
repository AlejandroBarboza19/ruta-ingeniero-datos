#creando funcion simple
"""
def saludar():
    print("Hola lucas mi maestro ")
#ejecutando la funcion simple
saludar()"""

#agregando una fucnion que tiene parametros
""""
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "mi reina"
    elif sexo == "hombre":
        adjetivo = "titan"
    else:
        adjetivo = "amor"
    print(f"hola {nombre} mi {adjetivo} ¿como andas?")

saludar("alejo","hombre")
saludar("valentina", "mujer")
saludar("wilmer","no binario")"""

#crear una funcion que nos retorne multiples valores 
def crear_contraseña_rendom(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num-2 
    c2 = num
    c3 = num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

#desempaquetando la funcion
password,primer_numero = crear_contraseña_rendom(981)

#mostrando los resultados obtenidos y los datos utilizados 
print(f"Tu contraseña es: {password}")
print(f"el numero utilizado para crearla fue: {primer_numero}")