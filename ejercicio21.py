# Escribe un programa que solicite por teclado 5 números positivos, forzando al usuario a que
# únicamente introduzca valores positivos. A continuación el programa tiene que escribe cuál
# es el valor más pequeño y cuál es el mayor valor de los introducidos por el usuario.


def comprobar_menor(lista):
    numero = min(lista)
    print("El numero " + str(numero) + " es el menor de todos")


def introduccion_numeros(lista):
    lista.append(eval(input("Introduce un número: ")))
    lista.append(eval(input("Introduce otro número: ")))
    lista.append(eval(input("Introduce otro número: ")))
    lista.append(eval(input("Introduce otro número: ")))
    lista.append(eval(input("Introduce otro número: ")))
    return lista


def negativos(lista):
    for n in lista:
        if n < 0:
            print("Has introducido numeros negativos")
            print("Solo se aceptan positivos")
            del lista[:]
            introduccion_numeros(lista)
    return lista


def comprobar(lista):
    numero = max(lista)
    print("El numero " + str(numero) + " es el mayor de todos")


lista = []
introduccion_numeros(lista)
negativos(lista)
comprobar(lista)
comprobar_menor(lista)
