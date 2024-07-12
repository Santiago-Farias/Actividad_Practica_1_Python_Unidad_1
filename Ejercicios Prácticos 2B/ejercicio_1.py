""" Ejercicio 1
Crear un programa que pueda sumar los números pares comprendidos
entre el 1 y el 10. """

num1 = 0 # Variable contador
amount = 0 # Variable que guarda el valor del contador actual y lo suma con el siguiente (SOLO PARES)

while num1 <= 10: # Se repite el ciclo Mientras num1 sea menor o igual a 10
    if num1 % 2 == 0 and num1 != 0: # Si el módulo, resto o residuo es igual a 0, se le suma a amount lo que vale num1
        amount += num1
        print("Número par actual:", num1)
    num1 += 1
print("La suma de los valores pares es de:", amount)