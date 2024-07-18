""" 
Ejercicio 3
Se deberá obtener tanto el nombre como la edad usando input y luego mostrar los datos concatenados con print. 
Ej: "Usted se llama José y su edad es 66 años". 
"""

# Declarar datos.
user_name = input("Ingrese su nombre: ")
user_age = int(input("Ingrese su edad: "))

# Mostrar datos.
#print("Usted se llama", user_name, "y su edad es de", str(user_age), "años.")

# Mas usada interpolado.
print(f"Usted se llama {user_name} y su edad es de {user_age} años.")

#print("Usted se llama {0} y su edad es de {1}".format(user_name, user_age))