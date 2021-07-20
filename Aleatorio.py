#
# Aleatorio.py
# Autor: Fernando Dias
#
# Uso: python3 Aleatorio.py [a] [b]
# Argumentos:
#   a : Valor em módulo que define o conjunto [-a,a] que limita a entrada aleatória. Se dado b = a.
#   b : Valor em módulo que define o limite do valor de soma no conjunto [-b,b]
#   ITR: Numero de vezes que o programa é executado
#   Padrao: a = b = 1000, ITR = 10
#
# Descricao: Programa que faz a soma contínua de valores aleatórios até que essa soma se anule. 
# O programa é executado ITR vezes e retorna em CSV o tempo de execucao e a quantidade de somas feitas.
# 

import sys
import time
import random

#
# help(): Imprime o texto de ajuda na tela
#
def help():
    print("""
Uso: python3 Aleatorio.py [a] [b] [ITR]

Descricao: 
    Programa que faz a soma contínua de valores aleatórios até que essa soma se anule. 
    O programa é executado ITR vezes e retorna em CSV o tempo de execucao e a quantidade de somas feitas.

Argumentos:
   a : Valor em módulo que define o conjunto [-a,a] que limita a entrada aleatória. Se dado b = a.
   b : Valor em módulo que define o limite do valor de soma no conjunto [-b,b]
   ITR: Numero de vezes que o programa é executado
   Padrao: a = b = 1000, ITR = 10
""")
 
#
# TestInput(): Valida cada argumento do usuario e encerra o programa se invalido
#
def TestInput(inpt):
    if inpt == "-h" or inpt == "--help":
        help()
        exit(0)
    try:
        a = int(inpt)
        if a < 0:
            a = -a
        if a == 0:
            raise Exception
    except:
        print("entrada invalida: ({inpt})" )
        exit(1)
    return a


#
# GetInput(): Trata a entrada do usuario (se existir) e retorna os valores de a, b e ITR
#
def GetInput():
    a = 1000
    b = a
    ITR = 10
    argc = len(sys.argv)
    if argc == 1:
        pass
    if argc >  4:
        print("numero de argumentos invalido")
        exit(1)
    if argc >= 2:
        a = TestInput(sys.argv[1])
    if argc >= 3:
        b = TestInput(sys.argv[2])
    if argc == 4:
        ITR = TestInput(sys.argv[3])
    return a,b,ITR


# ExecOnce()
# Descricao: Executa a funcao do programa uma vez
#
def ExecOnce(a,b):
    start = time.time()
    sumOfRand = 0
    numOps = 0
    while True:
        sumOfRand += max(min(random.randint(*[-a,a]),a),-b)
        numOps += 1
        if sumOfRand == 0:
            break

    end = time.time()

    return end-start,numOps


#
# Funcao principal
# 
if __name__ == "__main__":
    
    times, ops  = [],[]
    
    a,b,ITR = GetInput()

    # Loop de iteracoes do programa
    for i in range(ITR):
        timeUn,op = ExecOnce(a,b)
        times+= [timeUn]
        ops += [op]

    # Imprime resultado
    for index in range(len(times)):
        print(f"{times[index]},{ops[index]}")
