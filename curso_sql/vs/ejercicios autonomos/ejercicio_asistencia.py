numero_estudiantes = int(input("cuantos estudiantes hay: "))

asistieron = []
no_asistieron = []



for i in range(numero_estudiantes):
    nombre = input(f"ingrese el nombre del estudiante {i+1}: ")
    asistencia = input("este estudiante asistio a clase?: (s) si, (n) no : ").lower()

    if asistencia == 's':
        asistencia = asistieron.append(nombre)
    elif asistencia == 'n':
        asistencia = no_asistieron.append(nombre)
    else:
        print("caracter invalido")

cantidad_asistencia = len(asistieron)
porcentaje_asistencia = cantidad_asistencia / numero_estudiantes *100

print(f'estudiantes que asistieron: {asistieron}')
print(f'estudiantes que no asistieron: {no_asistieron}')
print(f'El porcentaje de asistencia es: {round(porcentaje_asistencia,2)}')



