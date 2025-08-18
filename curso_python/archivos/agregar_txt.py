
with open("archivos\\texto_de_dalto.txt","a",encoding="UTF-8") as archivo:
    #agregando al arhivo
    for i in range(5):
     #agregando lineas
     archivo.write(f"linea {i+1} agregada\n")

  

