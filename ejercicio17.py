# Escribe un programa que calcule y escriba la suma de los números pares por un lado, y de los
# impares por otro, de los números comprendidos entre dos número introducidos por teclado.

num1 = eval(input("Introduce el primer número: "))
num2 = eval(input("Introduce el segundo número: "))

def mostrar_pares(primero, segundo):
    lista = []
    if primero > segundo:
        aux = primero
        primero = segundo
        segundo = aux
    num = primero
    if primero % 2 != 0:
        num += 1
    while num <= segundo:
        lista.append(num)
        num = num + 2
    return lista


def mostrar_impares(primero, segundo):
    lista = []
    if primero > segundo:
        aux = primero
        primero = segundo
        segundo = aux
    num = primero
    if primero % 2 == 0:
        num += 1
    while num <= segundo:
        lista.append(num)
        num = num + 2
    return lista


print("Los numeros pares comprendidos entre " + str(num1) + " y " + str(num2) + " es:")
print(mostrar_pares(num1, num2))

print("Los numeros impares comprendidos entre " + str(num1) + " y " + str(num2) + " es:")
print(mostrar_impares(num1, num2))
