# Escribe un programa que pida por teclado el radio de una circunferencia,
# y que a continuación calcule y escriba en pantalla la longitud
# de la circunferencia y del área del círculo.

import math

radius = eval(input("Escribe el radio de una circunferencia: "))

long_circum = 2 * math.pi * radius
circle_area = math.pi * (radius ** 2)

print("La longitud de la circunferencia es " + str(long_circum))
print("El área del círculo es " + str(circle_area))
