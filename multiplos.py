"""Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma
mensagem "Sao Multiplos" ou "Nao sao Multiplos",indicando se os valores
lidos são múltiplos entre si."""


A,B = input().split()
A = int(A)
B = int(B)
if(A == 0 or B == 0):
    print("Sao Multiplos")
else:   
    C = B/A
    D = int(B/A)
    if(C < 1 and D == 0):
        E = A/B
        F = int(A/B)
        if(E == F):
            print("Sao Multiplos")
        else:
            print("Nao sao Multiplos")
    else:
       if(C == D):
            print("Sao Multiplos")
       else:
            print("Nao sao Multiplos") 
