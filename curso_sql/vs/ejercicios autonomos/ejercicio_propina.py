cuenta_sp = float(input("Ingrese el valor de la cuenta sin propina: "))
porcentaje_propina = 12

cuenta_propina = round(cuenta_sp * 0.12,2)
total_pagar = round(cuenta_sp + cuenta_propina,2)

print(f"el valor de la propina es: {cuenta_propina} ")
print(f"el valor de la toda la cuenta es: {total_pagar} ")
