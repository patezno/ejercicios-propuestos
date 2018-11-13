# Escribe un programa que pida por teclado dos valores de tipo numérico
# que se han de guardar en sendas variables. ¿Qué instrucciones
# habría que utilizar para intercambiar su contenido? (es necesario utilizar
# una variable auxiliar). Para comprobar que el algoritmo ideado es correcto,
# muestra en pantalla el contenido de las variables una vez leídas, y vuelve
# a mostrar su contenido una vez hayas intercambiado sus valores.

num1 = eval(input("Introduce el primer número entero: "))
num2 = eval(input("Introduce el segundo número entero: "))
auxiliar = num1

print ("El primer número introducido es " + str(num1))
print ("El segundo número introducido es " + str(num2))

num1 = num2
num2 = auxiliar

print ("Al intercambiarse, el primer número es " + str(num1))
print ("Al intercambiarse, el segundo número es " + str(num2))
