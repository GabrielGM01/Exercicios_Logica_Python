"""Leia um valor de ponto flutuante com duas casas decimais.
Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias."""



A,B,C,D = input().split(" ")

A = int(A)
B = int(B)
C = int(C)
D = int(D)



if(B > C and D > A and (C+D)>(A+B)and C > 0 and D > 0 and A%2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
