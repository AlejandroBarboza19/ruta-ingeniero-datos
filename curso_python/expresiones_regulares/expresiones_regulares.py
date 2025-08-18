import re 

texto = '''Hola maestro, esta es la cadena 1, como estas mi capitan
Esta es la segunda 2 linea de texto
Y Esta es la final 3 definitiva mi capitan'''

#haciendo una busqueda simple
resultado = re.findall("Hola",texto)

#\d -- busca digitos numericos del 0 al 9 
resultado = re.findall(r"\d",texto)

#\D -- busca TODO MENOS digitos numericos 
resultado = re.findall(r"\D",texto)

#\w busca caracteres alfanumeros [a-z A-Z 0-90 _]
resultado = re.findall(r"\w",texto)

#\W busca TODO menos caracteres alfanumeros [a-z A-Z 0-90 _]
resultado = re.findall(r"\w",texto)

#\s busca espacios em blanco,  espacios, tabs, saltos line
resultado = re.findall(r"\s",texto)

#\S busca TODO MENOS espacios eN blanco,  espacios, tabs, saltos line
resultado = re.findall(r"\S",texto)

#\n BUSCA SALTO EN LINEA
resultado = re.findall(r"\n",texto)

# . busca TODO menos saltos en linea
resultado = re.findall(r'.',texto)

#\. cancelar caracteres especiales
resultado = re.findall(r'\.',texto)

#armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(f'\d\.\s',texto)

#^ busca el comienzo de una linea 
#flags = re.M  activa la multilinea
resultado = re.findall(r'^Hola',texto,flags=re.M)

#$ busca el final de una linea
resultado = re.findall(r'capitan$',texto,flags=re.M)

#busca n cantidad de bese el valor de la izquierda
resultado = re.findall(r'\d{3}',texto)

#{n,m} al menos m, como maximo m
resultado = re.findall(r'\d{2,4}',texto)

# | busca una cosa o la otra 
resultado = re.findall(r'\d{2,4} | hola ',texto)

print(resultado)