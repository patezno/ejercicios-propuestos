# Escribe un programa que calcule el área de una finca rectangular en
# metros cuadrados, así como su perímetro exterior, también en metros.

base = eval(input("Escribe la longitud de la base de la finca: "))
altura = eval(input("Escribe la longitud de la altura de la finca: "))

area = base * altura
perimetro = 2 * (base + altura)

print("El área de la finca es " + str(area) + " metros cuadrados")
print("El perímetro de la finca es " + str(perimetro) + " metros")
