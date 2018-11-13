# Modifica el programa anterior para que en vez de mostrar un mensaje genérico
# en el caso de que alguno o los dos números sean negativos, escriba una salida
# diferenciada para cada una de las situaciones que se puedan producir,
# utilizando los siguientes mensajes:
# a. No se calcula la suma porque el primer número es negativo.
# b. No se calcula la suma porque el segundo número es negativo.
# c. No se calcula la suma porque los dos números son negativos.

num1 = eval(input("Introduce el primer número: "))
num2 = eval(input("Introduce el segundo número: "))

if num1 and num2 >= 0:
    suma = num1 + num2
    print("La suma de los dos números es: " + str(suma))
elif num1 < 0 and num2 >= 0:
    print("No se calcula la suma porque el primer número es negativo")
elif num2 < 0 and num1 >= 0:
    print("No se calcula la suma porque el segundo número es negativo")
elif num1 < 0 and num2 < 0:
    print("No se calcula la suma porque los dos números son negativos")
