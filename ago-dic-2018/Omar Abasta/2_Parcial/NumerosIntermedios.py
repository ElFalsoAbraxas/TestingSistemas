def sumatoria(gabriela):


    A=gabriela[0]
    B=gabriela[1]

    Sumando=0

    if (A < B):
        for x in range(A+1, B):
            if x % 2 != 0:
                Sumando+=x
            else:
                Sumando=Sumando
                
#Si el segundo numero es menor que el primero, se ejecuta de igual forma pero
#a la inversa
                
    elif (A > B):
        for x in range(B+1, A):
            if x % 2 != 0:
                Sumando+=x
            else:
                Sumando=Sumando
    return Sumando

if __name__ == '__main__':

    gabriela=list(map(int,input("Escribe 3 numeros para el rango(separalos con un espacio) ").split(" ")))

    resultado=sumatoria(gabriela)

    print("La sumatoria de numeros impares en el rango:", resultado)
