# Validar el ingreso de un número.
# Tiene que ser de 4 cifras y no contener 0 a la izquierda.

bandera = True
num = input("ingrese num: ")
digitos = len(num)
while bandera != False:
    if digitos != 4:
        num = input("Tiene que tener 4 cifras, intente de nuevo: ")
        digitos = len(num)
    else:
        bandera = False
    
    if num[0] == '0':
        bandera = True
        if num[1] == '0':
            bandera = True
            if num[2] == '0':
                bandera = True

    if bandera == True:
        num = input("Sin ceros a la izquierda, intente de nuevo: ")
        digitos = len(num)