ingreso_mensual= 12000
gasto_mensual = 8000
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual > 3000:
        print("ahora si estas bien")
    else:
        print("bajale a la gastadera, AHORRA")
elif ingreso_mensual > 1000:
    print("Estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print("estas bien en argetina")
else:
    print("sos pobre")