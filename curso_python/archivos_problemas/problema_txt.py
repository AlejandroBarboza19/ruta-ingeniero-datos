# 2 listas una con nombres otra con apellidos
nombres = ["lucas","matias","camila","pedro","roberto"]
apellidos = ["Dalto","Zing","Dalto","robetix","tarado"]

#registrar esta informacion en un TXT de forma optima
with open("archivos_problemas\\nombres_Y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"nombre: {n}\nApellido: {a}\n------------\n") for n,a in zip(nombres,apellidos)]
    