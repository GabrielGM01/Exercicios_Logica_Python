"""Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. 
   Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura.
"""



A,B,C = input().split()

A = float(A)
B = float(B)
C = float(C)
perimetro = A+B+C
area_trapezio = C*(A+B)/2

Condicao_1 = (B-C) <A <B+C
Condicao_2 = (A-C) <B <A+C
Condicao_3 = (A-B) <C <A+B

if(Condicao_1 == True and Condicao_2==True and Condicao_3 == True):
    print("Perimetro = {}".format(perimetro))
else:
    print("Area = {:.1f}".format(area_trapezio))
            
