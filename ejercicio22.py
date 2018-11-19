# Repite el programa anterior, pero en vez de leer 5 números, el usuario ha de indicar antes
# cuántos números van a ser leídos, indicándolo mediante el mensaje: Introduzca cuántos
# números tienen que leerse por teclado: _


def cuantos_numeros(cantidad, lista):
    count = 0
    while count < cantidad:
        lista.append(eval(input("Introduce un número: ")))
        count += 1
    return lista


def comprobar_menor(lista):
    numero = min(lista)
    print("El numero " + str(numero) + " es el menor de todos")


def negativos(lista):
    for n in lista:
        if n < 0:
            print("Has introducido numeros negativos")
            print("Solo se aceptan positivos")
            del lista[:]
            cantidad = eval(input("Introduzca cuántos números tienen que leerse por teclado: "))
            cuantos_numeros(cantidad, lista)
    return lista


def comprobar(lista):
    numero = max(lista)
    print("El numero " + str(numero) + " es el mayor de todos")

cantidad = eval(input("Introduzca cuántos números tienen que leerse por teclado: "))

lista = []

cuantos_numeros(cantidad, lista)
negativos(lista)
comprobar(lista)
comprobar_menor(lista)
