# Escribe un programa que pida por teclado un número entero mostrando un mensaje
# oportuno. A continuación escribe en pantalla el número leído, el doble del
# número leído y el triple del mismo.

num = eval(input("Escribe un número entero: "))

double_num = num * 2
triple_num = num * 3

print("Has escrito el número " + str(num))
print("El doble de " + str(num) + " es " + str(double_num))
print("El triple de " + str(num) + " es " + str(triple_num))
