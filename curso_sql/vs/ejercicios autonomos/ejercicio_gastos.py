comida = float(input("Ingrese el gasto en comida: "))
transporte = float(input("Ingrese el gasto en Transporte: "))
entretenimiento = float(input("Ingrese el gasto en entretenimiento: "))

gasto_total_mes = comida + transporte + entretenimiento 

porcentaje_comida = round((comida / gasto_total_mes) * 100,2)
porcentaje_transporte = round((transporte / gasto_total_mes) * 100,2)
porcentaje_entretenimiento = round((entretenimiento / gasto_total_mes) * 100,2)

categoria_mas_gastona = max(comida,transporte,entretenimiento)

print("gasto total: ", gasto_total_mes)
print("Porcentaje en comida: ",porcentaje_comida,'%')
print("Porcentaje en transporte: ",porcentaje_transporte,'%')
print("Porcentaje en entretenimiento: ",porcentaje_entretenimiento,'%')

if categoria_mas_gastona == comida:
    print("has gastado mas en comida")
elif categoria_mas_gastona == transporte:
    print("has gastado mas en transporte")
else:
    print("has gastado mas en entretenimiento")