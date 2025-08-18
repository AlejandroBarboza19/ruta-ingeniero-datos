import pandas as pd
df = pd.read_csv("archivos_problema\\\\datos.csv")

#cambiar el tipo de dato de una columna 
df['edad'] = df['edad'].astype(str) 

#mostrat el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))

#reemplazando los datos dalto por maestro 
df['nombre'].replace("dalto","maestro", inplace=True)


#eliminado filas con datos faltantes
df = df.dropna()

#eliminando filas repetidas
df = df.drop_duplicates()

#creando un csv con el dataframe resultante (limpio)
df.to_csv("archivos_problemas\\\\datos_limpios.csv")

