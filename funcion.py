import math
import os
import random
import re
import sys

posiciones = {}

def gameOfStones(n, movimientopos):
    if n==1 or n==0:
        return False
    elif n==2 or n==3 or n==4 or n==5 or n==6:
        return True
    for movimiento in movimientopos:
        if n-movimiento in posiciones.keys():
            return posiciones.get(n-movimiento)
        else:
            variable = gameOfStones(n-movimiento, movimientopos)
            posiciones.update({n-movimiento:variable})
        if variable == False:
            return True
    return False



if __name__ == '__main__':
    fptr = open('resultados.txt', 'w') #abre el archivo resultados.txt en modo write para guardar los resultados

    t = int(input("¿Cuantas partidas quieres jugar?: ").strip()) #numero de partidas que va a haber

    for t_itr in range(t): #para cada partida del numero t
        n = int(input("¿Con cuantas piedras quieres jugar en esta partida?: ").strip()) #n va a valer lo que escribas en la terminal, hay q escribir t nº de n
        print("Partida con {} piedras".format(n))
        result = gameOfStones(n, [2,3,5])
        if result == True:
            print("Gana el jugador 1")
            fptr.write("Gana el jugador 1" + '\n')
        else:
            print("Gana el jugador 2")
            fptr.write("Gana el jugador 2" + '\n')
        

    fptr.close()
