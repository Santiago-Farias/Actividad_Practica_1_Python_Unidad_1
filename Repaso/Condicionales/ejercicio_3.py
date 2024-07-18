"""
Ejercicio 3
A partir del ingreso de una edad, determinar si la persona es mayor de edad o no. Si es mayor de 18 se
mostrará el mensaje “UD ES MAYOR DE EDAD” caso contrario “UD ES MENOR DE EDAD”.
"""

user_age = int(input("Ingrese su edad: "))

if user_age > 17: # Si se compara si es mayor o igual a 18 son 2 comparaciones, en cambio con esto se hace un paso.
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad.")