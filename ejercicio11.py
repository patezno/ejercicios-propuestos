# Escribe un programa que pida por teclado tres valores de tipo entero,
# y que calcule si se cumple que la suma de dos de ellos es igual al tercero.
# La salida del programa tiene que tener el formato:
# Números introducidos: N1N2 N3 (tabulador)
# Y una de las cuatro líneas de salida siguientes:
#       Se cumple que N1 = N2 + N3
#       Se cumple que N2 = N1 + N3
#       Se cumple que N3 = N1 + N2
#       Los números no cumplen la condición

num1 = eval(input("Introduce el primer número: "))
num2 = eval(input("Introduce el segundo número: "))
num3 = eval(input("Introudce el tercer número: "))

print("Estos son los números introducidos: " + str(num1) + ", " + str(num2) + " y " + str(num3))

if num2 + num3 == num1:
    print("Se cumple que " + str(num1) + "= " + str(num2) + " + " + str(num3))
elif num1 + num3 == num2:
    print("Se cumple que " + str(num2) + "= " + str(num1) + " + " + str(num3))
elif num1 + num2 == num3:
    print("Se cumple que " + str(num3) + "= " + str(num1) + " + " + str(num2))
else:
    print("Los números no cumplen la condición")
