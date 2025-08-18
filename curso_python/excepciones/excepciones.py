
def sumar_dos():
    while True:
        a = input("numero 1: ")
        b = input("numero 2: ")
        try:
            resultado = int(a) + int(b)
        except Exception as e:
            print("Te pedi un numero salame, no te hagas el gracioso")
            print(f"ERROR: {type(e).__name__}")
        else:
            break
        finally:
            print("manejo de excepcion finalizado")

    return resultado 
        
    

print(sumar_dos())

