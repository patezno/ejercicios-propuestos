# Escribe un programa que pida por teclado dos números y que calcule y muestre
# su suma solamente si:
#     a. los dos son pares
#     b. el primero es menor que cincuenta
#     c. y el segundo está dentro del intervalo cerrado 100-500.
# En el caso de que no se cumplan las condiciones, en vez de la suma
# ha de visualizarse un mensaje de error.

num1 = eval(input("Introduce el primer número: "))
num2 = eval(input("Introduce el segundo número: "))

if (num1 % 2 == 0 and num2 % 2 == 0) or num1 < 50 or (num2 > 100 and num2 < 500):
    suma = num1 + num2
    print("La suma es " + str(suma))
else:
    print("No cumple los requisitos")
