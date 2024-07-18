""" 
Ejercicio 7
Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los
números positivos y el producto de los negativos.
"""

suma_numeros_positivos = 0
producto_numeros_negativos = 1
contador_negativo = 0
promedios_numeros = 0
opcion = 0
contador_ciclos = 0

while opcion != 1:
    numeros = int(input("Ingrese un número: "))
    opcion = int(input("¿Desea seguir ingresando números? (0 seguir, 1 detener)\n"))
    if numeros > 0:
        suma_numeros_positivos += numeros
    elif numeros < 0:
        producto_numeros_negativos = producto_numeros_negativos * numeros
        contador_negativo += 1
    contador_ciclos += 1

if contador_negativo == 0:
    producto_numeros_negativos = 0

print(f"\nSuma de números positivos: {suma_numeros_positivos}\nProducto de números negativos: {producto_numeros_negativos}")