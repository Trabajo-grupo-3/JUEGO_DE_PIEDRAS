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

    t = int(input().strip()) #numero de partidas que va a haber

    for t_itr in range(t): #para cada partida del numero t
        n = int(input().strip()) #n va a valer lo que escribas en la terminal, hay q escribir t nº de n
        result = gameOfStones(n) 

        fptr.write(result + '\n') 
        
    fptr.close()
