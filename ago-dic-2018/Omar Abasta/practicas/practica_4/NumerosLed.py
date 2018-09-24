def NumerosLed(led):
    num = []
    x = 0
    ContadorDeLeds = 0
    led = str(led)
    while x < len(led):
        num.append(led[x])
        x += 1

    for x in num:
        if x == '1':
            ContadorDeLeds += 2
        if x == '2':
            ContadorDeLeds += 5
        if x == '3':
            ContadorDeLeds += 5
        if x == '4':
            ContadorDeLeds += 4
        if x == '5':
            ContadorDeLeds += 5
        if x == '6':
            ContadorDeLeds += 6
        if x == '7':
            ContadorDeLeds += 3
        if x == '8':
            ContadorDeLeds += 7
        if x == '9':
            ContadorDeLeds += 6
        if x == '0':
            ContadorDeLeds += 6

    print("El numero total de focos Led´s que se usarán para formar tal numero son: '{}'  LEDs".format(ContadorDeLeds))
    return int(ContadorDeLeds)


if __name__ == '__main__':
     led = int(input('Teclee los numeros: '))
     res = NumerosLed(led)
