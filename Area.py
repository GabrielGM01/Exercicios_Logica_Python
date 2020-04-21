"""Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B."""

A,B,C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)

Triangulo = (A*C)/2
Circulo = 3.14159 * (C**2)
Trapezio = (A+B)*C/2
Quadrado = B*B
Retangulo = A*B

print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}"
      .format(Triangulo,Circulo,Trapezio,Quadrado,Retangulo))


"""
       entrada
    3.0 4.0 5.2

       saida

 TRIANGULO: 7.800
 CIRCULO: 84.949
 TRAPEZIO: 18.200
 QUADRADO: 16.000
 RETANGULO: 12.000


 """
