#creando una funcion de 3 parametros
def frase(nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido}, sos muy {adjetivo}"


#utilizando keyword arguments
frase = frase(adjetivo="sos muy capo", apellido="barboza",nombre="alejo")

print(frase)

#creando la misma funcion con un parametro opcional y un valor por defecto
def fraSe(nombre,apellido,adjetivo = "irresponsable"):
    return f"hola {nombre} {apellido}, sos muy {adjetivo}"

frase1 = fraSe("alejo","barboza")

print(frase1)
