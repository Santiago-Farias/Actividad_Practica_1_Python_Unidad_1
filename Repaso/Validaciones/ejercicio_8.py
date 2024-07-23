"""
Ejercicio 8
Ingresar 10 números enteros. Determinar el máximo y el mínimo.
El primer número que se ingrese será el mínimo y máximo, por que en la primera vuelta no tiene nada con que comparar.
"""

valor_maximo = 0
valor_minimo = 0
bandera = True
opcion = ""

while True:
    numero = int(input("Ingrese un número: "))

    if numero > valor_maximo or bandera == True: # Usamos el or, y en este caso pregunta por la primera expresión preguntando algo que ya está definido.
        valor_maximo = numero
    
    if numero < valor_minimo or bandera == True:
        valor_minimo = numero
        bandera = False
    
    opcion = input("Desea seguir (si/no)")
    if opcion.lower() == "no":
        break


print(f"Valor máximo: {valor_maximo}\nValor mínimo: {valor_minimo}")

""" valor_maximo = 0
valor_minimo = 99999

numero_1 = int(input("Ingrese un número: "))
numero_2 = int(input("Ingrese un número: "))
numero_3 = int(input("Ingrese un número: "))
numero_4 = int(input("Ingrese un número: "))
numero_5 = int(input("Ingrese un número: "))

# Calcular valor máximo.
if numero_1 > valor_maximo:
    valor_maximo = numero_1
if numero_2 > valor_maximo:
    valor_maximo = numero_2
if numero_3 > valor_maximo:
    valor_maximo = numero_3
if numero_4 > valor_maximo:
    valor_maximo = numero_4
if numero_5 > valor_maximo:
    valor_maximo = numero_5

# Calcular valor mínimo.
if numero_1 < valor_minimo:
    valor_minimo = numero_1
if numero_2 < valor_minimo:
    valor_minimo = numero_2
if numero_3 < valor_minimo:
    valor_minimo = numero_3
if numero_4 < valor_minimo:
    valor_minimo = numero_4
if numero_5 < valor_minimo:
    valor_minimo = numero_5

print(f"El número máximo es: {valor_maximo}\nEl número mínimo es: {valor_minimo}") """