# Escribe un programa que escriba en pantalla los 30 primeros números naturales (del 1 al 30),
# así como su media aritmética

count = 0
total = 0
while count < 30:
    count += 1
    media = count
    total = total + count
    print(count)
total = total / 30
print("La media aritmética es " + str(total))
