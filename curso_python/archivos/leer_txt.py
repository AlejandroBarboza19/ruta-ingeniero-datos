archivo = open("archivos\\texto_de_dalto.txt",encoding="UTF-8")


#leer archivo completo
# archivo = archivo_sin_leer.read()

#leer linea por linea 
#lineas = archivo_sin_leer.readlines()
#print(lineas)

#leer una sola linea 
linea = archivo.readline()

#cerrar el archivo
archivo.close()

print(linea)