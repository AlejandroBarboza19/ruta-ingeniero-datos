#promeido de duracion
otros_curso_min = 2.5
otros_curso_max = 7
otros_cursos_promedio = 4 
dalto_curso = 1.5


#duracion de crudos
crudo_promedio = 5 
crudo_dalto = 3.5

#diferencias de duracion 

diferencia_con_min = 100 - dalto_curso / otros_curso_min * 100
diferencia_con_max= 100 - dalto_curso *1000 // otros_curso_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vacio 
timepo_vacio_promedio = 100 - otros_cursos_promedio *1000 // crudo_promedio / 10
timepo_vacio_dalto = 100 - dalto_curso *1000 // crudo_dalto / 10

print("________________________________")
print(f'el curso de dalto dura un {diferencia_con_min}% menos que el rapido')
print(f'el curso de dalto dura un {diferencia_con_max}% menos que el lento')
print(f'el curso de dalto dura un {diferencia_con_promedio}% menos que el promedio')

print("________________________________")
print(f'un curso promedio elimina un  {timepo_vacio_promedio}% de tiempo vacio')
print(f'este curso elimino el {timepo_vacio_dalto}% de tiempo vacio')
print("________________________________")

#mostrando diferencias si los cursos duraran 10 horas
print(f'ver 10 horas de este curso equivale a ver {otros_cursos_promedio*1000 // dalto_curso/10}horas de otros cursos')
print(f'ver 10 horas de este curso equivale a ver {dalto_curso*100 // otros_cursos_promedio/10}horas de otros cursos')
print("________________________________")