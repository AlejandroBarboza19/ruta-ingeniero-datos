#importamos librerias con la que vamos a trabajar 
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt 

#hacemos conexion con la base de datos 
conn = sqlite3.connect("northwind.db")
#consultas para mostrar el producto mas rentable de la base de datos 
query = '''
        SELECT ProductName, SUM(Price * Quantity) as Revenue
        FROM OrderDetails od
        JOIN Products p ON p.ProductID = od.ProductID
        GROUP BY od.ProductID
        ORDER BY Revenue DESC
        LIMIT 10
'''
top_products = pd.read_sql_query(query,conn)

top_products.plot(x="ProductName", y="Revenue", kind="bar", figsize=(10,5),legend=False)

plt.title("10 Productos mas rentables")
plt.xlabel("Productos")
plt.ylabel("Revenue")
plt.xticks(rotation=90)

plt.show()

#OBTENIENDO LOS EMPLEADOS MAS EFECTIVOS 

query2 = '''
        SELECT FirstName || " " || LastName as Employee, COUNT(*) as Total
        FROM Orders o 
        JOIN Employees e 
        ON e.EmployeeID = o.EmployeeID
        GROUP BY o.EmployeeID
        ORDER BY Total ASC
        LIMIT 3
'''
top_employees = pd.read_sql_query(query2,conn)
top_employees.plot(x="Employee", y="Total", kind="bar",figsize=(10,5),legend=False)

plt.title("10 empleados mas efectivos")
plt.xlabel("Empleados")
plt.ylabel("Total Vendido")
plt.xticks(rotation = 45)
plt.show()

query3 = '''
        SELECT FirstName || " " || LastName as Employee,
		SUM(od.Quantity * p.Price) AS TotalRecaudado
		from Employees e
JOIN orders o on e.EmployeeID = o.EmployeeID

JOIN OrderDetails od on o.OrderID = od.OrderID

JOIN Products p on p.ProductID = od.ProductID

GROUP BY
    e.EmployeeID
ORDER BY
    TotalRecaudado DESC
LIMIT 10;
'''
top_employees_price = pd.read_sql_query(query3,conn)
top_employees_price.plot(x="Employee", y="TotalRecaudado", kind="bar",figsize=(10,5),legend=False)

plt.title("10 empleados con mas dinero recaudado")
plt.xlabel("Empleados")
plt.ylabel("Total Recaudado")
plt.xticks(rotation = 90)
plt.show()