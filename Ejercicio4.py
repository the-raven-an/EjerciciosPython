while True:
    num = int(input('Introduzca un número del 1 al 10: '))
    if num <= 10:
        break
    if num > 10:
        print('El número introducido es mayor que 10, y por lo tanto, no se procesará.')

mul = 0

while mul <= 10:
    print(str(num) + ' x ' + str(mul) + ' = ' + str(num*mul))
    mul += 1

