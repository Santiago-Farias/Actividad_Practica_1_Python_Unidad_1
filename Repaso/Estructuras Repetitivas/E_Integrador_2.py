from math import *

"""
La juguetería El MUNDO DE CHARLY nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

Medidas:

AB = Diágonal mayor
DC = Diágonal menor
BD y BC = lados menores
AD y AC = lados mayores

El usuario ingresará las medidas  BC, DC y AD.

Detalles de construcción
Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y
los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.
El cometa estará construido con papel de alta resistencia.
La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.
Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas.
Tener en cuenta que los valores de entrada están expresados en Cms.
"""

diagonal_mayor = 0.0 # AB
diagonal_menor = 0.0 # DC - Ingreso por usuario.
lados_mayores = 0.0 # AD y AC - Ingreso por usuario.
lados_menores = 0.0 # BD y BC - Ingreso por usuario.
perimetro_figura = 0.0
varillas_metros = 0.0

area_figura = 0.0
cola_figura = 0.0

print("| MEDIDAS EN CENTÍMETROS |")
lados_menores = float(input("Ingrese la medida para cada lado menor: "))
lados_mayores = float(input("Ingrese la medida para cada lado mayor: "))
diagonal_menor = float(input("Ingrese la medida para el diagonal menor: "))

# Calcular entrecruce mayor a = raiz2(b^2 + c^2).
diagonal_mayor = round(sqrt(lados_menores**2 + lados_mayores**2), 2)

# Calcular área preliminar del cometa area = diag. menor * diag. mayor / 2.
area_figura = round((diagonal_menor * diagonal_mayor) / 2, 2)

# Calcular cola del cometa.
cola_figura = area_figura * 10 / 100

# Calcular área final del cometa.
area_figura += cola_figura

# Calcular los lados.
lados_menores = lados_menores * 2
lados_mayores = lados_mayores * 2

# Calcular perímetros (Metros de varillas)
perimetro_figura = lados_menores + lados_mayores + diagonal_mayor + diagonal_menor

# Calcular metros de varilla.
varillas_metros = round(perimetro_figura / 100, 2)

# Calcular materiales para 10 unidades.
varillas_metros = round(varillas_metros * 10, 2)
area_figura = area_figura * 10

print(f"""\n 
| MATERIALES NECESARIOS |

Por unidad:
- Varillas: {round(varillas_metros/10, 2)} metros.
- Papel resistente: {round(area_figura/10, 2)} metros cuadrados.

10 unidades:
- Varillas: {varillas_metros} metros.
- Papel resistente: {area_figura} metros cuadrados.
""")