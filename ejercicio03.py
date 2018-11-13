# Repite el ejercicio 2 utilizando una constante que represente el valor de PI.

import math

radius = eval(input("Escribe el radio de una circunferencia: "))

num_pi = math.pi
long_circum = 2 * num_pi * radius
circle_area = num_pi * (radius ** 2)

print("La longitud de la circunferencia es " + str(long_circum))
print("El área del círculo es " + str(circle_area))
