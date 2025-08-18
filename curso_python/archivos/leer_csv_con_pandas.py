import pandas as pd 

#usando la funcion  read csv para leer archivo csv
df = pd.read_csv("archivos\\datos.csv",)
df2 = pd.read_csv("archivos\\datos.csv",)

#obteniendo los datos de la columna nombre
nombres = df["nombre"]


"""
#slising <- acceder a valores especificos
cadena = "0123456789"
print(cadena[0:9])"""


#ordendando el dataframe por la edad
df_ordenado_ascendente = df.sort_values("edad")


#ordenandolo de forma descendente
df_ordenado_descendente = df.sort_values("edad",ascending=False)


#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])


# accdiendo a la primeras 3 filas con head()
primeras_filas = df.head(3)

#accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

#accedienod a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del data frame
df_info = df.describe()

#accediendo a un elemento especifico del df con loc - accediendo a la edad de la fila 2 
elemento_especifico_loc = df.loc[2,"edad"]

#accediento a la edad de la fial 2 con iloc
elemento_especifico_loc = df.iloc[2,2]

#accediendo a la fila 3 con loc 
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]


