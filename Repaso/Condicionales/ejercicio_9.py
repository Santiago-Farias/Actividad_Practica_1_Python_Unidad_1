"""
Ejercicio 9
Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos naturalizados desde
los dieciocho (18) años están habilitados a votar. A partir del ingreso de la edad del usuario y el estado
(si es naturalizado o nativo), se deberá informar si es o no posible que la persona concurra a votar en
base a la información suministrada.
"""
# El método lower() convierte todas las letras de string en minúsculas solo si alguno esta en mayúscula,
# de lo contrario devuelve lo mismo.
estado_nativo = "nativo"
estado_naturalizado = "naturalizado"

usuario_edad = int(input("Ingrese su edad: "))
usuario_estado = input("Ingrese su estado (Nativo o Naturalizado): ")

if usuario_edad > 15 and usuario_estado.lower() == estado_nativo:
    print("Usted está habilitado para votar.")
elif usuario_edad > 17 and usuario_estado.lower() == estado_naturalizado:
    print("Usted está habilitado para votar.")
else:
    print("Usted no está habilitado para votar.")