from copy import deepcopy
from random import randint, seed
from time import time

def damas(numero, tablero, actual):
    global cont
    cont = cont + 1
    x,y = actual
    nuevoTablero = deepcopy(tablero)
    nuevoTablero[x][y] = "X"
    sumIndices = x + y
    difIndices = x - y
    for i in range (8):
        if (nuevoTablero[i][y] == "_"):
            nuevoTablero[i][y] = "Y"
        if (nuevoTablero[x][i] == "_"):
            nuevoTablero[x][i] = "Y"
        j = sumIndices - i
        if (j >=0 and j <= 7 and nuevoTablero[i][j] == "_"):
            nuevoTablero[i][j] = "Y"
        j = i - difIndices
        if (j >=0 and j <= 7 and nuevoTablero[i][j] == "_"):
            nuevoTablero[i][j] = "Y"

    if (numero == 8):
        print ("Exito")
        for fila in nuevoTablero:
            print(fila)
        return True
    else:
        for i in range(8):
            for j in range(8):
                if (nuevoTablero[i][j] == "_"):
                    if (damas(numero+1, nuevoTablero, (i,j))):
                        return True
        return False


tablero = [ ["_" for x in range (8)] for y in range(8)]
cont = 0
seed()
numRepeticiones = 500
tiempoInicial = time()
for i in range (numRepeticiones):
    damas(1, tablero , (randint(0,7), randint(0,7)))
tiempoTranscurrido = time() - tiempoInicial
print ()
print ("*** Algoritmo de fuerza bruta ***")
print ("Con un total de " + str(numRepeticiones) + " repeticiones")
print ("Total: " + str(cont) + " iteraciones")
print ("Con tiempo de: " +str(tiempoTranscurrido) + " segundos")
