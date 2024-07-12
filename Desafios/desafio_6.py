""" Desafío Máximos y Mínimos!
Hacer que el programa que tuvimos de prueba muestre tanto el valor máximo ingresado como el mínimo.
Ahora.. si lograste realizarlo utilizando el código de muestra hasta el momento
¿Qué sucede si ingresamos números consecutivos como 1,2,3,4? """

cont = 0
max_num = float('-inf')
min_num = float('inf')

while cont < 4:
    num1 = float(input("Ingrese un número: "))

    if num1 > max_num:
        max_num = num1
    
    if num1 < min_num:
        min_num = num1
    
    cont += 1

print("\nBucles relizados:", cont)
print("Valor máximo:", max_num)
print("Valor mínimo:", min_num)