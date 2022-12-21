import math
import os
import random
import re
import sys

def gameOfStones(n):
    print("Partida con {} piedras".format(n))
    return str(n)
if __name__ == '__main__':
    fptr = open('resultados.txt', 'w') #abre el archivo resultados.txt en modo write para guardar los resultados

    t = int(input("¿Cuantas partidas quieres jugar?: ").strip()) #numero de partidas que va a haber

    for t_itr in range(t): #para cada partida del numero t
        n = int(input("¿Con cuantas piedras quieres jugar en esta partida?: ").strip()) #n va a valer lo que escribas en la terminal, hay q escribir t nº de n
        if n == 1:
            print("Pierdes")
        elif n == 2:
            print("P1 elimina piedras y gana")
        elif n == 3:
            print("P1 elimina dos piedras dejando una y gana")
        elif n == 4:
            print("P1 elimina tres piedras dejando una y gana")
        elif n == 5:
            print("P1 elimina todas las piedras ganando")
        elif n == 6:
            print("P1 elimina cinco piedras dejando una y gana")
        elif n == 7:
            print("P1 elimina dos piedras, dejando cinco que coge P2 y gana P2", "P1 elimina cinco piedras dejando dos que coge P2 y gana P2", "P1 elimina 3 piedras dejando cuatro que P2 coge tres y gana P2")
        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
