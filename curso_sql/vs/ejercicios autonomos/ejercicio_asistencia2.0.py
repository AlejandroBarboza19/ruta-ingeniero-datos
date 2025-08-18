numero_estudiantes = int(input("Ingrese el número de estudiantes: "))
dias = int(input("¿Cuántos días quiere registrar?: "))

# Lista de estudiantes
estudiantes = []
for i in range(numero_estudiantes):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")  
    estudiantes.append(nombre)

# Diccionario para guardar asistencia
dias_asistencia = {nombre: 0 for nombre in estudiantes}

# Lista para guardar ausencias totales
no_asistio = []

# Registro de asistencia
for nombre in estudiantes:
    for dia in range(dias):
        asistencia = input(f"¿{nombre} asistió en el día {dia+1}? (s/n): ").lower()
        if asistencia == 's':
            dias_asistencia[nombre] += 1
        elif asistencia == 'n':
            pass  # No suma asistencia
        else:
            print("Opción inválida.")

# Identificar estudiantes que no asistieron ningún día
for nombre, asistencias in dias_asistencia.items():
    if asistencias == 0:
        no_asistio.append(nombre)

print("\nAsistencias registradas:", dias_asistencia)
print("Estudiantes que no asistieron ningún día:", no_asistio)
