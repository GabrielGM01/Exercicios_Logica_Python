"""Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo."""

import math

A,B,C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)
delta = (B**2) - (4 * A * C)
if(delta < 0 or A == 0 ):
    print("Impossivel calcular")
else:
    raiz = math.sqrt(delta)
    baskaraP = (-B + raiz) / (2 * A)
    baskaraN = (-B - raiz) / (2 * A)
    print("R1 = {:.5f}\nR2 = {:.5f}".format(baskaraP,baskaraN))

