HI,HF = input().split()

HI = int(HI)
HF = int(HF)

dia = 24

T = dia - HI + HF


if(T > 24 ):
    T = T - dia
    print("O JOGO DUROU {} HORA(S)".format(T))
else:
    print("O JOGO DUROU {} HORA(S)".format(T))
