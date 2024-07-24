pronombre = ""
genero = ""

genero = input("Escriba su género (Masculino/Femenino): ")
while genero.lower() != "masculino" and genero.lower() != "femenino":
    genero = input("Dato inválido\nIngrese una de las opciones (Masculino/Femenino): ")

if genero.lower() == "masculino":
    pronombre = 'o'
elif genero.lower() == "femenino":
    pronombre = 'a'

print(f"Bienvenid{pronombre}")