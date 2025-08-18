cadena1 = "Hola soy Dalto"

cadena2 = "Bienvenido Maquinola"

resultado = cadena1.upper() #convierte a mayusculas
resultado0 = cadena1.lower() #convierte a minisculas 

#primera letra en mayus
resultado1 = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no encuentra devuelve -1
busqueda_find = cadena1.find("D")

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
busqueda_index = cadena1.index("D")

#si es numerico, devuelve True si no False
es_numerico = cadena1.isnumeric()

#si es alfanumerico devuelve True, si no false
es_alfanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida 
contar_coincidencias = cadena1.count("a")

#contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
#es una funcion
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empizacon = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("a")

# reemplaza un pedazo de la cadena dada, por otra
cadena_nueva = cadena1.replace("Hola","Hello")


#separa cadena con la cadena que le pasemos
cadena_separada = cadena1.split(",")
