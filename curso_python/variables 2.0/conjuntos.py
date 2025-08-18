#creando un conjunto con set

conjunto = set(["dato1", "dato2"])

#metiendo unn cojunto dentro de otro conjunto
conjunto1= frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)

#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}
#verificando subconjuntos
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1 # OTRA FORMA 

#verificando subconjuntos
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 >= conjunto1 # OTRA FORMA 

#verificar si hay algun numero en comun 
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)