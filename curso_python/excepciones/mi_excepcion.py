#creanod mi propi excepcion, personalizada 
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"impresionaste cmetiste un error {err}")


#Lanzando mi propia excepcion
raise MiExcepcion("jajajaja, persona poco culta")

#manejandola
try:
    raise MiExcepcion("jajaja persona poco culta")
except:
    print("como vas a cometer eso")



