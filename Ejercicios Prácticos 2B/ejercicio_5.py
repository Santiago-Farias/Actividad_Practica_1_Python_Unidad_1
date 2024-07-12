""" Ejercicio 5
Crear un programa que solicite 5 números mediante prompt. Calcular la
suma acumulada y el promedio de los números ingresados. """

cont = 0
amount = 0
avg = 0.0
numbers = 5

while cont < numbers:
    num1 = int(input("Ingrese un número: "))
    amount += num1
    cont += 1

avg = amount / numbers
print("Valor total:", amount, "\nPromedio:", avg)