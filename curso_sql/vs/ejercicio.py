estudiantes = [
    {"nombre": "Ana", "edad": 22, "lenguajes": ["Python", "JavaScript"], "ciudad": "Medellín"},
    {"nombre": "Luis", "edad": 25, "lenguajes": ["Java"], "ciudad": "Bogotá"},
    {"nombre": "Sofía", "edad": 20, "lenguajes": ["Python", "C++"], "ciudad": "Cali"}
]

#ejercicio 3
estudiante_nuevo = [{"nombre": "alejo","edad": 20, "lenguajes":["Python", "SQL"],"ciudad":"bello"}]
estudiantes.extend(estudiante_nuevo)

#ejercico 4
estudiantes[0] = {"nombre": "Ana", "edad": 22, "lenguajes": ["Python", "JavaScript"], "ciudad": "tutunendo"}

#ejercicio 5
estudiantes[1]["lenguajes"].append("SQL")

#ejercicio 6 
estudiantes.pop(3)

#ejercicio 2 se dejo de ultimo para mostrar todos los cambios 
for estudiante in estudiantes:
    nombre=estudiante["nombre"]
    edad=estudiante["edad"]
    ciudad=estudiante["ciudad"]
    lenguajes = ", ".join(estudiante["lenguajes"])
    print(f"{nombre} ({edad} años) - {ciudad} - {lenguajes}")


#ejercicio 7
for clave in estudiantes:
    nombre = clave["nombre"]
    print(nombre)

#ejercicio 8 
total_lenguajes = set()

for estudiante in estudiantes:
    total_lenguajes.update(estudiante["lenguajes"])
    #ejerciocio 9 
print(total_lenguajes)

